---
player: Paolo Banchero
group: Wing
archetype: Modern Four
composite: 8.38
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Paolo_Banchero/2026-05-02_profile.md
scored_session: 139
last_updated_session: 153
rubric_version: v3
pot: 8.53
sd01_at_basket_finishing: 7.8
sd02_contact_finishing: 8.4
sd03_post_offense: 6.5
sd04_catch_shoot_3pt: 7.2
sd05_off_dribble_shooting: 5.5
sd06_mid_range: 5.5
sd07_free_throw: 7.5
sd08_handling_creation: 7.4
sd09_touch_feel: 7.1
sd10_ball_security: 5.7
sd11_court_vision: 8.0
sd12_decision_making: 6.3
sd13_passing_execution: 7.1
sd14_off_ball_movement: 6.2
sd15_on_ball_pressure: 5.8
sd16_help_defense: 6.0
sd17_rim_protection: 5.5
sd18_post_defense: 6.5
sd19_offensive_rebounding: 6.7
sd20_defensive_rebounding: 8.0
sd21_burst_explosion: 6.2
sd22_lateral_quickness: 5.8
sd23_strength: 8.5
sd24_shot_selection: 5.5
sd25_effort_motor: 6.4
sd26_competitive_character: 7.3
d1_finishing: 7.6
d2_shooting: 6.4
d3_ball_skills: 6.7
d4_playmaking: 6.9
d5_defense: 6.0
d6_rebounding: 7.4
d7_athleticism: 6.8
d8_iq_motor: 6.4
---

# Paolo Banchero

**[[Modern Four]]** Wing — composite **8.38** (Tier 6). 6'10" 250-lb downhill-force forward whose scheme-account contact-finishing, NBA-leading kickout playmaking, primary-rebounder DREB, and elite physical strength anchor a 4-strength upper-band Modern Four profile; capped below Tier 4 by no peak skill, no athletic edge, and no elite defensive trait.

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
2x All-Star; prior 8.28 (calibration correction 2026-05-06 — top-30 launch-cohort audit re-anchored sub-domains #1, #2, #8, #11, #20, #23, #26 against Tier 6 cluster context; new NBA POB methodology applied, POT 8.70 → 8.53)

## Sources
- Full profile: [output/Paolo_Banchero/2026-05-02_profile.md](../../output/Paolo_Banchero/2026-05-02_profile.md)
- Research packets: [raw/Paolo_Banchero/2026-05-02_research-packet.md](../../raw/Paolo_Banchero/2026-05-02_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
