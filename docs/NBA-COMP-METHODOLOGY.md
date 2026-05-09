# NBA COMP METHODOLOGY — Reference File
**Loaded by Skill 5 (scout-output) before assigning NBA Comps.**
**Two tracks — load surgically per Section 9 evaluation State.**

---

## PURPOSE

The NBA Comp assigns NBA player references to every profile. Two tracks govern how:

1. **§A — Prospect NBA Comp (States 1–3)** — full statistical match apparatus. Comp anchors a development archetype reference and serves as a statistical validation cross-check on the Projection Midpoint via rookie-season TS%. 2–3 comps per prospect, with comp tier (🟢/🟡/🔴) and aligned/flagged validation flag.

2. **§B — NBA Vet Lineage Comp** — single qualitative reference per § B. Universal for NBA vet evaluations — every active NBA-vet profile carries one lineage comp.

---

## §A — PROSPECT NBA COMP (States 1–3)

For prospect evaluations only — pre-NBA, pre-draft, or rookies/early-career players where rookie-season TS% remains the primary anchor. NBA vet evaluations (≥25 NBA games) skip this section entirely; see §B.

### A.1 — Assignment Rules

Apply in order:

**Rule 1 — Group match required.** Comp must come from the same positional group: Guards, Wings, or Bigs.

**Rule 2 — Archetype match required.** Comp must share the same archetype bucket. Style gate — a 3-and-D Wing prospect cannot comp to an Offensive Engine.

**Rule 3 — Cross-group exception.** A cross-group comp is permitted only when all three conditions are met:
- Prospect's size and skill profile is documented as anomalous for their listed position
- Cross-group comp has a higher archetype match than any in-group option
- At least two independent scouting sources explicitly reference the cross-group player as a comparison

If all three are met: cross-group comp is permitted, flagged in the similarity note, limited to one per player. Remaining comps must come from the correct group.

**Rule 4 — Recency preference.** Last 10 years preferred. Older comps permitted only when no modern equivalent exists — must be flagged with explanation.

**Rule 5 — Anchor signal required.**
- Signal: Rookie season True Shooting % (Basketball-Reference)
- When unavailable: flag as single-signal unavailable; comp tier falls to 🔴 Rubric only

**Rule 6 — 2–3 comps per player.** Minimum two, maximum three. Single comp is too brittle.

### A.2 — Statistical Similarity Match

The statistical match determines comp tier.

**Stats by positional group:**

| Group | Primary signal | Secondary signals |
|---|---|---|
| Guards | True Shooting % | Usage rate, Assist rate, Turnover rate |
| Wings | True Shooting % | Usage rate, Rebound rate, STL per 100 possessions |
| Bigs | True Shooting % | Usage rate, Rebound rate, BLK per 100 possessions |

**Fallback:** When True Shooting % is unavailable, substitute PPG.

**Tolerance bands:**

| Signal | Tolerance |
|---|---|
| True Shooting % | ±5% |
| PPG (fallback) | ±4 points |
| Usage rate | ±5% |
| Assist rate | ±4% |
| Turnover rate | ±2% |
| Rebound rate | ±5% |
| STL per 100 | ±0.5 |
| BLK per 100 | ±1.0 |

Stats outside the tolerance band do not disqualify the comp — they do not count toward the tier threshold.

**Note on STL/BLK rates:** Earlier methodology used Basketball-Reference STL%/BLK% (±1.5% / ±2%). The NBA Stats Advanced endpoint does not expose those columns (B4 backlog), so the script switched to per-100-possessions rates from the Base endpoint. Per-100 rates are >0.9 correlated with the percentages, so the substitution is cosmetic in practice; tolerance bands above are the per-100 equivalents of the original ±1.5% / ±2% bands.

### A.3 — Comp Tier Determination

| Tier | Criteria |
|---|---|
| 🟢 Full | Primary signal confirmed + at least two secondary signals confirmed |
| 🟡 Partial | Primary signal confirmed + one secondary confirmed; remainder inferred from qualitative profile |
| 🔴 Rubric only | Primary signal unavailable or no statistical match achievable; comp is archetype reference only |

### A.4 — Projection Midpoint Validation

Under the unified composite scale (Session 98), the Projection Midpoint equals the rubric composite directly — the comp is not a weighted numeric input. Comp tier signals validation strength:

| Comp Tier | Validation strength |
|---|---|
| 🟢 Full | Strong — comp statistically confirms rubric midpoint |
| 🟡 Partial | Moderate — comp partially confirms rubric midpoint |
| 🔴 Rubric only | Low — no statistical confirmation; rubric stands alone |

**Validation flag rule:** If the comp's rookie TS% implies a significantly different entering-the-league production level than the composite suggests, flag the midpoint output as `comp validation: flagged`. Otherwise `comp validation: aligned`. Divergence does not shift the Midpoint — the comp is a check, not a weight.

**Conflict rule:** If the comp contradicts the rubric score (either archetype/profile-level or statistical), the comp is invalid — reassign before proceeding. Conflict resolution is a quality control step, not a weighting problem.

### A.5 — Output Format

```
NBA COMP [N]: [Player name]
Archetype:       [Bucket]
Tier:            [🟢 Full | 🟡 Partial | 🔴 Rubric only]
Similarity:      [One sentence — what specifically matches]
Anchor:          Rookie TS%: [X%]
Flags:           [Cross-group | Single-signal | Older comp] — omit if none
```

---

## §B — NBA VET LINEAGE COMP

For NBA vet evaluations only — active NBA players (≥25 NBA games) rated at current NBA level (per NBA-PROJECTION-OUTPUT-BLOCK.md). Prospect evaluations (States 1–3) skip this section entirely; see §A.

### B.1 — What this comp is

A single qualitative reference for the NBA vet profile. No statistical match, no script run, no comp tier, no validation flag. The lineage comp serves a narrative-anchor role: a real NBA player whose profile a reader benefits from being pointed to when interpreting the subject's evaluation.

### B.2 — Selection criteria

Any player whose profile a reader would benefit from being pointed to. Lineage semantics implied — the comp is meant to foreshadow, parallel, or anchor the subject's profile in the reader's reference frame.

- **Cross-era OK without flag** — historical references are valid
- **Cross-archetype OK without flag** — lineage bridging archetype boundaries is valid
- **No required match dimensions** — group, archetype, era, and recency are all optional
- **No statistical anchor required** — TS%, USG, etc. are not required (NBA_Comp_Stats.py is not run)

### B.3 — Required vs optional

Universal for NBA vet evaluations. Always include one lineage comp — even for generational outliers, point to the closest historical/active analog the reader can grasp.

### B.4 — Output Format

Single callout line in Section 10:

```
LINEAGE COMP: [Player Name] — [1-line rationale]
```

No tier badge, no validation flag, no anchor signal, no flag list.

---

*Extracted from scouting-rubric SKILL.md v8, Session 91. NBA Comp Methodology confirmed Sessions 23–25. S98: Projection Midpoint weighting replaced with validation-only role per 1-minimal unification. S101: NBA-Vet Adaptation promoted from scout-output-learnings S96-F04 after 6 applications. S119: split into §A (prospects, States 1–3) + §B (NBA Vet Lineage Comp) — multi-comp + age-comparable-season machinery scoped to prospects; NBA vet evals now use single lineage comp. See scout-output-learnings.md S96-F04 archived coda for the rescope rationale. 2026-05-03: "State 4" terminology retired across active routing — replaced with "NBA vet" / "≥25 NBA games" routing per S119 NBA POB design.*
