---
player: Victor Wembanyama
group: Big
archetype: All-Around Big
composite: 9.34
tier: 3
tier_band: 9.20–9.49
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Victor_Wembanyama/2026-04-28_profile.md
scored_session: 113
last_updated_session: 118
rubric_version: v3
pot: 9.78
sd01_at_basket_finishing: 7.9
sd02_contact_finishing: 7.7
sd03_post_offense: 6.5
sd04_catch_shoot_3pt: 7.6
sd05_off_dribble_shooting: 6.5
sd06_mid_range: 7.5
sd07_free_throw: 8.7
sd08_handling_creation: 8.0
sd09_touch_feel: 8.0
sd10_ball_security: 7.2
sd11_court_vision: 8.5
sd12_decision_making: 8.0
sd13_passing_execution: 7.8
sd14_off_ball_movement: 7.5
sd15_on_ball_pressure: 7.5
sd16_help_defense: 9.5
sd17_rim_protection: 9.6
sd18_post_defense: 7.0
sd19_offensive_rebounding: 6.5
sd20_defensive_rebounding: 7.5
sd21_burst_explosion: 9.5
sd22_lateral_quickness: 7.8
sd23_strength: 6.0
sd24_shot_selection: 7.5
sd25_effort_motor: 9.0
sd26_competitive_character: 8.5
d1_finishing: 7.4
d2_shooting: 7.6
d3_ball_skills: 7.7
d4_playmaking: 8.0
d5_defense: 8.4
d6_rebounding: 7.0
d7_athleticism: 7.8
d8_iq_motor: 8.3
---

# Victor Wembanyama

**[[All-Around Big]]** Big — composite **9.34** (Tier 3). 7'5" one-of-one body anchoring the league's largest defensive on/off swing; unanimous DPOY 2026 + MVP finalist; Year-3 ascending peak.

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
Unanimous DPOY 2026. *Session 113: revised to 9.30 (was 9.14) with tier crossing 4→3 + archetype migration Switchable Big → All-Around Big. Largest upward revision in Workstream 2 cost-spike. Drivers: unanimous DPOY 2025-26 (one of two players in 50 yrs with two unanimous awards — ROY 2024 + DPOY 2026), MVP finalist + likely All-NBA First Team, full 64-GP healthy season post-DVT, Y3 production at 25.0/11.5/3.1/3.4 BPG on 61.3% TS / 31.0% USG, archetype reclassification reflecting elite playmaking dimension (8.5 vision, 8.0 decision-making, inverted PnR usage) + scoring versatility not present in initial 9.14 evaluation. S96-F02 empirical-override pattern applied 4× (#15, #17, #20, implicit #16) — verticality-based mechanism overcomes #23 Strength 6.0 cap on defensive sub-domains. Healthy Tier 3 comparison set (Giannis 9.40, KD 9.32, Curry 9.20) anchored placement at 9.30 lower-third upper edge — above Curry on net 2025-26 impact (peak vs decline), just below Durant on career resume. Initial Skill 4 draft 9.27 nudged to 9.30 on Tyler review — profile-shape density (22 strengths, three at 9.5+, zero liabilities — densest in active library) + clear current-level edge over Curry warranted upper edge of lower-third. R13 Stage 2 not fired (1 series — below sample minimum); Stage 1 POT modifier also below sample. POT 9.94 (one tick below 9.99 hard cap) reflects DVT longevity uncertainty bound on Tier 1 outcomes. S102-F02 negative-control: ascending trajectory + 0/3 post-peak conditions. S111-F01 anchor-deflation watchpoint applied (3rd application); not driving placement (healthy comparison set). **S118 (2026-04-29):** composite revised 9.30 → 9.34 — anchor-cluster recalibration sweep; current-state strongest-of-three signature (unanimous DPOY 2025-26 + MVP finalist + 64 GP healthy + ascending at 22 + densest peak cluster). **2026-05-04 NBA POB recompute (S119 sweep):** POT 9.94 → 9.78 (prospect modifier-stack → empirical anchor-band Jokić 9.64 / Kareem 9.82, upper-third placement under existing Tier 1 DVT narrative cap); Min 8.84 unchanged; Max 9.99 unchanged; Confidence tight → moderate.*

## Sources
- Full profile: [output/Victor_Wembanyama/2026-04-28_profile.md](../../output/Victor_Wembanyama/2026-04-28_profile.md)
- Research packets: [raw/Victor_Wembanyama/2026-04-28_research-packet.md](../../raw/Victor_Wembanyama/2026-04-28_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)

```dataviewjs
const DOM_KEYS = [
  "d1_finishing","d2_shooting","d3_ball_skills","d4_playmaking",
  "d5_defense","d6_rebounding","d7_athleticism","d8_iq_motor"
]
const DOM_LABELS = [
  "Finishing","Shooting","Ball Skills","Playmaking",
  "Defense","Rebounding","Athleticism","IQ/Motor"
]
const p = dv.current()

window.renderChart({
  type: "radar",
  data: {
    labels: DOM_LABELS,
    datasets: [
      {
        label: "Max",
        data: DOM_LABELS.map(() => 10),
        backgroundColor: "rgba(0,0,0,0)",
        borderColor: "rgba(200,200,200,0.55)",
        borderWidth: 1.5,
        borderDash: [4, 4],
        pointRadius: 0,
        fill: false,
        order: 2
      },
      {
        label: p.player,
        data: DOM_KEYS.map(k => p[k] ?? null),
        backgroundColor: "rgba(54,162,235,0.35)",
        borderColor: "rgb(54,162,235)",
        borderWidth: 2,
        pointBackgroundColor: "rgb(54,162,235)",
        pointRadius: 3,
        order: 1
      }
    ]
  },
  options: {
    scales: {
      r: {
        min: 0,
        max: 10,
        ticks: {
          stepSize: 2,
          color: "rgba(200,200,200,0.7)",
          backdropColor: "rgba(0,0,0,0)",
          font: { size: 10 }
        },
        grid: {
          color: "rgba(200,200,200,0.22)",
          lineWidth: 1
        },
        angleLines: {
          color: "rgba(200,200,200,0.35)",
          lineWidth: 1
        },
        pointLabels: {
          color: "rgba(230,230,230,0.9)",
          font: { size: 12 }
        }
      }
    },
    plugins: {
      legend: {
        labels: {
          filter: item => item.text !== "Max"
        }
      }
    }
  }
}, this.container)
```
```dataviewjs
const SUB_KEYS = [
  "sd01_at_basket_finishing","sd02_contact_finishing","sd03_post_offense",
  "sd04_catch_shoot_3pt","sd05_off_dribble_shooting","sd06_mid_range","sd07_free_throw",
  "sd08_handling_creation","sd09_touch_feel","sd10_ball_security",
  "sd11_court_vision","sd12_decision_making","sd13_passing_execution","sd14_off_ball_movement",
  "sd15_on_ball_pressure","sd16_help_defense","sd17_rim_protection","sd18_post_defense",
  "sd19_offensive_rebounding","sd20_defensive_rebounding",
  "sd21_burst_explosion","sd22_lateral_quickness","sd23_strength",
  "sd24_shot_selection","sd25_effort_motor","sd26_competitive_character"
]
const SUB_LABELS = [
  "At-Rim","Contact","Post O",
  "C&S 3PT","Pull-Up","Mid","FT",
  "Handle","Touch","Ball Sec",
  "Vision","Decisions","Passing","Off-Ball",
  "On-Ball D","Help D","Rim Pro","Post D",
  "OREB","DREB",
  "Burst","Lateral","Strength",
  "Shot IQ","Motor","Compete"
]
const p = dv.current()

window.renderChart({
  type: "radar",
  data: {
    labels: SUB_LABELS,
    datasets: [
      {
        label: "Max",
        data: SUB_LABELS.map(() => 10),
        backgroundColor: "rgba(0,0,0,0)",
        borderColor: "rgba(200,200,200,0.55)",
        borderWidth: 1.5,
        borderDash: [4, 4],
        pointRadius: 0,
        fill: false,
        order: 2
      },
      {
        label: p.player,
        data: SUB_KEYS.map(k => p[k] ?? null),
        backgroundColor: "rgba(54,162,235,0.35)",
        borderColor: "rgb(54,162,235)",
        borderWidth: 2,
        pointBackgroundColor: "rgb(54,162,235)",
        pointRadius: 1.5,
        order: 1
      }
    ]
  },
  options: {
    scales: {
      r: {
        min: 0,
        max: 10,
        ticks: {
          stepSize: 2,
          color: "rgba(200,200,200,0.7)",
          backdropColor: "rgba(0,0,0,0)",
          font: { size: 10 }
        },
        grid: {
          color: "rgba(200,200,200,0.22)",
          lineWidth: 1
        },
        angleLines: {
          color: "rgba(200,200,200,0.35)",
          lineWidth: 1
        },
        pointLabels: {
          color: "rgba(230,230,230,0.9)",
          font: { size: 9 }
        }
      }
    },
    plugins: {
      legend: {
        labels: {
          filter: item => item.text !== "Max"
        }
      }
    }
  }
}, this.container)
```
