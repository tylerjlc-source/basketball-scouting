---
player: Anthony Davis
group: Big
archetype: All-Around Big
composite: 8.75
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Anthony_Davis/2026-05-02_profile.md
scored_session: 136
last_updated_session: 136
rubric_version: v3
pot: 8.75
sd01_at_basket_finishing: 9.1
sd02_contact_finishing: 8.7
sd03_post_offense: 7.2
sd04_catch_shoot_3pt: 6.3
sd05_off_dribble_shooting: 7.1
sd06_mid_range: 7.6
sd07_free_throw: 8.5
sd08_handling_creation: 8.2
sd09_touch_feel: 8.6
sd10_ball_security: 7.6
sd11_court_vision: 7.2
sd12_decision_making: 7.4
sd13_passing_execution: 7.6
sd14_off_ball_movement: 7.1
sd15_on_ball_pressure: 8.6
sd16_help_defense: 9.0
sd17_rim_protection: 8.7
sd18_post_defense: 9.0
sd19_offensive_rebounding: 7.5
sd20_defensive_rebounding: 8.5
sd21_burst_explosion: 8.5
sd22_lateral_quickness: 8.5
sd23_strength: 7.5
sd24_shot_selection: 7.6
sd25_effort_motor: 7.2
sd26_competitive_character: 7.8
d1_finishing: 8.3
d2_shooting: 7.4
d3_ball_skills: 8.1
d4_playmaking: 7.3
d5_defense: 8.8
d6_rebounding: 8.0
d7_athleticism: 8.2
d8_iq_motor: 7.5
---

# Anthony Davis

**[[All-Around Big]]** Big — composite **8.75** (Tier 5). Two-way All-Around Big anchored by elite defense and interior scoring; healthy-baseline read of 2023-24 All-NBA 2nd / All-Def 1st peak placed against age-33 trajectory drag and 2025-26 active-injury dormancy.

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
Injury flag — 2026 dormant

## Sources
- Full profile: [output/Anthony_Davis/2026-05-02_profile.md](../../output/Anthony_Davis/2026-05-02_profile.md)
- Research packets: [raw/Anthony_Davis/2026-05-02_research-packet.md](../../raw/Anthony_Davis/2026-05-02_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
