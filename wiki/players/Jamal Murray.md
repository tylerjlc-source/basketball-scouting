---
player: Jamal Murray
group: Guard
archetype: Offensive Engine
composite: 8.68
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Jamal_Murray/2026-05-01_profile.md
scored_session: 129
last_updated_session: 129
rubric_version: v3
pot: 8.78
sd01_at_basket_finishing: 7.6
sd02_contact_finishing: 7.2
sd03_post_offense: 5.0
sd04_catch_shoot_3pt: 9.2
sd05_off_dribble_shooting: 9.1
sd06_mid_range: 8.5
sd07_free_throw: 9.1
sd08_handling_creation: 8.6
sd09_touch_feel: 8.2
sd10_ball_security: 8.1
sd11_court_vision: 7.9
sd12_decision_making: 7.5
sd13_passing_execution: 7.7
sd14_off_ball_movement: 8.2
sd15_on_ball_pressure: 6.0
sd16_help_defense: 6.0
sd17_rim_protection: 3.0
sd18_post_defense: 5.5
sd19_offensive_rebounding: 5.0
sd20_defensive_rebounding: 7.0
sd21_burst_explosion: 6.8
sd22_lateral_quickness: 6.0
sd23_strength: 7.0
sd24_shot_selection: 7.6
sd25_effort_motor: 7.0
sd26_competitive_character: 7.5
d1_finishing: 7.4
d2_shooting: 9.0
d3_ball_skills: 8.3
d4_playmaking: 7.8
d5_defense: 6.0
d6_rebounding: 7.0
d7_athleticism: 6.6
d8_iq_motor: 7.4
---

# Jamal Murray

**[[Offensive Engine]]** Guard — composite **8.68** (Tier 5). Three-level shotmaking co-star with elite Murray-Jokic two-man chemistry, sitting on a bifurcated playoff legacy (2020 Bubble + 2023 title peak vs. 2024 + 2026 first-round shrink to MIN) and an average-defender ceiling capped by structural length.

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
No update history recorded.

## Sources
- Full profile: [output/Jamal_Murray/2026-05-01_profile.md](../../output/Jamal_Murray/2026-05-01_profile.md)
- Research packets: [raw/Jamal_Murray/2026-05-01_research-packet.md](../../raw/Jamal_Murray/2026-05-01_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
