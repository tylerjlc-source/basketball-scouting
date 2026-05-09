---
player: Jalen Brunson
group: Guard
archetype: Offensive Engine
composite: 8.76
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Jalen_Brunson/2026-05-01_profile.md
scored_session: 130
last_updated_session: 152
rubric_version: v3
pot: 8.90
sd01_at_basket_finishing: 8.1
sd02_contact_finishing: 8.2
sd03_post_offense: 7.0
sd04_catch_shoot_3pt: 9.0
sd05_off_dribble_shooting: 8.7
sd06_mid_range: 8.8
sd07_free_throw: 8.2
sd08_handling_creation: 9.1
sd09_touch_feel: 9.0
sd10_ball_security: 8.6
sd11_court_vision: 8.0
sd12_decision_making: 8.7
sd13_passing_execution: 7.8
sd14_off_ball_movement: 7.0
sd15_on_ball_pressure: 4.8
sd16_help_defense: 5.5
sd17_rim_protection: 3.0
sd18_post_defense: 4.0
sd19_offensive_rebounding: 5.0
sd20_defensive_rebounding: 6.5
sd21_burst_explosion: 5.5
sd22_lateral_quickness: 5.0
sd23_strength: 8.5
sd24_shot_selection: 8.0
sd25_effort_motor: 7.8
sd26_competitive_character: 9.1
d1_finishing: 8.2
d2_shooting: 8.7
d3_ball_skills: 8.9
d4_playmaking: 7.9
d5_defense: 5.2
d6_rebounding: 6.5
d7_athleticism: 6.3
d8_iq_motor: 8.3
---

# Jalen Brunson

**[[Offensive Engine]]** Guard — composite **8.76** (Tier 5). Undersized strength-anchored primary-creator PG with elite handle, mid-range mastery, and clutch reputation; defensive ceiling capped by structural lateral and burst limits.

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
All-NBA 2nd; Clutch POTY 2024-25; prior 8.70 (calibration correction 2026-05-06 — Clutch POTY re-priced into #12)

## Sources
- Full profile: [output/Jalen_Brunson/2026-05-01_profile.md](../../output/Jalen_Brunson/2026-05-01_profile.md)
- Research packets: [raw/Jalen_Brunson/2026-05-01_research-packet.md](../../raw/Jalen_Brunson/2026-05-01_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
