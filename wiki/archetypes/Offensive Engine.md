---
archetype: Offensive Engine
group: Guard
---

# Offensive Engine

Creates shots for himself and others at high volume across all three levels. Ranges from complementary co-star to franchise anchor — the differentiator is usage and playmaking dominance, not a different skill profile.

> Merger note: DPS Guard merged into Offensive Engine (Session 46) — usage distinctions handled by the projection block, not separate archetypes. Legacy-tagged "Dribble Pass Shoot Guard" anchors pending migration lint. See [[Dribble Pass Shoot Guard]].

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
