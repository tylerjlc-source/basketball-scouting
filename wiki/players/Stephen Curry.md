---
player: Stephen Curry
group: Guard
archetype: Offensive Engine
composite: 9.20
tier: 3
tier_band: 9.20–9.49
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Stephen_Curry/2026-04-30_profile.md
scored_session: 123
last_updated_session: 123
rubric_version: v3
pot: 9.20
sd01_at_basket_finishing: 7.7
sd02_contact_finishing: 5.8
sd03_post_offense: 2.5
sd04_catch_shoot_3pt: 9.6
sd05_off_dribble_shooting: 9.4
sd06_mid_range: 8.5
sd07_free_throw: 10.0
sd08_handling_creation: 8.6
sd09_touch_feel: 9.4
sd10_ball_security: 6.9
sd11_court_vision: 7.8
sd12_decision_making: 7.6
sd13_passing_execution: 7.7
sd14_off_ball_movement: 9.9
sd15_on_ball_pressure: 4.8
sd16_help_defense: 6.1
sd17_rim_protection: 2.5
sd18_post_defense: 4.4
sd19_offensive_rebounding: 4.9
sd20_defensive_rebounding: 6.9
sd21_burst_explosion: 5.4
sd22_lateral_quickness: 4.9
sd23_strength: 4.7
sd24_shot_selection: 6.6
sd25_effort_motor: 9.3
sd26_competitive_character: 9.6
d1_finishing: 6.8
d2_shooting: 9.4
d3_ball_skills: 8.3
d4_playmaking: 8.3
d5_defense: 5.5
d6_rebounding: 6.9
d7_athleticism: 5.0
d8_iq_motor: 8.5
---

# Stephen Curry

**[[Offensive Engine]]** Guard — composite **9.20** (Tier 3). Best shooter in NBA history; record-holding offensive engine paired with structural defensive limitations.

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

Knee — fragment 2025-26

## Sources

- Full profile: [output/Stephen_Curry/2026-04-30_profile.md](../../output/Stephen_Curry/2026-04-30_profile.md)
- Research packets: [raw/Stephen_Curry/2026-04-30_research-packet.md](../../raw/Stephen_Curry/2026-04-30_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
