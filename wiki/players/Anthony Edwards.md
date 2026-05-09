---
player: Anthony Edwards
group: Wing
archetype: All-Around Wing
composite: 9.11
tier: 4
tier_band: 8.90–9.19
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Anthony_Edwards/2026-04-27_profile.md
scored_session: 111
last_updated_session: 111
rubric_version: v3
pot: 9.05
sd01_at_basket_finishing: 8.4
sd02_contact_finishing: 8.1
sd03_post_offense: 5
sd04_catch_shoot_3pt: 9.3
sd05_off_dribble_shooting: 8.1
sd06_mid_range: 7.5
sd07_free_throw: 8.2
sd08_handling_creation: 8.5
sd09_touch_feel: 7.4
sd10_ball_security: 7
sd11_court_vision: 7.5
sd12_decision_making: 7.3
sd13_passing_execution: 7.2
sd14_off_ball_movement: 7.3
sd15_on_ball_pressure: 7
sd16_help_defense: 6
sd17_rim_protection: 5.5
sd18_post_defense: 6
sd19_offensive_rebounding: 5.5
sd20_defensive_rebounding: 7
sd21_burst_explosion: 9.4
sd22_lateral_quickness: 7.5
sd23_strength: 8.2
sd24_shot_selection: 7.8
sd25_effort_motor: 6.5
sd26_competitive_character: 7.7
d1_finishing: 7.2
d2_shooting: 8.3
d3_ball_skills: 7.6
d4_playmaking: 7.3
d5_defense: 6.1
d6_rebounding: 6.3
d7_athleticism: 8.4
d8_iq_motor: 7.3
---

# Anthony Edwards

**[[All-Around Wing]]** Wing — composite **8.93** (Tier 4). Primary-engine two-way wing on Minnesota — All-NBA-Second-caliber scorer at 30.8% USG with elite physical profile and a defensive ceiling capped by effort variance.

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
Knee — out multiple weeks 4/2026.

Session 111: revised to 8.93 from prior 9.37. Tier crossing 3→4. Group migration Guard→Wing. Archetype migration Offensive Engine→All-Around Wing. Expedited-route legacy anchor drift correction (project_s99_anchor_library_recalibration). Initial Skill 4 draft 8.70 corrected to 8.93 on Tyler review (anchor-deflation pattern: Tatum 8.88 post-Achilles deflation pulled comparison set down; multi-ANBA-Second compounding restored Tier 4 entry). R13 Stage 2 not fired (convergence gate fails — statistical NEUTRAL, qualitative MIXED). Knee bone bruise + hyperextension Game 4 vs DEN 2026-04-25 — post-window event, no composite effect.

## Sources
- Full profile: [output/Anthony_Edwards/2026-04-27_profile.md](../../output/Anthony_Edwards/2026-04-27_profile.md)
- Research packets: [raw/Anthony_Edwards/2026-04-27_research-packet.md](../../raw/Anthony_Edwards/2026-04-27_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
