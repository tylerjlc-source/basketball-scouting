---
player: Devin Booker
group: Guard
archetype: All-Around Guard
composite: 8.94
tier: 4
tier_band: 8.90–9.19
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Devin_Booker/2026-05-01_profile.md
scored_session: 126
last_updated_session: 126
rubric_version: v3
pot: 8.94
sd01_at_basket_finishing: 7.9
sd02_contact_finishing: 8
sd03_post_offense: 6.5
sd04_catch_shoot_3pt: 7.7
sd05_off_dribble_shooting: 8
sd06_mid_range: 9
sd07_free_throw: 9.1
sd08_handling_creation: 8.4
sd09_touch_feel: 8.7
sd10_ball_security: 7.5
sd11_court_vision: 7.5
sd12_decision_making: 7.4
sd13_passing_execution: 7.8
sd14_off_ball_movement: 7.5
sd15_on_ball_pressure: 6
sd16_help_defense: 5.5
sd17_rim_protection: 3
sd18_post_defense: 5.5
sd19_offensive_rebounding: 5
sd20_defensive_rebounding: 6
sd21_burst_explosion: 6
sd22_lateral_quickness: 6
sd23_strength: 7
sd24_shot_selection: 7.5
sd25_effort_motor: 7.5
sd26_competitive_character: 7
d1_finishing: 8
d2_shooting: 8.5
d3_ball_skills: 8.2
d4_playmaking: 7.6
d5_defense: 5.8
d6_rebounding: 6
d7_athleticism: 6.3
d8_iq_motor: 7.3
---

# Devin Booker

**[[All-Around Guard]]** Guard — composite **8.92** (Tier 4). Mid-range mastery anchors a distributed offensive profile; below-average defense is the role limit, not the identity.

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

- Full profile: [output/Devin_Booker/2026-05-01_profile.md](../../output/Devin_Booker/2026-05-01_profile.md)
- Research packets: [raw/Devin_Booker/2026-05-01_research-packet.md](../../raw/Devin_Booker/2026-05-01_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
