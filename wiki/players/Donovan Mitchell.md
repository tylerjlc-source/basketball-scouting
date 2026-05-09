---
player: Donovan Mitchell
group: Guard
archetype: Offensive Engine
composite: 8.95
tier: 4
tier_band: 8.90–9.19
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Donovan_Mitchell/2026-04-23_profile.md
scored_session:
last_updated_session: 99
rubric_version: v3
pot: 9.02
sd01_at_basket_finishing: 8
sd02_contact_finishing: 7.8
sd03_post_offense: 3
sd04_catch_shoot_3pt: 8.8
sd05_off_dribble_shooting: 8.3
sd06_mid_range: 8
sd07_free_throw: 8.3
sd08_handling_creation: 8.5
sd09_touch_feel: 8.3
sd10_ball_security: 7.5
sd11_court_vision: 7.8
sd12_decision_making: 8
sd13_passing_execution: 7.5
sd14_off_ball_movement: 7.8
sd15_on_ball_pressure: 7
sd16_help_defense: 6.8
sd17_rim_protection: 3.5
sd18_post_defense: 4.5
sd19_offensive_rebounding: 4
sd20_defensive_rebounding: 6.8
sd21_burst_explosion: 8.3
sd22_lateral_quickness: 7.5
sd23_strength: 8
sd24_shot_selection: 8
sd25_effort_motor: 8.2
sd26_competitive_character: 8.3
d1_finishing: 7.9
d2_shooting: 8.4
d3_ball_skills: 8.1
d4_playmaking: 7.8
d5_defense: 6.9
d6_rebounding: 6.8
d7_athleticism: 7.9
d8_iq_motor: 8.2
---

# Donovan Mitchell

**[[Offensive Engine]]** Guard — composite **8.92** (Tier 4).

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
Updated Session 99 — was 8.86 Tier 5; drift correction post-2024-25 All-NBA First Team (first career selection), 7x consecutive All-Star (through 2025-26), franchise anchor for best-record East team 2024-25. Crossed Tier 5 → Tier 4 (All-NBA caliber). R13 Stage 2 did NOT fire — TS% delta −1.1 neutral, PPG delta +3.3 rise, qualitative "prolific scorer, team doesn't break past 2nd round" mixed rather than defining. S99-F01 (S99 Stage 2) — stats mixed, qualitative no-Finals.

## Sources
- Full profile: [output/Donovan_Mitchell/2026-04-23_profile.md](../../output/Donovan_Mitchell/2026-04-23_profile.md)
- Research packets: none (evaluated pre-raw/ persistence)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
