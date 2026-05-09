---
player: Ja Morant
group: Guard
archetype: Offensive Engine
composite: 8.22
tier: 7
tier_band: 7.90–8.29
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Ja_Morant/2026-04-22_profile.md
scored_session: 96
last_updated_session: 96
rubric_version: v3
pot: null
sd01_at_basket_finishing: 8.0
sd02_contact_finishing: 7.5
sd03_post_offense: 2.5
sd04_catch_shoot_3pt: 6.5
sd05_off_dribble_shooting: 7.0
sd06_mid_range: 8.0
sd07_free_throw: 7.5
sd08_handling_creation: 8.5
sd09_touch_feel: 8.5
sd10_ball_security: 6.0
sd11_court_vision: 8.5
sd12_decision_making: 5.5
sd13_passing_execution: 8.0
sd14_off_ball_movement: 5.5
sd15_on_ball_pressure: 5.0
sd16_help_defense: 5.0
sd17_rim_protection: 2.5
sd18_post_defense: 3.0
sd19_offensive_rebounding: 5.5
sd20_defensive_rebounding: 7.0
sd21_burst_explosion: 7.5
sd22_lateral_quickness: 7.0
sd23_strength: 5.0
sd24_shot_selection: 6.0
sd25_effort_motor: 5.5
sd26_competitive_character: 6.0
d1_finishing: 7.8
d2_shooting: 7.3
d3_ball_skills: 7.7
d4_playmaking: 6.9
d5_defense: 5.0
d6_rebounding: 7.0
d7_athleticism: 6.5
d8_iq_motor: 5.8
---

# Ja Morant

**[[Offensive Engine]]** Guard — composite **8.22** (Tier 7).

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
Added Session 96 — R12 override (2024-25 anchor); R13 Stage 2 dormant (elbow UCL); first archetype-migration anchor (Slasher → OE post-shoulder). Second 5-skill chain profile, first live R12 anchor override (2024-25 fragment selected over default 2022-23 walk-back per S96 calibration finding), first R13 Stage 2 active-injury dormancy invocation (2025-26 elbow UCL ruling out next playoff cycle), first documented archetype-migration anchor (pre-shoulder Slasher → post-shoulder Offensive Engine).

## Sources
- Full profile: [output/Ja_Morant/2026-04-22_profile.md](../../output/Ja_Morant/2026-04-22_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
