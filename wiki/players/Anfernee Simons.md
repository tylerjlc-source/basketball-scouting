---
player: Anfernee Simons
group: Guard
archetype: Microwave Scorer
composite: 7.58
tier: 8
tier_band: 7.50–7.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Anfernee_Simons/2026-04-20_profile.md
scored_session: 95
last_updated_session: 95
rubric_version: v3
pot: 7.65
sd01_at_basket_finishing: 6.8
sd02_contact_finishing: 4.5
sd03_post_offense: 2.0
sd04_catch_shoot_3pt: 8.6
sd05_off_dribble_shooting: 7.6
sd06_mid_range: 6.6
sd07_free_throw: 9.0
sd08_handling_creation: 7.4
sd09_touch_feel: 7.8
sd10_ball_security: 7.5
sd11_court_vision: 6.6
sd12_decision_making: 6.0
sd13_passing_execution: 6.8
sd14_off_ball_movement: 5.8
sd15_on_ball_pressure: 4.5
sd16_help_defense: 4.6
sd17_rim_protection: 2.0
sd18_post_defense: 3.0
sd19_offensive_rebounding: 4.0
sd20_defensive_rebounding: 5.2
sd21_burst_explosion: 7.8
sd22_lateral_quickness: 5.8
sd23_strength: 5.2
sd24_shot_selection: 5.8
sd25_effort_motor: 5.5
sd26_competitive_character: 6.5
d1_finishing: 4.4
d2_shooting: 8.0
d3_ball_skills: 7.6
d4_playmaking: 6.3
d5_defense: 4.6
d6_rebounding: 4.6
d7_athleticism: 6.3
d8_iq_motor: 5.9
---

# Anfernee Simons

**[[Microwave Scorer]]** Guard — composite **7.58** (Tier 8).

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
Added Session 95 — first 5-skill chain profile (S94 eval). The first anchor produced end-to-end via the 5-skill chain.

## Sources
- Full profile: [output/Anfernee_Simons/2026-04-20_profile.md](../../output/Anfernee_Simons/2026-04-20_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
