---
archetype: Energy/Hustle Wing
group: Wing
legacy: true
merged_into: Defensive Specialist (Wing)
merged_session: 47
---

# Energy/Hustle Wing (Legacy)

> **LEGACY ARCHETYPE — Merged into [[Defensive Specialist (Wing)]] at Session 47.**
> Athleticism-first defensive profiles now use the Defensive Specialist table; ceiling flagged in projection block. Anchors below retain the legacy tag in ANCHOR-LIBRARY.md pending migration lint.

Original value driver (pre-merger): Effort-and-athleticism-led wing profile — crashes the glass, plays multiple positions defensively, limited offensive ceiling.

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
- [[Defensive Specialist (Wing)]] — current canonical archetype
- Lint task: flag all `archetype: Energy/Hustle Wing` entries in `wiki/players/*.md` for re-classification.

## Source documents
- Merger record: [docs/ARCHETYPE-WEIGHTS-WINGS.md](../../docs/ARCHETYPE-WEIGHTS-WINGS.md) (see Session 47 note)
