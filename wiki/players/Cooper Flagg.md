---
player: Cooper Flagg
group: Wing
archetype: All-Around Wing
composite: 7.95
tier: 7
tier_band: 7.90–8.29
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Cooper_Flagg/2026-05-04_profile.md
scored_session: 140
last_updated_session: 140
rubric_version: v3
pot: 8.50
sd01_at_basket_finishing: 7.7
sd02_contact_finishing: 7.6
sd03_post_offense: 5.0
sd04_catch_shoot_3pt: 5.2
sd05_off_dribble_shooting: 5.7
sd06_mid_range: 5.7
sd07_free_throw: 8.5
sd08_handling_creation: 6.5
sd09_touch_feel: 7.7
sd10_ball_security: 7.8
sd11_court_vision: 8.0
sd12_decision_making: 7.0
sd13_passing_execution: 7.6
sd14_off_ball_movement: 7.0
sd15_on_ball_pressure: 6.7
sd16_help_defense: 8.0
sd17_rim_protection: 6.5
sd18_post_defense: 6.0
sd19_offensive_rebounding: 7.0
sd20_defensive_rebounding: 7.7
sd21_burst_explosion: 6.7
sd22_lateral_quickness: 6.7
sd23_strength: 6.5
sd24_shot_selection: 5.7
sd25_effort_motor: 8.8
sd26_competitive_character: 7.8
d1_finishing: 6.8
d2_shooting: 6.3
d3_ball_skills: 7.3
d4_playmaking: 7.4
d5_defense: 6.8
d6_rebounding: 7.4
d7_athleticism: 6.6
d8_iq_motor: 7.4
---

# Cooper Flagg

**[[All-Around Wing]]** Wing — composite **7.95** (Tier 7). Rookie #1 pick / 2025-26 ROY whose distributed two-way profile and elite competitive motor offset an archetype-anomalous shooting cluster as the load-bearing developmental variable.

## Anchors in context

**Tier neighbors:**

```dataviewjs
const p = dv.current()
const peers = dv.pages('"wiki/players"')
  .where(x => x.tier === p.tier && x.player !== p.player)
  .map(x => ({player: x.player, composite: x.composite, delta: Math.abs(x.composite - p.composite)}))
  .array()
  .sort((a, b) => a.delta - b.delta || a.composite - b.composite || a.player.localeCompare(b.player))
  .slice(0, 4)
dv.list(peers.map(x => `[[${x.player}]] (${x.composite.toFixed(2)})`))
```

**Archetype peers:**

```dataviewjs
const p = dv.current()
const peers = dv.pages('"wiki/players"')
  .where(x => x.archetype === p.archetype && x.player !== p.player)
  .sort(x => -x.composite)
dv.list(peers.map(x => `[[${x.player}]] (${x.composite.toFixed(2)})`))
```

## Library history
Rookie.

## Sources
- Full profile: [output/Cooper_Flagg/2026-05-04_profile.md](../../output/Cooper_Flagg/2026-05-04_profile.md)
- Research packets: [raw/Cooper_Flagg/2026-05-04_research-packet.md](../../raw/Cooper_Flagg/2026-05-04_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
