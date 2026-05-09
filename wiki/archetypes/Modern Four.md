---
archetype: Modern Four
group: Wing (cross-group — some Big-tagged anchors)
---

# Modern Four

Size-skill mismatch. Big enough to play the four, skilled enough to operate as a wing — post game, guard skills, and the ability to shoot. Interior-skill version of the large wing. Shooting-first large wings belong in Stretch Big (Bigs group).

> Modern Four / All-Around Big boundary (resolved Session 48): physical gate is the differentiator. Wing-sized with interior tools (~6'9" / 230 lbs or under, defends 2–4) = Modern Four. Physically a big with wing skills (6'9"+ / 225 lbs+ filled out, defends 4–5) = All-Around Big. Diagnostic: which assignment does the coach give first?

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
