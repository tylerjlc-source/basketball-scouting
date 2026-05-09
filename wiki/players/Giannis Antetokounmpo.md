---
player: Giannis Antetokounmpo
group: Big
archetype: All-Around Big
composite: 9.30
tier: 3
tier_band: 9.20–9.49
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Giannis_Antetokounmpo/2026-04-29_profile.md
scored_session: 116
last_updated_session: 116
rubric_version: v3
pot: 9.20
sd01_at_basket_finishing: 9.4
sd02_contact_finishing: 9.1
sd03_post_offense: 7.3
sd04_catch_shoot_3pt: 5.9
sd05_off_dribble_shooting: 6.5
sd06_mid_range: 7.1
sd07_free_throw: 5.7
sd08_handling_creation: 9.4
sd09_touch_feel: 6.9
sd10_ball_security: 6.4
sd11_court_vision: 8.1
sd12_decision_making: 7.6
sd13_passing_execution: 6.9
sd14_off_ball_movement: 7.4
sd15_on_ball_pressure: 8.3
sd16_help_defense: 8.9
sd17_rim_protection: 7.3
sd18_post_defense: 7.3
sd19_offensive_rebounding: 7.4
sd20_defensive_rebounding: 8.1
sd21_burst_explosion: 9.4
sd22_lateral_quickness: 9.0
sd23_strength: 8.3
sd24_shot_selection: 8.1
sd25_effort_motor: 9.5
sd26_competitive_character: 9.5
d1_finishing: 8.6
d2_shooting: 6.3
d3_ball_skills: 7.6
d4_playmaking: 7.5
d5_defense: 8.0
d6_rebounding: 7.8
d7_athleticism: 8.9
d8_iq_motor: 9.0
---

# Giannis Antetokounmpo

**[[All-Around Big]]** Big — composite **9.30** (Tier 3). Athletic primary-creator non-shooter Big with elite multi-position defense; Adebayo-direction within AAB rather than Jokić-direction.

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

2x MVP, 1x FMVP, 1x DPOY

## Sources

- Full profile: [output/Giannis_Antetokounmpo/2026-04-29_profile.md](../../output/Giannis_Antetokounmpo/2026-04-29_profile.md)
- Research packet: [raw/Giannis_Antetokounmpo/2026-04-29_research-packet.md](../../raw/Giannis_Antetokounmpo/2026-04-29_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
