---
archetype: Secondary Playmaker
group: Wing
---

# Secondary Playmaker

High-IQ ball movement in a limited offensive role. Does not need to score to justify roster spot. Reads the game, makes the right pass, stays out of trouble.

> NOTE (docs/ARCHETYPE-WEIGHTS-WINGS.md): Historically rare at the wing level. Low-usage by design — APG is not the primary signal. Assist rate relative to usage and assist-to-turnover ratio are the correct measures. Small roster reflects the archetype's rarity, not a research gap.

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
- Definition: [docs/ARCHETYPE-WEIGHTS-WINGS.md](../../docs/ARCHETYPE-WEIGHTS-WINGS.md)
- Structural-zero tables: [docs/DOMAIN-SCORE-ROLE-RELEVANCE.md](../../docs/DOMAIN-SCORE-ROLE-RELEVANCE.md)
- Non-negotiables gate: [docs/NON-NEGOTIABLES.md](../../docs/NON-NEGOTIABLES.md)
