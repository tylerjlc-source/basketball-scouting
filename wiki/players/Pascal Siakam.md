---
player: Pascal Siakam
group: Wing
archetype: Modern Four
composite: 8.70
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Pascal_Siakam/2026-04-23_profile.md
scored_session: null
last_updated_session: 99
rubric_version: v3
pot: 8.85
sd01_at_basket_finishing: 8.5
sd02_contact_finishing: 7.3
sd03_post_offense: 7.0
sd04_catch_shoot_3pt: 7.5
sd05_off_dribble_shooting: 7.3
sd06_mid_range: 6.3
sd07_free_throw: 6.0
sd08_handling_creation: 7.5
sd09_touch_feel: 8.0
sd10_ball_security: 7.3
sd11_court_vision: 6.5
sd12_decision_making: 7.5
sd13_passing_execution: 7.3
sd14_off_ball_movement: 7.0
sd15_on_ball_pressure: 7.0
sd16_help_defense: 6.8
sd17_rim_protection: 5.0
sd18_post_defense: 6.5
sd19_offensive_rebounding: 7.5
sd20_defensive_rebounding: 7.8
sd21_burst_explosion: 7.8
sd22_lateral_quickness: 7.0
sd23_strength: 8.0
sd24_shot_selection: 7.3
sd25_effort_motor: 8.2
sd26_competitive_character: 8.5
d1_finishing: 7.6
d2_shooting: 6.8
d3_ball_skills: 7.6
d4_playmaking: 7.1
d5_defense: 6.3
d6_rebounding: 7.7
d7_athleticism: 7.6
d8_iq_motor: 8.0
---

# Pascal Siakam

**[[Modern Four]]** Wing — composite **8.70** (Tier 5).

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
Updated Session 99 — was 8.66; small upward drift per sustained 2x All-Star cadence (2024-25 + 2025-26) and 2024-25 ECF co-star run absorbed into current composite, partially offset by defensive regression (DFGPOE +0.2% — neutral) and 2025-26 bad-team context post-Haliburton injury. R13 Stage 2 did NOT fire — career matched TS% delta −2.6 labeled "Neutral" by script, diverging from qualitative multi-run rise. Confirmation more than correction.

## Sources
- Full profile: [output/Pascal_Siakam/2026-04-23_profile.md](../../output/Pascal_Siakam/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
