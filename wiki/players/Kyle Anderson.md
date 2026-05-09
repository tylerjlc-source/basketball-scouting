---
player: Kyle Anderson
group: Wing
archetype: Secondary Playmaker
composite: 7.61
tier: 8
tier_band: 7.50–7.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Kyle_Anderson/2026-04-23_profile.md
scored_session: 100
last_updated_session: 100
rubric_version: v3
pot: null
sd01_at_basket_finishing: 8.2
sd02_contact_finishing: 7.1
sd03_post_offense: 4.0
sd04_catch_shoot_3pt: 6.4
sd05_off_dribble_shooting: 5.5
sd06_mid_range: 5.5
sd07_free_throw: 6.1
sd08_handling_creation: 7.1
sd09_touch_feel: 7.4
sd10_ball_security: 8.3
sd11_court_vision: 8.1
sd12_decision_making: 8.1
sd13_passing_execution: 7.4
sd14_off_ball_movement: 6.3
sd15_on_ball_pressure: 6.8
sd16_help_defense: 7.2
sd17_rim_protection: 5.7
sd18_post_defense: 5.5
sd19_offensive_rebounding: 6.8
sd20_defensive_rebounding: 7.3
sd21_burst_explosion: 5.4
sd22_lateral_quickness: 4.7
sd23_strength: 7.0
sd24_shot_selection: 7.1
sd25_effort_motor: 7.3
sd26_competitive_character: 7.5
d1_finishing: 7.7
d2_shooting: 6.3
d3_ball_skills: 7.6
d4_playmaking: 7.5
d5_defense: 7.0
d6_rebounding: 7.3
d7_athleticism: 5.7
d8_iq_motor: 7.3
---

# Kyle Anderson

**[[Secondary Playmaker]]** Wing — composite **7.61** (Tier 8).

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
Added Session 100 — first Secondary Playmaker anchor in library under current tag (archetype confirmed fit per ARCHETYPE-WEIGHTS-WINGS.md:290 — Kyle Anderson himself is the archetype template); R13 Neutral (no Stage 2 modifier); Boris Diaw age-comparable comp 🟢 Full tier validates archetype. Batch-1 player 2 of 4 in S100 wing/big scale validation sweep.

## Sources
- Full profile: [output/Kyle_Anderson/2026-04-23_profile.md](../../output/Kyle_Anderson/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
