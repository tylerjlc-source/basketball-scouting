#!/usr/bin/env python3
"""
Migrate static peer-list lines to dataviewjs blocks in player wiki pages.

For each player page where:
  - has_profile: true (full output/ profile exists)
  - the `## Anchors in context` section uses the legacy static format

replaces the section with templated dataviewjs blocks for tier neighbors
(cap 4, distance asc / composite asc / name alphabetical tiebreak) and
archetype peers (no cap, composite descending), per the W3 wiki-layer
pivot.

Idempotent: skips files where the section already contains a dataviewjs
block. Dry-run shows what would change without writing.

Run from project root:
  python scripts/migrate_to_dataview.py            # full sweep (has_profile: true only)
  python scripts/migrate_to_dataview.py --dry-run  # preview
  python scripts/migrate_to_dataview.py --all      # include legacy pages too
"""

import argparse
import sys
from pathlib import Path

from config import PROJECT_ROOT, WIKI_DIR

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


DATAVIEW_BLOCK = """## Anchors in context

**Tier neighbors:**

```dataviewjs
const p = dv.current()
const peers = dv.pages('"wiki/players"')
  .where(x => x.tier === p.tier && x.player !== p.player)
  .map(x => ({player: x.player, composite: x.composite, delta: Math.abs(x.composite - p.composite)}))
  .array()
  .sort((a, b) => a.delta - b.delta || a.composite - b.composite || a.player.localeCompare(b.player))
  .slice(0, 4)
dv.list(peers.map(x => `[[${x.player}]] (${x.composite.toFixed(2)})`))
```

**Archetype peers:**

```dataviewjs
const p = dv.current()
const peers = dv.pages('"wiki/players"')
  .where(x => x.archetype === p.archetype && x.player !== p.player)
  .sort(x => -x.composite)
dv.list(peers.map(x => `[[${x.player}]] (${x.composite.toFixed(2)})`))
```"""


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end == -1:
        return None
    fm_text = text[3:end].strip()
    out = {}
    for line in fm_text.split("\n"):
        line = line.rstrip()
        if not line or line.startswith("#") or ":" not in line:
            continue
        key, _, val = line.partition(":")
        out[key.strip()] = val.strip()
    return out


def has_profile_true(fm):
    if fm is None:
        return False
    return fm.get("has_profile", "").strip().lower() == "true"


def already_migrated(text):
    """True if the Anchors section already contains a dataviewjs block."""
    section_start = text.find("## Anchors in context")
    if section_start == -1:
        return False
    next_section = text.find("\n## ", section_start + 1)
    section_text = text[section_start : next_section if next_section != -1 else len(text)]
    return "dataviewjs" in section_text and "dv.pages" in section_text


def migrate(text):
    """Return (new_text, status). Status: migrated | already | no_section."""
    if already_migrated(text):
        return text, "already"

    marker = "\n## Anchors in context"
    section_start = text.find(marker)
    if section_start == -1:
        if text.startswith(marker[1:]):
            section_start = 0
        else:
            return text, "no_section"
    else:
        section_start += 1  # point to first '#' of '##'

    boundary = text.find("\n\n## ", section_start)
    if boundary == -1:
        # Section runs to EOF
        new_text = text[:section_start] + DATAVIEW_BLOCK + "\n"
    else:
        # Preserve the `\n\n## ...` boundary so the next section spacing is unchanged
        new_text = text[:section_start] + DATAVIEW_BLOCK + text[boundary:]

    return new_text, "migrated"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--all", action="store_true", help="Include legacy pages (has_profile: false)")
    parser.add_argument("--target", help="Specific glob (default: wiki/players/*.md)")
    args = parser.parse_args()

    if args.target:
        files = sorted(PROJECT_ROOT.glob(args.target))
    else:
        files = sorted((WIKI_DIR / "players").glob("*.md"))

    counts = {"migrated": 0, "already": 0, "no_section": 0, "skipped_legacy": 0, "errors": 0}
    actions = []

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            counts["errors"] += 1
            actions.append((path.name, "ERROR", str(e)))
            continue

        fm = parse_frontmatter(text)
        if not args.all and not has_profile_true(fm):
            counts["skipped_legacy"] += 1
            continue

        new_text, status = migrate(text)
        counts[status] += 1

        if status == "migrated":
            actions.append((path.name, status, None))
            if not args.dry_run:
                path.write_text(new_text, encoding="utf-8")
        elif status == "no_section":
            actions.append((path.name, status, None))

    bar = "=" * 60
    mode = " (DRY RUN)" if args.dry_run else ""
    print(bar)
    print(f"DATAVIEW MIGRATION{mode}")
    print(bar)
    print(f"Total scanned:   {len(files)}")
    print(f"Migrated:        {counts['migrated']}")
    print(f"Already done:    {counts['already']}")
    print(f"No section:      {counts['no_section']}")
    print(f"Skipped legacy:  {counts['skipped_legacy']}")
    print(f"Errors:          {counts['errors']}")
    print()

    if actions:
        print("Actions:")
        for name, status, err in actions:
            tag = {"migrated": "MIGRATE ", "no_section": "NO-SECT ", "ERROR": "ERROR   "}.get(status, status)
            note = f" -- {err}" if err else ""
            print(f"  {tag} {name}{note}")

    if args.dry_run:
        print()
        print("Dry run -- no files written.")


if __name__ == "__main__":
    main()
