---
player: Nikola Vučević
group: Big
archetype: Versatile Scoring Big
composite: 7.78
tier: 8
tier_band: 7.50–7.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Nikola_Vucevic/2026-04-24_profile.md
scored_session: 104
last_updated_session: 104
rubric_version: v3
pot: null
sd01_at_basket_finishing: 6.7
sd02_contact_finishing: 4.8
sd03_post_offense: 7.3
sd04_catch_shoot_3pt: 8.2
sd05_off_dribble_shooting: 4.8
sd06_mid_range: 7.0
sd07_free_throw: 8.3
sd08_handling_creation: 6.3
sd09_touch_feel: 8.3
sd10_ball_security: 7.8
sd11_court_vision: 8.2
sd12_decision_making: 7.5
sd13_passing_execution: 8.0
sd14_off_ball_movement: 7.0
sd15_on_ball_pressure: 4.5
sd16_help_defense: 5.5
sd17_rim_protection: 4.5
sd18_post_defense: 6.0
sd19_offensive_rebounding: 6.0
sd20_defensive_rebounding: 7.7
sd21_burst_explosion: 4.5
sd22_lateral_quickness: 4.5
sd23_strength: 7.3
sd24_shot_selection: 7.5
sd25_effort_motor: 6.5
sd26_competitive_character: 7.0
d1_finishing: 6.3
d2_shooting: 7.1
d3_ball_skills: 7.5
d4_playmaking: 7.7
d5_defense: 5.1
d6_rebounding: 6.9
d7_athleticism: 5.4
d8_iq_motor: 7.0
---

# Nikola Vučević

**[[Versatile Scoring Big]]** Big — composite **7.78** (Tier 8).

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
Added Session 104 — second new VSB anchor (after Sabonis S102), expanding the current-tag VSB pool to 3. **Active non-negotiable cap: #17 Rim protection cap binds composite below Tier 6** (mirrors Sabonis precedent — second consecutive VSB anchor with active C gate cap, suggesting archetype-level pattern). Library Notes: "C #17 cap active". 3x All-Star, traded from Chicago to Boston Feb 2026.

## Sources
- Full profile: [output/Nikola_Vucevic/2026-04-24_profile.md](../../output/Nikola_Vucevic/2026-04-24_profile.md)
- Research packets: [raw/Nikola_Vucevic/](../../raw/Nikola_Vucevic/) (one packet, 2026-04-24)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
