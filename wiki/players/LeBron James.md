---
player: LeBron James
group: Wing
archetype: All-Around Wing
composite: 8.91
tier: 4
tier_band: 8.90–9.19
status: Active
competition_level: NBA
has_profile: true
profile_path: output/LeBron_James/2026-04-30_profile.md
scored_session: 121
last_updated_session: 121
rubric_version: v3
pot: 8.91
sd01_at_basket_finishing: 9.1
sd02_contact_finishing: 7.8
sd03_post_offense: 7.5
sd04_catch_shoot_3pt: 7
sd05_off_dribble_shooting: 6.5
sd06_mid_range: 7
sd07_free_throw: 7
sd08_handling_creation: 8
sd09_touch_feel: 8.5
sd10_ball_security: 7.5
sd11_court_vision: 9.5
sd12_decision_making: 9
sd13_passing_execution: 9
sd14_off_ball_movement: 7.5
sd15_on_ball_pressure: 6
sd16_help_defense: 7.5
sd17_rim_protection: 6.5
sd18_post_defense: 7
sd19_offensive_rebounding: 5.5
sd20_defensive_rebounding: 8
sd21_burst_explosion: 7
sd22_lateral_quickness: 6
sd23_strength: 9
sd24_shot_selection: 8.5
sd25_effort_motor: 6.8
sd26_competitive_character: 9.5
d1_finishing: 8.1
d2_shooting: 6.9
d3_ball_skills: 8
d4_playmaking: 8.8
d5_defense: 6.8
d6_rebounding: 6.8
d7_athleticism: 7.3
d8_iq_motor: 8.3
---

# LeBron James

**[[All-Around Wing]]** Wing — composite **8.95** (Tier 4). Year-23 elder statesman accepting tertiary role on Doncic Lakers; elite playmaking + competitive resume hold while shooting + lateral athleticism decline at age 41.

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
4x FMVP; R13 active 4/2026

## Sources
- Full profile: [output/LeBron_James/2026-04-30_profile.md](../../output/LeBron_James/2026-04-30_profile.md)
- Research packets: [raw/LeBron_James/2026-04-30_research-packet.md](../../raw/LeBron_James/2026-04-30_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
