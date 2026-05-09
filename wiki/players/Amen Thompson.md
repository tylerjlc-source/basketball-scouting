---
player: Amen Thompson
group: Wing
archetype: Defensive Specialist
composite: 8.20
tier: 7
tier_band: 7.90–8.29
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Amen_Thompson/2026-04-23_profile.md
scored_session: null
last_updated_session: 99
rubric_version: v3
pot: 8.50
sd01_at_basket_finishing: 8.8
sd02_contact_finishing: 7.5
sd03_post_offense: 4.5
sd04_catch_shoot_3pt: 4.5
sd05_off_dribble_shooting: 3.5
sd06_mid_range: 4.5
sd07_free_throw: 7.0
sd08_handling_creation: 7.0
sd09_touch_feel: 7.0
sd10_ball_security: 7.3
sd11_court_vision: 7.3
sd12_decision_making: 7.5
sd13_passing_execution: 7.3
sd14_off_ball_movement: 8.0
sd15_on_ball_pressure: 8.8
sd16_help_defense: 8.3
sd17_rim_protection: 4.5
sd18_post_defense: 7.0
sd19_offensive_rebounding: 8.3
sd20_defensive_rebounding: 7.8
sd21_burst_explosion: 9.0
sd22_lateral_quickness: 8.3
sd23_strength: 8.0
sd24_shot_selection: 6.5
sd25_effort_motor: 8.8
sd26_competitive_character: 8.0
d1_finishing: 8.2
d2_shooting: 4.9
d3_ball_skills: 7.1
d4_playmaking: 7.5
d5_defense: 7.2
d6_rebounding: 8.1
d7_athleticism: 8.4
d8_iq_motor: 7.8
---

# Amen Thompson

**[[Defensive Specialist (Wing)]]** Wing — composite **8.20** (Tier 7).

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
Updated Session 99 — was 8.00 Dribble Pass Shoot Wing; archetype migration. Primary corrections: (1) archetype migration — prior tag required shooting he doesn't have (CAS 3PT 25.6%, pull-up 3PT 12.0%); (2) 2024-25 All-Defensive First Team credential (74/100 first-place votes). R13 Stage 2 did NOT fire — career TS% delta −6.2 strong shrink, qualitative undetermined (limited playoff sample). Tyler-approved upper Tier 7 placement with ceiling discipline per Draymond/Barnes shooting-limited archetypal ceiling. S99 recalibration sweep complete — 6 anchors revised.

## Sources
- Full profile: [output/Amen_Thompson/2026-04-23_profile.md](../../output/Amen_Thompson/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
