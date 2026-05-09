---
archetype: Versatile Scoring Big
group: Big
---

# Versatile Scoring Big

Scores from multiple areas with limited defensive contribution. Post game, mid-range, finishing, and some shooting. Defense is a liability the team accepts. Distinct from All-Around Big — defensive dimensions are genuinely weak, not secondary. Absorbs Post Scoring Big — post-dominant prospects land here with lower shooting sub-domain scores.

> Merger note: Post Scoring Big merged into this archetype Session 48. Hard ceiling signal captured by projection block, not a separate archetype.

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
