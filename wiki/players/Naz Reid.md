---
player: Naz Reid
group: Big
archetype: Stretch Big
composite: 7.75
tier: 8
tier_band: 7.50–7.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Naz_Reid/2026-04-24_profile.md
scored_session: 104
last_updated_session: 104
rubric_version: v3
pot: null
sd01_at_basket_finishing: 7.2
sd02_contact_finishing: 5.2
sd03_post_offense: 6.5
sd04_catch_shoot_3pt: 8.1
sd05_off_dribble_shooting: 6.5
sd06_mid_range: 5.5
sd07_free_throw: 7.4
sd08_handling_creation: 6.7
sd09_touch_feel: 7.1
sd10_ball_security: 6.5
sd11_court_vision: 6.8
sd12_decision_making: 6.7
sd13_passing_execution: 6.8
sd14_off_ball_movement: 6.2
sd15_on_ball_pressure: 6.5
sd16_help_defense: 6.3
sd17_rim_protection: 6.2
sd18_post_defense: 5.8
sd19_offensive_rebounding: 5.3
sd20_defensive_rebounding: 6.5
sd21_burst_explosion: 6.8
sd22_lateral_quickness: 6.5
sd23_strength: 7.0
sd24_shot_selection: 6.8
sd25_effort_motor: 6.7
sd26_competitive_character: 7.0
d1_finishing: 6.2
d2_shooting: 6.9
d3_ball_skills: 6.8
d4_playmaking: 6.6
d5_defense: 6.2
d6_rebounding: 5.9
d7_athleticism: 6.8
d8_iq_motor: 6.8
---

# Naz Reid

**[[Stretch Big]]** Big — composite **7.75** (Tier 8).

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
Updated Session 104 — was 7.65 (legacy anchor, no prior notes). Library Notes column updated to "6MOTY 2023-24" credential. R13 Stage 2 Directional Rise +0.05 applied (career matched +1.0 TS% delta at strong-rise boundary; qualitative mixed-positive; double-count guard zeroed Stage 1 POT). Library revision per Davion Mitchell precedent (update in place). First batch 3 Big re-eval alongside Vučević.

## Sources
- Full profile: [output/Naz_Reid/2026-04-24_profile.md](../../output/Naz_Reid/2026-04-24_profile.md)
- Research packets: [raw/Naz_Reid/](../../raw/Naz_Reid/) (one packet, 2026-04-24)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
