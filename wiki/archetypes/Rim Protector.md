---
archetype: Rim Protector
group: Big
---

# Rim Protector

Deterrence and conversion prevention at the basket. Shot-blocking, verticality, and positioning are the product. Offense is minimal — team accepts the liability in exchange for interior dominance.

> FLAG (docs/ARCHETYPE-WEIGHTS-BIGS.md): A prospect with elite shot-blocking AND legitimate floor spacing belongs in Stretch Big, not Rim Protector. Myles Turner is the reference case.

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
