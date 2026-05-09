---
archetype: Energy Big
group: Big
---

# Energy Big

Finishing and rebounding through effort and athleticism. Gets to the right spots, converts what the offense creates, crashes the glass on both ends. Absorbs Rebounding Specialist — rebounding-dominant prospects land here with lower finishing and defensive sub-domain scores.

> Merger note: Rebounding Specialist merged into this archetype Session 48. Hard ceiling signal captured by projection block, not a separate archetype.

## Anchor roster (by composite, descending)

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

## Source documents
- Definition: [docs/ARCHETYPE-WEIGHTS-BIGS.md](../../docs/ARCHETYPE-WEIGHTS-BIGS.md)
- Structural-zero tables: [docs/DOMAIN-SCORE-ROLE-RELEVANCE.md](../../docs/DOMAIN-SCORE-ROLE-RELEVANCE.md)
- Non-negotiables gate: [docs/NON-NEGOTIABLES.md](../../docs/NON-NEGOTIABLES.md)
