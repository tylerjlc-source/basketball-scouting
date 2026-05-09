---
player: De'Aaron Fox
group: Guard
archetype: Offensive Engine
composite: 8.47
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/De_Aaron_Fox/2026-05-02_profile.md
scored_session: 135
last_updated_session: 135
rubric_version: v3
pot: 8.58
sd01_at_basket_finishing: 8.2
sd02_contact_finishing: 7.2
sd03_post_offense: 2.5
sd04_catch_shoot_3pt: 7.6
sd05_off_dribble_shooting: 6.7
sd06_mid_range: 7.2
sd07_free_throw: 7.7
sd08_handling_creation: 8.0
sd09_touch_feel: 7.8
sd10_ball_security: 7.2
sd11_court_vision: 7.5
sd12_decision_making: 7.3
sd13_passing_execution: 7.4
sd14_off_ball_movement: 7.6
sd15_on_ball_pressure: 6.3
sd16_help_defense: 6.0
sd17_rim_protection: 4.5
sd18_post_defense: 4.5
sd19_offensive_rebounding: 5.0
sd20_defensive_rebounding: 7.0
sd21_burst_explosion: 9.2
sd22_lateral_quickness: 8.0
sd23_strength: 5.5
sd24_shot_selection: 7.2
sd25_effort_motor: 6.5
sd26_competitive_character: 7.8
d1_finishing: 7.7
d2_shooting: 7.3
d3_ball_skills: 7.7
d4_playmaking: 7.5
d5_defense: 6.2
d6_rebounding: 7.0
d7_athleticism: 7.6
d8_iq_motor: 7.2
---

# De'Aaron Fox

**[[Offensive Engine]]** Guard — composite **8.47** (Tier 6). Burst-defined PnR creator with restructured Spurs role; mid-prime All-Star without All-NBA reach.

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
2x All-Star; 2022-23 Clutch POY

## Sources
- Full profile: [output/De_Aaron_Fox/2026-05-02_profile.md](../../output/De_Aaron_Fox/2026-05-02_profile.md)
- Research packets: [raw/De_Aaron_Fox/2026-05-02_research-packet.md](../../raw/De_Aaron_Fox/2026-05-02_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
