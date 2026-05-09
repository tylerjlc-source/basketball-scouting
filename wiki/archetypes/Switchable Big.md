---
archetype: Switchable Big
group: Big
---

# Switchable Big

Defensive versatility at big size. Can guard the 5, can chase the 3 on a switch. Mobility and defensive IQ are the product. Offense is functional, not the reason this player is on the court.

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
