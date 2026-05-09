---
archetype: Defensive Specialist
group: Wing
---

# Defensive Specialist (Wing)

Elite multi-position defense and competitive character. Earns roster spot entirely through defensive impact. Offense is a liability the team manages. Includes athleticism-first defensive profiles (formerly Energy/Hustle Wing) — those players score lower on #16 help defense and IQ sub-domains; ceiling flagged in projection block.

> Merger note: Energy/Hustle Wing merged into Defensive Specialist (Session 47). Legacy-tagged anchors pending migration lint.

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

## Related
- Guard version: [[Defensive Specialist (Guard)]]
- Legacy (merged in): [[Energy Hustle Wing]]
