---
player: Trae Young
group: Guard
archetype: Offensive Engine
composite: 8.33
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Trae_Young/2026-05-05_profile.md
scored_session: 143
last_updated_session: 143
rubric_version: v3
pot: 8.70
sd01_at_basket_finishing: 5.2
sd02_contact_finishing: 8.5
sd03_post_offense: 2.5
sd04_catch_shoot_3pt: 7.1
sd05_off_dribble_shooting: 7.5
sd06_mid_range: 8.5
sd07_free_throw: 8.8
sd08_handling_creation: 8.5
sd09_touch_feel: 8.1
sd10_ball_security: 6.2
sd11_court_vision: 9.1
sd12_decision_making: 6.5
sd13_passing_execution: 8.1
sd14_off_ball_movement: 5.5
sd15_on_ball_pressure: 4.5
sd16_help_defense: 5.0
sd17_rim_protection: 2.0
sd18_post_defense: 3.0
sd19_offensive_rebounding: 5.0
sd20_defensive_rebounding: 6.0
sd21_burst_explosion: 5.0
sd22_lateral_quickness: 4.5
sd23_strength: 5.0
sd24_shot_selection: 6.0
sd25_effort_motor: 5.5
sd26_competitive_character: 4.7
d1_finishing: 6.9
d2_shooting: 8.0
d3_ball_skills: 7.6
d4_playmaking: 7.3
d5_defense: 4.8
d6_rebounding: 6.0
d7_athleticism: 4.8
d8_iq_motor: 5.4
---

# Trae Young

**[[Offensive Engine]]** Guard — composite **8.33** (Tier 6). Undersized lead guard with elite vision and engineered foul-draw, the most asymmetric two-way profile in the active anchor cohort.

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

Out 2025-26 quad/back; traded ATL→WAS 1/26

## Sources
- Full profile: [output/Trae_Young/2026-05-05_profile.md](../../output/Trae_Young/2026-05-05_profile.md)
- Research packets: [raw/Trae_Young/](../../raw/Trae_Young/)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
