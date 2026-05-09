---
player: Sam Hauser
group: Wing
archetype: Shooting Specialist
composite: 7.55
tier: 8
tier_band: 7.50–7.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Sam_Hauser/2026-04-23_profile.md
scored_session: 100
last_updated_session: 100
rubric_version: v3
pot: null
sd01_at_basket_finishing: 7.6
sd02_contact_finishing: 4.5
sd03_post_offense: 4.0
sd04_catch_shoot_3pt: 8.3
sd05_off_dribble_shooting: 7.8
sd06_mid_range: 7.9
sd07_free_throw: 9.1
sd08_handling_creation: 5.5
sd09_touch_feel: 8.2
sd10_ball_security: 8.1
sd11_court_vision: 5.5
sd12_decision_making: 7.5
sd13_passing_execution: 5.5
sd14_off_ball_movement: 7.6
sd15_on_ball_pressure: 6.6
sd16_help_defense: 6.5
sd17_rim_protection: 4.5
sd18_post_defense: 5.0
sd19_offensive_rebounding: 5.5
sd20_defensive_rebounding: 6.5
sd21_burst_explosion: 6.3
sd22_lateral_quickness: 6.0
sd23_strength: 6.0
sd24_shot_selection: 7.7
sd25_effort_motor: 7.5
sd26_competitive_character: 7.2
d1_finishing: 7.6
d2_shooting: 8.3
d3_ball_skills: 8.2
d4_playmaking: 7.6
d5_defense: 6.6
d6_rebounding: 6.0
d7_athleticism: 6.2
d8_iq_motor: 7.5
---

# Sam Hauser

**[[Shooting Specialist (Wing)]]** Wing — composite **7.55** (Tier 8).

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
Added Session 100 — second Shooting Specialist Wing anchor in library (first active vet — Knueppel 7.91 rookie is the other); Korver age-28 and Bertans age-28 🟢 Full comps validate archetype template; R13 Stage 2 moderate shrink −0.10 applied (pre-modifier 7.65), Stage 1 POT modifier −0.20 applied in projection block. Batch-1 player 3 of 4 in S100 wing/big scale validation sweep.

## Sources
- Full profile: [output/Sam_Hauser/2026-04-23_profile.md](../../output/Sam_Hauser/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
