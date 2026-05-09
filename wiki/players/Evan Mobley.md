---
player: Evan Mobley
group: Big
archetype: Switchable Big
composite: 8.67
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Evan_Mobley/2026-04-24_profile.md
scored_session: 102
last_updated_session: 102
rubric_version: v3
pot: 8.89
sd01_at_basket_finishing: 8.2
sd02_contact_finishing: 6.8
sd03_post_offense: 5.7
sd04_catch_shoot_3pt: 6.6
sd05_off_dribble_shooting: 6.4
sd06_mid_range: 6.8
sd07_free_throw: 5.9
sd08_handling_creation: 7.1
sd09_touch_feel: 7.8
sd10_ball_security: 7.3
sd11_court_vision: 8.1
sd12_decision_making: 7.3
sd13_passing_execution: 7.8
sd14_off_ball_movement: 8.2
sd15_on_ball_pressure: 9.2
sd16_help_defense: 8.8
sd17_rim_protection: 8.6
sd18_post_defense: 8.3
sd19_offensive_rebounding: 6.8
sd20_defensive_rebounding: 7.0
sd21_burst_explosion: 8.3
sd22_lateral_quickness: 9.2
sd23_strength: 7.2
sd24_shot_selection: 7.8
sd25_effort_motor: 7.9
sd26_competitive_character: 7.8
d1_finishing: 6.9
d2_shooting: 6.4
d3_ball_skills: 7.4
d4_playmaking: 7.9
d5_defense: 8.7
d6_rebounding: 6.9
d7_athleticism: 8.2
d8_iq_motor: 7.8
---

# Evan Mobley

**[[Switchable Big]]** Big — composite **8.67** (Tier 5).

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
Added Session 102 — first player of S101 batch 2 wing/big scale validation sweep; fills Tier 5 current-era Switchable Big gap between Bam 8.84 and JJJ 8.60; 2024-25 DPOY + All-NBA 2nd + 1st All-Star at age 23; R13 Stage 2 Directional Rise +0.05 applied (first Directional application in library); Bam age-24 🟢 Full + JJJ age-23 🟢 Full under NBA-Vet Adaptation; left-calf recurrence flag 2025-26.

## Sources
- Full profile: [output/Evan_Mobley/2026-04-24_profile.md](../../output/Evan_Mobley/2026-04-24_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
