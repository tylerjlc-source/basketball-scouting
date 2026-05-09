---
archetype: Defensive-Engine Playmaker
group: Wing
---

# Defensive-Engine Playmaker

Elite defensive IQ and switchability combined with genuine playmaking. Near-zero scoring threat. Cross-positional profile — listed position varies PG to PF but skills profile is wing-centric. Draymond Green is the prototype and the ceiling.

> NOTE (docs/ARCHETYPE-WEIGHTS-WINGS.md): Historically rare archetype — small anchor roster reflects reality, not a research gap.

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
