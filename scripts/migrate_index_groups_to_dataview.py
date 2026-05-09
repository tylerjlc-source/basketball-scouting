#!/usr/bin/env python3
"""
Migrate the GUARDS / WINGS / BIGS group bodies in wiki/index.md to dataviewjs blocks.

For each `### [[Archetype]] (N)` subsection:
  - Drops the count `(N)` from the header
  - Preserves any LEGACY blockquote (e.g. "Merged into X at S46")
  - Replaces the static player bullet list with a dataviewjs block that
    queries `wiki/players/*.md` filtered by archetype, sorted by composite
    descending. Format per Option A: name + composite + tier + (star if has_profile)

For the group headers (`## GUARDS (55)`, `## WINGS (25)`, `## BIGS (31, includes Giannis cross-group)`):
  - Drops the parenthetical count + cross-group annotation

Idempotent: skips the file if the first archetype subsection already contains
a dataviewjs block.

Run from project root:
  python scripts/migrate_index_groups_to_dataview.py
  python scripts/migrate_index_groups_to_dataview.py --dry-run
"""

import argparse
import re
import sys
from pathlib import Path

from config import PROJECT_ROOT, WIKI_DIR

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def build_dataview_block(archetype):
    return (
        "```dataviewjs\n"
        f'const archetype = "{archetype}"\n'
        "const players = dv.pages('\"wiki/players\"').where(x => x.archetype === archetype).sort(x => -x.composite)\n"
        'dv.list(players.map(x => `[[${x.player}]] — ${x.composite.toFixed(2)} / T${x.tier}${x.has_profile ? " ★" : ""}`))\n'
        "```"
    )


def already_migrated(text):
    """True if the first ### [[X]] subsection already contains a dataviewjs block."""
    m = re.search(r"^### \[\[[^\]]+\]\]", text, flags=re.MULTILINE)
    if not m:
        return False
    next_section = text.find("\n## ", m.start())
    if next_section == -1:
        next_section = len(text)
    section_text = text[m.start() : next_section]
    return "dataviewjs" in section_text


def migrate(text):
    if already_migrated(text):
        return text, "already"

    # 1. Drop count from group headers. Use [ \t]* so we don't consume the trailing
    #    newline (which \s* would, since \s matches \n).
    text = re.sub(
        r"^(## (?:GUARDS|WINGS|BIGS))[ \t]*\([^)]*\)[ \t]*$",
        r"\1",
        text,
        flags=re.MULTILINE,
    )

    # 2. Walk line-by-line, replacing each ### archetype subsection's bullet list
    lines = text.split("\n")
    out = []
    i = 0
    n = len(lines)

    while i < n:
        line = lines[i]
        m = re.match(r"^### \[\[([^\]]+)\]\](.*)$", line)
        if not m:
            out.append(line)
            i += 1
            continue

        archetype = m.group(1)
        rest = m.group(2)
        # Preserve LEGACY marker if present, drop counts and cross-group notes
        legacy_suffix = ""
        if "LEGACY" in rest:
            legacy_suffix = " — LEGACY"
        out.append(f"### [[{archetype}]]{legacy_suffix}")
        i += 1

        # Preserve a blank line if present
        if i < n and lines[i] == "":
            out.append("")
            i += 1

        # Preserve any blockquote lines (legacy merge notes)
        had_blockquote = False
        while i < n and lines[i].startswith(">"):
            out.append(lines[i])
            i += 1
            had_blockquote = True

        # If blockquote was present, add a blank separator
        if had_blockquote:
            out.append("")
            # Skip blank lines between blockquote and bullets
            while i < n and lines[i] == "":
                i += 1

        # Skip the static bullet list
        while i < n and (lines[i].startswith("- ") or (lines[i] == "" and i + 1 < n and lines[i + 1].startswith("- "))):
            i += 1

        # Blank line separator before dataview block, then the block itself
        if not out or out[-1] != "":
            out.append("")
        out.append(build_dataview_block(archetype))

    return "\n".join(out), "migrated"


def main():
    parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing")
    args = parser.parse_args()

    path = WIKI_DIR / "index.md"

    if not path.is_file():
        print(f"ERROR: {path} not found", file=sys.stderr)
        sys.exit(2)

    text = path.read_text(encoding="utf-8")
    new_text, status = migrate(text)

    bar = "=" * 60
    mode = " (DRY RUN)" if args.dry_run else ""
    print(bar)
    print(f"INDEX GROUPS MIGRATION{mode}")
    print(bar)
    print(f"File:    {path.relative_to(PROJECT_ROOT)}")
    print(f"Status:  {status}")

    if status == "migrated":
        # Quick sanity: count archetype subsections affected
        archetype_count = len(re.findall(r"^### \[\[", new_text, flags=re.MULTILINE))
        block_count = new_text.count("```dataviewjs")
        # block_count includes the existing tier-section block from 4.3
        print(f"Archetype subsections in new file: {archetype_count}")
        print(f"Total dataviewjs blocks in new file: {block_count}")

        if not args.dry_run:
            path.write_text(new_text, encoding="utf-8")
            print(f"\nWrote {len(new_text)} bytes (was {len(text)}).")
        else:
            print("\nDry run -- no file written.")
            # Print first ~30 lines of new content for visual check
            preview = "\n".join(new_text.split("\n")[:40])
            print("\n--- New content (first 40 lines) ---")
            print(preview)


if __name__ == "__main__":
    main()
