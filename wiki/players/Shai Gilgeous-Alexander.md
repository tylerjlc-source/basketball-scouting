---
player: Shai Gilgeous-Alexander
group: Guard
archetype: Offensive Engine
composite: 9.62
tier: 2
tier_band: 9.50–9.79
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Shai_Gilgeous-Alexander/2026-04-23_profile.md
scored_session: null
last_updated_session: 99
rubric_version: v3
pot: 9.72
sd01_at_basket_finishing: 9.3
sd02_contact_finishing: 9.3
sd03_post_offense: 3.0
sd04_catch_shoot_3pt: 9.0
sd05_off_dribble_shooting: 9.3
sd06_mid_range: 9.5
sd07_free_throw: 8.8
sd08_handling_creation: 9.3
sd09_touch_feel: 9.0
sd10_ball_security: 8.8
sd11_court_vision: 8.5
sd12_decision_making: 9.2
sd13_passing_execution: 8.0
sd14_off_ball_movement: 7.5
sd15_on_ball_pressure: 8.3
sd16_help_defense: 8.0
sd17_rim_protection: 4.0
sd18_post_defense: 5.5
sd19_offensive_rebounding: 4.5
sd20_defensive_rebounding: 7.3
sd21_burst_explosion: 8.5
sd22_lateral_quickness: 8.5
sd23_strength: 7.0
sd24_shot_selection: 9.3
sd25_effort_motor: 8.5
sd26_competitive_character: 9.3
d1_finishing: 9.3
d2_shooting: 9.2
d3_ball_skills: 9.0
d4_playmaking: 8.3
d5_defense: 8.2
d6_rebounding: 7.3
d7_athleticism: 8.0
d8_iq_motor: 9.0
---

# Shai Gilgeous-Alexander

**[[Offensive Engine]]** Guard — composite **9.62** (Tier 2).

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
Updated Session 99 — was 9.46 Tier 3; drift correction post-2024-25 MVP + Finals MVP + Championship + 2025-26 Clutch POY + MVP finalist. Crossed Tier 3 → Tier 2. R13 Stage 2 did NOT fire (strict convergence gate; stat TS% shrink diverged from qualitative Finals MVP rise) — composite move driven by credential-driven placement alone per S99-F01 scout-composite learning.

## Sources
- Full profile: [output/Shai_Gilgeous-Alexander/2026-04-23_profile.md](../../output/Shai_Gilgeous-Alexander/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
