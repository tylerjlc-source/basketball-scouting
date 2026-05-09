---
player: Jalen Duren
group: Big
archetype: Energy Big
composite: 8.40
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Jalen_Duren/2026-04-24_profile.md
scored_session: 106
last_updated_session: 106
rubric_version: v3
pot: 8.70
sd01_at_basket_finishing: 8.7
sd02_contact_finishing: 8.0
sd03_post_offense: 6.5
sd04_catch_shoot_3pt: 4.0
sd05_off_dribble_shooting: 4.5
sd06_mid_range: 5.5
sd07_free_throw: 7.4
sd08_handling_creation: 7.0
sd09_touch_feel: 7.6
sd10_ball_security: 6.5
sd11_court_vision: 7.0
sd12_decision_making: 6.8
sd13_passing_execution: 7.0
sd14_off_ball_movement: 8.2
sd15_on_ball_pressure: 6.3
sd16_help_defense: 7.5
sd17_rim_protection: 7.5
sd18_post_defense: 7.5
sd19_offensive_rebounding: 8.7
sd20_defensive_rebounding: 8.0
sd21_burst_explosion: 8.8
sd22_lateral_quickness: 5.5
sd23_strength: 7.5
sd24_shot_selection: 8.0
sd25_effort_motor: 8.0
sd26_competitive_character: 7.5
d1_finishing: 7.7
d2_shooting: 7.4
d3_ball_skills: 7.1
d4_playmaking: 7.5
d5_defense: 7.2
d6_rebounding: 8.4
d7_athleticism: 7.3
d8_iq_motor: 7.8
---

# Jalen Duren

**[[Energy Big]]** Big — composite **8.40** (Tier 6).

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
Updated Session 106 — was 8.30 (legacy anchor, no prior notes). Full 5-skill chain re-evaluation completed; archetype confirmed as Energy Big. Composite +0.10 upward in-band.

## Sources
- Full profile: [output/Jalen_Duren/2026-04-24_profile.md](../../output/Jalen_Duren/2026-04-24_profile.md)
- Research packets: [raw/Jalen_Duren/](../../raw/Jalen_Duren/) (one packet, 2026-04-24)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
