---
player: Joel Embiid
group: Big
archetype: All-Around Big
composite: 8.40
tier: 6
tier_band: 8.30–8.59
status: Active (injury flag)
competition_level: NBA
has_profile: true
profile_path: output/Joel_Embiid/2026-04-26_profile.md
scored_session: 110
last_updated_session: 110
rubric_version: v3
pot: 8.40
sd01_at_basket_finishing: 8.7
sd02_contact_finishing: 9.1
sd03_post_offense: 9.0
sd04_catch_shoot_3pt: 7.4
sd05_off_dribble_shooting: 7.3
sd06_mid_range: 8.5
sd07_free_throw: 8.9
sd08_handling_creation: 8.4
sd09_touch_feel: 8.5
sd10_ball_security: 7.1
sd11_court_vision: 8.1
sd12_decision_making: 6.9
sd13_passing_execution: 7.9
sd14_off_ball_movement: 6.9
sd15_on_ball_pressure: 5.5
sd16_help_defense: 7.4
sd17_rim_protection: 8.6
sd18_post_defense: 7.5
sd19_offensive_rebounding: 6.4
sd20_defensive_rebounding: 7.4
sd21_burst_explosion: 5.9
sd22_lateral_quickness: 5.4
sd23_strength: 9.1
sd24_shot_selection: 7.9
sd25_effort_motor: 5.6
sd26_competitive_character: 5.1
d1_finishing: 8.9
d2_shooting: 8.0
d3_ball_skills: 8.0
d4_playmaking: 7.5
d5_defense: 7.3
d6_rebounding: 6.9
d7_athleticism: 6.8
d8_iq_motor: 6.2
---

# Joel Embiid

**[[All-Around Big]]** Big — composite **8.40** (Tier 6). 7'0" 280-lb post hub + face-up scorer + interior anchor; MVP-era ceiling tempered by structural injury history and active-injury dormancy in the 2026 playoff cycle.

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
Injury flag — 2026 dormant. *Session 110: revised to 8.40 (was 8.05) with tier crossing 7→6. R12 anchor on 2022-23 MVP year + S96-F03 athletic recalibration (R9 not formally applied to avoid double-temper) + R13 Stage 2 skipped per active-injury dormancy (appendectomy 4/2026 ruled him out of current Sixers-Celtics R1 series).*

## Sources
- Full profile: [output/Joel_Embiid/2026-04-26_profile.md](../../output/Joel_Embiid/2026-04-26_profile.md)
- Research packets: [raw/Joel_Embiid/2026-04-26_research-packet.md](../../raw/Joel_Embiid/2026-04-26_research-packet.md)
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
