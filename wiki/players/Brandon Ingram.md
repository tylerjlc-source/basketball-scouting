---
player: Brandon Ingram
group: Wing
archetype: Score-First Wing
composite: 8.26
tier: 7
tier_band: 7.90–8.29
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Brandon_Ingram/2026-05-06_profile.md
scored_session: 154
last_updated_session: 154
rubric_version: v3
pot: 8.40
sd01_at_basket_finishing: 7.6
sd02_contact_finishing: 7.2
sd03_post_offense: 5.0
sd04_catch_shoot_3pt: 8.6
sd05_off_dribble_shooting: 7.0
sd06_mid_range: 8.7
sd07_free_throw: 8.1
sd08_handling_creation: 7.4
sd09_touch_feel: 8.5
sd10_ball_security: 7.2
sd11_court_vision: 7.2
sd12_decision_making: 7.0
sd13_passing_execution: 7.1
sd14_off_ball_movement: 6.9
sd15_on_ball_pressure: 5.5
sd16_help_defense: 5.5
sd17_rim_protection: 5.0
sd18_post_defense: 5.0
sd19_offensive_rebounding: 5.2
sd20_defensive_rebounding: 6.7
sd21_burst_explosion: 6.4
sd22_lateral_quickness: 5.5
sd23_strength: 5.0
sd24_shot_selection: 7.0
sd25_effort_motor: 5.7
sd26_competitive_character: 5.7
d1_finishing: 6.6
d2_shooting: 8.1
d3_ball_skills: 7.7
d4_playmaking: 7.1
d5_defense: 5.5
d6_rebounding: 6.0
d7_athleticism: 5.6
d8_iq_motor: 6.1
---

# Brandon Ingram

**[[Score-First Wing]]** Wing — composite **8.26** (Tier 7). Mid-range bucket-getter on a long lean frame; offensive density priced against a defensive structural floor and a documented playoff-shrink pattern.

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
2x All-Star; R13 active shrink

## Sources
- Full profile: [output/Brandon_Ingram/2026-05-06_profile.md](../../output/Brandon_Ingram/2026-05-06_profile.md)
- Research packets: [raw/Brandon_Ingram/](../../raw/Brandon_Ingram/)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
