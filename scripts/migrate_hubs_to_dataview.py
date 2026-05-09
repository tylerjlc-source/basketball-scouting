#!/usr/bin/env python3
"""
Migrate static archetype-hub roster tables to dataviewjs blocks.

For each `wiki/archetypes/*.md`:
  - Removes `anchor_count: N` from frontmatter (now derived implicitly)
  - Replaces the static `## Anchor roster` table with a dataviewjs table
    query against `wiki/players/*.md` filtered by archetype

Idempotent: skips files where the section already contains a dataviewjs
block. Dry-run shows what would change without writing.

Run from project root:
  python scripts/migrate_hubs_to_dataview.py
  python scripts/migrate_hubs_to_dataview.py --dry-run
"""

import argparse
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


DATAVIEW_HUB_BLOCK = """```dataviewjs
const archetype = dv.current().archetype
const roster = dv.pages('"wiki/players"')
  .where(x => x.archetype === archetype)
  .sort(x => -x.composite)
dv.table(
  ["Composite", "Tier", "Player", "Status"],
  roster.map(x => [x.composite.toFixed(2), `T${x.tier}`, x.file.link, x.status ?? ""])
)
```"""


def already_migrated_hub(text):
    """True if the Anchor roster section already contains a dataviewjs block."""
    section_start = text.find("## Anchor roster")
    if section_start == -1:
        return False
    next_section = text.find("\n## ", section_start + 1)
    section_text = text[section_start : next_section if next_section != -1 else len(text)]
    return "dataviewjs" in section_text and "dv.pages" in section_text


def drop_anchor_count(text):
    """Remove the `anchor_count: N` line from frontmatter, if present."""
    return re.sub(r"^anchor_count:\s*\d+\s*\n", "", text, count=1, flags=re.MULTILINE)


def migrate_hub(text):
    """Return (new_text, status). Status: migrated | already | no_section."""
    if already_migrated_hub(text):
        return text, "already"

    new_text = drop_anchor_count(text)

    # Find ## Anchor roster section
    marker = "## Anchor roster"
    section_start = new_text.find(marker)
    if section_start == -1:
        return text, "no_section"

    # End of section header line
    header_end = new_text.find("\n", section_start)
    if header_end == -1:
        return text, "no_section"

    # Find the boundary to next section, or EOF
    boundary = new_text.find("\n\n## ", header_end)
    if boundary == -1:
        # Section runs to EOF
        rebuilt = new_text[:header_end] + "\n\n" + DATAVIEW_HUB_BLOCK + "\n"
    else:
        rebuilt = new_text[:header_end] + "\n\n" + DATAVIEW_HUB_BLOCK + new_text[boundary:]

    return rebuilt, "migrated"


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    parser.add_argument("--target", help="Specific glob (default: wiki/archetypes/*.md)")
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent.parent
    if args.target:
        files = sorted(repo_root.glob(args.target))
    else:
        files = sorted((repo_root / "wiki" / "archetypes").glob("*.md"))

    counts = {"migrated": 0, "already": 0, "no_section": 0, "errors": 0}
    actions = []

    for path in files:
        try:
            text = path.read_text(encoding="utf-8")
        except Exception as e:
            counts["errors"] += 1
            actions.append((path.name, "ERROR", str(e)))
            continue

        new_text, status = migrate_hub(text)
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
    print(f"ARCHETYPE HUB MIGRATION{mode}")
    print(bar)
    print(f"Total scanned:   {len(files)}")
    print(f"Migrated:        {counts['migrated']}")
    print(f"Already done:    {counts['already']}")
    print(f"No section:      {counts['no_section']}")
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
