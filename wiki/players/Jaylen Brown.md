---
player: Jaylen Brown
group: Wing
archetype: Score-First Wing
composite: 8.83
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Jaylen_Brown/2026-04-23_profile.md
scored_session: null
last_updated_session: 99
rubric_version: v3
pot: 8.95
sd01_at_basket_finishing: 8.5
sd02_contact_finishing: 7.8
sd03_post_offense: 6.5
sd04_catch_shoot_3pt: 7.0
sd05_off_dribble_shooting: 7.5
sd06_mid_range: 7.0
sd07_free_throw: 7.0
sd08_handling_creation: 7.8
sd09_touch_feel: 7.5
sd10_ball_security: 6.0
sd11_court_vision: 7.0
sd12_decision_making: 7.5
sd13_passing_execution: 7.0
sd14_off_ball_movement: 7.0
sd15_on_ball_pressure: 7.5
sd16_help_defense: 7.0
sd17_rim_protection: 3.5
sd18_post_defense: 5.0
sd19_offensive_rebounding: 6.5
sd20_defensive_rebounding: 7.5
sd21_burst_explosion: 8.3
sd22_lateral_quickness: 7.8
sd23_strength: 8.0
sd24_shot_selection: 7.0
sd25_effort_motor: 8.0
sd26_competitive_character: 8.5
d1_finishing: 7.6
d2_shooting: 7.1
d3_ball_skills: 7.1
d4_playmaking: 7.1
d5_defense: 7.3
d6_rebounding: 7.0
d7_athleticism: 8.0
d8_iq_motor: 7.8
---

# Jaylen Brown

**[[Score-First Wing]]** Wing — composite **8.83** (Tier 5).

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
Updated Session 99 — was 8.79; small upward drift per 2025-26 scoring surge (22.2→29.3 PPG absorbing Tatum injury) + 7x consecutive All-Star; R13 Stage 2 did not fire (S99-F01 — 2024 FMVP already priced into anchor comparison; double-count protection).

## Sources
- Full profile: [output/Jaylen_Brown/2026-04-23_profile.md](../../output/Jaylen_Brown/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
