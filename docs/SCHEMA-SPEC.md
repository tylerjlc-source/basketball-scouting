# SCHEMA SPEC

Schema and data-model definition for the basketball-scouting system.

**Status:** Canonical v1.0 — promoted S151 (2026-05-06). §10-A/B/C/D/E resolved S109 (2026-04-26); §10-F/G/H/K/L resolved S151 (2026-05-06); §10-I and §10-J explicitly deferred.

**Load scope:** Task-loaded at backend / pipeline / public-DB work. Not session-open governance.

---

## PURPOSE

Formalize the implicit schema currently spread across `output/*.md` profiles, `wiki/` frontmatter, and `docs/ANCHOR-LIBRARY.md`, so that:

1. Any artifact can be validated against a single shape.
2. The public ratings DB (Product 2) can be statically generated from `wiki/` + `output/` at build time without per-player schema reverse-engineering.
3. Re-evaluations preserve longitudinal series integrity rather than overwrite history.
4. Rubric drift, anchor library drift, and archetype migrations are explicit version-tracked events, not silent state changes.

This spec describes the schema as it exists today (v3 rubric / 105-anchor library) and surfaces the decisions that the current implicit schema does not yet answer (§10).

---

## ARTIFACT MAP

Five layers, listed in source-of-truth order (upper layers override lower):

| Layer | Path | Owner | Artifact role |
|---|---|---|---|
| 1. Schema | [docs/](.) | Tyler | Rubric, scales, rules, anchor table, this spec |
| 2. Process | [skills/](../skills/) | Tyler | 6-skill evaluation chain definitions |
| 3. Evidence | [raw/](../raw/) | Skill 1 | Immutable dated research packets |
| 4. Evaluation | [output/](../output/) | Skill 5 | Canonical finished profiles |
| 5. Graph | [wiki/](../wiki/) | Skill 6 (LLM) | Derived player pages, archetype hubs, index, log |

**Source-of-truth rule (W1 from WIKI-PROTOCOL):** Layer N is authoritative over layer N+1. If layer 5 contradicts layer 4, layer 5 is corrected — never the reverse.

---

## ENTITIES

### 1. Player (identity)

Stable identity record. One per player, regardless of how many times evaluated.

| Field | Type | Required | Notes |
|---|---|---|---|
| `player` | string | yes | Full name, canonical form. Used as natural key. |
| `group` | enum | yes | `Guard` \| `Wing` \| `Big` |
| `position` | string | yes | `PG` \| `SG` \| `SF` \| `PF` \| `C`, optionally hyphenated (`SG/SF`) |
| `competition_level` | enum | yes | `NBA` \| `College D1` \| `International` \| `HS` |
| `career_status` | enum | yes | `Active` \| `Retired` \| `Draft prospect` (per §10-E resolution) |
| `injury_note` | string \| null | yes | Freetext; `null` if no flag. E.g. `Achilles 5/2025 — active recovery`, `Left-calf flag` |
| `draft_class` | int \| null | yes | Year, e.g. `2026`. Required when `career_status = Draft prospect`; null otherwise |
| `archetype` | string | yes | One of the 25 active archetype names; see [docs/ARCHETYPE-WEIGHTS-*.md](.) |

**Filename canonicalization:** Spaces in `wiki/players/` (Obsidian-native), underscores in `output/` and `raw/` (filesystem-historical). Both forms map to the same `player` string. See W5.

### 2. Evaluation (one Skill 1–5 chain run)

A complete scouting chain produces one Evaluation. A Player may have many Evaluations over time; today only the most recent is materialized in `output/`.

**Profile artifact** at `output/[First_Last]_profile.md` contains 11 numbered sections. Frontmatter is currently absent; section 1 is a markdown table acting as header.

| Field | Section | Type | Notes |
|---|---|---|---|
| `composite` | §1, §8 | float, X.XX | 0.00–10.00, two-decimal precision |
| `tier` | §1, §8 | int 1–13 | Derived from composite via tier band table |
| `tier_band` | §1, §8 | string `X.XX–X.XX` | Derived; both stored for redundancy |
| `tier_label` | §1 | string | E.g. `Perennial All-Star — legitimate star`. From [COMPOSITE-SCALE-AND-TIERS.md](COMPOSITE-SCALE-AND-TIERS.md) |
| `evaluation_date` | §1 | date `YYYY-MM-DD` | Inconsistent — present in Şengün/Turner, missing from Tatum/Bridges |
| `prior_anchor` | §1 | float \| null | If re-eval. Drift = composite − prior_anchor |
| `scored_session` | (wiki) | int | Session number when this evaluation ran |
| `rubric_version` | (wiki) | enum | `v3` \| `unknown` (legacy anchors pre-v3) |

**Sub-records nested in §4–§10** (defined below): sub-domain scores (×26), domain summaries (×8), profile shape, non-negotiables gate, composite rationale, projection block, NBA comps (×1–3), QC1–5.

**Section 11** is the anchor library entry payload (the row appended to / revised in `docs/ANCHOR-LIBRARY.md`). Present in Tatum/Şengün/Bridges; appended into Section 11 (Quality Checks) in Turner — inconsistency, see §10-G.

### 3. Sub-domain score (26 rows per evaluation)

The atomic measurement unit.

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | int 1–26 | yes | Stable across rubric versions within v3 |
| `name` | string | yes | Per [SUB-DOMAINS_v3.md](SUB-DOMAINS_v3.md) |
| `domain` | int 1–8 | yes | Parent domain, derived |
| `score` | float | yes | 0.0–10.0, **0.1 precision** |
| `confidence` | enum | yes | `Low` \| `Medium` \| `Medium-High` \| `High` |
| `rationale` | string | yes | One paragraph. Mandatory per CLAUDE.md "qualitative validation" rule |
| `structural_zero` | bool | yes | True if archetype excludes this sub-domain. SZ score conventionally `4.0` placeholder |
| `caps_considered` | string[] | optional | Cross-reference cap log: `#5→#24 cap applied`, etc. |
| `empirical_overrides` | string[] | optional | E.g. `S96-F02 R8 override applied` |
| `universal_marker` | bool | derived | True for #12, #24, #25, #26 (universals — applied to all archetypes) |

**Score precision rule:** Per SCORING-RULES.md R14, use the full `.0–.9` range; only Low/Very-Low confidence rounds to `.5`. Default-to-`.5` is a draft-time anti-pattern.

### 4. Domain score (8 rows per evaluation)

Band-matched assignment per [DOMAIN-SCALE_v1.md](DOMAIN-SCALE_v1.md), informed by role-relevant sub-domains per [DOMAIN-SCORE-ROLE-RELEVANCE.md](DOMAIN-SCORE-ROLE-RELEVANCE.md).

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | int 1–8 | yes | D1 Finishing, D2 Shooting, ... D8 IQ/Motor |
| `name` | string | yes | Domain label |
| `score` | float | yes | Band-match assignment from DOMAIN-SCALE_v1.md, integrating `included` sub-domains, **0.1 precision** |
| `included` | int[] | yes | Sub-domain ids that informed the band-match (role-relevant sub-domains) |
| `excluded` | int[] | yes | Sub-domain ids excluded as structural zeros for this archetype |
| `synthesis` | string | yes | One-sentence synthesis naming the sub-domains that anchored the band-match AND any constraining sub-domain that pulled within the band (mandatory per scout-profile.md Step 3) |

### 5. Profile shape

Derived classification of the score distribution.

| Field | Type | Required | Notes |
|---|---|---|---|
| `strengths` | sub-domain ref[] | yes | Score ≥ 7.0 |
| `liabilities` | sub-domain ref[] | yes | Score ≤ 4.9, role-relevant only (excludes structural zeros) |
| `below_strength` | sub-domain ref[] | yes | Score 5.0–6.9 — not formal liabilities, surfaced for transparency |
| `structural_zero_set` | int[] | yes | Per archetype, from DOMAIN-SCORE-ROLE-RELEVANCE |
| `profile_type` | enum | yes | `Distributed` \| `Specialist` \| `Polarized` \| `Compact` \| (others — see §10-J) |

### 6. Non-negotiables gate

Position-driven threshold check per [NON-NEGOTIABLES.md](NON-NEGOTIABLES.md).

| Field | Type | Required |
|---|---|---|
| `position_primary` | enum (PG/SG/SF/PF/C) | yes |
| `position_secondary` | enum \| null | optional (e.g. SF/PF for Tatum) |
| `gate_results` | array of `{sub_domain_id, score, threshold, result: PASS/FAIL}` | yes |
| `active_caps` | string[] | yes | Empty array means none firing |
| `position_shift_flag` | bool | yes | True if gate failure forced a position re-classification |

### 7. Composite rationale (Skill 4 output)

| Field | Type | Required | Notes |
|---|---|---|---|
| `composite` | float X.XX | yes | Same value as in §2 |
| `candidate_band` | string | yes | E.g. `Tier 6 (8.30–8.59)` |
| `placement_within_band` | enum | yes | `Lower` \| `Middle` \| `Upper` third |
| `anchor_comparisons` | array of `{anchor_player, anchor_composite, relationship, margin}` | yes | Full library cross-reference per S102-F03 |
| `awards_cross_check` | string | yes | Hardware reconciliation narrative |
| `r13_stage_2_modifier` | float \| null | yes | Playoff modifier per R13; `null` if no shrink/rise gate fires |
| `ambiguity_flag` | string \| null | yes | Boundary-case note. Per C4, ambiguity resolves DOWN |
| `pre_modifier_composite` | float \| null | optional | If R13 Stage 2 fires, pre-modifier value preserved (Bridges precedent: `7.95 → 7.85`) |
| `self_correction_sequence` | float[] | optional | Multi-draft correction log when initial draft was off (Bridges: `[7.62, 7.75, 7.85]`) |

### 8. Projection block (Skill 5 output)

Two structurally distinct schemas, routed by NBA experience per NBA-PROJECTION-OUTPUT-BLOCK.md eligibility rule:

- **§8a — Prospect projection block** ([PROJECTION-OUTPUT-BLOCK.md](PROJECTION-OUTPUT-BLOCK.md)): players with <25 NBA games (States 1–3)
- **§8b — NBA vet projection block** ([NBA-PROJECTION-OUTPUT-BLOCK.md](NBA-PROJECTION-OUTPUT-BLOCK.md)): players with ≥25 NBA games

The two schemas share only `pot`, `min`, `max`, `confidence`, `spread_note` as field names — all other fields are non-overlapping. The S119 split reflects a structural difference in projection methodology: prospect projection uses composite-to-POT band + modifier stack + probabilistic Bust/Avg/Boom; NBA vet projection uses anchor-based placement against named ceiling anchors with no probabilistic outcome modeling (observed career data replaces it).

**Discriminator:** Not stored as a field on the evaluation. Derivable from `career_status` + cumulative NBA games. (Per "derive-don't-tag" — adding a `projection_block_type` field is redundant with already-available signals.)

#### §8a — Prospect projection block

| Field | Type | Required | Notes |
|---|---|---|---|
| `status_state` | enum 1–3 | yes | `1` = Consensus+Declared, `2` = Consensus+Undeclared (Pre-declaration), `3` = No-consensus+Undeclared (Pre-consensus) |
| `consensus_confidence` | enum | yes | `Near-certain` \| `High` \| `Moderate` \| `Low` \| `Very low` \| `N/A` (State 3 only) |
| `slot_source` | string | yes | E.g. `5 of 6 mocks — pick range: 4–7` (or `N/A` for State 3) |
| `projection_midpoint` | float | yes | Equals composite |
| `comp_tier_indicator` | enum | yes | Inline comp validation glyph: `🟢 Full` \| `🟡 Partial` \| `🔴 None` (storage form open per §10-K) |
| `comp_validation` | enum | yes | `aligned` \| `flagged` |
| `pot` | float | yes | Career ceiling per Block 2 (composite-to-POT band + modifier stack, capped at 9.99) |
| `min` | float | yes | Floor per Block 3 (POT − base spread − risk modifiers) |
| `max` | float | yes | Ceiling per Block 3 (POT + base spread, symmetric) |
| `pot_modifier_stack` | array of `{name, value, rationale}` | yes | Block 2 modifiers — composite delta + projection modifiers + R13 Stage 1. E.g. `+0.40 elite competitive character`, `−0.50 significant injury history` |
| `avg_pct_anchor` | string | yes | POT-implied expected outcome (e.g. `Reliable rotation contributor`) per Block 4 anchor table |
| `bust_pct` | float | yes | Block 4. Floor: 3% |
| `avg_pct` | float | yes | Block 4. `100 − bust_pct − boom_pct` (residual; minimum 20%) |
| `boom_pct` | float | yes | Block 4. Floor: 3% |
| `bust_drivers` | string[] | yes | Confirmed Bust% modifier drivers, or `["baseline only"]` |
| `boom_drivers` | string[] | yes | Confirmed Boom% modifier drivers, or `["baseline only"]` |
| `confidence` | enum | yes | `tight` \| `moderate` \| `wide` |
| `spread_note` | string | yes | One line — data sparsity, profile risk, or both |
| `divergence_flag` | enum | yes | `none` \| `sleeper candidate` \| `bust-risk signal` + one-line explanation. Sleeper criteria per PROJECTION-OUTPUT-BLOCK.md Sleeper section (Path A composite-led / Path B POT-led with three validation gates / Path C combined) |

#### §8b — NBA vet projection block

| Field | Type | Required | Notes |
|---|---|---|---|
| `career_stage` | enum | yes | `Pre-peak ascending` \| `Approaching peak` \| `Peak` \| `Post-peak` \| `Late career` per NBA POB Step 1 (governs available POT growth + Min/Max spread shape) |
| `trajectory` | enum | yes | `Ascending` \| `Plateau` \| `Declining` \| `Recovering` per NBA POB Step 2 (commits POT placement within ceiling anchor band) |
| `trajectory_evidence` | string | yes | One-line cite supporting the trajectory flag (statistical or qualitative) |
| `demonstrated_peak` | float \| string | yes | Best observed season composite. Use `string` (e.g. `All-NBA 2nd 2024-25`) when peak season was not formally evaluated; estimate composite from accolade table per NBA POB Step 3.1 |
| `ceiling_anchors` | array of `{player, composite}` | yes | 2–3 anchors from ANCHOR-LIBRARY.md per NBA POB Step 3.2 (share archetype, or share group at minimum) |
| `ceiling_band_low` | float | yes | Lowest composite among named ceiling anchors |
| `ceiling_band_high` | float | yes | Highest composite among named ceiling anchors |
| `skill_gap_caps` | string[] | yes | Structural ceiling bounds named in narrative; empty array = `["none identified"]` |
| `r13_stage_1_modifier` | float | yes | `+0.40` \| `+0.20` \| `0` \| `−0.20` \| `−0.40` per R13 Stage 1; subject to NBA POB double-count guard if ceiling anchors already embed playoff signal |
| `r13_stage_1_cite` | string | yes | Playoff signal evidence supporting the modifier |
| `current_composite` | float | yes | Mirror of §1 composite — explicit in projection block per NBA POB output format |
| `pot` | float | yes | Anchor-based central projection per NBA POB Step 3 (band placement + skill-gap caps + R13 stack, capped at demonstrated peak + career-stage allowance per Validation Check #2) |
| `min` | float | yes | Floor per NBA POB Step 4 (current − trajectory adjustment − risk modifiers; asymmetric anchoring) |
| `max` | float | yes | Ceiling per NBA POB Step 4 (top of anchor band + stage buffer; capped by narrative-stated tier exclusions) |
| `confidence` | enum | yes | `tight` \| `moderate` \| `wide` (Recovering trajectory auto-routes to `wide`) |
| `spread_note` | string | yes | One line — what Min and Max represent for this vet |
| `trajectory_note` | string | yes | One line — what the trajectory flag commits to (methodology, not evidence; pairs with `trajectory_evidence`) |

**No Bust/Avg/Boom for §8b.** Observed career data replaces probabilistic outcome modeling per NBA POB design (S119).

### 9. NBA comp (1–3 per evaluation)

| Field | Type | Required | Notes |
|---|---|---|---|
| `comp_player` | string | yes | Full name |
| `comp_archetype` | string | yes | Need not match subject's archetype (cross-archetype flagged) |
| `comp_tier` | enum | yes | `🟢 Full` \| `🟡 Partial` \| `🔴 None` |
| `similarity` | string | yes | Narrative |
| `anchor_season` | string `YYYY-YY` | yes | E.g. `2018-19` |
| `anchor_age` | int | yes | Subject's age-comparable |
| `anchor_ts_pct` | float | yes | Primary signal |
| `secondary_signals` | array of `{name, value, delta_pct, within_tolerance}` | yes | Typically USG%, REB%, BLK% |
| `flags` | string[] | optional | E.g. `Older comp >10y per Rule 4`, `S100-F01 BLK% endpoint None`, `Cross-archetype` |

### 10. Quality Checks (QC1–5)

Per scout-output Section 11.

| Field | Type | Required |
|---|---|---|
| `qc1_completeness` | bool | yes |
| `qc2_consistency` | bool | yes |
| `qc3_narrative_integrity` | bool | yes |
| `qc4_projection_coherence` | bool | yes |
| `qc5_source_fidelity` | bool | yes |

### 11. Anchor library row (`docs/anchors/Tier_{N}.md`)

The anchor library is split across per-tier files at `docs/anchors/Tier_{N}.md` (one pipe-delimited table per file, with the same row schema below). The cross-tier index `docs/ANCHOR-LIBRARY.md` carries the per-tier file index, loading policy, and maintenance rules — not row data. The canonical anchor record:

| Column | Type | Required | Notes |
|---|---|---|---|
| `Composite` | float X.XX | yes | Sort key within tier (descending) |
| `Player` | string | yes | Wiki-page-resolvable |
| `Status` | string | yes | Display column. Renders the Player's `career_status` + `injury_note` joined (e.g. `Active — Achilles 5/2025 recovery`). Authoritative split lives on the Player record per §1 |
| `Group` | enum | yes | Guard/Wing/Big |
| `Archetype` | string | yes | |
| `Notes` | string | yes | **Verbatim, load-bearing per W2.** Calibration history, R13 firings, archetype migrations |

### 12. Wiki player page

See [wiki/WIKI-PROTOCOL.md](../wiki/WIKI-PROTOCOL.md). Adds these fields beyond Player + Evaluation:

| Field | Type | Required |
|---|---|---|
| `has_profile` | bool | yes |
| `profile_path` | path \| null | yes | Points to the latest profile in the BRANCH layout (per §10-A): `output/[First_Last]/[YYYY-MM-DD]_profile.md` |
| `last_updated_session` | int \| null | yes |

### 14. Evaluation ledger row (`wiki/evaluations.jsonl`)

Append-only structured longitudinal record per §10-C resolution. Written by Skill 6 (scout-ingest) on every evaluation — both first-time scoring and re-evals. One JSON object per line.

This is the canonical longitudinal data source for the public ratings DB. Anything queryable about "Player X over time" is derivable from this file.

| Field | Type | Required | Notes |
|---|---|---|---|
| `player` | string | yes | Canonical full name (matches Player record) |
| `session` | int | yes | Session number when evaluation ran |
| `eval_date` | date `YYYY-MM-DD` | yes | |
| `composite` | float X.XX | yes | Final post-modifier composite |
| `pre_modifier_composite` | float \| null | yes | If R13 Stage 2 fires, pre-modifier value. Null otherwise. (See §10-H) |
| `pot` | float \| null | yes | Central projection (POT) from profile §9 — NBA POB STEP 3 for vets, prospect POB BLOCK 2 for States 1–3. `null` until profile is recomputed under the current schema. Min/Max intentionally not in ledger per WIKI-PROTOCOL W9 — central projection is the queryable surface; full uncertainty band stays in profile narrative. |
| `tier` | int 1–13 | yes | |
| `archetype` | string | yes | Archetype as of this evaluation — implicit history via successive rows |
| `group` | enum | yes | |
| `position` | string | yes | |
| `rubric_version` | enum | yes | `v3` \| `unknown` |
| `prior_composite` | float \| null | yes | The most recent prior `composite` for this player, if any. Drift = `composite − prior_composite` |
| `prior_archetype` | string \| null | yes | The most recent prior `archetype`, if any. Non-null when archetype migration occurred |
| `profile_path` | string | yes | The dated BRANCH'd profile file: `output/[First_Last]/[YYYY-MM-DD]_profile.md` |
| `research_packet_path` | string | yes | `raw/[First_Last]/[YYYY-MM-DD]_research-packet.md` |

**Append-only invariant:** Rows are never modified or deleted. Corrections require a new row referencing the prior session; the correction-row schema can be specified when the first correction case arises.

### 15. Archetype hub

(Previously §13 in the v1 draft.) See WIKI-PROTOCOL. Aggregates all anchors of one archetype.

| Field | Type | Required |
|---|---|---|
| `archetype` | string | yes |
| `group` | enum | yes |
| `anchor_count` | int | yes |
| `roster` | row[] (composite, tier, player ref, status) | yes — sorted desc by composite |

### 16. Research packet (`raw/[Player]/[YYYY-MM-DD]_research-packet.md`)

Currently informal — Skill 1 produces it but the spec is implicit in the skill file. **The packet structure is not formalized in this draft (§10-I).** Known invariants:

- Filename: `raw/[First_Last]/[YYYY-MM-DD]_research-packet.md`
- Immutable once written (longitudinal record)
- Multiple packets per player allowed (one per re-eval)

---

## ENUMERATIONS

### Group
`Guard` | `Wing` | `Big`

### Position
`PG` | `SG` | `SF` | `PF` | `C` (hyphenated combos allowed: `SG/SF`, `SF/PF`)

### Tier (1–13)
Composite-band-derived. Lower number = higher rating. See [COMPOSITE-SCALE-AND-TIERS.md](COMPOSITE-SCALE-AND-TIERS.md) for the canonical band table.

### Confidence (sub-domain)
`Low` | `Medium` | `Medium-High` | `High`

### Confidence (projection)
`tight` | `moderate` | `wide` — distinct enum from sub-domain confidence. Lowercase per current PROJECTION-OUTPUT-BLOCK.md / NBA-PROJECTION-OUTPUT-BLOCK.md output formats. Applies to both §8a and §8b.

### Comp tier
`🟢 Full` | `🟡 Partial` | `🔴 None` — currently emoji-prefixed. Open decision §10-K. Used in §8a `comp_tier_indicator` (prospect projection) and entity §9 (NBA Comp). NBA vet projection §8b does not carry a comp validation field — comp validation is structurally separate from §8b output.

### Profile type
`Distributed` (most common in v3 anchors) | `Specialist` | other types observed in legacy anchors. Not yet enumerated exhaustively (§10-J).

### Status state (projection)
`1` | `2` | `3` — prospect-only per §8a. NBA vets use §8b which has no `status_state` field; routing is by NBA experience (≥25 NBA games), not by state enum. State 4 is retired (S119).

### Career stage (NBA vet projection — §8b)
`Pre-peak ascending` | `Approaching peak` | `Peak` | `Post-peak` | `Late career`. Per NBA POB Step 1.

### Trajectory (NBA vet projection — §8b)
`Ascending` | `Plateau` | `Declining` | `Recovering`. Per NBA POB Step 2. `Recovering` auto-widens projection confidence to `wide`.

### Rubric version
`v3` | `unknown` (legacy pre-v3 anchors)

---

## TRANSFORMATIONS / DERIVATIONS

These fields are computable from others and should not be the source of inconsistency:

| Derived | From | Definition |
|---|---|---|
| `tier` | `composite` | COMPOSITE-SCALE-AND-TIERS band lookup |
| `tier_band` | `composite` | Same |
| `tier_label` | `tier` | Same |
| `domain.score` | `included` sub-domain scores | Mean (0.1 precision) |
| `profile_shape.strengths` | sub-domain `score` ≥ 7.0 | Filter |
| `profile_shape.liabilities` | sub-domain `score` ≤ 4.9 AND not SZ | Filter |
| `non_negotiables.gate_results` | `position` + sub-domain scores + NON-NEGOTIABLES.md thresholds | Lookup + compare |
| `archetype.structural_zero_set` | `archetype` | DOMAIN-SCORE-ROLE-RELEVANCE.md table |
| `wiki/players/[Name].md` | latest `output/[First_Last]/[YYYY-MM-DD]_profile.md` + ANCHOR-LIBRARY row | Skill 6 (scout-ingest) |
| `archetype_hub.roster` | All Players with that archetype | Filter ANCHOR-LIBRARY |
| `evaluations.jsonl.prior_composite` | preceding row for same player | Lookup most-recent prior |

**Filename canonicalization:** `output/First_Last/YYYY-MM-DD_profile.md` ↔ `wiki/players/First Last.md` ↔ `raw/First_Last/YYYY-MM-DD_research-packet.md`. The space/underscore divergence is per-folder by W5.

---

## VERSIONING

| Dimension | Tracked? | Where | Purpose |
|---|---|---|---|
| `rubric_version` | yes | wiki frontmatter, ledger row | Sub-domain definitions (v3 = current) |
| `rules_version` | **no** | — | R1–R13 scoring rules; promotions/changes (e.g. S99-F01 → R13) drift silently. Open decision §10-L sub-bullet |
| `schema_version` | **no** | — | This spec's own version. Open decision §10-L |

**Anchor library state is intentionally not tagged** (§10-B resolved). The composite at time T is interpretable via the eval's `session` + `eval_date` plus git-blame on `docs/ANCHOR-LIBRARY.md` at that point. The project has a single linear calibration history; tagging would add update friction without adding capability.

---

## RE-EVAL SEMANTICS — target behavior

Post §10-A and §10-C resolution. Target shape:

1. `output/[First_Last]/[YYYY-MM-DD]_profile.md` — **branched dated files** under a per-player directory. Each evaluation produces a new immutable file. Latest = lexicographically last filename. Migration from current flat `output/[First_Last]_profile.md` layout is a one-time relocation (see §10-A migration plan).
2. `raw/[First_Last]/[YYYY-MM-DD]_research-packet.md` — **unchanged** (already branched).
3. `docs/ANCHOR-LIBRARY.md` row — **revised in place** with Notes-column annotation (Davion Mitchell precedent unchanged). Anchor count unchanged on re-eval.
4. `wiki/players/[Name].md` — **overwritten in place** by Skill 6. Frontmatter `profile_path` repoints to the latest dated file.
5. `wiki/evaluations.jsonl` — **append-only structured ledger.** Skill 6 writes one row per evaluation (entity §14). This is the authoritative longitudinal series.
6. `wiki/log.md` — append-only narrative entry per evaluation, unchanged.

**Effect:** Longitudinal series is now query-cheap from `evaluations.jsonl` alone. Per-evaluation deep-dive recovers the full profile from the dated `output/` file. Anchor library state at any point is reachable via `git show <session-commit>:docs/ANCHOR-LIBRARY.md`.

**Skill 5 + 6 contract change:** Skill 5 writes to `output/[First_Last]/[YYYY-MM-DD]_profile.md` (creates the player directory if needed). Skill 6 appends one row to `evaluations.jsonl` and overwrites `wiki/players/[Name].md`. Both skill files need updating once this spec is canonical.

---

## OPEN DECISIONS

§10-F/G/H/K/L resolved S151 (2026-05-06); §10-I and §10-J remain deferred. See per-section entries for detail.

### §10-A. Re-eval persistence model — RESOLVED: BRANCH

**Decision:** Branch dated profile files. Layout: `output/[First_Last]/[YYYY-MM-DD]_profile.md`, mirroring `raw/`. Each evaluation produces a new immutable file. Latest = lexicographically last filename (no symlink or pointer file needed).

**Rationale:** "Make this longitudinal and comparable over time." Prior profile content is preserved in the `output/` layer rather than only reachable via git history. Raw-symmetric directory structure (one folder per player) keeps the file tree predictable.

**Migration completed:** All `output/[First_Last]/` directories created; `wiki/players/` frontmatter, CLAUDE.md output-discipline section, and Skill 5/6 write paths updated.

### §10-B. Anchor library snapshotting — RESOLVED: no version tag

**Decision:** No `anchor_library_version` field. Anchor library state at any point is reachable via `git show <session-commit>:docs/ANCHOR-LIBRARY.md`. The project has a single linear calibration history (no parallel branches), so `session` + `eval_date` already pin you to the exact library state.

**Rationale:** A version tag would add update friction without adding capability. The use cases (drift detection, retrospective comparison) are answered by git plus the §10-C ledger; a redundant field that humans must remember to update on every library shift creates a synchronization liability.

### §10-C. Longitudinal series materialization — RESOLVED: append-only ledger

**Decision:** `wiki/evaluations.jsonl`, written by Skill 6 (scout-ingest) on every evaluation — both first-time and re-evals. One JSON object per line. Schema = entity §14.

**Rationale:** Structured, query-cheap, append-only. Becomes the authoritative longitudinal data source for the public ratings DB. Re-evaluations are not redundant with `raw/` + `ANCHOR-LIBRARY` because those are unstructured / freetext; the ledger is the parseable layer.

**Skill 6 contract addition:** After updating the player wiki page and archetype hub, append one row to `evaluations.jsonl` capturing the schema in §14. If the file does not exist, create it.

### §10-D. Archetype migration across re-evals — RESOLVED via §10-C

**Decision:** Archetype history is captured implicitly in the `evaluations.jsonl` ledger — successive rows for the same player carry their archetype-of-the-time. The `prior_archetype` field on each row makes migrations explicit. No separate `archetype_history[]` field on player wiki pages.

Current state: WIKI-PROTOCOL says "move player across archetype hubs, update both rosters, update anchor_count." Prior archetype is implicit only — not stored anywhere except in git history.

### §10-E. Status field structure — RESOLVED: split

**Decision:** Replace the single `status` string with three fields on the Player record:

- `career_status` — enum: `Active` \| `Retired` \| `Draft prospect`
- `injury_note` — string \| null. Freetext (e.g. `Achilles 5/2025 — active recovery`)
- `draft_class` — int year \| null. Required when `career_status = Draft prospect`; null otherwise

**Rationale:** Makes the public DB filterable (`WHERE career_status = 'Active'` works without losing injury-flagged actives). Concerns are separated cleanly.

**Migration plan:** Batched into the legacy-anchor cleanup sweep already on the roadmap. ANCHOR-LIBRARY's `Status` column becomes a display join (`career_status` + ` — ` + `injury_note`) — Player record holds the authoritative split.

### §10-F. Score precision in serialized form — RESOLVED

**Decision:** Composite stored at `X.XX` (2-decimal). Sub-domain and domain scores stored at `X.X` (1-decimal). All artifacts that consume scores (JSON export, evaluations.jsonl, public profile) preserve exact precision. No int truncation.

**Rationale:** Two-decimal composite is what tier-band placement depends on; one-decimal sub-domain is the rubric's authoritative grain (R14). Truncation loses calibration the system worked to earn.

### §10-G. Section count discrepancy — RESOLVED

**Decision:** Canonical profile structure is §1–§10 main content + §11 Anchor Library Entry. QC1–5 are enforced at Skill 5 write-time as a pre-write gate but **not persisted** in the profile. If a profile lives in `output/`, it passed QC by precondition.

**Rationale:** Resolves the Cooper-Flagg-vs-Tatum/Şengün/Bridges-vs-Turner inconsistency. QC checks add no value to the persisted artifact — they're forensic at best, absent at worst (Turner). Removing them from the saved template makes the profile structure unambiguous and slightly leaner.

**Touched:** `skills/scout-output.md` — drop the QC section from the saved template; QC checklist becomes a pre-write gate. (Edit happens in Phase 3 / Skill 7 work or as a follow-up — flagged here as a contract change.)

### §10-H. Pre-modifier composite preservation — RESOLVED

**Decision:** Preserve `pre_modifier_composite` as a structured nullable field on the Composite Rationale entity (§7) and on the Evaluation ledger row (§14). Null when R13 Stage 2 does not fire.

**Rationale:** Already wired in §14 ledger schema. Promoting from "Recommendation" to "Decision" makes the contract explicit. Enables a future "playoff context" view at the public DB layer if/when frontend wants to expose it; does not require it.

**Bridges precedent reference:** `pre_modifier 7.95 → final 7.85` (R13 Stage 2 −0.10) — the canonical example of why this field needs to persist.

### §10-I. Research packet schema — DEFERRED to workstream 2

`raw/[Player]/[YYYY-MM-DD]_research-packet.md` shape is currently informal. For the pipeline cost spike (workstream 2), the packet shape needs to be formalized so token cost can be measured per-section.

**Recommendation:** Defer to workstream 2 — formalize alongside cost measurement, then back-port to this spec.

### §10-J. Profile type enumeration — DEFERRED

`Distributed` is the only profile type observed in v3 anchors. Legacy anchors may use other labels. The full enumeration is not yet authoritative.

**Recommendation:** Audit during legacy-anchor cleanup; defer enum-locking.

**Publishable-layer note:** `profile_type` is not a public field in the v1.0 publishable layer (per S151 plan). Full enum audit deferred to legacy-anchor cleanup; closure is not a publishable-layer blocker.

### §10-K. Comp tier glyph vs text — RESOLVED

**Decision:** Storage form is text enum: `Full` | `Partial` | `None`. Emoji are presentation-layer only. Existing markdown profiles keep their emoji prefixes; the JSON export pipeline strips emoji at parse time and stores text. New profiles may continue using emoji in markdown for human scannability.

**Rationale:** Emoji break greppability, JSON serialization, and accessibility. Text storage with optional emoji presentation is the standard pattern. Migration is zero-cost (parser handles both forms).

### §10-L. Schema and rules versioning — RESOLVED

**Decision:** This spec is `schema_version: "1.0"` as of canonical promotion. Two version fields propagate to artifacts:
- `schema_version` (string, semver-style) — pins the artifact to a specific SCHEMA-SPEC version. Required on all JSON exports and all new evaluations.jsonl rows.
- `rules_version` (string, e.g. `"R1-R15 / S151"`) — pins the artifact to a specific SCORING-RULES.md state. Required on all JSON exports and all new evaluations.jsonl rows.

**Migration:** Existing ledger rows lack both fields — write `null` rather than back-fill (append-only invariant per §10-C). Future schema changes follow semver: minor for additive (v1.1), major for breaking (v2.0).

---

## NON-GOALS

- This spec does not redesign existing artifacts. It formalizes them.
- This spec does not specify the public ratings site's UI or routes.
- This spec does not specify pipeline / queue / retry semantics — that is workstream 3.
- This spec does not formalize the rubric, scales, or scoring rules — those are upstream documents (`docs/SUB-DOMAINS_v3.md`, `docs/POSITION_SCALE_*.md`, `docs/SCORING-RULES.md`).

---

*Created Session 109 (2026-04-25). Workstream 1 of the backend foundation track (workstream 2 = pipeline cost spike, workstream 3 = pipeline design). §10-A/B/C/D/E resolved S109 (2026-04-26). §10-F/G/H/K/L resolved S151 (2026-05-06) as part of the publishable-layer phase. §10-I and §10-J remain deferred. Canonical v1.0 promoted 2026-05-06.*
