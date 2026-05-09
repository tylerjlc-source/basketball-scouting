---
player: Mikal Bridges
group: Wing
archetype: 3-and-D Wing
composite: 7.85
tier: 8
tier_band: 7.50–7.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Mikal_Bridges/2026-04-24_profile.md
scored_session: null
last_updated_session: 102
rubric_version: v3
pot: null
sd01_at_basket_finishing: 7.2
sd02_contact_finishing: 5.2
sd03_post_offense: 4.0
sd04_catch_shoot_3pt: 7.7
sd05_off_dribble_shooting: 5.9
sd06_mid_range: 7.4
sd07_free_throw: 8.3
sd08_handling_creation: 6.8
sd09_touch_feel: 7.8
sd10_ball_security: 8.2
sd11_court_vision: 6.8
sd12_decision_making: 7.3
sd13_passing_execution: 7.0
sd14_off_ball_movement: 7.9
sd15_on_ball_pressure: 7.4
sd16_help_defense: 7.3
sd17_rim_protection: 6.3
sd18_post_defense: 6.2
sd19_offensive_rebounding: 4.0
sd20_defensive_rebounding: 6.2
sd21_burst_explosion: 6.8
sd22_lateral_quickness: 7.5
sd23_strength: 6.7
sd24_shot_selection: 6.8
sd25_effort_motor: 7.8
sd26_competitive_character: 6.5
d1_finishing: 6.2
d2_shooting: 7.3
d3_ball_skills: 7.6
d4_playmaking: 7.3
d5_defense: 6.8
d6_rebounding: 6.2
d7_athleticism: 7.0
d8_iq_motor: 7.0
---

# Mikal Bridges

**[[3-and-D Wing]]** Wing — composite **7.85** (Tier 8).

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
Updated Session 102 — was 7.62; re-eval per Tyler S100 knowledge-calibration note ("Bridges > Hauser; 7.62 too low"); **first library re-eval requiring multi-draft upward correction** — initial draft at 7.62 validated existing anchor, subsequent drafts corrected pre-modifier upward after Tyler anchor-library cross-reference feedback (7.62 → 7.75 → 7.85 sequence). Final pre-modifier 7.95 reflects starter-role-volume + contender-team-context + iron-man durability (555+ consecutive games, NBA minutes leader 2024-25) correctly weighted; R13 Stage 2 Moderate Shrink −0.10 applied explicitly (statistical strong shrink career −5.1 TS% delta + qualitative convergent-on-shrink with 2024-25 ECF clutch offset + active recency). **Methodology learning:** anchor-library cross-reference sweep at pre-modifier stage is essential for correct placement of role-volume-defined wings; Hauser-only comparison missed role-volume edge over Tier 8 lower-middle specialist cluster (Pritchard, Caruso, Jones, Claxton).

## Sources
- Full profile: [output/Mikal_Bridges/2026-04-24_profile.md](../../output/Mikal_Bridges/2026-04-24_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
