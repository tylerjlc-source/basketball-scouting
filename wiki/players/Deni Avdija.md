---
player: Deni Avdija
group: Wing
archetype: Dribble Pass Shoot Wing
composite: 8.24
tier: 7
tier_band: 7.90–8.29
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Deni_Avdija/2026-05-02_profile.md
scored_session: 132
last_updated_session: 132
rubric_version: v3
pot: null
sd01_at_basket_finishing: 7.4
sd02_contact_finishing: 8.7
sd03_post_offense: 5.0
sd04_catch_shoot_3pt: 7.6
sd05_off_dribble_shooting: 5.8
sd06_mid_range: 7.3
sd07_free_throw: 7.8
sd08_handling_creation: 8.0
sd09_touch_feel: 7.3
sd10_ball_security: 5.5
sd11_court_vision: 8.2
sd12_decision_making: 7.2
sd13_passing_execution: 7.3
sd14_off_ball_movement: 7.0
sd15_on_ball_pressure: 7.0
sd16_help_defense: 6.8
sd17_rim_protection: 5.5
sd18_post_defense: 5.5
sd19_offensive_rebounding: 5.7
sd20_defensive_rebounding: 7.8
sd21_burst_explosion: 6.8
sd22_lateral_quickness: 7.0
sd23_strength: 7.5
sd24_shot_selection: 7.3
sd25_effort_motor: 7.7
sd26_competitive_character: 7.5
d1_finishing: 7.0
d2_shooting: 7.1
d3_ball_skills: 6.9
d4_playmaking: 7.4
d5_defense: 6.9
d6_rebounding: 6.8
d7_athleticism: 7.1
d8_iq_motor: 7.5
---

# Deni Avdija

**[[Dribble Pass Shoot Wing]]** Wing — composite **8.24** (Tier 7). 6'8" wing primary ball-handler whose ascending creator profile delivered first All-Star and MIP-finalist credentials in 2025-26.

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
1x All-Star; back recurrence

## Sources
- Full profile: [output/Deni_Avdija/2026-05-02_profile.md](../../output/Deni_Avdija/2026-05-02_profile.md)
- Research packets: [raw/Deni_Avdija/2026-05-02_research-packet.md](../../raw/Deni_Avdija/2026-05-02_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
