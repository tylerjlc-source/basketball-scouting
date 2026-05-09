---
archetype: Dribble Pass Shoot Guard
group: Guard
legacy: true
merged_into: Offensive Engine
merged_session: 46
---

# Dribble Pass Shoot Guard (Legacy)

> **LEGACY ARCHETYPE — Merged into [[Offensive Engine]] at Session 46.**
> Usage distinctions handled by the projection block, not separate archetypes. Anchors below retain the legacy tag in ANCHOR-LIBRARY.md pending migration lint.

Original value driver (pre-merger): Offensive versatility from the guard position — scores off the dribble, shoots from 3, and creates for others.

## Anchor roster (by composite, descending — tag pending migration)

```dataviewjs
const archetype = dv.current().archetype
const roster = dv.pages('"wiki/players"')
  .where(x => x.archetype === archetype)
  .sort(x => -x.composite)
dv.table(
  ["Composite", "Tier", "Player", "Status"],
  roster.map(x => [x.composite.toFixed(2), `T${x.tier}`, x.file.link, x.status ?? ""])
)
```

## Migration target
- [[Offensive Engine]] — current canonical archetype for these player profiles
- Lint task: flag all `archetype: Dribble Pass Shoot Guard` entries in `wiki/players/*.md` for re-classification.

## Source documents
- Merger record: [docs/ARCHETYPE-WEIGHTS-GUARDS.md](../../docs/ARCHETYPE-WEIGHTS-GUARDS.md) (see Session 46 note)
