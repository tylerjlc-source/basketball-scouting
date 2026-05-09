---
type: comparison
title: Stretch Bigs — radar comparison
players: [Myles Turner, Naz Reid, Nikola Vučević]
---

# Stretch Bigs — radar comparison

Overlay of three Stretch Bigs on the 26-axis sub-domain web.

To compare different players: edit the `const players = [...]` line in the code block below. Names must match the `player:` frontmatter field in `wiki/players/<Player>.md` exactly.

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
const WEDGE_OPACITY = 0.12
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

// EDIT THIS LINE — change the names to swap players in/out of the comparison.
// Names must match the `player:` frontmatter field in wiki/players/<Player>.md exactly.
const players = ["Jaylen Brown", "Jayson Tatum", "Scottie Barnes"]

const colors = [
  "54,162,235","255,99,132","75,192,192",
  "255,159,64","153,102,255","255,205,86"
]

const playerDatasets = players.map((name, i) => {
  const page = dv.pages('"wiki/players"').where(p => p.player === name).first()
  if (!page) return null
  const c = colors[i % colors.length]
  return {
    label: name,
    data: SUB_KEYS.map(k => page[k] ?? null),
    backgroundColor: `rgba(${c},0.15)`,
    borderColor: `rgb(${c})`,
    borderWidth: 2,
    pointBackgroundColor: `rgb(${c})`,
    pointRadius: 1.5,
    order: 1
  }
}).filter(d => d !== null)

const maxBoundary = {
  label: "Max",
  data: SUB_LABELS.map(() => 10),
  backgroundColor: "rgba(0,0,0,0)",
  borderColor: "rgba(200,200,200,0.55)",
  borderWidth: 1.5,
  borderDash: [4, 4],
  pointRadius: 0,
  fill: false,
  order: 2
}

window.renderChart({
  type: "radar",
  data: {
    labels: SUB_LABELS,
    datasets: [maxBoundary, ...playerDatasets]
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
