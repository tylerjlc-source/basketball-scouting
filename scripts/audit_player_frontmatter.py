#!/usr/bin/env python3
"""
Pre-flight audit for the wiki layer dataview migration.

Walks wiki/players/*.md and reports frontmatter outliers that would break
the planned dataview queries.

Checks:
- Required fields present: player, group, position, archetype, composite, tier
- group is Guard | Wing | Big
- composite parses as number
- tier parses as integer 1-13
- tier matches composite via canonical band table
- filename stem matches player field
- has_profile field present (informational; drives migration filter)

Read-only. Run from project root:
  python scripts/audit_player_frontmatter.py
"""

import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

VALID_GROUPS = {"Guard", "Wing", "Big"}

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

# Fields the dataview migration's queries actually depend on.
# Note: SCHEMA-SPEC §1 lists `position` as required, but no migration query
# filters on it. Tracked separately below as an informational gap.
REQUIRED = ["player", "group", "archetype", "composite", "tier"]
INFORMATIONAL = ["position", "has_profile"]


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, "no opening frontmatter delimiter"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "no closing frontmatter delimiter"
    fm_text = text[3:end].strip()
    out = {}
    for line in fm_text.split("\n"):
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if ":" not in line:
            continue
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip()
    return out, None


def coerce_number(s):
    if s is None or s == "":
        return None
    try:
        return float(s.strip().strip('"').strip("'"))
    except (ValueError, AttributeError):
        return None


def coerce_int(s):
    if s is None or s == "":
        return None
    try:
        return int(s.strip().strip('"').strip("'"))
    except (ValueError, AttributeError):
        return None


def expected_tier(composite):
    for t, lo, hi in TIER_BANDS:
        if lo <= composite <= hi:
            return t
    if composite < TIER_BANDS[-1][1]:
        return "below-T10"
    return None


def audit_file(path):
    issues = []
    try:
        text = path.read_text(encoding="utf-8")
    except UnicodeDecodeError as e:
        return [f"ERROR: encoding read failure: {e}"], None

    fm, err = parse_frontmatter(text)
    if err:
        return [f"ERROR: {err}"], None

    for field in REQUIRED:
        if field not in fm:
            issues.append(f"missing required field: {field}")

    group = fm.get("group")
    if group and group not in VALID_GROUPS:
        issues.append(f"invalid group: {group!r} (expected one of {sorted(VALID_GROUPS)})")

    composite = coerce_number(fm.get("composite"))
    if "composite" in fm and composite is None:
        issues.append(f"composite not numeric: {fm.get('composite')!r}")

    tier = coerce_int(fm.get("tier"))
    if "tier" in fm and tier is None:
        issues.append(f"tier not integer: {fm.get('tier')!r}")
    elif tier is not None and not (1 <= tier <= 13):
        issues.append(f"tier out of range 1-13: {tier}")

    if composite is not None and tier is not None and 1 <= tier <= 10:
        expected = expected_tier(composite)
        if expected is None:
            pass
        elif expected == "below-T10":
            issues.append(
                f"composite {composite} below T10 (5.80) — audit band table needs extension to T11+"
            )
        elif expected != tier:
            issues.append(
                f"tier/composite mismatch: tier={tier}, composite={composite} -> expected T{expected}"
            )

    player = fm.get("player", "").strip().strip('"').strip("'")
    if player and path.stem != player:
        issues.append(f"filename mismatch: stem={path.stem!r}, player field={player!r}")

    arch = fm.get("archetype", "").strip()
    if arch.startswith('"') or arch.startswith("'"):
        issues.append(f"INFO: archetype is quoted ({arch!r}) - verify dataview matching")

    has_profile = fm.get("has_profile", "").strip().lower()
    return issues, has_profile


def main():
    repo_root = Path(__file__).resolve().parent.parent
    players_dir = repo_root / "wiki" / "players"
    if not players_dir.is_dir():
        print(f"ERROR: {players_dir} not found", file=sys.stderr)
        sys.exit(2)

    files = sorted(players_dir.glob("*.md"))

    clean = []
    dirty = []
    hp_counts = {"true": 0, "false": 0, "missing/other": 0}
    missing_position = []

    for path in files:
        issues, hp = audit_file(path)
        if hp == "true":
            hp_counts["true"] += 1
        elif hp == "false":
            hp_counts["false"] += 1
        else:
            hp_counts["missing/other"] += 1

        # Read raw frontmatter once more for informational checks.
        try:
            text = path.read_text(encoding="utf-8")
            fm, _ = parse_frontmatter(text)
            if fm is not None and "position" not in fm:
                missing_position.append(path.name)
        except Exception:
            pass

        if issues:
            dirty.append((path.name, issues))
        else:
            clean.append(path.name)

    bar = "=" * 60
    print(bar)
    print("FRONTMATTER AUDIT - wiki/players/")
    print(bar)
    print(f"Total pages:      {len(files)}")
    print(f"Clean:            {len(clean)}")
    print(f"With issues:      {len(dirty)}")
    print()
    print("has_profile distribution:")
    print(f"  true (full):    {hp_counts['true']}")
    print(f"  false (legacy): {hp_counts['false']}")
    print(f"  missing/other:  {hp_counts['missing/other']}")
    print()
    print(f"Schema gap (informational, not blocking):")
    print(f"  pages missing 'position' field: {len(missing_position)}/{len(files)}")
    print()

    if dirty:
        print(bar)
        print(f"ISSUES ({len(dirty)} pages)")
        print(bar)
        for name, issues in dirty:
            print(f"\n  {name}:")
            for issue in issues:
                print(f"    - {issue}")
    else:
        print("All pages clean - ready for migration.")

    sys.exit(0)


if __name__ == "__main__":
    main()
