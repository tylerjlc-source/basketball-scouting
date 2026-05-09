---
player: Kevin Durant
group: Wing
archetype: All-Around Wing
composite: 9.26
tier: 3
tier_band: 9.20–9.49
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Kevin_Durant/2026-04-29_profile.md
scored_session: 119
last_updated_session: 119
rubric_version: v3
pot: 9.26
sd01_at_basket_finishing: 8.4
sd02_contact_finishing: 8.0
sd03_post_offense: 7.5
sd04_catch_shoot_3pt: 9.5
sd05_off_dribble_shooting: 9.4
sd06_mid_range: 9.4
sd07_free_throw: 9.2
sd08_handling_creation: 9.2
sd09_touch_feel: 9.3
sd10_ball_security: 7.3
sd11_court_vision: 8.0
sd12_decision_making: 8.0
sd13_passing_execution: 7.6
sd14_off_ball_movement: 7.7
sd15_on_ball_pressure: 7.5
sd16_help_defense: 7.4
sd17_rim_protection: 7.0
sd18_post_defense: 7.0
sd19_offensive_rebounding: 4.5
sd20_defensive_rebounding: 6.7
sd21_burst_explosion: 7.3
sd22_lateral_quickness: 7.3
sd23_strength: 7.0
sd24_shot_selection: 8.5
sd25_effort_motor: 8.3
sd26_competitive_character: 8.7
d1_finishing: 8.0
d2_shooting: 9.4
d3_ball_skills: 8.6
d4_playmaking: 7.8
d5_defense: 7.2
d6_rebounding: 5.6
d7_athleticism: 7.2
d8_iq_motor: 8.5
---

# Kevin Durant

**[[All-Around Wing]]** Wing — composite **9.26** (Tier 3). Three-level scoring wing-forward at 7'5" wingspan; densest offensive cluster in the active library paired with the heaviest career resume in the Tier 3 cluster.

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
2x FMVP; R13 dormant 4/2026

## Sources
- Full profile: [output/Kevin_Durant/2026-04-29_profile.md](../../output/Kevin_Durant/2026-04-29_profile.md)
- Research packets: [raw/Kevin_Durant/2026-04-29_research-packet.md](../../raw/Kevin_Durant/2026-04-29_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
