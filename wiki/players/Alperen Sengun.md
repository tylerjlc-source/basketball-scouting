---
player: Alperen Sengun
group: Big
archetype: All-Around Big
composite: 8.45
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Alperen_Sengun/2026-04-24_profile.md
scored_session: 105
last_updated_session: 105
rubric_version: v3
pot: 8.55
sd01_at_basket_finishing: 8.3
sd02_contact_finishing: 7.5
sd03_post_offense: 9.0
sd04_catch_shoot_3pt: 6.0
sd05_off_dribble_shooting: 4.5
sd06_mid_range: 5.5
sd07_free_throw: 6.5
sd08_handling_creation: 7.5
sd09_touch_feel: 8.0
sd10_ball_security: 6.5
sd11_court_vision: 9.0
sd12_decision_making: 7.5
sd13_passing_execution: 8.0
sd14_off_ball_movement: 7.0
sd15_on_ball_pressure: 5.0
sd16_help_defense: 7.0
sd17_rim_protection: 5.5
sd18_post_defense: 6.5
sd19_offensive_rebounding: 8.0
sd20_defensive_rebounding: 8.0
sd21_burst_explosion: 5.5
sd22_lateral_quickness: 5.0
sd23_strength: 7.0
sd24_shot_selection: 7.0
sd25_effort_motor: 7.5
sd26_competitive_character: 7.5
d1_finishing: 8.3
d2_shooting: 5.6
d3_ball_skills: 7.3
d4_playmaking: 7.9
d5_defense: 6.0
d6_rebounding: 8.0
d7_athleticism: 5.8
d8_iq_motor: 7.3
---

# Alperen Sengun

**[[All-Around Big]]** Big — composite **8.45** (Tier 6).

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
Updated Session 105 — was 8.38 (legacy anchor, no prior notes). Full 5-skill chain re-evaluation completed; archetype confirmed as All-Around Big. Composite +0.07 upward in-band.

## Sources
- Full profile: [output/Alperen_Sengun/2026-04-24_profile.md](../../output/Alperen_Sengun/2026-04-24_profile.md)
- Research packets: [raw/Alperen_Sengun/](../../raw/Alperen_Sengun/) (one packet, 2026-04-24)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
