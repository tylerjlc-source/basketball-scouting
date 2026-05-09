---
player: Bogdan Bogdanović
group: Wing
archetype: 3-and-some-D Wing
composite: 6.85
tier: 9
tier_band: 6.80–7.49
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Bogdan_Bogdanovic/2026-04-23_profile.md
scored_session: 100
last_updated_session: 100
rubric_version: v3
pot: null
sd01_at_basket_finishing: 6.7
sd02_contact_finishing: 5.8
sd03_post_offense: 4.0
sd04_catch_shoot_3pt: 7.2
sd05_off_dribble_shooting: 7.2
sd06_mid_range: 7.8
sd07_free_throw: 8.8
sd08_handling_creation: 6.6
sd09_touch_feel: 7.4
sd10_ball_security: 7.5
sd11_court_vision: 6.8
sd12_decision_making: 6.8
sd13_passing_execution: 6.9
sd14_off_ball_movement: 6.4
sd15_on_ball_pressure: 5.3
sd16_help_defense: 5.5
sd17_rim_protection: 3.4
sd18_post_defense: 4.5
sd19_offensive_rebounding: 4.1
sd20_defensive_rebounding: 5.4
sd21_burst_explosion: 5.1
sd22_lateral_quickness: 5.0
sd23_strength: 7.1
sd24_shot_selection: 6.6
sd25_effort_motor: 7.1
sd26_competitive_character: 6.6
d1_finishing: 6.3
d2_shooting: 7.8
d3_ball_skills: 7.2
d4_playmaking: 6.7
d5_defense: 4.7
d6_rebounding: 5.4
d7_athleticism: 5.7
d8_iq_motor: 6.8
---

# Bogdan Bogdanović

**[[3-and-some-D Wing]]** Wing — composite **6.85** (Tier 9).

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
Added Session 100 — first 3-and-some-D Wing anchor in library (archetype previously zero-populated); completes Bogdan as batch-1 player of the S100 wing/big scale validation sweep; R13 Stage 2 moderate shrink −0.10 applied at composite (pre-modifier 6.95), Stage 1 POT modifier −0.20 applied in projection block; archetype confirmed via structural parallel to Bojan Bogdanović (confirmed fit).

## Sources
- Full profile: [output/Bogdan_Bogdanovic/2026-04-23_profile.md](../../output/Bogdan_Bogdanovic/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
