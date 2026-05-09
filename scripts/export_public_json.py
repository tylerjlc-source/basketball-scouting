"""
export_public_json.py — Phase 4 publishable-layer pipeline.

Transforms internal player evaluations into validated public-facing JSON for the
ratings DB. Reads from output/[Player]/[YYYY-MM-DD]_profile.md (canonical
scores) and output/[Player]/[YYYY-MM-DD]_public.md (Skill 7 editorial rewrites);
emits per-player JSON + index.json + filtered timeseries.jsonl into published/.

Eight stages:
  1. parse_profile / parse_public           — extract structured data
  2. reconcile                              — assemble JSON; fail-loud on drift
  3. validate_schema                        — jsonschema Draft 2020-12 check
  4. extract_facts / cross_check_facts      — verify named claims
  5. present_manifest                       — Tyler approval gate (stdin)
  6. emit_player_json + emit_audit_log      — write per-player artifacts
  7. build_index                            — published/index.json
  8. filter_timeseries                      — published/timeseries.jsonl

Usage:
  python scripts/export_public_json.py "Jalen Duren"
  python scripts/export_public_json.py --all
  python scripts/export_public_json.py "Jalen Duren" --auto-approve
  python scripts/export_public_json.py --all --dry-run

The expected `_public.md` template (produced by Skill 7) is documented in the
PUBLIC_MD_TEMPLATE constant below.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any, Optional

from jsonschema import Draft202012Validator

# ============================================================================
# CONSTANTS
# ============================================================================

PROJECT_ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = PROJECT_ROOT / "output"
RAW_DIR = PROJECT_ROOT / "raw"
WIKI_DIR = PROJECT_ROOT / "wiki"
DOCS_DIR = PROJECT_ROOT / "docs"
PUBLISHED_DIR = PROJECT_ROOT / "published"
AUDITS_DIR = PUBLISHED_DIR / "audits"
SCHEMA_PATH = DOCS_DIR / "schema" / "public-profile.schema.json"
ANCHOR_LIBRARY_PATH = DOCS_DIR / "ANCHOR-LIBRARY.md"
SIGNATURES_DOC_PATH = DOCS_DIR / "SIGNATURES.md"
LEDGER_PATH = WIKI_DIR / "evaluations.jsonl"

SCHEMA_VERSION = "1.1"
RULES_VERSION = "R1-R15 / S151"

POSITION_MAP = {
    "Point Guard": "PG", "Shooting Guard": "SG",
    "Small Forward": "SF", "Power Forward": "PF",
    "Center": "C",
}

ACCOLADE_PATTERNS = [
    r"All-Star", r"All-NBA(?:\s+(?:First|Second|Third)\s+Team)?",
    r"All-Defensive", r"MVP\b", r"DPOY", r"6MOY", r"6MOTY",
    r"Rookie of the Year", r"ROTY", r"ROY\b",
    r"Finals MVP", r"Most Improved", r"All-Rookie",
]

# Skill 7 editorial output template.
# `_public.md` parser expects exactly these section headings (case-sensitive,
# H2 form). Skill 7 must produce this shape.
#
# Canonical spec: skills/scout-publish.md (TEMPLATE section).
# This constant is the implementation echo — keep in sync with that spec.
PUBLIC_MD_TEMPLATE = """\
# [Player Name] — Public Profile

## Identity
[Paragraph 1]

## Strength
[Paragraph 2]

## Weakness
[Paragraph 3]

## Projection-verdict
[Paragraph 4]

## Sub-domain rationales

| # | Sub-domain | Score | Signature | Public rationale |
|---|---|---|---|---|
| 1 | At-basket finishing | 8.4 | Rim Finisher (Proven) | [...] |
... (26 rows; Signature column reads `[Name] (Tier)` when score >= 8.0,
     `—` otherwise; row #7 always `—`; row #22 always `—` since the
     Athleticism Signature renders on row #21 per SIGNATURES.md §5.1)

## Domain one-lines

| # | Domain | One-line |
|---|---|---|
| 1 | Finishing | [...] |
... (8 rows) ...

## Projection (public)

[≤2-sentence projection narrative]

## NBA Comp(s)

| Comp player | Comp tier | Similarity |
|---|---|---|
| [Player] | Full | [...] |

## Career stats

### Regular Season

| Season | Team | GP | GS | MIN | PTS | REB | AST | STL | BLK | TOV | FG% | 3P% | FT% |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2003-04 | CLE | 79 | 79 | 39.5 | 20.9 | 5.5 | 5.9 | 1.6 | 0.7 | 3.5 | .417 | .290 | .754 |
... (per-season rows) ...
| **Career** |  | **1622** | **1620** | **37.6** | **26.8** | **7.5** | **7.4** | **1.5** | **0.7** | **3.5** | **.507** | **.348** | **.737** |

### Playoffs
... (same shape; omitted when CareerTotalsPostSeason is empty) ...

(College prospects render `### College career` instead of the two NBA sub-sections.
HS profiles or web-fallback failures omit the entire `## Career stats` section.)
"""


# ============================================================================
# SIGNATURES — derivation rules per docs/SIGNATURES.md §3-§4
# ============================================================================
# Tier bands are half-open [low, next_low); Generational is the singleton 10.0.
# Matches §4 explicit boundary spec: 8.0→Proven, 8.5→Elite, 9.0→Superstar,
# 9.5→Iconic, 10.0→Generational. Sub-domain #7 (Free Throw) excluded entirely;
# #22 (Lateral) folded into the Athleticism Signature on #21.

EM_DASH = "—"  # — (U+2014). Empty Signature column cell uses exactly this.

SIGNATURE_TIER_LABELS = ("Proven", "Elite", "Superstar", "Iconic", "Generational")


def _tier_for_score(score: float) -> Optional[str]:
    """Return the Signature tier label for `score` per docs/SIGNATURES.md §3.

    Returns None when score < 8.0 (no Signature awarded). Bands are half-open
    [low, next_low) except Generational which is exactly 10.0.
    """
    if score < 8.0:
        return None
    if score < 8.5:
        return "Proven"
    if score < 9.0:
        return "Elite"
    if score < 9.5:
        return "Superstar"
    if score < 10.0:
        return "Iconic"
    return "Generational"


def load_signature_roster() -> dict[int, tuple[str, str]]:
    """Parse docs/SIGNATURES.md §2 to build the Signature roster.

    Returns dict mapping sub-domain id (or 21 for the combined Athleticism row)
    to (signature_name, description). Excludes #7 (free throw, not in table)
    and #22 (lateral, folded into Athleticism on #21). The doc is the canonical
    source — the script reads it rather than duplicating content.
    """
    text = SIGNATURES_DOC_PATH.read_text(encoding="utf-8")
    section_match = re.search(
        r"^##\s+§2\s+—\s+The 24 Signatures.*?$(.*?)(?=^##\s+§|\Z)",
        text, re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        raise ParseError("SIGNATURES.md §2 section not found")
    body = section_match.group(1)

    roster: dict[int, tuple[str, str]] = {}
    for line in body.splitlines():
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) != 4:
            continue
        if cols[0] in ("#", "") or re.match(r"^-+$", cols[0]) or ":---" in cols[0]:
            continue
        id_cell = cols[0]
        if id_cell == "21+22":
            sub_id = 21
        elif re.match(r"^\d+$", id_cell):
            sub_id = int(id_cell)
        else:
            continue
        name_match = re.match(r"^\*\*(.+?)\*\*$", cols[2])
        if not name_match:
            raise ParseError(
                f"SIGNATURES.md §2 row {sub_id} signature name not bold-wrapped: {cols[2]!r}"
            )
        roster[sub_id] = (name_match.group(1), cols[3])
    if len(roster) != 24:
        raise ParseError(f"SIGNATURES.md §2 expected 24 entries, got {len(roster)}")
    return roster


def derive_signature(sub_domain_id: int, score: float,
                     roster: dict[int, tuple[str, str]],
                     sub_domain_22_score: Optional[float] = None) -> Optional[dict]:
    """Compute the expected Signature per docs/SIGNATURES.md §3-§4.

    Returns {name, tier, description} when a Signature is awarded; None otherwise.
    None cases: sub-domain #7 (Free Throw); sub-domain #22 (Lateral, Athleticism
    renders on #21); score below 8.0 (or for #21, average(#21, #22) below 8.0).

    Caller must pass `sub_domain_22_score` when `sub_domain_id == 21`.
    """
    if sub_domain_id in (7, 22):
        return None
    if sub_domain_id == 21:
        if sub_domain_22_score is None:
            raise ValueError("derive_signature(#21) requires sub_domain_22_score")
        # Round to one decimal — matches SCHEMA-SPEC §10-F sub-domain score precision.
        score = round((score + sub_domain_22_score) / 2.0, 1)
    tier = _tier_for_score(score)
    if tier is None:
        return None
    if sub_domain_id not in roster:
        raise ParseError(
            f"sub-domain #{sub_domain_id} qualifies for a Signature (score {score}) "
            f"but is not in SIGNATURES.md §2 roster"
        )
    name, description = roster[sub_domain_id]
    return {"name": name, "tier": tier, "description": description}


def _parse_signature_label(label: str) -> Optional[dict]:
    """Parse a Signature column cell into {name, tier} or None.

    Format: `[Name] ([Tier])` or `—` (em-dash, U+2014).
    Returns None for `—`. Raises ParseError on malformed input.
    """
    stripped = label.strip()
    if stripped == EM_DASH:
        return None
    m = re.match(
        rf"^(.+?)\s*\(({'|'.join(SIGNATURE_TIER_LABELS)})\)$",
        stripped,
    )
    if not m:
        raise ParseError(
            f"malformed Signature column cell: {label!r} — "
            f"expected '[Name] ([Tier])' or '{EM_DASH}'"
        )
    return {"name": m.group(1).strip(), "tier": m.group(2)}


# ============================================================================
# DATACLASSES
# ============================================================================

@dataclass
class FactClaim:
    text: str
    type: str   # "player_name" | "accolade" | "symbol_number"
    value: str


@dataclass
class FactCheck:
    claim: str
    type: str
    source_checked: str
    status: str  # "verified" | "unverifiable" | "mismatch"
    note: str = ""


@dataclass
class ExportResult:
    player: str
    status: str   # "published" | "skipped" | "rejected" | "failed"
    reason: str = ""
    audit_summary: dict = field(default_factory=dict)


class ParseError(Exception):
    """Fail-loud signal for stage 1 / 2 drift."""


# ============================================================================
# STAGE 1a — PARSE PROFILE
# ============================================================================

def _read_section(text: str, section_num: int) -> str:
    """Return the body of `## Section N — Title` up to the next H2."""
    pattern = rf"^##\s+Section\s+{section_num}\s+—.*?$(.*?)(?=^##\s+Section\s+\d+\s+—|\Z)"
    m = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if not m:
        raise ParseError(f"Section {section_num} not found in profile")
    return m.group(1).strip()


def _parse_kv_table(body: str) -> dict[str, str]:
    """Extract `| **Field** | value |` rows into {field: value}.

    Strict-bold form per scout-output.md §1 canon (template locked at the
    canonical-format pivot). Field name MUST be bold-wrapped; Composite value
    MUST be bold-wrapped (other values are free-form). Drift is caught at the
    linter (scripts/lint_profile.py) — defense-in-depth at the deliverable
    boundary, not at the parser.
    """
    out = {}
    for line in body.splitlines():
        m = re.match(r"\|\s*\*\*([^*|]+?)\*\*\s*\|\s*([^|]+?)\s*\|", line)
        if m:
            value = m.group(2).strip()
            if value.startswith("**") and value.endswith("**") and len(value) >= 4:
                value = value[2:-2].strip()
            out[m.group(1).strip()] = value
    return out


def parse_profile(path: Path) -> dict:
    """Extract structured fields from `_profile.md`. Stage 1a."""
    text = path.read_text(encoding="utf-8")

    # §1 header
    s1 = _read_section(text, 1)
    kv = _parse_kv_table(s1)
    for required in ("Player", "Group", "Position", "Archetype", "Composite", "Tier"):
        if required not in kv:
            raise ParseError(f"§1 missing field: {required}")

    pos_raw = kv["Position"]
    position = POSITION_MAP.get(pos_raw, pos_raw)
    if not re.match(r"^(PG|SG|SF|PF|C)(/(PG|SG|SF|PF|C))?$", position):
        raise ParseError(f"§1 unrecognized position: {pos_raw!r}")

    composite = float(kv["Composite"])
    tier_raw = kv["Tier"]
    tm = re.match(r"^(\d+)\s*[—-]\s*(.+)$", tier_raw)
    if not tm:
        raise ParseError(f"§1 tier format unexpected: {tier_raw!r}")
    tier = int(tm.group(1))
    tier_label = tm.group(2).strip()

    eval_date = kv.get("Evaluation Date") or _date_from_filename(path.name)
    if not re.match(r"^\d{4}-\d{2}-\d{2}$", eval_date):
        raise ParseError(f"evaluation_date not YYYY-MM-DD: {eval_date!r}")

    # §4 sub-domain scores (8 domain tables, 26 rows)
    s4 = _read_section(text, 4)
    sub_domains = []
    for line in s4.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+\.\d)\s*\|", line)
        if m and m.group(1) != "#":
            sub_domains.append({
                "id": int(m.group(1)),
                "name": m.group(2).strip(),
                "score": float(m.group(3)),
            })
    if len(sub_domains) != 26:
        raise ParseError(f"§4 expected 26 sub-domains, got {len(sub_domains)}")

    # §5 domain summaries (8 rows). Format: `| D1 Finishing | 7.7 | ... |`
    s5 = _read_section(text, 5)
    domains = []
    for line in s5.splitlines():
        m = re.match(r"\|\s*D(\d+)\s+([^|]+?)\s*\|\s*(\d+\.\d)\s*\|", line)
        if m and 1 <= int(m.group(1)) <= 8:
            domains.append({
                "id": int(m.group(1)),
                "name": m.group(2).strip(),
                "score": float(m.group(3)),
            })
    if len(domains) != 8:
        raise ParseError(f"§5 expected 8 domains, got {len(domains)}")

    # §9 projection
    s9 = _read_section(text, 9)
    projection = _parse_projection_block(s9)

    # §10 NBA comp
    s10 = _read_section(text, 10)
    comps = _parse_comp_block(s10)
    if not comps:
        raise ParseError("§10 no comps found")

    return {
        "player": kv["Player"],
        "group": kv["Group"],
        "position": position,
        "archetype": kv["Archetype"],
        "evaluation_date": eval_date,
        "composite_score": round(composite, 2),
        "tier": tier,
        "tier_label": tier_label,
        "sub_domains": sub_domains,
        "domains": domains,
        "projection": projection,
        "comps": comps,
    }


def _parse_projection_block(body: str) -> dict:
    """Parse §9 ASCII text-block format: `KEY:    Value ...`.

    Both NBA-vet and prospect blocks use the same KEY:VALUE shape; field set
    differs (vet has POT/MIN/MAX/CONFIDENCE; prospect adds BUST/AVG/BOOM)."""
    def kv_num(label: str, max_val: float = 10.0) -> Optional[float]:
        # Anchor to start of line (after optional whitespace) to avoid matching
        # numbers embedded in narrative prose. Allow 1- or 2-decimal precision.
        m = re.search(rf"^\s*{label}\s*[:\|]\s*(\d+(?:\.\d{{1,2}})?)",
                      body, re.MULTILINE | re.IGNORECASE)
        if m:
            v = float(m.group(1))
            return round(v, 2) if v <= max_val + 0.01 else None
        return None

    pot = kv_num("POT")
    min_v = kv_num("MIN")
    max_v = kv_num("MAX")
    if pot is None or min_v is None or max_v is None:
        raise ParseError(f"§9 missing POT/MIN/MAX — got pot={pot} min={min_v} max={max_v}")

    conf_match = re.search(r"^\s*CONFIDENCE\s*[:\|]\s*(tight|moderate|wide)",
                           body, re.MULTILINE | re.IGNORECASE)
    if not conf_match:
        raise ParseError("§9 missing CONFIDENCE (tight/moderate/wide)")

    proj = {
        "pot": pot, "min": min_v, "max": max_v,
        "confidence": conf_match.group(1).lower(),
    }

    bust = kv_num("BUST(?:%|_PCT)?", max_val=100)
    avg = kv_num("AVG(?:%|_PCT)?", max_val=100)
    boom = kv_num("BOOM(?:%|_PCT)?", max_val=100)
    if bust is not None and avg is not None and boom is not None:
        proj["bust_pct"] = bust
        proj["avg_pct"] = avg
        proj["boom_pct"] = boom
    return proj


def _parse_comp_block(body: str) -> list[dict]:
    """Parse §10 — branch by canon form.

    NBA-vet branch: a single `**LINEAGE COMP: [Player] ([era])** — prose.` line.
    Player name extracted from the bold-prefixed callout; comp_tier set to
    "Lineage" (qualitative-only per NBA-COMP-METHODOLOGY § B.4).

    Prospect branch (States 1–3): one or more H3 blocks of the form

        ### Comp 1: Player Name
        - **Tier:** 🟢 Full
        - **Similarity:** ...

    Tier text mapped via leading glyph; profiles with neither glyph nor
    canonical word raise.

    Mixed shapes (LINEAGE + ### Comp headers in the same §10) raise — the
    canonical templates are mutually exclusive.
    """
    glyph_to_text = {"🟢": "Full", "🟡": "Partial", "🔴": "None"}

    lineage_iter = list(re.finditer(
        r"\*\*LINEAGE COMP:\s*(.+?)\*\*", body,
    ))
    headers = list(re.finditer(r"^###\s+Comp\s+\d+:\s+(.+?)\s*$",
                               body, re.MULTILINE))

    if lineage_iter and headers:
        raise ParseError(
            "§10 has both `**LINEAGE COMP:` and `### Comp N:` forms — "
            "exactly one branch (NBA-vet lineage OR prospect multi-comp) is canonical"
        )

    if lineage_iter:
        if len(lineage_iter) > 1:
            raise ParseError(f"§10 expected exactly one LINEAGE COMP line, got {len(lineage_iter)}")
        raw = lineage_iter[0].group(1).strip()
        # Strip trailing "(era)" parenthetical if present: "Player (era)" -> "Player".
        m = re.match(r"^(.+?)\s*\([^)]+\)\s*$", raw)
        player = (m.group(1) if m else raw).strip()
        if not player:
            raise ParseError("§10 LINEAGE COMP line has empty player name")
        return [{"comp_player": player, "comp_tier": "Lineage"}]

    out: list[dict] = []
    for i, h in enumerate(headers):
        player = h.group(1).strip()
        block_end = headers[i + 1].start() if i + 1 < len(headers) else len(body)
        block = body[h.end():block_end]
        tier_match = re.search(r"\*\*Tier:\*\*\s*([🟢🟡🔴])?\s*([A-Za-z]+)?",
                               block)
        if not tier_match:
            raise ParseError(f"§10 comp '{player}' missing **Tier:** line")
        glyph = tier_match.group(1) or ""
        word = (tier_match.group(2) or "").strip()
        canonical = glyph_to_text.get(glyph)
        if canonical is None and word in ("Full", "Partial", "None"):
            canonical = word
        if canonical is None:
            raise ParseError(
                f"§10 comp '{player}' has non-canonical tier "
                f"(glyph={glyph!r}, word={word!r})"
            )
        out.append({"comp_player": player, "comp_tier": canonical})
    return out


def _date_from_filename(name: str) -> str:
    m = re.match(r"^(\d{4}-\d{2}-\d{2})_", name)
    return m.group(1) if m else ""


# ============================================================================
# STAGE 1b — PARSE PUBLIC
# ============================================================================

def parse_public(path: Path) -> dict:
    """Extract editorial rewrites from `_public.md`. Stage 1b."""
    text = path.read_text(encoding="utf-8")

    def section(heading: str) -> str:
        pattern = rf"^##\s+{re.escape(heading)}\s*$(.*?)(?=^##\s+|\Z)"
        m = re.search(pattern, text, re.MULTILINE | re.DOTALL)
        if not m:
            raise ParseError(f"public.md missing section: '## {heading}'")
        return m.group(1).strip()

    narrative = {
        "identity": section("Identity"),
        "strength": section("Strength"),
        "weakness": section("Weakness"),
        "projection_verdict": section("Projection-verdict"),
    }
    for k, v in narrative.items():
        if not v:
            raise ParseError(f"narrative.{k} empty")

    sub_rows = _parse_public_sub_domain_table(section("Sub-domain rationales"))
    domain_one_lines = _parse_id_rationale_table(section("Domain one-lines"), expected=8)
    projection_prose = section("Projection (public)").strip()
    comp_rows = _parse_comp_similarity_table(section("NBA Comp(s)"))
    career_stats = _parse_career_stats_section(text)

    return {
        "narrative": narrative,
        "sub_rows": sub_rows,
        "domain_one_lines": domain_one_lines,
        "projection_prose": projection_prose,
        "comp_similarities": comp_rows,
        "career_stats": career_stats,
    }


def _parse_id_rationale_table(body: str, expected: int) -> dict[int, str]:
    out = {}
    for line in body.splitlines():
        m = re.match(r"\|\s*(\d+)\s*\|\s*[^|]+\|\s*(.+?)\s*\|\s*$", line)
        if m and m.group(1) != "#":
            out[int(m.group(1))] = m.group(2).strip()
    if len(out) != expected:
        raise ParseError(f"public table expected {expected} rows, got {len(out)}")
    return out


def _parse_public_sub_domain_table(body: str) -> dict[int, dict]:
    """Parse the 5-column sub-domain rationales table from `_public.md`.

    Format: `| # | Sub-domain | Score | Signature | Public rationale |`.
    Returns dict mapping id to {score, signature_label, rationale}.
    `signature_label` is the raw cell text (e.g. `Rim Finisher (Proven)` or `—`).
    """
    out: dict[int, dict] = {}
    for line in body.splitlines():
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) != 5:
            continue
        if cols[0] in ("#", "") or re.match(r"^-+$", cols[0]) or ":---" in cols[0]:
            continue
        if not re.match(r"^\d+$", cols[0]):
            continue
        idx = int(cols[0])
        try:
            score = float(cols[2])
        except ValueError:
            raise ParseError(
                f"public sub-domain row #{idx} has non-numeric score: {cols[2]!r}"
            )
        out[idx] = {
            "score": score,
            "signature_label": cols[3],
            "rationale": cols[4],
        }
    if len(out) != 26:
        raise ParseError(
            f"public sub-domain table expected 26 rows, got {len(out)}"
        )
    return out


def _parse_career_stats_section(text: str) -> Optional[dict]:
    """Parse the optional `## Career stats` appendix per PUBLIC-LANGUAGE-GUIDE §9.

    Returns a dict containing any subset of {regular_season, playoffs,
    college_career}. Returns None when the section is absent (HS profiles or
    web-fallback failures). Numbers in this section are independently sourced
    from `nba_api`/web-fallback and are NOT byte-equal-checked against
    `_profile.md` — see PUBLIC-LANGUAGE-GUIDE §8 QC4 carve-out.
    """
    section_match = re.search(
        r"^##\s+Career stats\s*$(.*?)(?=^##\s+|\Z)",
        text, re.MULTILINE | re.DOTALL,
    )
    if not section_match:
        return None
    body = section_match.group(1)

    heading_to_key = {
        "Regular Season": "regular_season",
        "Playoffs": "playoffs",
        "College career": "college_career",
    }
    out: dict[str, list[dict]] = {}
    sub_iter = re.finditer(
        r"^###\s+(Regular Season|Playoffs|College career)\s*$(.*?)(?=^###\s+|\Z)",
        body, re.MULTILINE | re.DOTALL,
    )
    for m in sub_iter:
        key = heading_to_key[m.group(1)]
        rows = _parse_career_stats_table(m.group(2))
        if rows:
            out[key] = rows
    return out or None


def _parse_career_stats_table(body: str) -> list[dict]:
    """Parse one career-stats markdown table to row dicts.

    The career-aggregate row is bolded (cells wrapped in `**…**`); its Season
    cell reads `**Career**`. Per-season rows are not bolded. Numeric cells use
    PUBLIC-LANGUAGE-GUIDE §9.3 form: per-game stats to 1 decimal, percentages
    in `.XXX` NBA.com form, missing values render as `-`.
    """
    rows: list[dict] = []
    for line in body.splitlines():
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) != 14:
            continue
        if cols[0] in ("Season", "") or re.match(r"^-+$", cols[0]) or ":---" in cols[0]:
            continue

        is_career = cols[0] == "**Career**"

        def unbold(c: str) -> str:
            if c.startswith("**") and c.endswith("**") and len(c) >= 4:
                return c[2:-2].strip()
            return c
        cols = [unbold(c) for c in cols]

        rows.append({
            "season_id": cols[0],
            "team": cols[1],
            "gp": _stat_int_or_null(cols[2]),
            "gs": _stat_int_or_null(cols[3]),
            "min": _stat_num_or_null(cols[4]),
            "pts": _stat_num_or_null(cols[5]),
            "reb": _stat_num_or_null(cols[6]),
            "ast": _stat_num_or_null(cols[7]),
            "stl": _stat_num_or_null(cols[8]),
            "blk": _stat_num_or_null(cols[9]),
            "tov": _stat_num_or_null(cols[10]),
            "fg_pct": _stat_pct_or_null(cols[11]),
            "fg3_pct": _stat_pct_or_null(cols[12]),
            "ft_pct": _stat_pct_or_null(cols[13]),
            "is_career": is_career,
        })
    return rows


def _stat_int_or_null(s: str) -> Optional[int]:
    if not s or s == "-":
        return None
    try:
        return int(s)
    except ValueError:
        return None


def _stat_num_or_null(s: str) -> Optional[float]:
    if not s or s == "-":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def _stat_pct_or_null(s: str) -> Optional[float]:
    """`.468` (NBA.com form) → 0.468; `-` → None."""
    if not s or s == "-":
        return None
    try:
        if s.startswith("."):
            return float("0" + s)
        return float(s)
    except ValueError:
        return None


def _parse_comp_similarity_table(body: str) -> list[dict]:
    rows = []
    for line in body.splitlines():
        cols = [c.strip() for c in line.split("|")[1:-1]]
        if len(cols) >= 3 and cols[0] not in ("Comp player", "---") and ":---" not in cols[0]:
            if not re.match(r"^-+$", cols[0]):
                rows.append({
                    "comp_player": cols[0],
                    "comp_tier": cols[1],
                    "similarity_public": cols[2],
                })
    return rows


# ============================================================================
# STAGE 2 — RECONCILE
# ============================================================================

def reconcile(profile: dict, public: dict, career_status: str,
              draft_class: Optional[int],
              signature_roster: dict[int, tuple[str, str]]) -> dict:
    """Assemble JSON output. Stage 2 — fail-loud on drift."""
    # Sub-domain ids must be a 1:1 match between profile and public rewrites.
    profile_ids = {sd["id"] for sd in profile["sub_domains"]}
    public_ids = set(public["sub_rows"].keys())
    missing_pub = profile_ids - public_ids
    extra_pub = public_ids - profile_ids
    if missing_pub or extra_pub:
        raise ParseError(
            f"sub-domain id mismatch — missing in public: {sorted(missing_pub)}; "
            f"extra in public: {sorted(extra_pub)}"
        )

    domain_ids = {d["id"] for d in profile["domains"]}
    public_dom_ids = set(public["domain_one_lines"].keys())
    if profile_ids != public_ids or domain_ids != public_dom_ids:
        raise ParseError(
            f"domain id mismatch — profile: {sorted(domain_ids)}, "
            f"public: {sorted(public_dom_ids)}"
        )

    # Comp count must match (and tier values must agree on overlap).
    if len(public["comp_similarities"]) != len(profile["comps"]):
        raise ParseError(
            f"comp count mismatch — profile: {len(profile['comps'])}, "
            f"public: {len(public['comp_similarities'])}"
        )
    for p_comp, pub_comp in zip(profile["comps"], public["comp_similarities"]):
        if p_comp["comp_player"] != pub_comp["comp_player"]:
            raise ParseError(
                f"comp player mismatch — profile: {p_comp['comp_player']!r}, "
                f"public: {pub_comp['comp_player']!r}"
            )
        if p_comp["comp_tier"] != pub_comp["comp_tier"]:
            raise ParseError(
                f"comp tier mismatch for {p_comp['comp_player']} — "
                f"profile: {p_comp['comp_tier']}, public: {pub_comp['comp_tier']}"
            )

    # Score + Signature reconciliation: profile is canonical, public must match.
    sub22_score = next(
        (sd["score"] for sd in profile["sub_domains"] if sd["id"] == 22), None
    )

    sub_domains = []
    for sd in profile["sub_domains"]:
        pub_row = public["sub_rows"][sd["id"]]
        if abs(pub_row["score"] - sd["score"]) > 1e-9:
            raise ParseError(
                f"sub-domain #{sd['id']} score mismatch — "
                f"profile: {sd['score']}, public: {pub_row['score']}"
            )

        expected_sig = derive_signature(
            sd["id"], sd["score"], signature_roster,
            sub_domain_22_score=sub22_score if sd["id"] == 21 else None,
        )
        parsed_sig = _parse_signature_label(pub_row["signature_label"])
        if expected_sig is None and parsed_sig is not None:
            raise ParseError(
                f"sub-domain #{sd['id']}: expected no Signature "
                f"(score {sd['score']}) but public has "
                f"{pub_row['signature_label']!r}"
            )
        if expected_sig is not None and parsed_sig is None:
            raise ParseError(
                f"sub-domain #{sd['id']}: expected Signature "
                f"{expected_sig['name']} ({expected_sig['tier']}) but public has "
                f"{EM_DASH!r}"
            )
        if expected_sig is not None and parsed_sig is not None:
            if (parsed_sig["name"] != expected_sig["name"]
                    or parsed_sig["tier"] != expected_sig["tier"]):
                raise ParseError(
                    f"sub-domain #{sd['id']}: Signature mismatch — "
                    f"expected '{expected_sig['name']} ({expected_sig['tier']})', "
                    f"got '{parsed_sig['name']} ({parsed_sig['tier']})'"
                )

        sub_domains.append({
            "id": sd["id"],
            "name": sd["name"],
            "score": sd["score"],
            "rationale_public": pub_row["rationale"],
            "signature": expected_sig,
        })

    domains = []
    for d in profile["domains"]:
        domains.append({
            "id": d["id"],
            "name": d["name"],
            "score": d["score"],
            "one_line": public["domain_one_lines"][d["id"]],
        })

    projection = dict(profile["projection"])
    projection["spread_note_public"] = public["projection_prose"]

    comps = []
    for p_comp, pub_comp in zip(profile["comps"], public["comp_similarities"]):
        comps.append({
            "comp_player": p_comp["comp_player"],
            "comp_tier": p_comp["comp_tier"],
            "similarity_public": pub_comp["similarity_public"],
        })

    out = {
        "schema_version": SCHEMA_VERSION,
        "rules_version": RULES_VERSION,
        "player": profile["player"],
        "group": profile["group"],
        "position": profile["position"],
        "career_status": career_status,
        "draft_class": draft_class,
        "archetype": profile["archetype"],
        "evaluation_date": profile["evaluation_date"],
        "composite_label": "Composite",
        "composite_score": profile["composite_score"],
        "tier": profile["tier"],
        "tier_label": profile["tier_label"],
        "narrative": public["narrative"],
        "domains": domains,
        "sub_domains": sub_domains,
        "projection": projection,
        "comps": comps,
        "history": [],  # populated separately from ledger
    }

    # Career-stats appendix (PUBLIC-LANGUAGE-GUIDE §9). Optional — omitted for
    # HS profiles or web-fallback failures. Numbers are independently sourced
    # at publish time and NOT byte-equal-checked against `_profile.md` (§8 QC4
    # carve-out). Cheap sanity check: career-row GP reconciles to per-season
    # sum (GP only — PerGame mode means PTS isn't summable).
    cs = public.get("career_stats")
    if cs is not None:
        for key in ("regular_season", "playoffs", "college_career"):
            rows = cs.get(key)
            if not rows:
                continue
            career_rows = [r for r in rows if r.get("is_career")]
            season_rows = [r for r in rows if not r.get("is_career")]
            if len(career_rows) > 1:
                raise ParseError(f"career_stats.{key} has {len(career_rows)} career rows (expected 1)")
            if not career_rows:
                raise ParseError(f"career_stats.{key} missing the bolded career-aggregate row")
            career_gp = career_rows[0].get("gp")
            season_gp_sum = sum((r.get("gp") or 0) for r in season_rows)
            if career_gp is not None and season_rows and abs(career_gp - season_gp_sum) > 1:
                raise ParseError(
                    f"career_stats.{key} GP reconcile fail — "
                    f"career row {career_gp}, sum of seasons {season_gp_sum}"
                )
        out["career_stats"] = cs

    return out


# ============================================================================
# STAGE 3 — VALIDATE SCHEMA
# ============================================================================

def validate_schema(obj: dict, schema: dict) -> None:
    """Stage 3. Raises if invalid."""
    Draft202012Validator(schema).validate(obj)


# ============================================================================
# STAGE 4 — FACT EXTRACTION + CROSS-CHECK
# ============================================================================

def extract_facts(public_text: str, anchor_names: set[str]) -> list[FactClaim]:
    """Stage 4a — pattern-based extraction."""
    facts: list[FactClaim] = []
    seen: set[tuple[str, str]] = set()

    # Player names: any "Capitalized Word(s)" that match an anchor library entry.
    for m in re.finditer(r"\b([A-Z][a-z'.\-]+(?:\s+[A-Z][A-Za-z'.\-]+){1,3})\b", public_text):
        candidate = m.group(1)
        if candidate in anchor_names and ("player_name", candidate) not in seen:
            facts.append(FactClaim(text=candidate, type="player_name", value=candidate))
            seen.add(("player_name", candidate))

    # Accolades.
    for pattern in ACCOLADE_PATTERNS:
        for m in re.finditer(pattern, public_text):
            tok = m.group(0)
            if ("accolade", tok) not in seen:
                facts.append(FactClaim(text=tok, type="accolade", value=tok))
                seen.add(("accolade", tok))

    # Symbol-form numbers (defensive — language guide says shouldn't appear).
    for m in re.finditer(r"\b(\d+(?:\.\d+)?%|\d+\.\d{2})\b", public_text):
        tok = m.group(1)
        if ("symbol_number", tok) not in seen:
            facts.append(FactClaim(text=tok, type="symbol_number", value=tok))
            seen.add(("symbol_number", tok))

    return facts


def cross_check_facts(
    facts: list[FactClaim],
    profile_text: str,
    research_packet_text: str,
    anchor_library_text: str,
    player_name: str,
) -> list[FactCheck]:
    """Stage 4b — verify each claim against source documents."""
    out: list[FactCheck] = []
    player_anchor_block = _extract_anchor_notes(anchor_library_text, player_name)

    for f in facts:
        if f.type == "player_name":
            if f.value in anchor_library_text:
                out.append(FactCheck(claim=f.text, type=f.type,
                                     source_checked="ANCHOR-LIBRARY.md",
                                     status="verified"))
            else:
                out.append(FactCheck(claim=f.text, type=f.type,
                                     source_checked="ANCHOR-LIBRARY.md",
                                     status="mismatch",
                                     note="Player name not in anchor library"))
        elif f.type == "accolade":
            in_anchor = bool(player_anchor_block and re.search(re.escape(f.value), player_anchor_block, re.IGNORECASE))
            in_packet = bool(re.search(re.escape(f.value), research_packet_text, re.IGNORECASE))
            in_profile = bool(re.search(re.escape(f.value), profile_text, re.IGNORECASE))
            if in_anchor or in_packet or in_profile:
                src = "ANCHOR-LIBRARY Notes" if in_anchor else (
                    "research packet" if in_packet else "profile")
                out.append(FactCheck(claim=f.text, type=f.type,
                                     source_checked=src, status="verified"))
            else:
                out.append(FactCheck(claim=f.text, type=f.type,
                                     source_checked="profile / packet / anchor-lib",
                                     status="unverifiable",
                                     note="Accolade not found in any source"))
        elif f.type == "symbol_number":
            if f.value in profile_text:
                out.append(FactCheck(claim=f.text, type=f.type,
                                     source_checked="profile", status="verified"))
            else:
                out.append(FactCheck(claim=f.text, type=f.type,
                                     source_checked="profile",
                                     status="mismatch",
                                     note="Symbol-form number not in profile (language guide §5.4 says use word form)"))
    return out


def _extract_anchor_notes(anchor_text: str, player: str) -> Optional[str]:
    """Find the player's row in ANCHOR-LIBRARY.md and return the Notes column."""
    for line in anchor_text.splitlines():
        if line.startswith("|") and player in line:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 6:
                return cols[5]
    return None


def load_anchor_names(anchor_text: str) -> set[str]:
    """Pull every Player column entry from anchor-library tier tables."""
    names = set()
    for line in anchor_text.splitlines():
        if line.startswith("|"):
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 6 and re.match(r"^\d+\.\d{2}$", cols[0]):
                names.add(cols[1])
    return names


# ============================================================================
# STAGE 5 — TYLER MANIFEST GATE
# ============================================================================

def present_manifest(obj: dict, audit: list[FactCheck], auto_approve: bool) -> tuple[bool, str]:
    """Stage 5 — interactive approval. Returns (approved, decision_label)."""
    summary = _audit_summary(audit)
    has_mismatch = summary["mismatch"] > 0

    print("\n" + "=" * 60)
    print(f"PUBLISH MANIFEST — {obj['player']}")
    print("=" * 60)
    print(f"Composite: {obj['composite_score']:.2f}  Tier: {obj['tier']} ({obj['tier_label']})")
    print(f"Archetype: {obj['archetype']}  Group: {obj['group']}  Position: {obj['position']}")
    print(f"Career status: {obj['career_status']}  Draft class: {obj['draft_class']}")
    print(f"Eval date: {obj['evaluation_date']}")
    print()
    print(f"Audit: {summary['verified']} verified, "
          f"{summary['unverifiable']} unverifiable, "
          f"{summary['mismatch']} mismatch")
    if summary["mismatch"]:
        print("\nMISMATCHES (block publish):")
        for c in audit:
            if c.status == "mismatch":
                print(f"  - {c.claim} [{c.type}] — {c.note} (checked: {c.source_checked})")
    if summary["unverifiable"]:
        print("\nUNVERIFIABLE (need Tyler eyeballs):")
        for c in audit:
            if c.status == "unverifiable":
                print(f"  - {c.claim} [{c.type}] — {c.note}")
    print()

    if has_mismatch:
        print("REJECTED — fix mismatches in source artifacts before re-running.")
        return (False, "rejected_mismatch")

    if auto_approve:
        print("AUTO-APPROVED.")
        return (True, "auto_approved")

    while True:
        ans = input("Approve publish? [y/n/details]: ").strip().lower()
        if ans in ("y", "yes"):
            return (True, "approved")
        if ans in ("n", "no"):
            return (False, "rejected_user")
        if ans in ("d", "details"):
            print("\nFull audit log:")
            for c in audit:
                print(f"  [{c.status}] {c.claim} ({c.type}) — {c.source_checked} — {c.note}")
            print()


def _audit_summary(audit: list[FactCheck]) -> dict:
    s = {"verified": 0, "unverifiable": 0, "mismatch": 0}
    for c in audit:
        s[c.status] = s.get(c.status, 0) + 1
    return s


# ============================================================================
# STAGE 6 — EMIT PER-PLAYER ARTIFACTS
# ============================================================================

def emit_player_json(obj: dict, player_filename: str) -> Path:
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    path = PUBLISHED_DIR / f"{player_filename}.json"
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


def emit_audit_log(player: str, eval_date: str, audit: list[FactCheck],
                   decision: str, player_filename: str) -> Path:
    AUDITS_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "player": player,
        "evaluation_date": eval_date,
        "checks": [asdict(c) for c in audit],
        "summary": _audit_summary(audit),
        "decision": decision,
    }
    path = AUDITS_DIR / f"{player_filename}.audit.json"
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return path


# ============================================================================
# STAGE 7 — INDEX
# ============================================================================

def build_index() -> Path:
    """Scan published/*.json and emit index.json."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    entries = []
    for p in sorted(PUBLISHED_DIR.glob("*.json")):
        if p.name == "index.json":
            continue
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        entries.append({
            "player": data["player"],
            "composite": data["composite_score"],
            "tier": data["tier"],
            "archetype": data["archetype"],
            "file": p.name,
        })
    entries.sort(key=lambda e: (-e["composite"], e["player"]))
    out = PUBLISHED_DIR / "index.json"
    out.write_text(json.dumps({"count": len(entries), "players": entries},
                              indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    return out


# ============================================================================
# STAGE 8 — TIMESERIES FILTER
# ============================================================================

PUBLIC_LEDGER_FIELDS = (
    "player", "session", "eval_date", "composite", "pot",
    "tier", "archetype", "group", "position", "rubric_version",
)


def filter_timeseries() -> Path:
    """Filter wiki/evaluations.jsonl to published-safe columns."""
    PUBLISHED_DIR.mkdir(parents=True, exist_ok=True)
    out = PUBLISHED_DIR / "timeseries.jsonl"
    if not LEDGER_PATH.exists():
        out.write_text("", encoding="utf-8")
        return out
    rows = []
    for line in LEDGER_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        rows.append({k: row.get(k) for k in PUBLIC_LEDGER_FIELDS})
    out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in rows) + ("\n" if rows else ""),
                   encoding="utf-8")
    return out


# ============================================================================
# ORCHESTRATOR
# ============================================================================

def export_player(player_dir_name: str, schema: dict, anchor_text: str,
                  anchor_names: set[str],
                  signature_roster: dict[int, tuple[str, str]],
                  auto_approve: bool, dry_run: bool) -> ExportResult:
    """Run stages 1–6 for one player. Returns ExportResult."""
    player_dir = OUTPUT_DIR / player_dir_name
    if not player_dir.is_dir():
        return ExportResult(player=player_dir_name, status="failed",
                            reason=f"output/{player_dir_name}/ not found")

    profiles = sorted(player_dir.glob("*_profile.md"))
    publics = sorted(player_dir.glob("*_public.md"))
    if not profiles:
        return ExportResult(player=player_dir_name, status="failed",
                            reason="no _profile.md found")
    if not publics:
        return ExportResult(player=player_dir_name, status="skipped",
                            reason="no _public.md (run scout-publish first)")
    profile_path = profiles[-1]
    public_path = publics[-1]
    if _date_from_filename(profile_path.name) != _date_from_filename(public_path.name):
        return ExportResult(player=player_dir_name, status="failed",
                            reason=f"date mismatch: {profile_path.name} vs {public_path.name}")

    try:
        profile = parse_profile(profile_path)
        public = parse_public(public_path)
    except ParseError as e:
        return ExportResult(player=player_dir_name, status="failed",
                            reason=f"parse error: {e}")

    career_status, draft_class = _resolve_career_status(profile["player"], anchor_text)

    try:
        obj = reconcile(profile, public, career_status, draft_class, signature_roster)
    except ParseError as e:
        return ExportResult(player=player_dir_name, status="failed",
                            reason=f"reconcile error: {e}")

    try:
        validate_schema(obj, schema)
    except Exception as e:
        return ExportResult(player=player_dir_name, status="failed",
                            reason=f"schema validation error: {e}")

    public_text = public_path.read_text(encoding="utf-8")
    profile_text = profile_path.read_text(encoding="utf-8")
    packet_text = _load_research_packet(player_dir_name)

    facts = extract_facts(public_text, anchor_names)
    audit = cross_check_facts(facts, profile_text, packet_text, anchor_text,
                              profile["player"])

    if dry_run:
        summary = _audit_summary(audit)
        print(f"[dry-run] {profile['player']}: parse OK, schema OK, audit "
              f"{summary['verified']}V/{summary['unverifiable']}U/{summary['mismatch']}M")
        return ExportResult(player=profile["player"], status="skipped",
                            reason="dry-run", audit_summary=summary)

    approved, decision = present_manifest(obj, audit, auto_approve)
    if not approved:
        emit_audit_log(profile["player"], profile["evaluation_date"], audit,
                       decision, player_dir_name)
        return ExportResult(player=profile["player"], status="rejected",
                            reason=decision, audit_summary=_audit_summary(audit))

    obj["history"] = _history_for(profile["player"])

    emit_player_json(obj, player_dir_name)
    emit_audit_log(profile["player"], profile["evaluation_date"], audit,
                   decision, player_dir_name)
    return ExportResult(player=profile["player"], status="published",
                        reason=decision, audit_summary=_audit_summary(audit))


def _resolve_career_status(player: str, anchor_text: str) -> tuple[str, Optional[int]]:
    """Derive career_status + draft_class from ANCHOR-LIBRARY Status column."""
    for line in anchor_text.splitlines():
        if line.startswith("|") and player in line:
            cols = [c.strip() for c in line.split("|")[1:-1]]
            if len(cols) >= 3:
                status = cols[2]
                if "Retired" in status:
                    return ("Retired", None)
                draft_match = re.search(r"(\d{4})\s+draft\s+class", status, re.IGNORECASE)
                if draft_match:
                    return ("Draft prospect", int(draft_match.group(1)))
                return ("Active", None)
    return ("Active", None)


def _load_research_packet(player_dir_name: str) -> str:
    pdir = RAW_DIR / player_dir_name
    if not pdir.is_dir():
        return ""
    packets = sorted(pdir.glob("*_research-packet.md"))
    if not packets:
        return ""
    return packets[-1].read_text(encoding="utf-8")


def _history_for(player: str) -> list[dict]:
    if not LEDGER_PATH.exists():
        return []
    rows = []
    for line in LEDGER_PATH.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            row = json.loads(line)
        except json.JSONDecodeError:
            continue
        if row.get("player") == player:
            rows.append({
                "date": row.get("eval_date"),
                "composite": row.get("composite"),
                "tier": row.get("tier"),
                "archetype": row.get("archetype"),
            })
    rows.sort(key=lambda r: r["date"] or "")
    return rows


# ============================================================================
# CLI
# ============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(description="Export public profile JSON.")
    parser.add_argument("player", nargs="?",
                        help="Player name (use spaces or underscores)")
    parser.add_argument("--all", action="store_true",
                        help="Export every player with both _profile and _public")
    parser.add_argument("--auto-approve", action="store_true",
                        help="Bypass the interactive Tyler gate (post-launch use)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Run stages 1–4 only; skip approval, write nothing")
    args = parser.parse_args()

    if not args.player and not args.all:
        parser.error("provide a player name or --all")

    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))
    anchor_text = ANCHOR_LIBRARY_PATH.read_text(encoding="utf-8")
    anchor_names = load_anchor_names(anchor_text)
    try:
        signature_roster = load_signature_roster()
    except ParseError as e:
        print(f"FATAL: cannot load Signature roster — {e}", file=sys.stderr)
        return 2

    if args.all:
        targets = [p.name for p in sorted(OUTPUT_DIR.iterdir()) if p.is_dir()]
    else:
        targets = [args.player.replace(" ", "_")]

    results: list[ExportResult] = []
    for tgt in targets:
        try:
            results.append(export_player(tgt, schema, anchor_text, anchor_names,
                                          signature_roster,
                                          args.auto_approve, args.dry_run))
        except KeyboardInterrupt:
            print("\nInterrupted.")
            break

    if not args.dry_run and not args.all:
        # Per-player invocation skips index/timeseries rebuild — those run only
        # on --all to avoid stale partial-state writes during single-player work.
        pass
    elif not args.dry_run and args.all:
        build_index()
        filter_timeseries()

    print("\n" + "=" * 60)
    print(f"SUMMARY — {len(results)} target(s)")
    print("=" * 60)
    for r in results:
        line = f"  [{r.status:9s}] {r.player}"
        if r.reason and r.status != "published":
            line += f" — {r.reason}"
        print(line)
    failed = sum(1 for r in results if r.status == "failed")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
