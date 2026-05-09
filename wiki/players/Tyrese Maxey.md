---
player: Tyrese Maxey
group: Guard
archetype: Offensive Engine
composite: 8.66
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Tyrese_Maxey/2026-05-01_profile.md
scored_session: 131
last_updated_session: 131
rubric_version: v3
pot: 8.90
sd01_at_basket_finishing: 7.9
sd02_contact_finishing: 7.2
sd03_post_offense: 2.5
sd04_catch_shoot_3pt: 8.6
sd05_off_dribble_shooting: 7.2
sd06_mid_range: 7.6
sd07_free_throw: 9.0
sd08_handling_creation: 7.9
sd09_touch_feel: 7.6
sd10_ball_security: 8.0
sd11_court_vision: 7.4
sd12_decision_making: 7.4
sd13_passing_execution: 7.4
sd14_off_ball_movement: 8.1
sd15_on_ball_pressure: 7.3
sd16_help_defense: 6.8
sd17_rim_protection: 2.5
sd18_post_defense: 3.5
sd19_offensive_rebounding: 5.0
sd20_defensive_rebounding: 6.8
sd21_burst_explosion: 8.4
sd22_lateral_quickness: 8.0
sd23_strength: 6.5
sd24_shot_selection: 7.3
sd25_effort_motor: 8.3
sd26_competitive_character: 8.2
d1_finishing: 7.6
d2_shooting: 8.1
d3_ball_skills: 7.8
d4_playmaking: 7.6
d5_defense: 7.1
d6_rebounding: 6.8
d7_athleticism: 7.6
d8_iq_motor: 7.9
---

# Tyrese Maxey

**[[Offensive Engine]]** Guard — composite **8.66** (Tier 5). Speed-based primary-handler lead guard whose value rests on elite catch-and-shoot 3PT, transition-pull-up gravity, and an ascending defensive trajectory at modest size.

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
- Full profile: [output/Tyrese_Maxey/2026-05-01_profile.md](../../output/Tyrese_Maxey/2026-05-01_profile.md)
- Research packets: [raw/Tyrese_Maxey/2026-05-01_research-packet.md](../../raw/Tyrese_Maxey/2026-05-01_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
