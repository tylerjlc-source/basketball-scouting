"""
lint_profile.py — canonical-format linter for `_profile.md` deliverables.

Validates a single profile against the canon spec defined in
skills/scout-output.md (§1, §4, §5, §9, §10, §11). Invoked at:
  - Skill 5 QC6 (after profile assembly, before delivery)
  - Skill 7 Step 2 (pre-flight before publish drafting)

Design: defense-in-depth at the deliverable boundary, so the JSON export
pipeline (export_public_json.py) sees only canon-clean profiles. Strict-
everywhere parser shape — drift is caught HERE, not loosened in the
parser. Linter is a single subprocess call from each skill; no shared
state with the parser.

Exit codes:
  0 — clean
  1 — drift (one or more findings; report and fix in source)
  2 — fatal parse error (file unreadable, section missing entirely)

Usage:
  python scripts/lint_profile.py output/Donovan_Mitchell/2026-04-23_profile.md
  python scripts/lint_profile.py --all                  # lint every profile
  python scripts/lint_profile.py --all --quiet          # summary only
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from config import PROJECT_ROOT, OUTPUT_DIR

POSITION_RE = re.compile(r"^(PG|SG|SF|PF|C)(/(PG|SG|SF|PF|C))?$")
TIER_RE = re.compile(r"^(\d+)\s*[—-]\s*(.+)$")
COMPOSITE_RE = re.compile(r"^\d+\.\d{2}$")
DATE_RE = re.compile(r"^\d{4}-\d{2}-\d{2}$")

REQUIRED_S1_FIELDS = ("Player", "Position", "Group", "Archetype", "Composite", "Tier")
CONFIDENCE_VALUES = ("tight", "moderate", "wide")


@dataclass
class Finding:
    section: str
    line: int  # 1-based; 0 if section-level
    message: str

    def fmt(self, path: Path) -> str:
        loc = f"{path}:{self.line}" if self.line else f"{path}"
        return f"  [{self.section}] {loc}: {self.message}"


def lint(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    findings: list[Finding] = []

    findings += _lint_section_1(text, lines)
    findings += _lint_section_4(text)
    findings += _lint_section_5(text)
    findings += _lint_section_9(text)
    findings += _lint_section_10(text)
    findings += _lint_section_11(text, _composite_from_section_1(text))

    return findings


# ----------------------------------------------------------------------------
# Section helpers
# ----------------------------------------------------------------------------

_SECTION_PATTERN = (
    r"^##\s+Section\s+{n}\s+[—-].*?$(.*?)(?=^##\s+Section\s+\d+\s+[—-]|^##\s+(?:Quality|How|Anchor)|\Z)"
)


def _read_section(text: str, n: int) -> str | None:
    m = re.search(_SECTION_PATTERN.format(n=n), text, re.MULTILINE | re.DOTALL)
    return m.group(1).strip() if m else None


def _section_start_line(text: str, n: int) -> int:
    for i, line in enumerate(text.splitlines(), 1):
        if re.match(rf"^##\s+Section\s+{n}\s+[—-]", line):
            return i
    return 0


def _composite_from_section_1(text: str) -> str | None:
    body = _read_section(text, 1)
    if body is None:
        return None
    for line in body.splitlines():
        m = re.match(r"\|\s*\*\*Composite\*\*\s*\|\s*\*\*([0-9]+\.[0-9]{2})\*\*\s*\|", line)
        if m:
            return m.group(1)
        m = re.match(r"\|\s*Composite\s*\|\s*\*?\*?([0-9]+\.[0-9]{2})\*?\*?\s*\|", line)
        if m:
            return m.group(1)
    return None


# ----------------------------------------------------------------------------
# Section 1 — Header
# ----------------------------------------------------------------------------

def _lint_section_1(text: str, lines: list[str]) -> list[Finding]:
    out: list[Finding] = []
    body = _read_section(text, 1)
    start = _section_start_line(text, 1)

    # Heading form: prefer em-dash. Allow ASCII hyphen but warn? Per plan, em-dash is canon.
    heading_re = re.compile(r"^##\s+Section\s+1\s+(.)\s+Header\s*$")
    found_heading = False
    for i, line in enumerate(lines, 1):
        m = heading_re.match(line)
        if m:
            found_heading = True
            if m.group(1) != "—":
                out.append(Finding("§1", i, f"heading separator must be em-dash (—), got {m.group(1)!r}"))
            break
    if not found_heading:
        if body is None:
            out.append(Finding("§1", 0, "Section 1 not found (expected `## Section 1 — Header`)"))
            return out
        out.append(Finding("§1", start or 0, "heading does not match `## Section 1 — Header`"))

    if body is None:
        return out

    fields = _parse_kv_table_strict(body, section_start=start, out=out)

    for required in REQUIRED_S1_FIELDS:
        if required not in fields:
            out.append(Finding("§1", start, f"missing required field `{required}`"))

    # Drift variants.
    if "Listed position" in fields:
        out.append(Finding("§1", start, "field `Listed position` must be renamed to `Position`"))
    if "Composite (OVR)" in fields:
        out.append(Finding("§1", start, "field `Composite (OVR)` must be renamed to `Composite`"))

    # Forbidden rows in §1 (belong in §8).
    for forbidden in ("Band", "Placement"):
        if forbidden in fields:
            out.append(Finding("§1", start, f"`{forbidden}` row not allowed in §1 (belongs in §8)"))

    if "Position" in fields:
        pos = fields["Position"]
        if not POSITION_RE.match(pos):
            out.append(Finding("§1", start, f"`Position` value {pos!r} not a position code (expected `PG/SG/SF/PF/C`, optionally two joined by `/`)"))

    if "Tier" in fields:
        tier = fields["Tier"]
        if not TIER_RE.match(tier):
            out.append(Finding("§1", start, f"`Tier` value {tier!r} does not match `N — label` form"))

    if "Composite" in fields:
        comp_raw = fields["Composite"]
        comp = comp_raw.strip("*").strip()
        if not COMPOSITE_RE.match(comp):
            out.append(Finding("§1", start, f"`Composite` value must be two-decimal float (e.g. `8.40`), got {comp_raw!r}"))

    if "Evaluation Date" in fields:
        ed = fields["Evaluation Date"]
        if not DATE_RE.match(ed):
            out.append(Finding("§1", start, f"`Evaluation Date` must be `YYYY-MM-DD`, got {ed!r}"))

    return out


def _parse_kv_table_strict(body: str, section_start: int, out: list[Finding]) -> dict[str, str]:
    """Parse `| **Field** | value |` rows. Field name MUST be bold-wrapped.

    Composite value MUST also be bold-wrapped. Other values are free-form.
    Records findings for any non-bold field name or non-bold Composite value.
    """
    fields: dict[str, str] = {}
    for offset, raw in enumerate(body.splitlines()):
        # Skip the table header / divider rows.
        if not raw.lstrip().startswith("|"):
            continue
        if re.match(r"^\|[\s|:-]+\|", raw.strip()):  # divider row: | --- | --- |
            continue
        cells = [c.strip() for c in raw.split("|")[1:-1]]
        if len(cells) != 2:
            continue
        field_cell, value_cell = cells
        # Header row.
        if field_cell.lower() == "field" and value_cell.lower() == "value":
            continue

        bold_field = re.match(r"^\*\*(.+?)\*\*$", field_cell)
        if not bold_field:
            out.append(Finding(
                "§1",
                section_start + offset + 1,
                f"field name `{field_cell}` must be bold-wrapped (`**{field_cell}**`)",
            ))
            field_name = field_cell
        else:
            field_name = bold_field.group(1)

        # Composite value MUST be bold.
        if field_name == "Composite":
            if not (value_cell.startswith("**") and value_cell.endswith("**")):
                out.append(Finding(
                    "§1",
                    section_start + offset + 1,
                    f"`Composite` value `{value_cell}` must be bold-wrapped (`**{value_cell}**`)",
                ))

        # Strip outer ** for storage.
        clean = value_cell
        if clean.startswith("**") and clean.endswith("**") and len(clean) >= 4:
            clean = clean[2:-2].strip()
        fields[field_name] = clean
    return fields


# ----------------------------------------------------------------------------
# Section 4 — Sub-domain scores
# ----------------------------------------------------------------------------

def _lint_section_4(text: str) -> list[Finding]:
    body = _read_section(text, 4)
    start = _section_start_line(text, 4)
    if body is None:
        return [Finding("§4", 0, "Section 4 not found")]

    sub_ids: list[int] = []
    row_re = re.compile(r"\|\s*(\d+)\s*\|\s*([^|]+?)\s*\|\s*(\d+\.\d)\s*\|")
    for line in body.splitlines():
        m = row_re.match(line.strip())
        if m:
            sub_ids.append(int(m.group(1)))

    if len(sub_ids) != 26:
        return [Finding("§4", start, f"expected 26 sub-domain rows, found {len(sub_ids)}")]
    if sorted(sub_ids) != list(range(1, 27)):
        return [Finding("§4", start, f"sub-domain ids not 1–26 (got {sorted(set(sub_ids))})")]
    return []


# ----------------------------------------------------------------------------
# Section 5 — Domain summaries
# ----------------------------------------------------------------------------

def _lint_section_5(text: str) -> list[Finding]:
    body = _read_section(text, 5)
    start = _section_start_line(text, 5)
    if body is None:
        return [Finding("§5", 0, "Section 5 not found")]

    domain_ids: list[int] = []
    row_re = re.compile(r"\|\s*D(\d+)\s+([^|]+?)\s*\|\s*(\d+\.\d)\s*\|")
    for line in body.splitlines():
        m = row_re.match(line.strip())
        if m and 1 <= int(m.group(1)) <= 8:
            domain_ids.append(int(m.group(1)))

    if len(domain_ids) != 8:
        return [Finding("§5", start, f"expected 8 domain rows (D1–D8), found {len(domain_ids)}")]
    if sorted(domain_ids) != list(range(1, 9)):
        return [Finding("§5", start, f"domain ids not D1–D8 (got {sorted(set(domain_ids))})")]
    return []


# ----------------------------------------------------------------------------
# Section 9 — Projection Output Block
# ----------------------------------------------------------------------------

def _lint_section_9(text: str) -> list[Finding]:
    body = _read_section(text, 9)
    start = _section_start_line(text, 9)
    if body is None:
        return [Finding("§9", 0, "Section 9 not found")]

    out: list[Finding] = []
    pot = _kv_match(body, "POT")
    min_v = _kv_match(body, "MIN")
    max_v = _kv_match(body, "MAX")
    if pot is None:
        out.append(Finding("§9", start, "missing `POT:` line"))
    if min_v is None:
        out.append(Finding("§9", start, "missing `MIN:` (or `Min:`) line"))
    if max_v is None:
        out.append(Finding("§9", start, "missing `MAX:` (or `Max:`) line"))

    conf_match = re.search(
        r"^\s*CONFIDENCE\s*[:|]\s*(\w+)",
        body, re.MULTILINE | re.IGNORECASE,
    )
    if not conf_match:
        out.append(Finding("§9", start, "missing `CONFIDENCE:` line"))
    elif conf_match.group(1).lower() not in CONFIDENCE_VALUES:
        out.append(Finding(
            "§9", start,
            f"`CONFIDENCE` value `{conf_match.group(1)}` not in {CONFIDENCE_VALUES}",
        ))

    # Cross-check Min < POT < Max where all three present.
    if pot is not None and min_v is not None and max_v is not None:
        if not (min_v <= pot <= max_v):
            out.append(Finding(
                "§9", start,
                f"projection ordering violated: Min={min_v} POT={pot} Max={max_v}",
            ))
        if pot > 9.99:
            out.append(Finding("§9", start, f"POT {pot} exceeds hard ceiling 9.99 (QC4)"))

    # Prospect track: if any of BUST/AVG/BOOM present, all three must be and sum to ~100.
    bust = _kv_match(body, "BUST(?:%|_PCT)?", max_val=100)
    avg = _kv_match(body, "AVG(?:%|_PCT)?", max_val=100)
    boom = _kv_match(body, "BOOM(?:%|_PCT)?", max_val=100)
    triplet = [bust, avg, boom]
    if any(v is not None for v in triplet):
        if not all(v is not None for v in triplet):
            out.append(Finding(
                "§9", start,
                f"prospect projection requires all three of BUST/AVG/BOOM (got bust={bust}, avg={avg}, boom={boom})",
            ))
        else:
            total = bust + avg + boom
            if abs(total - 100.0) > 0.5:
                out.append(Finding(
                    "§9", start,
                    f"BUST+AVG+BOOM should sum to 100, got {total}",
                ))

    return out


def _kv_match(body: str, label: str, max_val: float = 10.0) -> float | None:
    m = re.search(
        rf"^\s*{label}\s*[:|]\s*(\d+(?:\.\d{{1,2}})?)",
        body, re.MULTILINE | re.IGNORECASE,
    )
    if not m:
        return None
    try:
        v = float(m.group(1))
    except ValueError:
        return None
    return v if v <= max_val + 0.01 else None


# ----------------------------------------------------------------------------
# Section 10 — NBA Comp
# ----------------------------------------------------------------------------

def _lint_section_10(text: str) -> list[Finding]:
    body = _read_section(text, 10)
    start = _section_start_line(text, 10)
    if body is None:
        return [Finding("§10", 0, "Section 10 not found")]

    has_lineage = bool(re.search(r"\*\*LINEAGE COMP:\s*[^*]+\*\*", body))
    comp_headers = re.findall(r"^###\s+(NBA\s+)?Comp\s+\d+:\s+.+$", body, re.MULTILINE)
    has_comp_headers = len(comp_headers) > 0
    nba_prefix_count = sum(1 for h in comp_headers if h)  # h is the NBA prefix capture group

    if has_lineage and has_comp_headers:
        return [Finding(
            "§10", start,
            "both `**LINEAGE COMP:` and `### Comp N:` headers present — pick exactly one branch (NBA-vet lineage OR prospect multi-comp)",
        )]
    if not has_lineage and not has_comp_headers:
        return [Finding(
            "§10", start,
            "no recognized comp form — expected single `**LINEAGE COMP: [Player] ([era])** — prose.` (NBA vet) OR ≥2 `### Comp N: Player` blocks (prospect)",
        )]

    out: list[Finding] = []
    if has_lineage:
        # NBA-vet branch — exactly one occurrence; no `**Primary comp:` / `**Secondary comp:` legacy forms.
        lineage_count = len(re.findall(r"\*\*LINEAGE COMP:\s*[^*]+\*\*", body))
        if lineage_count != 1:
            out.append(Finding("§10", start, f"expected exactly one `**LINEAGE COMP:` line, got {lineage_count}"))
        if re.search(r"\*\*Primary comp:", body):
            out.append(Finding("§10", start, "legacy `**Primary comp:` prose form forbidden — collapse into single LINEAGE COMP line"))
        if re.search(r"\*\*Secondary comp:", body):
            out.append(Finding("§10", start, "legacy `**Secondary comp:` prose form forbidden — flag-comp notes go in trailing prose, not a separate header"))
        # No tier glyph required on lineage — but flag stray glyph if it sits on the LINEAGE line.
        for line in body.splitlines():
            if "**LINEAGE COMP:" in line and re.search(r"[🟢🟡🔴]", line):
                out.append(Finding("§10", start, "tier glyph (🟢/🟡/🔴) forbidden on LINEAGE COMP line — lineage is qualitative-only per § B.4"))
                break
    else:
        # Prospect branch.
        if nba_prefix_count > 0:
            out.append(Finding("§10", start, "prospect comp headers must read `### Comp N:` not `### NBA Comp N:`"))
        if len(comp_headers) < 2:
            out.append(Finding("§10", start, f"prospect track requires 2–3 comps, got {len(comp_headers)}"))
        if len(comp_headers) > 3:
            out.append(Finding("§10", start, f"prospect track allows max 3 comps, got {len(comp_headers)}"))
        # Each comp block must have a **Tier:** line with a recognized tier.
        comp_blocks = re.split(r"^###\s+(?:NBA\s+)?Comp\s+\d+:\s+", body, flags=re.MULTILINE)[1:]
        for idx, block in enumerate(comp_blocks, 1):
            tier_m = re.search(r"\*\*Tier:\*\*\s*([🟢🟡🔴])?\s*(\w+)?", block)
            if not tier_m:
                out.append(Finding("§10", start, f"Comp {idx} missing `**Tier:**` bullet"))
                continue
            glyph = tier_m.group(1) or ""
            word = (tier_m.group(2) or "").strip()
            glyph_to_word = {"🟢": "Full", "🟡": "Partial", "🔴": "None"}
            canonical = glyph_to_word.get(glyph) or (word if word in ("Full", "Partial", "None") else None)
            if canonical is None:
                out.append(Finding("§10", start, f"Comp {idx} `**Tier:**` line not canonical (glyph={glyph!r}, word={word!r})"))

    return out


# ----------------------------------------------------------------------------
# Section 11 — Anchor Library Entry
# ----------------------------------------------------------------------------

def _lint_section_11(text: str, s1_composite: str | None) -> list[Finding]:
    body = _read_section(text, 11)
    start = _section_start_line(text, 11)
    if body is None:
        return [Finding("§11", 0, "Section 11 not found — required on every evaluation")]

    out: list[Finding] = []
    # Find a row of form: | composite | Player | Status | Group | Archetype | Notes |
    row_re = re.compile(r"^\|\s*(\d+\.\d{2})\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*$")
    matched = None
    for line in body.splitlines():
        m = row_re.match(line.strip())
        if m:
            matched = m
            break
    if not matched:
        out.append(Finding("§11", start, "missing canonical anchor row `| composite | Player | Status | Group | Archetype | Notes |`"))
        return out

    s11_composite = matched.group(1)
    s11_status = matched.group(3).strip()
    s11_group = matched.group(4).strip()

    if s1_composite and s11_composite != s1_composite:
        out.append(Finding(
            "§11", start,
            f"row composite {s11_composite} ≠ §1 composite {s1_composite} (must match)",
        ))

    if s11_group not in ("Guard", "Wing", "Big"):
        out.append(Finding("§11", start, f"Group column `{s11_group}` not in (Guard, Wing, Big)"))

    if not (s11_status in ("Active", "Retired") or re.match(r"^\d{4}\s+draft\s+class$", s11_status, re.IGNORECASE)):
        out.append(Finding("§11", start, f"Status column `{s11_status}` not Active / Retired / `YYYY draft class`"))

    return out


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def _resolve_targets(args) -> list[Path]:
    if args.all:
        return sorted(OUTPUT_DIR.rglob("*_profile.md"))
    if not args.path:
        return []
    p = Path(args.path)
    if not p.is_absolute():
        p = (PROJECT_ROOT / args.path).resolve()
    return [p]


def main() -> int:
    # Windows consoles default to cp1252; § / em-dash / ≥ break the default codec.
    for stream in (sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    parser = argparse.ArgumentParser(description="Lint a `_profile.md` against canon spec.")
    parser.add_argument("path", nargs="?", help="path to a `_profile.md` file")
    parser.add_argument("--all", action="store_true", help="lint every `*_profile.md` under output/")
    parser.add_argument("--quiet", action="store_true", help="summary only; no per-finding output")
    args = parser.parse_args()

    targets = _resolve_targets(args)
    if not targets:
        parser.error("provide a path or --all")

    total_files = 0
    clean_files = 0
    drift_files = 0
    fatal_files = 0

    for path in targets:
        total_files += 1
        if not path.exists():
            print(f"FATAL: {path} does not exist", file=sys.stderr)
            fatal_files += 1
            continue
        try:
            findings = lint(path)
        except Exception as e:  # noqa: BLE001
            print(f"FATAL: {path} — unhandled error: {e}", file=sys.stderr)
            fatal_files += 1
            continue

        if not findings:
            clean_files += 1
            if not args.quiet:
                print(f"OK   {path}")
            continue

        drift_files += 1
        if not args.quiet:
            print(f"DRIFT {path}  ({len(findings)} finding(s))")
            for f in findings:
                print(f.fmt(path))

    if total_files > 1 or args.all:
        print()
        print(f"SUMMARY — {total_files} file(s): {clean_files} clean, {drift_files} drift, {fatal_files} fatal")

    if fatal_files:
        return 2
    if drift_files:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
