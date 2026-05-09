---
player: Chet Holmgren
group: Big
archetype: Switchable Big
composite: 8.48
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Chet_Holmgren/2026-05-06_profile.md
scored_session: 155
last_updated_session: 155
rubric_version: v3
pot: 8.60
sd01_at_basket_finishing: 7.7
sd02_contact_finishing: 7.4
sd03_post_offense: 5.5
sd04_catch_shoot_3pt: 7.6
sd05_off_dribble_shooting: 6.7
sd06_mid_range: 7.8
sd07_free_throw: 8.5
sd08_handling_creation: 7.7
sd09_touch_feel: 7.8
sd10_ball_security: 6.8
sd11_court_vision: 7.2
sd12_decision_making: 7.1
sd13_passing_execution: 7.2
sd14_off_ball_movement: 7.4
sd15_on_ball_pressure: 7.0
sd16_help_defense: 8.5
sd17_rim_protection: 8.9
sd18_post_defense: 5.7
sd19_offensive_rebounding: 5.8
sd20_defensive_rebounding: 7.2
sd21_burst_explosion: 7.1
sd22_lateral_quickness: 7.0
sd23_strength: 5.7
sd24_shot_selection: 7.1
sd25_effort_motor: 8.6
sd26_competitive_character: 7.7
d1_finishing: 6.9
d2_shooting: 7.7
d3_ball_skills: 7.4
d4_playmaking: 7.2
d5_defense: 7.5
d6_rebounding: 6.5
d7_athleticism: 6.6
d8_iq_motor: 7.8
---

# Chet Holmgren

**[[Switchable Big]]** Big — composite **8.48** (Tier 6). 7'1" defensive anchor with skill-big offense layered on top — championship-validated rim protection paired with stretch-five shooting touch and guard-style handle, held below the star tier by structural strength and post-defense gaps.

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
1x All-Star; 2024-25 Champion; prior 8.31

## Sources
- Full profile: [output/Chet_Holmgren/2026-05-06_profile.md](../../output/Chet_Holmgren/2026-05-06_profile.md)
- Research packets: [raw/Chet_Holmgren/2026-05-06_research-packet.md](../../raw/Chet_Holmgren/2026-05-06_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
