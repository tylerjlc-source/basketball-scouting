"""
lint_public.py — content-level linter for `_public.md` deliverables.

Counterpart to lint_profile.py. Validates a single public artifact against
the editorial-content rules in PUBLIC-LANGUAGE-GUIDE.md — currently §5.3-P
(citation-required percentage syntax) / §8 QC7 (reconcilable temporal
frame). Independent file (P3 — one tool, one job).

Invoked at:
  - Skill 7 Step 3.4 PRE-FLIGHT — runs against the draft text BEFORE the
    Step 3.5 reviewer subagents (V + F) fire, so mechanical bare-%
    failures are caught cheaply without paying for a reviewer turn.
    The draft is piped via stdin (`--stdin`); no draft file written.
  - Skill 7 Step 6 (defense-in-depth post-Write file-mode lint)
  - Wave-2 backfill QA (Curry, then Mitchell / JJJ / Kawhi republishes)

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


def lint_text(text: str) -> list[Finding]:
    """Lint a `_public.md`-shaped string. Used by `lint(path)` and by the
    Skill 7 Step 3.4 pre-flight (`--stdin` mode), which has the draft in
    main context and skips writing it to disk before reviewer fires.
    """
    findings: list[Finding] = []

    for heading in NARRATIVE_HEADINGS:
        sec = _extract_section(text, heading)
        if sec is None:
            continue
        body, base_line = sec
        findings += _lint_text_block(f"§{heading}", body, base_line)

    for line_no, rationale in _extract_subdomain_rationales(text):
        findings += _lint_text_block(
            "Sub-domain rationale",
            rationale,
            line_no,
        )

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
    for stream in (sys.stdout, sys.stderr):
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
