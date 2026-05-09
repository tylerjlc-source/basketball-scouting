---
player: Karl-Anthony Towns
group: Big
archetype: Stretch Big
composite: 8.42
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Karl-Anthony_Towns/2026-05-02_profile.md
scored_session: 134
last_updated_session: 134
rubric_version: v3
pot: 8.54
sd01_at_basket_finishing: 7.5
sd02_contact_finishing: 7.4
sd03_post_offense: 7.7
sd04_catch_shoot_3pt: 9.0
sd05_off_dribble_shooting: 7.0
sd06_mid_range: 6.0
sd07_free_throw: 9.2
sd08_handling_creation: 7.5
sd09_touch_feel: 8.0
sd10_ball_security: 6.7
sd11_court_vision: 7.4
sd12_decision_making: 7.0
sd13_passing_execution: 7.5
sd14_off_ball_movement: 7.7
sd15_on_ball_pressure: 5.5
sd16_help_defense: 6.0
sd17_rim_protection: 5.0
sd18_post_defense: 5.7
sd19_offensive_rebounding: 7.6
sd20_defensive_rebounding: 8.5
sd21_burst_explosion: 7.0
sd22_lateral_quickness: 5.0
sd23_strength: 8.5
sd24_shot_selection: 7.0
sd25_effort_motor: 6.5
sd26_competitive_character: 6.5
d1_finishing: 7.5
d2_shooting: 7.8
d3_ball_skills: 7.4
d4_playmaking: 7.4
d5_defense: 5.6
d6_rebounding: 8.1
d7_athleticism: 6.8
d8_iq_motor: 6.7
---

# Karl-Anthony Towns

**[[Stretch Big]]** Big — composite **8.42** (Tier 6). Unicorn-shooting Center whose CAS 3PT (9.0) and FT (9.2) define the archetype, with elite defensive rebounding and real post game balanced against a four-sub-domain defensive band that caps the ceiling.

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
No update history recorded.

## Sources
- Full profile: [output/Karl-Anthony_Towns/2026-05-02_profile.md](../../output/Karl-Anthony_Towns/2026-05-02_profile.md)
- Research packets: [raw/Karl-Anthony_Towns/2026-05-02_research-packet.md](../../raw/Karl-Anthony_Towns/2026-05-02_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
