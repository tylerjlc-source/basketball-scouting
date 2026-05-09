---
player: Walker Kessler
group: Big
archetype: Rim Protector
composite: 7.87
tier: 8
tier_band: 7.50–7.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Walker_Kessler/2026-04-23_profile.md
scored_session: 101
last_updated_session: 101
rubric_version: v3
pot: null
sd01_at_basket_finishing: 7.9
sd02_contact_finishing: 5.8
sd03_post_offense: 4.3
sd04_catch_shoot_3pt: 4.3
sd05_off_dribble_shooting: 4.0
sd06_mid_range: 4.0
sd07_free_throw: 4.6
sd08_handling_creation: 4.4
sd09_touch_feel: 5.7
sd10_ball_security: 6.1
sd11_court_vision: 5.9
sd12_decision_making: 6.1
sd13_passing_execution: 5.8
sd14_off_ball_movement: 7.9
sd15_on_ball_pressure: 5.6
sd16_help_defense: 8.6
sd17_rim_protection: 9.3
sd18_post_defense: 7.8
sd19_offensive_rebounding: 9.2
sd20_defensive_rebounding: 8.3
sd21_burst_explosion: 8.3
sd22_lateral_quickness: 5.6
sd23_strength: 7.7
sd24_shot_selection: 7.4
sd25_effort_motor: 7.9
sd26_competitive_character: 7.3
d1_finishing: 6.0
d2_shooting: 4.6
d3_ball_skills: 5.9
d4_playmaking: 6.6
d5_defense: 7.8
d6_rebounding: 8.8
d7_athleticism: 7.2
d8_iq_motor: 7.5
---

# Walker Kessler

**[[Rim Protector]]** Big — composite **7.87** (Tier 8).

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
Added Session 101 — 4th player / first Big of S100 batch 1 completion; first Rim Protector anchor added since initial library construction; fills current-era mid-tier Rim Protector gap between Gobert 7.98 and Claxton 7.68 (prior pool skewed older: Gobert 30+, Bamba/Moses Brown 5.88-5.95); 2024-25 99th-pct rim deterrence per BBall Index + led league OREB; labrum surgery flag 2025-26; R13 below sample (zero NBA playoffs career); comps Gobert 2016-17 🟢, Claxton 2022-23 🟢, Capela 2017-18 🟡 under S96-F04 NBA-vet adaptation (age-comparable seasons); S96-F04 6th application — promotion threshold reached, formal rule rewrite pending this session. Anchor count: 100 — library milestone.

## Sources
- Full profile: [output/Walker_Kessler/2026-04-23_profile.md](../../output/Walker_Kessler/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
