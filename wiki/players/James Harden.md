---
player: James Harden
group: Guard
archetype: Offensive Engine
composite: 8.40
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/James_Harden/2026-05-02_profile.md
scored_session: 137
last_updated_session: 137
rubric_version: v3
pot: 8.40
sd01_at_basket_finishing: 7.4
sd02_contact_finishing: 9.0
sd03_post_offense: 5.5
sd04_catch_shoot_3pt: 9.0
sd05_off_dribble_shooting: 7.8
sd06_mid_range: 7.5
sd07_free_throw: 9.0
sd08_handling_creation: 8.7
sd09_touch_feel: 8.5
sd10_ball_security: 7.0
sd11_court_vision: 9.5
sd12_decision_making: 7.2
sd13_passing_execution: 8.5
sd14_off_ball_movement: 6.0
sd15_on_ball_pressure: 5.0
sd16_help_defense: 5.5
sd17_rim_protection: 5.0
sd18_post_defense: 6.0
sd19_offensive_rebounding: 5.0
sd20_defensive_rebounding: 7.5
sd21_burst_explosion: 5.0
sd22_lateral_quickness: 5.0
sd23_strength: 7.5
sd24_shot_selection: 7.8
sd25_effort_motor: 6.5
sd26_competitive_character: 5.0
d1_finishing: 8.2
d2_shooting: 8.3
d3_ball_skills: 8.1
d4_playmaking: 7.8
d5_defense: 5.3
d6_rebounding: 7.5
d7_athleticism: 5.8
d8_iq_motor: 6.4
---

# James Harden

**[[Offensive Engine]]** Guard — composite **8.40** (Tier 6). Craft-driven lead guard whose elite vision, foul-drawing, and shooting peaks hold an All-Star floor while age-related burst loss and a multi-decade R13 shrink pattern cap the ceiling.

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
1x MVP; All-NBA 3rd 2024-25

## Sources
- Full profile: [output/James_Harden/2026-05-02_profile.md](../../output/James_Harden/2026-05-02_profile.md)
- Research packets: [raw/James_Harden/2026-05-02_research-packet.md](../../raw/James_Harden/2026-05-02_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
