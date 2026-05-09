---
player: Bam Adebayo
group: Big
archetype: All-Around Big
composite: 8.80
tier: 5
tier_band: 8.60–8.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Bam_Adebayo/2026-05-01_profile.md
scored_session: 127
last_updated_session: 127
rubric_version: v3
pot: 8.90
sd01_at_basket_finishing: 7.8
sd02_contact_finishing: 8.1
sd03_post_offense: 7.1
sd04_catch_shoot_3pt: 6.6
sd05_off_dribble_shooting: 6.1
sd06_mid_range: 7.2
sd07_free_throw: 8.2
sd08_handling_creation: 7.8
sd09_touch_feel: 7.7
sd10_ball_security: 7.7
sd11_court_vision: 8.2
sd12_decision_making: 7.6
sd13_passing_execution: 8.1
sd14_off_ball_movement: 6.7
sd15_on_ball_pressure: 9.1
sd16_help_defense: 8.3
sd17_rim_protection: 4.9
sd18_post_defense: 7.2
sd19_offensive_rebounding: 6.2
sd20_defensive_rebounding: 7.4
sd21_burst_explosion: 8.3
sd22_lateral_quickness: 9.2
sd23_strength: 8.1
sd24_shot_selection: 7.2
sd25_effort_motor: 8.1
sd26_competitive_character: 8.1
d1_finishing: 7.7
d2_shooting: 7.0
d3_ball_skills: 7.7
d4_playmaking: 7.7
d5_defense: 7.4
d6_rebounding: 6.8
d7_athleticism: 8.5
d8_iq_motor: 7.8
---

# Bam Adebayo

**[[All-Around Big]]** Big — composite **8.80** (Tier 5). Premier passing-hub center with the league's most credible 1-through-5 switch defense and a structural rim-protection deficit that fires the C non-negotiable cap.

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
C #17 cap active

## Sources
- Full profile: [output/Bam_Adebayo/2026-05-01_profile.md](../../output/Bam_Adebayo/2026-05-01_profile.md)
- Research packets: [raw/Bam_Adebayo/](../../raw/Bam_Adebayo/)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
