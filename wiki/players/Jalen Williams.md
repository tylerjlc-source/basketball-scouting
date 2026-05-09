---
player: Jalen Williams
group: Guard
archetype: All-Around Guard
composite: 8.72
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Jalen_Williams/2026-04-23_profile.md
scored_session: null
last_updated_session: 99
rubric_version: v3
pot: 9.05
sd01_at_basket_finishing: 8.3
sd02_contact_finishing: 7.5
sd03_post_offense: 3.0
sd04_catch_shoot_3pt: 7.7
sd05_off_dribble_shooting: 7.0
sd06_mid_range: 7.5
sd07_free_throw: 7.5
sd08_handling_creation: 8.0
sd09_touch_feel: 7.8
sd10_ball_security: 8.2
sd11_court_vision: 7.3
sd12_decision_making: 8.2
sd13_passing_execution: 7.5
sd14_off_ball_movement: 7.5
sd15_on_ball_pressure: 8.5
sd16_help_defense: 8.0
sd17_rim_protection: 4.0
sd18_post_defense: 5.0
sd19_offensive_rebounding: 5.5
sd20_defensive_rebounding: 7.8
sd21_burst_explosion: 7.8
sd22_lateral_quickness: 8.0
sd23_strength: 7.5
sd24_shot_selection: 7.5
sd25_effort_motor: 8.3
sd26_competitive_character: 8.7
d1_finishing: 7.9
d2_shooting: 7.4
d3_ball_skills: 8.0
d4_playmaking: 7.6
d5_defense: 8.3
d6_rebounding: 7.8
d7_athleticism: 7.8
d8_iq_motor: 8.2
---

# Jalen Williams

**[[All-Around Guard]]** Guard — composite **8.72** (Tier 5).

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
Updated Session 99 — was 8.29 Offensive Engine; drift correction post-2024-25 All-NBA 3rd + All-D 2nd + NBA champion + Finals Game 5 hero credential stack pulls to Tier 5 upper-middle. Archetype migration Offensive Engine → All-Around Guard. First S99 anchor recalibration re-score; full 5-skill chain run with new DOMAIN-SCORE-ROLE-RELEVANCE.md applied.

## Sources
- Full profile: [output/Jalen_Williams/2026-04-23_profile.md](../../output/Jalen_Williams/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
