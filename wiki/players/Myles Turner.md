---
player: Myles Turner
group: Big
archetype: Stretch Big
composite: 7.88
tier: 8
tier_band: 7.50–7.89
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Myles_Turner/2026-04-25_profile.md
scored_session: 107
last_updated_session: 107
rubric_version: v3
pot: null
sd01_at_basket_finishing: 6.8
sd02_contact_finishing: 5.5
sd03_post_offense: 5.5
sd04_catch_shoot_3pt: 8.5
sd05_off_dribble_shooting: 5.5
sd06_mid_range: 7.0
sd07_free_throw: 7.5
sd08_handling_creation: 6.0
sd09_touch_feel: 7.0
sd10_ball_security: 7.0
sd11_court_vision: 6.0
sd12_decision_making: 6.5
sd13_passing_execution: 6.0
sd14_off_ball_movement: 7.5
sd15_on_ball_pressure: 6.0
sd16_help_defense: 7.5
sd17_rim_protection: 8.0
sd18_post_defense: 8.0
sd19_offensive_rebounding: 5.5
sd20_defensive_rebounding: 5.5
sd21_burst_explosion: 5.5
sd22_lateral_quickness: 5.0
sd23_strength: 6.0
sd24_shot_selection: 7.5
sd25_effort_motor: 7.0
sd26_competitive_character: 7.0
d1_finishing: 6.2
d2_shooting: 7.1
d3_ball_skills: 6.7
d4_playmaking: 6.5
d5_defense: 7.4
d6_rebounding: 5.5
d7_athleticism: 5.5
d8_iq_motor: 7.2
---

# Myles Turner

**[[Stretch Big]]** Big — composite **7.88** (Tier 8).

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
Added Session 107 — first added Stretch Big anchor since initial library construction. Library Notes: "2x BPG league leader". Validates the ARCHETYPE-WEIGHTS-BIGS.md flag: "A prospect with elite shot-blocking AND legitimate floor spacing belongs in Stretch Big, not Rim Protector — Myles Turner is the reference case." Anchor count: 104.

## Sources
- Full profile: [output/Myles_Turner/2026-04-25_profile.md](../../output/Myles_Turner/2026-04-25_profile.md)
- Research packets: [raw/Myles_Turner/](../../raw/Myles_Turner/) (one packet, 2026-04-25)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
