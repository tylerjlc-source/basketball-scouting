---
player: Jayson Tatum
group: Wing
archetype: All-Around Wing
composite: 8.88
tier: 5
tier_band: 8.60–8.89
status: Active (injury flag)
competition_level: NBA
has_profile: true
profile_path: output/Jayson_Tatum/2026-04-25_profile.md
scored_session: 108
last_updated_session: 108
rubric_version: v3
pot: 8.95
sd01_at_basket_finishing: 8.0
sd02_contact_finishing: 7.0
sd03_post_offense: 6.5
sd04_catch_shoot_3pt: 8.5
sd05_off_dribble_shooting: 7.0
sd06_mid_range: 7.5
sd07_free_throw: 8.0
sd08_handling_creation: 8.0
sd09_touch_feel: 7.5
sd10_ball_security: 8.0
sd11_court_vision: 8.0
sd12_decision_making: 8.0
sd13_passing_execution: 7.5
sd14_off_ball_movement: 7.0
sd15_on_ball_pressure: 8.0
sd16_help_defense: 8.0
sd17_rim_protection: 6.0
sd18_post_defense: 7.5
sd19_offensive_rebounding: 5.0
sd20_defensive_rebounding: 9.0
sd21_burst_explosion: 7.0
sd22_lateral_quickness: 7.5
sd23_strength: 7.5
sd24_shot_selection: 7.0
sd25_effort_motor: 7.5
sd26_competitive_character: 8.5
d1_finishing: 7.2
d2_shooting: 7.8
d3_ball_skills: 7.8
d4_playmaking: 7.6
d5_defense: 7.4
d6_rebounding: 7.0
d7_athleticism: 7.3
d8_iq_motor: 7.7
---

# Jayson Tatum

**[[All-Around Wing]]** Wing — composite **8.88** (Tier 5, top of band). Achilles recovery active.

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
Achilles 5/2025 — active recovery

## Sources
- Full profile: [output/Jayson_Tatum/2026-04-25_profile.md](../../output/Jayson_Tatum/2026-04-25_profile.md)
- Research packets: [raw/Jayson_Tatum/2026-04-25_research-packet.md](../../raw/Jayson_Tatum/2026-04-25_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
