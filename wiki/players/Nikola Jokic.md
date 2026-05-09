---
player: Nikola Jokic
group: Big
archetype: All-Around Big
composite: 9.64
tier: 2
tier_band: 9.50–9.79
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Nikola_Jokic/2026-04-30_profile.md
scored_session: 122
last_updated_session: 122
rubric_version: v3
pot: 9.64
sd01_at_basket_finishing: 9.1
sd02_contact_finishing: 7.6
sd03_post_offense: 9.5
sd04_catch_shoot_3pt: 9.1
sd05_off_dribble_shooting: 8.6
sd06_mid_range: 9.6
sd07_free_throw: 8.7
sd08_handling_creation: 9.5
sd09_touch_feel: 9.6
sd10_ball_security: 9.0
sd11_court_vision: 10.0
sd12_decision_making: 9.5
sd13_passing_execution: 9.7
sd14_off_ball_movement: 9.7
sd15_on_ball_pressure: 5.5
sd16_help_defense: 9.5
sd17_rim_protection: 6.0
sd18_post_defense: 6.5
sd19_offensive_rebounding: 7.6
sd20_defensive_rebounding: 9.5
sd21_burst_explosion: 4.0
sd22_lateral_quickness: 5.5
sd23_strength: 7.0
sd24_shot_selection: 9.6
sd25_effort_motor: 8.4
sd26_competitive_character: 9.0
d1_finishing: 8.7
d2_shooting: 9.0
d3_ball_skills: 9.4
d4_playmaking: 9.7
d5_defense: 6.9
d6_rebounding: 8.6
d7_athleticism: 5.5
d8_iq_motor: 9.0
---

# Nikola Jokic

**[[All-Around Big]]** Big — composite **9.64** (Tier 2). Canonical All-Around Big anchor; passing-genius vet at peak — 3× MVP front-running for a 4th in 2025-26 with league-leading 50.4% assist rate and FG% 13.9 above expected; vertical floor (17" P3 lowest of 1,000+ tested) inverts the typical big athletic profile, with skill, IQ, and positioning carrying the body.

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
3x MVP, 2023 FMVP

## Sources
- Full profile: [output/Nikola_Jokic/2026-04-30_profile.md](../../output/Nikola_Jokic/2026-04-30_profile.md)
- Research packets: [raw/Nikola_Jokic/2026-04-30_research-packet.md](../../raw/Nikola_Jokic/2026-04-30_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
