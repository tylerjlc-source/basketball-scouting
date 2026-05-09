---
archetype: Shooting Specialist
group: Guard
---

# Shooting Specialist (Guard)

Catch-and-shoot 3PT only. Off-ball movement is the delivery vehicle. Shot selection protects against self-destruction. Everything else is at or near zero.

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
- Wing version: [[Shooting Specialist (Wing)]]
