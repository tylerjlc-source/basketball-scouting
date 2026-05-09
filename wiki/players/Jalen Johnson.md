---
player: Jalen Johnson
group: Wing
archetype: All-Around Wing
composite: 8.45
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Jalen_Johnson/2026-05-02_profile.md
scored_session: 138
last_updated_session: 138
rubric_version: v3
pot: 8.75
sd01_at_basket_finishing: 8.2
sd02_contact_finishing: 7.6
sd03_post_offense: 5.5
sd04_catch_shoot_3pt: 7.0
sd05_off_dribble_shooting: 5.7
sd06_mid_range: 6.7
sd07_free_throw: 7.5
sd08_handling_creation: 7.6
sd09_touch_feel: 7.2
sd10_ball_security: 6.0
sd11_court_vision: 8.5
sd12_decision_making: 7.0
sd13_passing_execution: 7.6
sd14_off_ball_movement: 7.1
sd15_on_ball_pressure: 7.1
sd16_help_defense: 7.0
sd17_rim_protection: 6.6
sd18_post_defense: 6.5
sd19_offensive_rebounding: 6.5
sd20_defensive_rebounding: 9.0
sd21_burst_explosion: 7.6
sd22_lateral_quickness: 7.2
sd23_strength: 7.1
sd24_shot_selection: 7.0
sd25_effort_motor: 8.0
sd26_competitive_character: 7.5
d1_finishing: 7.1
d2_shooting: 6.7
d3_ball_skills: 6.9
d4_playmaking: 7.6
d5_defense: 6.8
d6_rebounding: 7.8
d7_athleticism: 7.3
d8_iq_motor: 7.5
---

# Jalen Johnson

**[[All-Around Wing]]** Wing — composite **8.45** (Tier 6). 6'9" 220-lb forward whose 2025-26 All-Star ascension fused multi-level scoring, primary-creator playmaking, and elite wing rebounding into a distributed All-Around profile.

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
1x All-Star 2025-26

## Sources
- Full profile: [output/Jalen_Johnson/2026-05-02_profile.md](../../output/Jalen_Johnson/2026-05-02_profile.md)
- Research packets: [raw/Jalen_Johnson/2026-05-02_research-packet.md](../../raw/Jalen_Johnson/2026-05-02_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
