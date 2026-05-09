---
archetype: Defensive Specialist
group: Guard
---

# Defensive Specialist (Guard)

Defense, effort, and competitive character. Earns roster spot entirely through defensive impact and competitive intensity. Scoring is a liability, not a trade.

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
- Definition: [docs/ARCHETYPE-WEIGHTS-GUARDS.md](../../docs/ARCHETYPE-WEIGHTS-GUARDS.md)
- Structural-zero tables: [docs/DOMAIN-SCORE-ROLE-RELEVANCE.md](../../docs/DOMAIN-SCORE-ROLE-RELEVANCE.md)
- Non-negotiables gate: [docs/NON-NEGOTIABLES.md](../../docs/NON-NEGOTIABLES.md)

## Related
- Wing version: [[Defensive Specialist (Wing)]]
