---
player: Jimmy Butler
group: Wing
archetype: Dribble Pass Shoot Wing
composite: 8.21
tier: 7
tier_band: 7.90–8.29
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Jimmy_Butler/2026-05-05_profile.md
scored_session: 142
last_updated_session: 142
rubric_version: v3
pot: 8.85
sd01_at_basket_finishing: 8.2
sd02_contact_finishing: 9.4
sd03_post_offense: 7.2
sd04_catch_shoot_3pt: 7.8
sd05_off_dribble_shooting: 6.5
sd06_mid_range: 5.8
sd07_free_throw: 9.1
sd08_handling_creation: 8.4
sd09_touch_feel: 7.8
sd10_ball_security: 9.0
sd11_court_vision: 8.2
sd12_decision_making: 8.2
sd13_passing_execution: 7.8
sd14_off_ball_movement: 6.0
sd15_on_ball_pressure: 6.5
sd16_help_defense: 7.8
sd17_rim_protection: 5.5
sd18_post_defense: 6.8
sd19_offensive_rebounding: 7.4
sd20_defensive_rebounding: 7.0
sd21_burst_explosion: 6.5
sd22_lateral_quickness: 6.6
sd23_strength: 8.0
sd24_shot_selection: 8.2
sd25_effort_motor: 6.4
sd26_competitive_character: 7.9
d1_finishing: 8.3
d2_shooting: 7.3
d3_ball_skills: 8.4
d4_playmaking: 7.6
d5_defense: 7.2
d6_rebounding: 7.2
d7_athleticism: 7.0
d8_iq_motor: 7.5
---

# Jimmy Butler

**[[Dribble Pass Shoot Wing]]** Wing — composite **8.21** (Tier 7). Late-career creator-scorer-passer wing whose value comes from elite foul-draw efficiency, primary-handler ball security, and high-IQ secondary playmaking; two-way All-Star athleticism has aged into help-and-IQ defense.

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
ACL — out 2025-26 / mid-2026-27

## Sources
- Full profile: [output/Jimmy_Butler/2026-05-05_profile.md](../../output/Jimmy_Butler/2026-05-05_profile.md)
- Research packets: [raw/Jimmy_Butler/](../../raw/Jimmy_Butler/)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
