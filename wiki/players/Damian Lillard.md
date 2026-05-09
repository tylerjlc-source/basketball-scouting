---
player: Damian Lillard
group: Guard
archetype: Offensive Engine
composite: 8.55
tier: 6
tier_band: 8.30–8.59
status: Active — Achilles dormant
competition_level: NBA
has_profile: true
profile_path: output/Damian_Lillard/2026-05-05_profile.md
scored_session: 151
last_updated_session: 151
rubric_version: v3
pot: 8.55
sd01_at_basket_finishing: 8.1
sd02_contact_finishing: 8.2
sd03_post_offense: 2.5
sd04_catch_shoot_3pt: 8.2
sd05_off_dribble_shooting: 9.4
sd06_mid_range: 8.1
sd07_free_throw: 9.6
sd08_handling_creation: 8.6
sd09_touch_feel: 8.5
sd10_ball_security: 7.7
sd11_court_vision: 8.1
sd12_decision_making: 7.8
sd13_passing_execution: 7.8
sd14_off_ball_movement: 7.1
sd15_on_ball_pressure: 5.2
sd16_help_defense: 5.2
sd17_rim_protection: 1.5
sd18_post_defense: 2.5
sd19_offensive_rebounding: 5.1
sd20_defensive_rebounding: 7.6
sd21_burst_explosion: 7.6
sd22_lateral_quickness: 6.6
sd23_strength: 7.1
sd24_shot_selection: 7.2
sd25_effort_motor: 5.7
sd26_competitive_character: 8.7
d1_finishing: 8.2
d2_shooting: 8.8
d3_ball_skills: 8.3
d4_playmaking: 7.7
d5_defense: 5.2
d6_rebounding: 7.6
d7_athleticism: 7.1
d8_iq_motor: 7.2
---

# Damian Lillard

**[[Offensive Engine]]** Guard — composite **8.55** (Tier 6). Off-dribble shooting and Dame Time clutch identity carry the profile; defensive liability and active-injury dormancy (Achilles 4/2025, age-36 return target) compress from prime-era All-NBA tier to high Tier 6.

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

Achilles 4/2025 — out 2025-26; age-36 return

## Sources

- Full profile: [output/Damian_Lillard/2026-05-05_profile.md](../../output/Damian_Lillard/2026-05-05_profile.md)
- Research packet: [raw/Damian_Lillard/2026-05-05_research-packet.md](../../raw/Damian_Lillard/2026-05-05_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
