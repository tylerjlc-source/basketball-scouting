---
archetype: All-Around Guard
group: Guard
---

# All-Around Guard

Balanced contribution across offense and defense. No elite ceiling in any single category — competent across all of them. Earns lineup flexibility by having no exploitable weakness.

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
