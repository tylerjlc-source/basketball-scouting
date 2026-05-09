---
player: Tyrese Haliburton
group: Guard
archetype: Pure Point Guard
composite: 8.92
tier: 4
tier_band: 8.90–9.19
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Tyrese_Haliburton/2026-04-30_profile.md
scored_session: 120
last_updated_session: 120
rubric_version: v3
pot: 9.11
sd01_at_basket_finishing: 7.3
sd02_contact_finishing: 5.2
sd03_post_offense: 2.5
sd04_catch_shoot_3pt: 9.5
sd05_off_dribble_shooting: 7.6
sd06_mid_range: 9
sd07_free_throw: 8.5
sd08_handling_creation: 7.7
sd09_touch_feel: 9.2
sd10_ball_security: 9.2
sd11_court_vision: 9.5
sd12_decision_making: 9
sd13_passing_execution: 9.1
sd14_off_ball_movement: 8.6
sd15_on_ball_pressure: 5
sd16_help_defense: 7.4
sd17_rim_protection: 4.8
sd18_post_defense: 4.8
sd19_offensive_rebounding: 5
sd20_defensive_rebounding: 6.4
sd21_burst_explosion: 5
sd22_lateral_quickness: 5
sd23_strength: 4.8
sd24_shot_selection: 9
sd25_effort_motor: 7.2
sd26_competitive_character: 9
d1_finishing: 6.3
d2_shooting: 8.7
d3_ball_skills: 8.7
d4_playmaking: 9.1
d5_defense: 6.2
d6_rebounding: 5.7
d7_athleticism: 4.9
d8_iq_motor: 8.4
---

# Tyrese Haliburton

**[[Pure Point Guard]]** Guard — composite **9.11** (Tier 4). 6'5" floor general whose value is delivered through elite playmaking, ball security, and shot-making rather than self-creation volume — the most efficient passer-shooter combo of his era.

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

Achilles 6/2025 — R13 dormant 2025-26

## Sources

- Full profile: [output/Tyrese_Haliburton/2026-04-30_profile.md](../../output/Tyrese_Haliburton/2026-04-30_profile.md)
- Research packets: [raw/Tyrese_Haliburton/2026-04-30_research-packet.md](../../raw/Tyrese_Haliburton/2026-04-30_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
