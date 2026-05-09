---
player: Domantas Sabonis
group: Big
archetype: Versatile Scoring Big
composite: 8.22
tier: 7
tier_band: 7.90–8.29
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Domantas_Sabonis/2026-04-24_profile.md
scored_session: 102
last_updated_session: 102
rubric_version: v3
pot: null
sd01_at_basket_finishing: 7.3
sd02_contact_finishing: 7.0
sd03_post_offense: 8.1
sd04_catch_shoot_3pt: 7.4
sd05_off_dribble_shooting: 5.7
sd06_mid_range: 7.3
sd07_free_throw: 7.3
sd08_handling_creation: 6.0
sd09_touch_feel: 8.2
sd10_ball_security: 6.8
sd11_court_vision: 8.4
sd12_decision_making: 7.0
sd13_passing_execution: 8.0
sd14_off_ball_movement: 7.2
sd15_on_ball_pressure: 5.3
sd16_help_defense: 5.8
sd17_rim_protection: 4.7
sd18_post_defense: 6.3
sd19_offensive_rebounding: 8.8
sd20_defensive_rebounding: 9.1
sd21_burst_explosion: 5.5
sd22_lateral_quickness: 5.2
sd23_strength: 7.7
sd24_shot_selection: 7.3
sd25_effort_motor: 8.3
sd26_competitive_character: 6.5
d1_finishing: 7.5
d2_shooting: 6.9
d3_ball_skills: 7.0
d4_playmaking: 7.7
d5_defense: 5.5
d6_rebounding: 9.0
d7_athleticism: 6.1
d8_iq_motor: 7.4
---

# Domantas Sabonis

**[[Versatile Scoring Big]]** Big — composite **8.22** (Tier 7).

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
Added Session 102 — second player of S101 batch 2 wing/big scale validation sweep; first current-tag VSB anchor with credentialed Tier 6-level production; **library's first NBA-vet anchor with active non-negotiable cap** — #17 Rim protection 4.7 fails C gate (5.0), cap binds composite below Tier 6 entry; 3x NBA rebounding champion + 3x All-Star + 2x All-NBA; meniscus surgery Feb 2026 (season-ending); R13 historical-only strong shrink — Stage 2 skipped, Stage 1 POT −0.40 full magnitude; Vucevic age-28 🔴 + Cousins age-27 🔴 (both fail primary TS% tolerance — Sabonis efficiency outlier for VSB archetype).

## Sources
- Full profile: [output/Domantas_Sabonis/2026-04-24_profile.md](../../output/Domantas_Sabonis/2026-04-24_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
