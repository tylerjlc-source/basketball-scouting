---
player: Luka Doncic
group: Guard
archetype: Jumbo Playmaker
composite: 9.14
tier: 4
tier_band: 8.90–9.19
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Luka_Doncic/2026-04-30_profile.md
scored_session: 124
last_updated_session: 124
rubric_version: v3
pot: 9.17
sd01_at_basket_finishing: 8.7
sd02_contact_finishing: 9.5
sd03_post_offense: 8.5
sd04_catch_shoot_3pt: 8
sd05_off_dribble_shooting: 9
sd06_mid_range: 7.8
sd07_free_throw: 7.5
sd08_handling_creation: 9.5
sd09_touch_feel: 9.3
sd10_ball_security: 7
sd11_court_vision: 9.5
sd12_decision_making: 7.5
sd13_passing_execution: 9.3
sd14_off_ball_movement: 5
sd15_on_ball_pressure: 5
sd16_help_defense: 5.5
sd17_rim_protection: 4.5
sd18_post_defense: 6.5
sd19_offensive_rebounding: 5
sd20_defensive_rebounding: 9
sd21_burst_explosion: 5
sd22_lateral_quickness: 5
sd23_strength: 8.5
sd24_shot_selection: 6
sd25_effort_motor: 5
sd26_competitive_character: 7
d1_finishing: 8.9
d2_shooting: 8.1
d3_ball_skills: 8.6
d4_playmaking: 7.8
d5_defense: 5.3
d6_rebounding: 7
d7_athleticism: 6.2
d8_iq_motor: 6
---

# Luka Doncic

**[[Jumbo Playmaker]]** Guard — composite **9.07** (Tier 4). A 6'7" 244-pound primary creator who runs offense like a point guard and bullies the post like a wing — canonical Jumbo Playmaker, alongside LeBron and Magic on the archetype roster.

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
Hamstring 4/2026 — R13 dormant

## Sources
- Full profile: [output/Luka_Doncic/2026-04-30_profile.md](../../output/Luka_Doncic/2026-04-30_profile.md)
- Research packets:
  - [raw/Luka_Doncic/2026-04-30_research-packet.md](../../raw/Luka_Doncic/2026-04-30_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
