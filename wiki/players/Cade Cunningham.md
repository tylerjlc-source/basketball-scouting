---
player: Cade Cunningham
group: Guard
archetype: Jumbo Playmaker
composite: 8.96
tier: 4
tier_band: 8.90–9.19
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Cade_Cunningham/2026-04-27_profile.md
scored_session: 112
last_updated_session: 112
rubric_version: v3
pot: 9.00
sd01_at_basket_finishing: 7.2
sd02_contact_finishing: 7.0
sd03_post_offense: 3.5
sd04_catch_shoot_3pt: 6.5
sd05_off_dribble_shooting: 7.5
sd06_mid_range: 7.5
sd07_free_throw: 8.2
sd08_handling_creation: 8.5
sd09_touch_feel: 8.0
sd10_ball_security: 7.0
sd11_court_vision: 9.0
sd12_decision_making: 8.0
sd13_passing_execution: 8.0
sd14_off_ball_movement: 5.5
sd15_on_ball_pressure: 6.0
sd16_help_defense: 7.0
sd17_rim_protection: 5.5
sd18_post_defense: 6.5
sd19_offensive_rebounding: 5.5
sd20_defensive_rebounding: 7.5
sd21_burst_explosion: 5.5
sd22_lateral_quickness: 6.0
sd23_strength: 7.5
sd24_shot_selection: 7.5
sd25_effort_motor: 8.0
sd26_competitive_character: 8.5
d1_finishing: 5.9
d2_shooting: 7.4
d3_ball_skills: 7.8
d4_playmaking: 7.6
d5_defense: 6.5
d6_rebounding: 6.5
d7_athleticism: 6.3
d8_iq_motor: 8.0
---

# Cade Cunningham

**[[Jumbo Playmaker]]** Guard — composite **8.96** (Tier 4). Wing-sized lead guard whose value is the playmaking, not the scoring; physical mismatch is the product.

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
No update history recorded.

## Sources
- Full profile: [output/Cade_Cunningham/2026-04-27_profile.md](../../output/Cade_Cunningham/2026-04-27_profile.md)
- Research packets: [raw/Cade_Cunningham/2026-04-27_research-packet.md](../../raw/Cade_Cunningham/2026-04-27_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
