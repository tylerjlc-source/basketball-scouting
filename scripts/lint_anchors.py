"""
lint_anchors.py — pre-flight integrity check for the anchor-library tier split.

The anchor library is split into per-tier files at docs/anchors/Tier_N.md
with an index at docs/ANCHOR-LIBRARY.md (commit 4975211, A1, 2026-05-08).
The split multiplies the surfaces where the same fact (an anchor's tier,
the total count, the per-tier count) can live, which makes silent drift
possible across maintenance edits.

This linter locks three integrity invariants:

  C1 — Composite-in-band.
       Every row in Tier_N.md has a composite value that falls inside the
       band defined by that file's "### Tier N — A.BB–C.DD — ..." heading.
       A composite of 8.15 written to Tier_7 (floor 8.29) gets caught here.

  C2 — Per-tier count sync.
       ANCHOR-LIBRARY.md's tier-index table reports an "Anchors" count per
       tier. That count must equal the actual data-row count of the
       corresponding Tier_N.md file.

  C3 — Cached-total sync.
       ANCHOR-LIBRARY.md "**Anchor count:** N" and CLAUDE.md's
       "N confirmed anchor players" both cache the grand total. Both must
       equal the sum of per-tier row counts.

Invocation:
  python scripts/lint_anchors.py            # human-readable report
  python scripts/lint_anchors.py --strict   # exit 1 on any finding

Exit codes:
  0 — clean
  1 — drift findings (warn in default mode, block in --strict mode)
  2 — fatal parse error
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path

from config import DOCS_DIR, PROJECT_ROOT


ANCHORS_DIR = DOCS_DIR / "anchors"
INDEX_PATH = DOCS_DIR / "ANCHOR-LIBRARY.md"
CLAUDE_MD_PATH = PROJECT_ROOT / "CLAUDE.md"

# "### Tier 5 — 8.60–8.89 — Perennial All-Star — legitimate star"
# Accepts en-dash (U+2013) or hyphen between the band endpoints.
TIER_HEADING_RE = re.compile(
    r"^###\s+Tier\s+(?P<tier>\d{1,2})\s+[—\-]\s+"
    r"(?P<low>\d+\.\d{2})[–\-](?P<high>\d+\.\d{2})\s+[—\-]",
)

# A data row in a tier table: "| 8.88 | Jayson Tatum | ... |"
# First cell must be a composite (digit.digit{2}).
DATA_ROW_RE = re.compile(r"^\|\s*(?P<composite>\d+\.\d{2})\s*\|")

# Tier-index table row in ANCHOR-LIBRARY.md:
# "| 5 | 8.60–8.89 | Perennial All-Star | [docs/anchors/Tier_5.md](anchors/Tier_5.md) | 11 |"
INDEX_ROW_RE = re.compile(
    r"^\|\s*(?P<tier>\d{1,2})\s*\|\s*"
    r"(?P<band>\d+\.\d{2}[–\-]\d+\.\d{2})\s*\|\s*"
    r"[^|]+\|\s*"  # label column
    r"[^|]+\|\s*"  # file-link column
    r"(?P<count>\d+|\*no anchors yet\*)\s*\|",
)

# "**Anchor count:** 116 confirmed players ..."
INDEX_TOTAL_RE = re.compile(r"\*\*Anchor count:\*\*\s+(?P<total>\d+)")

# CLAUDE.md doc-map line: "... 116 confirmed anchor players, split per-tier ..."
CLAUDE_TOTAL_RE = re.compile(
    r"(?P<total>\d+)\s+confirmed\s+anchor\s+players",
    re.I,
)


@dataclass
class TierFile:
    tier: int
    path: Path
    band_low: float
    band_high: float
    composites: list[float] = field(default_factory=list)

    @property
    def count(self) -> int:
        return len(self.composites)


@dataclass
class Finding:
    severity: str  # "fatal" or "drift"
    check: str
    message: str

    def render(self) -> str:
        return f"  [{self.check}] {self.message}"


def parse_tier_file(path: Path) -> TierFile | None:
    """Return TierFile, or None if the file does not contain a parseable
    tier heading. Raises ValueError on malformed data rows."""
    text = path.read_text(encoding="utf-8")
    tier: int | None = None
    low: float | None = None
    high: float | None = None
    composites: list[float] = []

    for line in text.splitlines():
        m = TIER_HEADING_RE.match(line)
        if m:
            tier = int(m["tier"])
            low = float(m["low"])
            high = float(m["high"])
            continue
        if tier is None:
            continue
        m = DATA_ROW_RE.match(line)
        if m:
            composites.append(float(m["composite"]))

    if tier is None or low is None or high is None:
        return None
    return TierFile(tier=tier, path=path, band_low=low, band_high=high,
                    composites=composites)


def parse_index(path: Path) -> tuple[dict[int, int], int | None]:
    """Return (per_tier_counts, cached_total) from ANCHOR-LIBRARY.md.
    per_tier_counts maps tier number to the index-row "Anchors" count
    (omitting "*no anchors yet*" rows since those don't have files yet)."""
    text = path.read_text(encoding="utf-8")
    per_tier: dict[int, int] = {}
    cached_total: int | None = None

    for line in text.splitlines():
        m = INDEX_ROW_RE.match(line)
        if m:
            count_str = m["count"].strip()
            if count_str.startswith("*"):  # "*no anchors yet*"
                continue
            per_tier[int(m["tier"])] = int(count_str)
            continue
        m = INDEX_TOTAL_RE.search(line)
        if m and cached_total is None:
            cached_total = int(m["total"])

    return per_tier, cached_total


def parse_claude_md(path: Path) -> int | None:
    """Return the cached anchor count from CLAUDE.md's doc map, or None
    if the cached line is missing."""
    text = path.read_text(encoding="utf-8")
    m = CLAUDE_TOTAL_RE.search(text)
    return int(m["total"]) if m else None


def run_checks() -> list[Finding]:
    findings: list[Finding] = []

    tier_files: list[TierFile] = []
    for path in sorted(ANCHORS_DIR.glob("Tier_*.md")):
        try:
            tf = parse_tier_file(path)
        except ValueError as exc:
            findings.append(Finding("fatal", "parse",
                                    f"{path.name}: {exc}"))
            continue
        if tf is None:
            findings.append(Finding("fatal", "parse",
                                    f"{path.name}: no '### Tier N — X.XX–Y.YY' "
                                    f"heading found"))
            continue
        tier_files.append(tf)

    # ---- C1: composite-in-band ----
    for tf in tier_files:
        for composite in tf.composites:
            if not (tf.band_low <= composite <= tf.band_high):
                findings.append(Finding(
                    "drift",
                    "C1",
                    f"{tf.path.name}: composite {composite:.2f} outside "
                    f"band {tf.band_low:.2f}–{tf.band_high:.2f}",
                ))

    # ---- C2: per-tier count sync ----
    try:
        index_counts, cached_total = parse_index(INDEX_PATH)
    except FileNotFoundError:
        findings.append(Finding("fatal", "parse",
                                f"missing {INDEX_PATH.name}"))
        return findings

    tier_file_map = {tf.tier: tf for tf in tier_files}
    all_tier_nums = sorted(set(index_counts) | set(tier_file_map))
    for tier in all_tier_nums:
        tf = tier_file_map.get(tier)
        index_count = index_counts.get(tier)
        if tf is None and index_count and index_count > 0:
            findings.append(Finding(
                "drift",
                "C2",
                f"Tier {tier}: index reports {index_count} rows but "
                f"Tier_{tier}.md not found",
            ))
        elif tf is not None and index_count is None:
            findings.append(Finding(
                "drift",
                "C2",
                f"Tier {tier}: Tier_{tier}.md exists with {tf.count} rows "
                f"but no index entry in {INDEX_PATH.name}",
            ))
        elif tf is not None and index_count != tf.count:
            findings.append(Finding(
                "drift",
                "C2",
                f"Tier {tier}: file has {tf.count} rows but index "
                f"reports {index_count}",
            ))

    # ---- C3: cached-total sync ----
    actual_total = sum(tf.count for tf in tier_files)

    if cached_total is None:
        findings.append(Finding(
            "drift",
            "C3",
            f"{INDEX_PATH.name}: '**Anchor count:** N' line not found",
        ))
    elif cached_total != actual_total:
        findings.append(Finding(
            "drift",
            "C3",
            f"{INDEX_PATH.name}: cached total {cached_total} != actual sum "
            f"{actual_total}",
        ))

    try:
        claude_total = parse_claude_md(CLAUDE_MD_PATH)
    except FileNotFoundError:
        findings.append(Finding("fatal", "parse",
                                f"missing {CLAUDE_MD_PATH.name}"))
        return findings

    if claude_total is None:
        findings.append(Finding(
            "drift",
            "C3",
            "CLAUDE.md: 'N confirmed anchor players' line not found",
        ))
    elif claude_total != actual_total:
        findings.append(Finding(
            "drift",
            "C3",
            f"CLAUDE.md: cached total {claude_total} != actual sum "
            f"{actual_total}",
        ))

    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero on drift findings (default: warn-only).",
    )
    args = parser.parse_args()

    findings = run_checks()

    if not findings:
        print("lint_anchors: clean — C1 in-band, C2 index counts, "
              "C3 cached totals all sync")
        return 0

    fatal = [f for f in findings if f.severity == "fatal"]
    drift = [f for f in findings if f.severity == "drift"]

    if fatal:
        print(f"lint_anchors: FATAL — {len(fatal)} parse error(s)")
        for f in fatal:
            print(f.render())

    if drift:
        print(f"lint_anchors: DRIFT — {len(drift)} finding(s)")
        for f in drift:
            print(f.render())

    if fatal:
        return 2
    return 1 if args.strict else 0


if __name__ == "__main__":
    sys.exit(main())
