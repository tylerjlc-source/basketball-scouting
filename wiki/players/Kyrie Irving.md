---
player: Kyrie Irving
group: Guard
archetype: Offensive Engine
composite: 8.78
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Kyrie_Irving/2026-05-01_profile.md
scored_session: 128
last_updated_session: 128
rubric_version: v3
pot: 8.78
sd01_at_basket_finishing: 9.6
sd02_contact_finishing: 7.1
sd03_post_offense: 2.5
sd04_catch_shoot_3pt: 8.7
sd05_off_dribble_shooting: 9.1
sd06_mid_range: 8.2
sd07_free_throw: 9.2
sd08_handling_creation: 9.7
sd09_touch_feel: 9.5
sd10_ball_security: 8.2
sd11_court_vision: 7.6
sd12_decision_making: 7.5
sd13_passing_execution: 7.6
sd14_off_ball_movement: 7.1
sd15_on_ball_pressure: 6.6
sd16_help_defense: 6.3
sd17_rim_protection: 2.5
sd18_post_defense: 3.5
sd19_offensive_rebounding: 7.1
sd20_defensive_rebounding: 7.1
sd21_burst_explosion: 6.5
sd22_lateral_quickness: 6.6
sd23_strength: 6.0
sd24_shot_selection: 7.0
sd25_effort_motor: 7.0
sd26_competitive_character: 6.3
d1_finishing: 8.4
d2_shooting: 8.8
d3_ball_skills: 9.1
d4_playmaking: 7.5
d5_defense: 6.5
d6_rebounding: 7.1
d7_athleticism: 6.4
d8_iq_motor: 6.8
---

# Kyrie Irving

**[[Offensive Engine]]** Guard — composite **8.78** (Tier 5). Multi-level scoring lead guard with one of the most discussed handles of his generation, anchored on the 2024-25 pre-ACL 50-GP fragment per R12.

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
ACL — out 2025-26

## Sources
- Full profile: [output/Kyrie_Irving/2026-05-01_profile.md](../../output/Kyrie_Irving/2026-05-01_profile.md)
- Research packets: [raw/Kyrie_Irving/2026-05-01_research-packet.md](../../raw/Kyrie_Irving/2026-05-01_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
