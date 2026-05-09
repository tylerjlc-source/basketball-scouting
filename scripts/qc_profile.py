#!/usr/bin/env python3
"""
Run deterministic QC checks on a finished player profile.

Catches transcription drift and consistency errors that don't require
LLM judgment. Skips QC3 (narrative integrity, LLM-only) and QC5 (source
fidelity, requires Skills 2-4 persistence we explicitly didn't build).

Checks:
  QC1.1  Sections 1-10 all present
  QC1.2  No placeholder strings (e.g. [TODO], [X.XX], <placeholder>)
  QC2.1  Composite in Section 1 == Composite in Section 8
  QC2.2  Tier matches the canonical band table for the composite
  QC4.1  Projection percentages sum to 100 (prospect); omitted for vet
  QC4.2  Projection midpoint (Section 9) == Composite (Section 1)

Run from project root:
  python scripts/qc_profile.py output/[Player]/[YYYY-MM-DD]_profile.md

Exit 0 = all checks pass; exit 1 = any FAIL or ERROR.
"""

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


TIER_BANDS = [
    (1, 9.80, 10.00),
    (2, 9.50, 9.79),
    (3, 9.20, 9.49),
    (4, 8.90, 9.19),
    (5, 8.60, 8.89),
    (6, 8.30, 8.59),
    (7, 7.90, 8.29),
    (8, 7.50, 7.89),
    (9, 6.80, 7.49),
    (10, 5.80, 6.79),
]

# Strings that should never appear in a finished profile (template placeholders
# left over from drafting). Kept narrow to avoid false positives in narrative.
PLACEHOLDER_PATTERNS = [
    r"\[TODO\]",
    r"\[X\.XX\]",
    r"\[X\.X\]",
    r"\[N\]",
    r"<placeholder>",
    r"\[your text here\]",
    r"\[fill in\]",
]


def normalize(body):
    """Strip markdown bold markers so the regex matches both bolded and unbolded variants."""
    return body.replace("**", "")


def expected_tier(composite):
    for t, lo, hi in TIER_BANDS:
        if lo <= composite <= hi:
            return t
    return None


def find_section(text, n):
    """Return (start, end) byte offsets of `## Section N — ...`, or None."""
    pattern = rf"^## Section {n} [—-]"
    m = re.search(pattern, text, flags=re.MULTILINE)
    if not m:
        return None
    start = m.start()
    nxt = re.search(r"^## ", text[start + 1 :], flags=re.MULTILINE)
    end = start + 1 + nxt.start() if nxt else len(text)
    return start, end


def section_body(text, n):
    """Return the body of Section N with `**` markers stripped, or None."""
    section = find_section(text, n)
    if not section:
        return None
    return normalize(text[section[0] : section[1]])


def extract_section1_composite(text):
    body = section_body(text, 1)
    if body is None:
        return None
    m = re.search(r"\|\s*Composite\s*\|\s*(\d+\.\d+)", body, flags=re.IGNORECASE)
    return float(m.group(1)) if m else None


def extract_section1_tier(text):
    body = section_body(text, 1)
    if body is None:
        return None
    m = re.search(r"\|\s*Tier\s*\|\s*(\d+)", body, flags=re.IGNORECASE)
    return int(m.group(1)) if m else None


def extract_section8_composite_tier(text):
    body = section_body(text, 8)
    if body is None:
        return None, None
    # Match "Composite: X.XX <separator> Tier N" with flexible separator
    # (em-dash, hyphen, pipe, or other punctuation between the two values).
    m = re.search(
        r"Composite:\s*(\d+\.\d+).{0,40}?\bTier:?\s+(\d+)\b",
        body,
        flags=re.IGNORECASE | re.DOTALL,
    )
    if not m:
        return None, None
    return float(m.group(1)), int(m.group(2))


def parse_pct(s):
    """Parse a value like '15.0' or '15.0%' as float. Return None if non-numeric."""
    if s is None:
        return None
    s = s.strip().rstrip("%").rstrip(",")
    try:
        return float(s)
    except ValueError:
        return None


def extract_projection(text):
    body = section_body(text, 9)
    if body is None:
        return {}
    out = {}

    # Status state — "State N" appears in code-block ("STATUS: State N: ...")
    # and in table format ("| Status | State N: ...")
    m = re.search(r"\bState\s+(\d+)\b", body)
    if m:
        out["state"] = int(m.group(1))

    # Projection midpoint — code block: "PROJECTION MIDPOINT:    X.XX"
    # Table: "| Projection Midpoint | X.XX — comp tier: ..."
    m = re.search(r"Projection Midpoint[:\s|]+(\d+\.\d+)", body, flags=re.IGNORECASE)
    if m:
        out["midpoint"] = float(m.group(1))

    # Bust/Avg/Boom — try to find a numeric value following the label.
    # If only "Omitted" / "N/A" appears, leave as None (treated as omitted).
    for label, key in [("Bust%", "bust"), ("Avg%", "avg"), ("Boom%", "boom")]:
        # Match label, then up to ~80 chars of any non-newline content, capturing
        # either a number-ish token or a non-numeric placeholder
        m = re.search(
            rf"{re.escape(label)}[:\s|]+(\S+)",
            body,
        )
        if m:
            out[key + "_raw"] = m.group(1)
            out[key] = parse_pct(m.group(1))

    # Detect the "all three omitted" pattern (footnote style):
    # "Bust% / Avg% / Boom%: Omitted per State 4 spec"
    if re.search(r"Bust%\s*/\s*Avg%\s*/\s*Boom%[:\s]+(?:OMITTED|Omitted|omitted|N/A)", body):
        out["all_omitted_footnote"] = True

    return out


def scan_placeholders(text):
    found = []
    for pattern in PLACEHOLDER_PATTERNS:
        for m in re.finditer(pattern, text):
            line_no = text[: m.start()].count("\n") + 1
            found.append((line_no, m.group(0)))
    return found


def run_checks(text):
    """Return list of (id, description, status, detail). Status: PASS|FAIL|ERROR|WARN."""
    results = []

    # QC1.1 sections 1-10 present
    missing = [n for n in range(1, 11) if find_section(text, n) is None]
    if missing:
        results.append(("QC1.1", "All sections 1-10 present", "FAIL", f"missing: {missing}"))
    else:
        results.append(("QC1.1", "All sections 1-10 present", "PASS", None))

    # QC1.2 placeholder scan
    placeholders = scan_placeholders(text)
    if placeholders:
        sample = "; ".join(f"L{ln}: {p!r}" for ln, p in placeholders[:5])
        if len(placeholders) > 5:
            sample += f"; +{len(placeholders) - 5} more"
        results.append(("QC1.2", "No placeholder strings", "FAIL", sample))
    else:
        results.append(("QC1.2", "No placeholder strings", "PASS", None))

    # QC2.1 §1 composite == §8 composite
    s1_composite = extract_section1_composite(text)
    s8_composite, s8_tier = extract_section8_composite_tier(text)

    if s1_composite is None:
        results.append(("QC2.1", "Sec1 composite = Sec8 composite", "ERROR", "could not extract Sec1 composite"))
    elif s8_composite is None:
        results.append(("QC2.1", "Sec1 composite = Sec8 composite", "ERROR", "could not extract Sec8 composite"))
    elif abs(s1_composite - s8_composite) > 0.001:
        results.append(("QC2.1", "Sec1 composite = Sec8 composite", "FAIL",
                        f"Sec1={s1_composite}, Sec8={s8_composite}"))
    else:
        results.append(("QC2.1", "Sec1 composite = Sec8 composite", "PASS", f"both = {s1_composite}"))

    # QC2.2 tier band rule
    s1_tier = extract_section1_tier(text)
    if s1_composite is None:
        results.append(("QC2.2", "Tier matches composite band", "ERROR", "could not extract composite"))
    elif s1_tier is None:
        results.append(("QC2.2", "Tier matches composite band", "ERROR", "could not extract tier"))
    else:
        expected = expected_tier(s1_composite)
        if expected is None:
            results.append(("QC2.2", "Tier matches composite band", "WARN",
                            f"composite {s1_composite} below T10 (5.80) - band table not extended"))
        elif s1_tier != expected:
            results.append(("QC2.2", "Tier matches composite band", "FAIL",
                            f"tier={s1_tier}, composite={s1_composite} -> expected T{expected}"))
        else:
            results.append(("QC2.2", "Tier matches composite band", "PASS",
                            f"T{s1_tier} for composite {s1_composite}"))

    # QC4 projection
    proj = extract_projection(text)
    state = proj.get("state")

    # QC4.1
    if state is None:
        results.append(("QC4.1", "Projection percentages", "ERROR", "could not extract State"))
    elif state == 4:
        # Vet — bust/avg/boom should be non-numeric (Omitted / N/A) or absent
        bust_n = proj.get("bust")
        avg_n = proj.get("avg")
        boom_n = proj.get("boom")
        has_numbers = any(v is not None for v in [bust_n, avg_n, boom_n])
        has_footnote = proj.get("all_omitted_footnote", False)
        if has_numbers:
            results.append(("QC4.1", "Projection % omitted for vet", "FAIL",
                            f"State 4 should not have numeric Bust/Avg/Boom; got bust={bust_n} avg={avg_n} boom={boom_n}"))
        else:
            note = "all 3 omitted (footnote)" if has_footnote else "all 3 omitted"
            results.append(("QC4.1", "Projection % omitted for vet", "PASS", note))
    else:
        # Prospect — sum to 100 ±1
        b = proj.get("bust")
        a = proj.get("avg")
        o = proj.get("boom")
        if None in (b, a, o):
            missing = [k for k, v in [("bust", b), ("avg", a), ("boom", o)] if v is None]
            results.append(("QC4.1", "Projection % sum to 100 (prospect)", "ERROR",
                            f"could not parse: missing {missing}"))
        else:
            total = b + a + o
            if abs(total - 100) <= 1:
                results.append(("QC4.1", "Projection % sum to 100 (prospect)", "PASS",
                                f"{b}+{a}+{o} = {total}"))
            else:
                results.append(("QC4.1", "Projection % sum to 100 (prospect)", "FAIL",
                                f"{b}+{a}+{o} = {total} (off by {abs(total - 100):.1f})"))

    # QC4.2 midpoint = composite
    midpoint = proj.get("midpoint")
    if midpoint is None:
        results.append(("QC4.2", "Sec9 midpoint = Sec1 composite", "ERROR", "could not extract midpoint"))
    elif s1_composite is None:
        results.append(("QC4.2", "Sec9 midpoint = Sec1 composite", "ERROR", "could not extract composite"))
    elif abs(midpoint - s1_composite) > 0.001:
        results.append(("QC4.2", "Sec9 midpoint = Sec1 composite", "FAIL",
                        f"midpoint={midpoint}, composite={s1_composite}"))
    else:
        results.append(("QC4.2", "Sec9 midpoint = Sec1 composite", "PASS", f"both = {midpoint}"))

    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("profile", help="Path to profile markdown file")
    args = parser.parse_args()

    profile_path = Path(args.profile).resolve()
    if not profile_path.is_file():
        print(f"ERROR: {profile_path} not found", file=sys.stderr)
        sys.exit(2)

    text = profile_path.read_text(encoding="utf-8")
    results = run_checks(text)

    bar = "=" * 60
    print(bar)
    print(f"QC LINT - {profile_path.name}")
    print(bar)

    counts = {"PASS": 0, "FAIL": 0, "ERROR": 0, "WARN": 0}
    for qc_id, name, status, detail in results:
        counts[status] = counts.get(status, 0) + 1
        marker = {"PASS": "[OK]  ", "FAIL": "[FAIL]", "ERROR": "[ERR] ", "WARN": "[WARN]"}.get(status, status)
        line = f"  {marker} {qc_id}  {name}"
        if detail:
            line += f" -- {detail}"
        print(line)

    print()
    print(f"Pass: {counts['PASS']} | Fail: {counts['FAIL']} | Error: {counts['ERROR']} | Warn: {counts['WARN']}")

    sys.exit(1 if counts["FAIL"] or counts["ERROR"] else 0)


if __name__ == "__main__":
    main()
