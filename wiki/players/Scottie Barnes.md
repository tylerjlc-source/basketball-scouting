---
player: Scottie Barnes
group: Wing
archetype: Defensive-Engine Playmaker
composite: 8.57
tier: 6
tier_band: 8.30–8.59
status: Active
competition_level: NBA
has_profile: true
profile_path: output/Scottie_Barnes/2026-05-05_profile.md
scored_session: 103
last_updated_session: 141
rubric_version: v3
pot: 8.87
sd01_at_basket_finishing: 8.2
sd02_contact_finishing: 6.7
sd03_post_offense: 5.5
sd04_catch_shoot_3pt: 5.8
sd05_off_dribble_shooting: 5.2
sd06_mid_range: 7.7
sd07_free_throw: 7.8
sd08_handling_creation: 7.1
sd09_touch_feel: 7.6
sd10_ball_security: 7.0
sd11_court_vision: 8.7
sd12_decision_making: 7.5
sd13_passing_execution: 8.4
sd14_off_ball_movement: 6.3
sd15_on_ball_pressure: 8.5
sd16_help_defense: 9.1
sd17_rim_protection: 8.0
sd18_post_defense: 7.8
sd19_offensive_rebounding: 7.0
sd20_defensive_rebounding: 9.0
sd21_burst_explosion: 7.1
sd22_lateral_quickness: 8.2
sd23_strength: 8.5
sd24_shot_selection: 7.0
sd25_effort_motor: 7.8
sd26_competitive_character: 8.2
d1_finishing: 6.8
d2_shooting: 7.8
d3_ball_skills: 7.2
d4_playmaking: 7.7
d5_defense: 8.3
d6_rebounding: 8.0
d7_athleticism: 7.9
d8_iq_motor: 7.7
---

# Scottie Barnes

**[[Defensive-Engine Playmaker]]** Wing — composite **8.57** (Tier 6).

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

const DOMAIN_GROUPS = [
  { name: "Finishing",   indices: [0, 1, 2],         color: "240, 128, 128" },
  { name: "Shooting",    indices: [3, 4, 5, 6],      color: "255, 165, 80"  },
  { name: "Ball Skills", indices: [7, 8, 9],         color: "230, 200, 90"  },
  { name: "Playmaking",  indices: [10, 11, 12, 13],  color: "120, 200, 130" },
  { name: "Defense",     indices: [14, 15, 16, 17],  color: "100, 160, 220" },
  { name: "Rebounding",  indices: [18, 19],          color: "160, 130, 220" },
  { name: "Athleticism", indices: [20, 21, 22],      color: "220, 130, 200" },
  { name: "IQ/Motor",    indices: [23, 24, 25],      color: "170, 170, 180" }
]
const WEDGE_OPACITY = 0.18
const LABEL_OFFSET = 50

const wedgePlugin = {
  id: 'domainWedges',
  beforeDatasetsDraw(chart) {
    const scale = chart.scales.r
    if (!scale) return
    const ctx = chart.ctx
    const cx = scale.xCenter
    const cy = scale.yCenter
    const maxRadius = scale.drawingArea
    const N = chart.data.labels.length
    const angleStep = (2 * Math.PI) / N
    DOMAIN_GROUPS.forEach(d => {
      const firstIdx = d.indices[0]
      const lastIdx = d.indices[d.indices.length - 1]
      const startAngle = -Math.PI/2 + (firstIdx - 0.5) * angleStep
      const endAngle = -Math.PI/2 + (lastIdx + 0.5) * angleStep
      ctx.save()
      ctx.beginPath()
      ctx.moveTo(cx, cy)
      ctx.arc(cx, cy, maxRadius, startAngle, endAngle, false)
      ctx.closePath()
      ctx.fillStyle = `rgba(${d.color}, ${WEDGE_OPACITY})`
      ctx.fill()
      ctx.restore()
    })
  },
  afterDraw(chart) {
    const scale = chart.scales.r
    if (!scale) return
    const ctx = chart.ctx
    const cx = scale.xCenter
    const cy = scale.yCenter
    const maxRadius = scale.drawingArea
    const N = chart.data.labels.length
    const angleStep = (2 * Math.PI) / N
    const labelRadius = maxRadius + LABEL_OFFSET
    ctx.save()
    ctx.font = 'bold 12px sans-serif'
    ctx.textAlign = 'center'
    ctx.textBaseline = 'middle'
    DOMAIN_GROUPS.forEach(d => {
      const firstIdx = d.indices[0]
      const lastIdx = d.indices[d.indices.length - 1]
      const midAngle = -Math.PI/2 + ((firstIdx + lastIdx) / 2) * angleStep
      const x = cx + Math.cos(midAngle) * labelRadius
      const y = cy + Math.sin(midAngle) * labelRadius
      ctx.fillStyle = `rgba(${d.color}, 1.0)`
      ctx.fillText(d.name, x, y)
    })
    ctx.restore()
  }
}

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
    layout: { padding: 50 },
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
  },
  plugins: [wedgePlugin]
}, this.container)
```

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
2x All-Star

## Sources
- Full profile: [output/Scottie_Barnes/2026-05-05_profile.md](../../output/Scottie_Barnes/2026-05-05_profile.md)
- Research packets: [raw/Scottie_Barnes/2026-05-05_research-packet.md](../../raw/Scottie_Barnes/2026-05-05_research-packet.md)
- Anchor library: [docs/ANCHOR-LIBRARY.md](../../docs/ANCHOR-LIBRARY.md)
