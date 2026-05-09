---
player: Jaren Jackson Jr.
group: Big
archetype: Switchable Big
composite: 8.52
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Jaren_Jackson_Jr/2026-05-02_profile.md
scored_session: 133
last_updated_session: 133
rubric_version: v3
pot: 8.70
sd01_at_basket_finishing: 8.1
sd02_contact_finishing: 7.2
sd03_post_offense: 5.5
sd04_catch_shoot_3pt: 8.5
sd05_off_dribble_shooting: 5.0
sd06_mid_range: 5.7
sd07_free_throw: 8.7
sd08_handling_creation: 7.0
sd09_touch_feel: 7.7
sd10_ball_security: 6.0
sd11_court_vision: 6.0
sd12_decision_making: 5.7
sd13_passing_execution: 6.5
sd14_off_ball_movement: 7.5
sd15_on_ball_pressure: 8.5
sd16_help_defense: 8.0
sd17_rim_protection: 7.7
sd18_post_defense: 5.7
sd19_offensive_rebounding: 4.5
sd20_defensive_rebounding: 5.0
sd21_burst_explosion: 7.7
sd22_lateral_quickness: 8.5
sd23_strength: 5.5
sd24_shot_selection: 7.5
sd25_effort_motor: 6.5
sd26_competitive_character: 7.0
d1_finishing: 6.9
d2_shooting: 7.0
d3_ball_skills: 6.9
d4_playmaking: 6.4
d5_defense: 7.5
d6_rebounding: 4.8
d7_athleticism: 7.2
d8_iq_motor: 7.0
---

# Jaren Jackson Jr.

**[[Switchable Big]]** Big — composite **8.52** (Tier 6). DPOY-tier switchable defender with elite spacing, capped by structural rebounding and strength shortfalls.

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
PVNS knee 2/2026 — out 2025-26

## Sources
- Full profile: [output/Jaren_Jackson_Jr/2026-05-02_profile.md](../../output/Jaren_Jackson_Jr/2026-05-02_profile.md)
- Research packets: [raw/Jaren_Jackson_Jr/2026-05-02_research-packet.md](../../raw/Jaren_Jackson_Jr/2026-05-02_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
