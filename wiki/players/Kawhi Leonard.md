---
player: Kawhi Leonard
group: Wing
archetype: Score-First Wing
composite: 8.90
tier: 4
tier_band: 8.90–9.19
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Kawhi_Leonard/2026-05-01_profile.md
scored_session: 125
last_updated_session: 125
rubric_version: v3
pot: 8.90
sd01_at_basket_finishing: 8.2
sd02_contact_finishing: 7.2
sd03_post_offense: 7.6
sd04_catch_shoot_3pt: 8.7
sd05_off_dribble_shooting: 8.1
sd06_mid_range: 9.1
sd07_free_throw: 9.2
sd08_handling_creation: 8.6
sd09_touch_feel: 8.6
sd10_ball_security: 8.5
sd11_court_vision: 7.2
sd12_decision_making: 7.6
sd13_passing_execution: 7.3
sd14_off_ball_movement: 8.0
sd15_on_ball_pressure: 6.7
sd16_help_defense: 6.7
sd17_rim_protection: 6.0
sd18_post_defense: 7.0
sd19_offensive_rebounding: 6.5
sd20_defensive_rebounding: 7.5
sd21_burst_explosion: 7.0
sd22_lateral_quickness: 7.0
sd23_strength: 8.6
sd24_shot_selection: 8.6
sd25_effort_motor: 7.0
sd26_competitive_character: 8.7
d1_finishing: 7.7
d2_shooting: 8.8
d3_ball_skills: 8.6
d4_playmaking: 7.5
d5_defense: 6.7
d6_rebounding: 7.0
d7_athleticism: 7.5
d8_iq_motor: 8.1
---

# Kawhi Leonard

**[[Score-First Wing]]** Wing — composite **8.90** (Tier 4). Late-prime two-way wing transitioning to scoring-first identity; signature mid-range engine and championship credential weight, with defense recalibrated to functional-not-elite post multi-season knee management.

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
2x FMVP; chronic knee — 2025-26 healthy 65 GP

## Sources
- Full profile: [output/Kawhi_Leonard/2026-05-01_profile.md](../../output/Kawhi_Leonard/2026-05-01_profile.md)
- Research packets: [raw/Kawhi_Leonard/2026-05-01_research-packet.md](../../raw/Kawhi_Leonard/2026-05-01_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
