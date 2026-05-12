"""
lint_public.py — content-level linter for `_public.md` deliverables.

Counterpart to lint_profile.py. Validates a single public artifact
against the editorial-content rules in PUBLIC-LANGUAGE-GUIDE.md and the
regex-pure subset of PUBLIC-RUBRIC.md (V's rubric). Independent file
(P3 — one tool, one job).

Checks covered (all run on every invocation):
  - QC7 — §5.3-P citation-required percentage syntax / §8 QC7
          reconcilable temporal frame.
  - §2 — Hedge phrases (PUBLIC-RUBRIC.md §2).
  - §6 — AI-tells (rubric vocab + source-attribution; §6).
  - §7 — Em-dashes in narrative prose (§7).
  - §10 — Height/weight/wingspan outside Identity (§10 mechanical
          subset; archetype + comp-player repetition remain in V).
  - §12 — Acronyms with no parenthetical expansion anywhere in doc
          (§12 simplified; full first-use-per-section logic remains
          in V).
  - §13 — Signature column format (§13).

V (PUBLIC-RUBRIC) keeps the LLM-required checks: §1 (worst line), §3
(cosmetic stats + density target), §4 (representative patterns), §5
(archetype close), §8 (fact-check), §9 (overclaiming), §11 (clichés).
Moved out of V into this linter as of Phase C C3 (2026-05-10) to cut
per-publish reviewer token cost. §4 was rewritten from specific-moment
counting to representative-pattern counting in the 2026-05-10
narrative-essence pivot — no impact on this linter, but the docstring
above tracks V's current scope.

Invoked at:
  - Skill 7 Step 3.4 PRE-FLIGHT — runs against the draft text BEFORE
    the Step 3.5 reviewer subagent (V) fires, so mechanical drift is
    caught cheaply without paying for a reviewer turn. The draft is
    piped via stdin (`--stdin`); no draft file written.
  - Skill 7 Step 6 (defense-in-depth post-Write file-mode lint).
  - Wave-2 backfill QA (Curry, then Mitchell / JJJ / Kawhi republishes).

Default mode: flag-only (non-zero exit warns but does not block). Pre-
flight invocation in Step 3.4 uses --strict (exit 1 on findings); Step 6
post-Write lint stays flag-only until the strict promotion ships.

Exit codes:
  0 — clean
  1 — drift findings (warn in default mode, block in --strict mode)
  2 — fatal parse error

Usage:
  python scripts/lint_public.py output/Stephen_Curry/2026-05-09_public.md
  python scripts/lint_public.py output/Donovan_Mitchell/2026-04-23_public.md --strict
  python scripts/lint_public.py --all
  python scripts/lint_public.py --stdin --strict < draft.md          # pre-flight
  Get-Content draft.md | python scripts/lint_public.py --stdin --strict  # PowerShell pre-flight
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path

from config import PROJECT_ROOT, OUTPUT_DIR

# Percentage forms appearing in narrative / sub-domain rationales:
#   "40.7%"  "78%"  ".468"  ".346"
PCT_RE = re.compile(r"(?<![\w.])(\d{1,3}(?:\.\d+)?%|\.\d{3})(?![\w])")

# Indicators that a percentage has a temporal frame the reader can reconstruct.
# Loose set — the linter is flag-only by default; precision over recall.
SEASON_RE = re.compile(r"\b(19|20)\d{2}[-–]\d{2}\b")           # "2025-26"
SINCE_RE = re.compile(r"\bsince\s+(19|20)\d{2}\b", re.I)        # "since 2024"
CAREER_RE = re.compile(r"\bcareer\b", re.I)
RAW_COUNT_RE = re.compile(r"\bon\s+\d{1,4}(?:,\d{3})*\b")       # "on 343" / "on 1,200"
# Paren-count anchor: "(343 attempts" or "(251 of 623". Per PUBLIC-LANGUAGE-GUIDE
# §5.3-P since-aggregate form. Catches the inverse of RAW_COUNT_RE: "X% (343 of 850)".
PAREN_COUNT_RE = re.compile(r"\(\s*\d{1,4}(?:,\d{3})*\s+(?:attempts|of)\b", re.I)
# Bare N-of-M form (no leading paren): "251 of 623 since 2024-25".
N_OF_M_RE = re.compile(r"\b\d{1,4}(?:,\d{3})*\s+of\s+\d{1,4}(?:,\d{3})*\b", re.I)
THIS_SEASON_RE = re.compile(
    r"\bthis (season|year)\b|\blast (season|year)\b|\bprior (season|year)\b",
    re.I,
)


# ============================================
# Phase C C3 (2026-05-10) — Mechanical V-rubric checks
# Six regex-pure checks moved from V's subagent context into this
# pre-flight linter. V keeps the LLM-required checks (§1, §3, §4,
# §5, §8, §9, §11).
# ============================================

# §2 — Hedge phrases. Target 0 occurrences.
HEDGE_RE = re.compile(
    r"\b(?:might|perhaps|potentially|shows flashes of|has the potential to|"
    r"is poised to|projects as a|could become|tends to|can be)\b",
    re.I,
)

# §6 — AI-tells. Rubric vocabulary at the public surface + source attribution.
RUBRIC_VOCAB_RE = re.compile(
    r"\bTier\s+\d+\b|\bAll-NBA\s+caliber\b|\bstructural\s+zero\b|"
    r"\bcomposite\b|\bsub-domain\b|\bnon-negotiable\b|"
    r"\bfranchise\s+piece\b|\bdomain\s+score\b",
    re.I,
)
SOURCE_ATTRIBUTION_RE = re.compile(
    r"\bscouts\s+say\b|\baccording\s+to\b|\breports\s+indicate\b|"
    r"\banalysts\s+have\s+noted\b|\bconsensus\s+view\b",
    re.I,
)

# §7 — Em-dash count in narrative prose. U+2014 only; hyphen / en-dash
# do not count.
EM_DASH_CHAR = "—"

# §10 — Repetition (mechanical subset). Height / weight / wingspan in
# narrative paragraphs outside Identity. Archetype name + primary comp
# player repetition are not mechanically detectable without source-
# profile context and remain in V's scope (or Tyler's review pass).
HEIGHT_RE = re.compile(
    r"\b[5-7]['’]\d+(?:[\"”])?\b|"               # 5'0 to 7'9 (player range)
    r"\b[5-7](?:\.\d+)?\s*(?:feet|ft)\b",        # 5-7 feet / 6.5 ft (player range)
    re.I,
)
WEIGHT_RE = re.compile(r"\b\d{2,3}\s*(?:lb|lbs|pounds)\b", re.I)
WINGSPAN_RE = re.compile(r"\bwingspan\b", re.I)

# §12 — Acronyms. Pinned glossary list per PUBLIC-LANGUAGE-GUIDE
# §5.3-G. Checked at the doc level: if an acronym appears anywhere
# without a parenthetical group within ~80 chars of ANY occurrence,
# flag once. Per-scan-standalone-group first-use logic remains in V.
ACRONYMS_RE = re.compile(
    r"\bDFGPOE\b|\bPPP\b|\bA:TO\b|\bFTR\b|"
    r"\bOREB%|\bDREB%|\bTS%|"
    r"\bUSG\b|\bTOV/100\b|\bCAS\s+3PT%|"
    r"\bPnR\b|\bDHO\b|\bISO\b|"
    r"\bDPOY\b|\bMVP\b|\bFMVP\b|\b6MOTY\b"
)
PAREN_NEAR_RE = re.compile(r"\([^)]+\)")

# §13 — Signature column format.
# Cell must be `[Name] (Tier)` with Tier ∈ {Proven, Elite, Superstar,
# Iconic, Generational}. Empty cells must use the em-dash `—`.
SIGNATURE_VALID_RE = re.compile(
    r"^(?:"
    r"[A-Z][A-Za-z' ’\-.]*(?:\s[A-Z][A-Za-z' ’\-.]*)*"
    r"\s\((?:Proven|Elite|Superstar|Iconic|Generational)\)"
    r"|—)$"
)


@dataclass
class Finding:
    section: str
    line: int
    snippet: str
    message: str

    def fmt(self, path: Path) -> str:
        loc = f"{path}:{self.line}" if self.line else f"{path}"
        return f"  [{self.section}] {loc}: {self.message}\n      → {self.snippet}"


# ----------------------------------------------------------------------------
# Section extraction
# ----------------------------------------------------------------------------

NARRATIVE_HEADINGS = ("Identity", "Strength", "Weakness", "Projection-verdict")


def _extract_section(text: str, heading: str) -> tuple[str, int] | None:
    """Return (body, start_line) for a `## heading` section, or None."""
    pattern = (
        rf"^##\s+{re.escape(heading)}\s*$(?P<body>.*?)"
        rf"(?=^##\s+|\Z)"
    )
    m = re.search(pattern, text, re.MULTILINE | re.DOTALL)
    if not m:
        return None
    start_line = text[: m.start()].count("\n") + 1
    return (m.group("body").strip(), start_line)


def _extract_subdomain_rationales(text: str) -> list[tuple[int, str]]:
    """Return [(line_no, rationale_cell), ...] from the Sub-domain rationales table.

    Table shape: | # | Sub-domain | Score | Signature | Public rationale |
    Skips header + divider rows.
    """
    sec = _extract_section(text, "Sub-domain rationales")
    if sec is None:
        return []
    body, sec_start = sec
    out: list[tuple[int, str]] = []
    for offset, raw in enumerate(body.splitlines()):
        line = raw.strip()
        if not line.startswith("|"):
            continue
        if re.match(r"^\|[\s|:-]+\|$", line):  # divider row
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) != 5:
            continue
        # Header row.
        if cells[0].lower() in ("#", "id"):
            continue
        rationale = cells[4]
        out.append((sec_start + offset + 1, rationale))
    return out


# ----------------------------------------------------------------------------
# QC7 check
# ----------------------------------------------------------------------------

def _has_temporal_frame(snippet: str) -> bool:
    """Loose proxy for §5.3 reconcilable-temporal-frame rule.

    Returns True if the snippet contains any of: a season label (2025-26),
    a "since YYYY" frame, a raw count ("on 343"), a paren-count anchor
    ("(343 attempts" / "(251 of"), a bare N-of-M aggregate ("251 of 623"),
    the word "career", or a relative season phrase ("this year" / "last
    season"). Maps to PUBLIC-LANGUAGE-GUIDE §5.3-P legitimate citation
    patterns: season-anchor, since-aggregate (paren-count + N-of-M), and
    career-row.
    """
    return bool(
        SEASON_RE.search(snippet)
        or SINCE_RE.search(snippet)
        or CAREER_RE.search(snippet)
        or RAW_COUNT_RE.search(snippet)
        or PAREN_COUNT_RE.search(snippet)
        or N_OF_M_RE.search(snippet)
        or THIS_SEASON_RE.search(snippet)
    )


def _lint_text_block(section_label: str, text: str, base_line: int) -> list[Finding]:
    """Scan a narrative paragraph or rationale cell for unframed percentages."""
    out: list[Finding] = []
    for offset, line in enumerate(text.splitlines()):
        for m in PCT_RE.finditer(line):
            pct = m.group(1)
            # Window: ±60 chars around the percentage to gauge frame proximity.
            start = max(0, m.start() - 60)
            end = min(len(line), m.end() + 60)
            window = line[start:end]
            if _has_temporal_frame(window):
                continue
            # Whole-line fallback: temporal frame may sit at line start outside the window.
            if _has_temporal_frame(line):
                continue
            out.append(Finding(
                section_label,
                base_line + offset,
                line.strip(),
                f"percentage `{pct}` lacks adjacent temporal frame "
                f"(season label, raw count, 'since YYYY', or 'career')",
            ))
    return out


def _extract_signature_cells(text: str) -> list[tuple[int, str]]:
    """Return [(line_no, signature_cell), ...] from the Sub-domain rationales table.

    Table shape: | # | Sub-domain | Score | Signature | Public rationale |
    Reuses the same parsing rules as `_extract_subdomain_rationales` but
    returns column index 3 (Signature) instead of 4 (rationale).
    """
    sec = _extract_section(text, "Sub-domain rationales")
    if sec is None:
        return []
    body, sec_start = sec
    out: list[tuple[int, str]] = []
    for offset, raw in enumerate(body.splitlines()):
        line = raw.strip()
        if not line.startswith("|"):
            continue
        if re.match(r"^\|[\s|:-]+\|$", line):
            continue
        cells = [c.strip() for c in line.split("|")[1:-1]]
        if len(cells) != 5:
            continue
        if cells[0].lower() in ("#", "id"):
            continue
        signature = cells[3]
        out.append((sec_start + offset + 1, signature))
    return out


def _scan_regex_in_blocks(
    label: str,
    pattern: re.Pattern,
    blocks: list[tuple[str, str, int]],
    note: str,
) -> list[Finding]:
    """Run a regex over each (section_label, body, base_line) block and
    emit one Finding per match.
    """
    out: list[Finding] = []
    for sec_label, body, base_line in blocks:
        for offset, line in enumerate(body.splitlines()):
            for m in pattern.finditer(line):
                out.append(Finding(
                    f"{label} {sec_label}",
                    base_line + offset,
                    line.strip(),
                    f"{note}: `{m.group(0)}`",
                ))
    return out


# ----------------------------------------------------------------------------
# Phase C C3 — Mechanical V-rubric check functions
# ----------------------------------------------------------------------------

def _check_hedges(narrative_blocks, rationale_blocks) -> list[Finding]:
    """§2 — Hedge-phrase scan. Target 0 across narrative + rationale cells."""
    return _scan_regex_in_blocks(
        "§2 Hedge", HEDGE_RE,
        narrative_blocks + rationale_blocks,
        "hedge phrase (PUBLIC-RUBRIC §2; rewrite as soft commitment)",
    )


def _check_ai_tells(narrative_blocks, rationale_blocks) -> list[Finding]:
    """§6 — AI-tell scan. Two categories: rubric vocabulary + source attribution."""
    out = _scan_regex_in_blocks(
        "§6 AI-tell", RUBRIC_VOCAB_RE,
        narrative_blocks + rationale_blocks,
        "rubric vocabulary at public surface (PUBLIC-RUBRIC §6)",
    )
    out += _scan_regex_in_blocks(
        "§6 AI-tell", SOURCE_ATTRIBUTION_RE,
        narrative_blocks + rationale_blocks,
        "source-attribution phrase (PUBLIC-RUBRIC §6; synthesize, don't cite)",
    )
    return out


def _check_em_dashes(narrative_blocks) -> list[Finding]:
    """§7 — Em-dash count in narrative prose. Target 0."""
    out: list[Finding] = []
    for sec_label, body, base_line in narrative_blocks:
        for offset, line in enumerate(body.splitlines()):
            count = line.count(EM_DASH_CHAR)
            if count == 0:
                continue
            out.append(Finding(
                f"§7 Em-dash {sec_label}",
                base_line + offset,
                line.strip(),
                f"{count} em-dash(es) in narrative line (PUBLIC-RUBRIC §7; "
                f"replace with commas / semicolons / periods)",
            ))
    return out


def _check_repetition(non_identity_blocks) -> list[Finding]:
    """§10 — Repetition (mechanical subset).

    Flags height / weight / wingspan tokens in narrative paragraphs that
    are NOT Identity. Per the rubric, these dimensions belong in Identity
    only; any appearance outside is a repetition.
    """
    out: list[Finding] = []
    for sec_label, body, base_line in non_identity_blocks:
        for offset, line in enumerate(body.splitlines()):
            for pattern, note in (
                (HEIGHT_RE, "height token outside Identity"),
                (WEIGHT_RE, "weight token outside Identity"),
                (WINGSPAN_RE, "wingspan mention outside Identity"),
            ):
                for m in pattern.finditer(line):
                    out.append(Finding(
                        f"§10 Repetition {sec_label}",
                        base_line + offset,
                        line.strip(),
                        f"{note} (PUBLIC-RUBRIC §10): `{m.group(0)}`",
                    ))
    return out


def _check_acronyms(text: str) -> list[Finding]:
    """§12 — Acronym scan (simplified).

    For each acronym in the pinned glossary that appears anywhere in the
    document, check whether at least one occurrence has a parenthetical
    group within ~80 chars (either side). If no occurrence is expanded,
    flag once at the first appearance. Per-section first-use precision
    remains in V.
    """
    out: list[Finding] = []
    seen: set[str] = set()
    for m in ACRONYMS_RE.finditer(text):
        acro = m.group(0)
        if acro in seen:
            continue
        seen.add(acro)
        has_expansion = False
        for occ in re.finditer(re.escape(acro), text):
            start = max(0, occ.start() - 80)
            end = min(len(text), occ.end() + 80)
            if PAREN_NEAR_RE.search(text[start:end]):
                has_expansion = True
                break
        if has_expansion:
            continue
        line_no = text[: m.start()].count("\n") + 1
        line_start = text.rfind("\n", 0, m.start()) + 1
        line_end = text.find("\n", m.end())
        if line_end == -1:
            line_end = len(text)
        snippet = text[line_start:line_end].strip()
        out.append(Finding(
            "§12 Acronym",
            line_no,
            snippet,
            f"acronym `{acro}` never expanded in parentheses anywhere in doc "
            f"(PUBLIC-RUBRIC §12; expand at first use per scan-standalone group)",
        ))
    return out


def _check_signatures(text: str) -> list[Finding]:
    """§13 — Signature column format compliance.

    Each filled cell in the Signature column must match `[Name] (Tier)`
    with Tier ∈ {Proven, Elite, Superstar, Iconic, Generational}. Empty
    cells must be `—` (U+2014). Anything else is a format violation.
    """
    out: list[Finding] = []
    for line_no, sig in _extract_signature_cells(text):
        if not sig:
            out.append(Finding(
                "§13 Signature", line_no, "(empty cell)",
                "Signature cell empty; use `—` for absent (PUBLIC-RUBRIC §13)",
            ))
            continue
        if SIGNATURE_VALID_RE.match(sig):
            continue
        out.append(Finding(
            "§13 Signature", line_no, sig,
            "Signature cell format invalid; expected `[Name] (Proven|Elite|"
            "Superstar|Iconic|Generational)` or `—` (PUBLIC-RUBRIC §13)",
        ))
    return out


def lint_text(text: str) -> list[Finding]:
    """Lint a `_public.md`-shaped string. Used by `lint(path)` and by the
    Skill 7 Step 3.4 pre-flight (`--stdin` mode), which has the draft in
    main context and skips writing it to disk before reviewer fires.
    """
    findings: list[Finding] = []

    # Collect narrative + rationale blocks for the regex checks.
    narrative_blocks: list[tuple[str, str, int]] = []
    for heading in NARRATIVE_HEADINGS:
        sec = _extract_section(text, heading)
        if sec is None:
            continue
        body, base_line = sec
        narrative_blocks.append((f"§{heading}", body, base_line))

    rationale_blocks: list[tuple[str, str, int]] = [
        ("Sub-domain rationale", rationale, line_no)
        for line_no, rationale in _extract_subdomain_rationales(text)
    ]

    # QC7 percentage-syntax check.
    for sec_label, body, base_line in narrative_blocks:
        findings += _lint_text_block(sec_label, body, base_line)
    for sec_label, body, base_line in rationale_blocks:
        findings += _lint_text_block(sec_label, body, base_line)

    # Phase C C3 mechanical V-rubric checks.
    findings += _check_hedges(narrative_blocks, rationale_blocks)
    findings += _check_ai_tells(narrative_blocks, rationale_blocks)
    findings += _check_em_dashes(narrative_blocks)

    non_identity_blocks = [b for b in narrative_blocks if b[0] != "§Identity"]
    findings += _check_repetition(non_identity_blocks)

    findings += _check_acronyms(text)
    findings += _check_signatures(text)

    return findings


def lint(path: Path) -> list[Finding]:
    return lint_text(path.read_text(encoding="utf-8"))


# ----------------------------------------------------------------------------
# CLI
# ----------------------------------------------------------------------------

def _resolve_targets(args) -> list[Path]:
    if args.all:
        return sorted(OUTPUT_DIR.rglob("*_public.md"))
    if not args.path:
        return []
    p = Path(args.path)
    if not p.is_absolute():
        p = (PROJECT_ROOT / args.path).resolve()
    return [p]


def _run_stdin(args) -> int:
    """Pre-flight mode: lint draft text piped via stdin. Used by Skill 7
    Step 3.4 before the Step 3.5 reviewer subagents fire.
    """
    text = sys.stdin.read()
    if not text.strip():
        print("FATAL: --stdin received empty input", file=sys.stderr)
        return 2
    try:
        findings = lint_text(text)
    except Exception as e:  # noqa: BLE001
        print(f"FATAL: stdin lint — unhandled error: {e}", file=sys.stderr)
        return 2

    if not findings:
        if not args.quiet:
            print("OK   <stdin>")
        return 0

    prefix = "DRIFT" if args.strict else "WARN "
    if not args.quiet:
        print(f"{prefix} <stdin>  ({len(findings)} finding(s))")
        for f in findings:
            # Path placeholder — line numbers are still meaningful relative
            # to the stdin draft text.
            print(f.fmt(Path("<stdin>")))

    return 1 if args.strict else 0


def main() -> int:
    for stream in (sys.stdin, sys.stdout, sys.stderr):
        try:
            stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError):
            pass

    parser = argparse.ArgumentParser(description="Lint a `_public.md` for QC7 (PUBLIC-LANGUAGE-GUIDE §5.3-P / §8 QC7).")
    parser.add_argument("path", nargs="?", help="path to a `_public.md` file")
    parser.add_argument("--all", action="store_true", help="lint every `*_public.md` under output/")
    parser.add_argument("--stdin", action="store_true", help="read draft text from stdin (Skill 7 Step 3.4 pre-flight mode)")
    parser.add_argument("--strict", action="store_true", help="exit 1 on findings (block); default is exit 0 with warning report")
    parser.add_argument("--quiet", action="store_true", help="summary only; no per-finding output")
    args = parser.parse_args()

    if args.stdin:
        if args.path or args.all:
            parser.error("--stdin is mutually exclusive with path/--all")
        return _run_stdin(args)

    targets = _resolve_targets(args)
    if not targets:
        parser.error("provide a path, --all, or --stdin")

    total = clean = drift = fatal = 0

    for path in targets:
        total += 1
        if not path.exists():
            print(f"FATAL: {path} does not exist", file=sys.stderr)
            fatal += 1
            continue
        try:
            findings = lint(path)
        except Exception as e:  # noqa: BLE001
            print(f"FATAL: {path} — unhandled error: {e}", file=sys.stderr)
            fatal += 1
            continue

        if not findings:
            clean += 1
            if not args.quiet:
                print(f"OK   {path}")
            continue

        drift += 1
        prefix = "DRIFT" if args.strict else "WARN "
        if not args.quiet:
            print(f"{prefix} {path}  ({len(findings)} finding(s))")
            for f in findings:
                print(f.fmt(path))

    if total > 1 or args.all:
        print()
        print(f"SUMMARY — {total} file(s): {clean} clean, {drift} drift, {fatal} fatal")

    if fatal:
        return 2
    if drift and args.strict:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
