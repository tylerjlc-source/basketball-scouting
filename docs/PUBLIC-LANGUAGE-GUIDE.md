# PUBLIC LANGUAGE GUIDE

Editorial transform spec consumed by Skill 7 (`scout-publish`) to convert an `output/[Player]/[YYYY-MM-DD]_profile.md` into the public-facing `_public.md` artifact that feeds the JSON export pipeline.

**Status:** Canonical v1.0 — created S151 (2026-05-06) as Phase 2 of the publishable layer.

**Load scope:** Loaded by `skills/scout-publish.md` only. Not session-open. Not loaded by Skills 1–6. Single-skill consumer per [ARCHITECTURAL_PRINCIPLES.md](ARCHITECTURAL_PRINCIPLES.md) P1.

**Cross-references (do not duplicate):**
- Numeric precision is preserved verbatim per [SCHEMA-SPEC.md §10-F](SCHEMA-SPEC.md).
- Single-game evidence prohibition per [SCORING-RULES.md R15](SCORING-RULES.md). Stripped at publish time even when upstream profile retains a single-game reference.
- Sub-domain Signature names, tiers, descriptions, and assignment rules per [SIGNATURES.md](SIGNATURES.md). Signatures are derived at publish from the byte-equal sub-domain scores; this guide does not redefine them.

---

## Contents

- §1 — Purpose
- §2 — Preserved (QC5 source-fidelity)
- §3 — Stripped
- §4 — Pull policy and per-element rewrites — §4-A pull policy / §4-B per-element rewrites
- §5 — Structure and voice — §5.1 structural template / §5.2 voice register / §5.3 universal operational rules / §5.4 calibration targets (reviewer-only)
- §6 — Anchor comp handling
- §7 — One-line domain justification format
- §8 — QC checklist (Skill 7 pre-write gate)
- §9 — Career stats appendix — §9.1–§9.5

Skill 7 LOADING (per [skills/scout-publish.md](../skills/scout-publish.md)) reads §§1–§4 + §5.1 + §5.2 + §5.3 + §6 + §7 + §8 + §9 upfront. **§5.4 is reviewer-only** — load on demand if Step 3-T surfaces a voice-question the rules section cannot answer.

---

## §1 — Purpose

Every public profile is the same product: a structured 4-paragraph narrative plus byte-equal numeric scores. The internal profile contains scoring scaffolding (R-codes, cap notes, override sequences, session IDs) plus calibration sections (profile shape, non-negotiables gate, composite rationale, anchor library entry, QC) that must not reach the public surface. Per S174-F02, narrative prose authorship defaults to Tyler; Claude assembles structured fields (sub-domain rationales, domain one-lines, projection prose, comp prose) and pulls selectively per §4-A. Numeric scores pass through byte-equal.

---

## §2 — Preserved (QC5 source-fidelity)

These pass through byte-equal from `_profile.md`:

- All numeric scores: composite, sub-domain (×26), domain (×8), projection POT/Min/Max, percentages.
- All sub-domain ids and names (per `SUB-DOMAINS_v3.md`).
- Profile shape lists: `strengths`, `liabilities`, `below_strength`.
- Tier number, tier label, archetype name, comp player names + comp tier (`Full` | `Partial` | `None`).
- Projection band: confidence, spread.

Numeric drift between `_profile.md` and `_public.md` is a pipeline failure caught at Phase 4 stage 2 (fail-loud).

---

## §3 — Stripped

Skill 7 removes from the published narrative:

- **R-rule cite codes:** `R1`, `R13 Stage 2`, `R8 override`, etc.
- **Session cite codes:** `S102-F03`, `S119`, `S96-F02`, etc.
- **Internal abbreviations:** `SZ`, `CAPPED by #22`, `#5→#24 cap applied`.
- **Composite-rationale internal fields:** `caps_considered`, `empirical_overrides`, `self_correction_sequence`. The narrative justification of `pre_modifier_composite` is stripped; the number itself persists in JSON for transparency.
- **Tier vocabulary at the public surface:** "Tier N", "All-NBA caliber", "the tier", "franchise piece" used as system-rubric labels. Plain credential references ("All-NBA First Team", "All-Star") are kept; system-register vocabulary is stripped. The reader should see the player, not the rubric.
- **System-internal cross-player comparisons in prose:** comparisons of the form "X-efficient", "better than Y on Z", "not as good as W at [skill]" woven into the narrative as triangulation. Cross-player anchoring belongs in §10 NBA Comp, not in the 4-paragraph narrative. Plain-language references to a player ("in the territory of Kawhi Leonard at his peak") are kept where they ground a projection; system-triangulation comparisons ("score-first but not Curry-efficient") are stripped.
- **System recency-window framing AND its weighted-blend numbers:** "eval window", "within recency", "recency-window", "two-season evaluation window", "current 2-year cycle" — internal calibration vocabulary, stripped. The 60/40 weighted-blend stat values themselves are also stripped — narrative numbers must carry a reconcilable temporal frame per §5.3 (single named season, two-season raw aggregate with raw counts + "since [year]", or career-aggregate row from the appendix). Reframe as plain context — "the 2024 championship", "this season", "the prior year" — anchored to data the reader can verify.
- **Single-game references** per [SCORING-RULES.md R15](SCORING-RULES.md). Stripped at publish time regardless of upstream state. The narrow exception is a clutch moment in a championship-deciding game (Finals Game 6 / Game 7 close-out, or a game directly clinching the title); conference-finals, first-round, and regular-season single games never qualify.
- **QC1–5 markers** (already absent from canonical profiles per SCHEMA §10-G; defensive strip if present in legacy artifacts).

---

## §4 — Pull policy and per-element rewrites

### §4-A — Pull policy

Skill 7 reads the source `_profile.md` selectively. Profile sections map to public output as follows.

| Profile § | Pull? | Form in public artifact |
|---|---|---|
| §1 Header | Yes | Structured fields (name, group, position, archetype, composite, tier, eval_date) |
| §2 Physical profile | Yes | Absorbed into Identity paragraph as prose; height, wingspan, weight only |
| §3 Scouting narrative | Yes — rewritten | Source for the 4-paragraph Vecenie restructure (§5.1) |
| §4 Sub-domain scores | Yes | Numbers + names byte-equal; rationales rewritten per §4-B; Signature column derived from score per [SIGNATURES.md](SIGNATURES.md) |
| §5 Domain summaries | Yes | Numbers + names byte-equal; one-line justification per §7 |
| §6 Profile shape | **No** | Internal calibration scaffolding |
| §7 Non-negotiables gate | **No** | Internal calibration scaffolding |
| §8 Composite rationale | **No** | Absorbed by Vecenie verdict paragraph (§5.1) — no standalone rationale in public artifact |
| §9 Projection | Yes — narrow | POT/Min/Max + confidence; prospects (States 1–3) also Bust/Avg/Boom. Drop: modifier stack, status_state, divergence_flag, trajectory scaffolding |
| §10 NBA Comp | Yes | Comp player + comp tier text + similarity prose ≤2 sentences. Drop: anchor_season, anchor_age, anchor_ts_pct, secondary_signals |
| §11 Anchor library entry | **No** | Internal artifact (lives in [ANCHOR-LIBRARY.md](ANCHOR-LIBRARY.md)) |
| QC1–5 | **No** | Already absent from canonical profiles per [SCHEMA-SPEC §10-G](SCHEMA-SPEC.md) |

### §4-B — Per-element rewrite rules

| Element | Public form |
|---|---|
| Sub-domain rationale | ≤1 sentence, ≤30 words. Numbers in numerical form ("40.7%", "85th percentile"), not word form. Every numeric carries a reconcilable temporal frame per §5.3 — single named season, two-season raw aggregate with counts + "since [year]", or career-aggregate row. The 60/40 weighted blend as a flat unmarked number is forbidden. |
| Sub-domain Signature column | `[Signature Name] ([Tier])` when sub-domain score ≥ 8.0; `—` otherwise. Name and tier deterministic from score per [SIGNATURES.md](SIGNATURES.md) §3–§4. Never editorialized; reconciliation is fail-loud at JSON export. |
| Domain synthesis | ≤1 sentence per domain. One-line justification format per §7. |
| Projection narrative | ≤2 sentences. POT/Min/Max preserved; `pot_modifier_stack` rationale strings translated to plain language ("elite competitive character" stays, "+0.40 modifier" goes). Verdict-bound language modulates with Max POT: within ~0.10 of the next-tier credential floor (e.g., 8.85 All-NBA, 7.90 All-Star), use "unlikely to become" + structural-gap-as-problem-to-solve framing rather than definitive "will not become" bounds. |

---

## §5 — Structure and voice

Two concerns: structural template enforced at publish (§5.1); voice register externalized to [validation/PUBLIC-VOICE-CALIBRATION.md](validation/PUBLIC-VOICE-CALIBRATION.md) (§5.2 cross-ref). Universal operational rules apply regardless of voice (§5.3). System-output calibration target (§5.4).

### §5.1 — Structural template (Sam Vecenie)

Fixed 4-paragraph public narrative shape, identical for every player:

1. **Identity** — what this player is, in plain language. Archetype, physical profile, headline credentials.
2. **Strength evidence** — the value drivers, anchored to numbers and observed pattern.
3. **Weakness evidence** — the gaps, named directly. Not buried, not softened.
4. **Projection-verdict** — realistic floor, realistic ceiling, what they will and will not become.

Same shape every profile. Solves consistency across 30+ launch profiles.

### §5.2 — Voice register

[PUBLIC-VOICE-CALIBRATION.md](validation/PUBLIC-VOICE-CALIBRATION.md) holds writer exemplars (Lowe, Tjarks, Mann, etc.) as reference inspiration for understanding the pro NBA writing register. Per S174-F02, the system's actual published-output target lives in §5.4 below: Tyler-authored prose, not Lowe-imitation. Claude does not attempt to reproduce upstream exemplars at sentence level; that path failed across four iterations on Mitchell.

Skill 7 carries the system's internal posture to the public surface, not the source's. Ambiguity resolves DOWN (C4); the Negative Balance Rule applies. No softening at publish.

### §5.3 — Universal operational rules

- Numbers in numerical form ("40.7%", "6'10\"", "9.02"). Source-profile precision preserved byte-equal.
- No em dashes in narrative prose. Use commas, semicolons, periods. Em dashes were tested in v4-rev2 and produced stilted prose; see S174-F02.
- No source attribution. Never "scouts say", "according to ESPN", "reports indicate", "the consensus view", "analysts have noted".
- No single-game references (per R15, see §3).
- Factual claims must trace to source profile §1–§5 / §9 / §10. No extrapolation beyond the profile's stated framing. Cross-check before publish (PUBLIC-RUBRIC §8).
- No overclaiming team state on individual action. Team success / standing / record is not attributed to a single player's named action ("Cleveland finished with the best record in the East with him running the pick-and-roll" overclaims).
- One subject per paragraph. No bullet lists inside the published narrative; bullets belong in structured fields, not prose.
- Acronyms and jargon translated inline at first use. Non-intuitive metric acronyms — DFGPOE, PPP, A:TO, FTR, OREB%, DREB%, TS%, USG, TOV/100 — render as plain language: "holds opponents X% below their expected field-goal percentage" (DFGPOE), "points per possession" (PPP), "assist-to-turnover ratio" (A:TO), "free throws per field-goal attempt" (FTR), "offensive/defensive rebound rate" (OREB%/DREB%), "true shooting" (TS%), "usage" (USG). Public-facing language carries no internal shorthand. First-use applies per structured-field group: sub-domain rationale tables, domain one-line tables, and comp tables that scan standalone re-expand at the first occurrence within the group, even when the narrative has already established the acronym upstream. Credential acronyms (DPOY, MVP, FMVP) follow the same rule in structured-field rows.
- Raw counts beat opaque rate units. When a stat's unit isn't named-and-recognizable (per-game, percentage, raw count), reach for the raw form first. "TOV/100 touches at 5.0" is opaque; "220 turnovers in 71 games" is not. The unit must communicate magnitude without the reader doing math.
- Dormant-vet verdict-opener tense. When a player is currently injured or sidelined at publish time, the Projection-verdict opener frames him as he is today, with past-tense reference to season disruption ("Jackson is a recent-vintage All-Star Switchable Big who missed time due to knee injury during the 2025-26 season"). Avoid in-progress "currently out for [year]" framing; by publish time the regular season is past, not in-progress. Anchor today's reading state, not the upstream profile's snapshot moment. Applies to any R13-dormant or active-injury vet.
- **Reconcilable temporal frame on every narrative number.** Every percentage and granular split in narrative + sub-domain rationale carries a temporal frame the reader can reconstruct against visible data. Three legitimate forms:
  - **Single named season** — "40.7% on 343 attempts in 2025-26". Reconciles to a row in the `## Career stats` appendix (per-season row) or to `current_season` / `prior_season` in the Step 1.8 payload (granular splits the appendix doesn't show).
  - **Two-season raw aggregate** — "251 of 623 since 2024-25". Sum/sum across both seasons (the `two_season_aggregate` view in Step 1.8). Must include raw count and explicit "since [year]" boundary so the reader can mentally check by adding the two season rows.
  - **Career-aggregate row** — "career 39.4%". Reconciles to the bolded **Career** row in the `## Career stats` appendix. Basic per-game stats only (PPG, REB, AST, FG%, 3P%, FT%); granular career aggregates (career CAS 3PT%) are not surfaced and should not be cited.
  - **Forbidden** — the 60/40 weighted blend cited as a flat number with no temporal frame ("40.7%" with no season label, no raw count, no "since" frame). The weighted blend is the scoring substrate (S83, locked) and stays internal; the public surface anchors to single seasons or raw aggregates. Aggregate ≈ weighted within ~0.5% in typical cases — well inside R14 dial tolerance — so the reader sees a defensible reconcilable number that matches what the score is calibrated against.
  Default emphasis: most-recent season. Two-season aggregate is preferred for advanced/sample-sensitive stats (DFGPOE, drives, contested-shot splits) where current-season alone is too thin. Career framing is for trajectory-spanning claims where the appendix career row is the source.

### §5.4 — Calibration targets: Mitchell (healthy-vet) and Jackson (dormant-vet) samples

> **Pre-pivot status (2026-05-09):** The samples below predate the single-season-anchor pivot and cite eval-window-weighted numbers without explicit temporal frames (e.g., "40.7% on 623 attempts" is a 2-season weighted blend, not a single season). They remain the structural calibration target (4-paragraph shape, voice register, Identity → Strength → Weakness → Projection-verdict) but the **numbers** in these samples violate the new §5.3 reconcilable-temporal-frame rule. Slated for replacement: Curry (healthy-vet) replaces Mitchell post-Wave-2 publish; Jackson dormant-vet sample re-issued under the new policy on next JJJ republish. See plan: `~/.claude/plans/we-need-to-address-staged-reddy.md`.

The sample below is the system's published-output target: what the 4-paragraph narrative in `_public.md` should read like. Tyler-authored per the S174-F02 pivot; replaces the prior Duren v2 sample (which used em dashes and prose-form numbers, both since prohibited per §5.3). Each paragraph is labeled with its structural role. Numbers are numerical; em dashes are absent; physical attributes appear once (Identity); team state is not attributed to a single player's named action.

```
[Identity] Donovan Mitchell is a player on the cusp of greatness. A 7x All-Star, a 1st Team All-NBA nod, and an elite offensive engine in both the regular season and playoffs. The question is whether or not he crosses the threshold. At 6'1"/215lbs, Mitchell's length (6'10" wingspan) sneaks up on defenses. His strength is underrated, leading to body control that allows him to score efficiently at the rim.

[Strength] Offensively, Mitchell profiles as a 3-level, efficient scorer. His Catch-and-shoot 3PT at 40.7% on 623 attempts is elite volume-plus-conversion. This, combined with efficient mid range game and an above average conversion at the rim, showcase a player well within the top 10 offensive contributors league wide. A high usage pick and roll ball handler, with serviceable playmaking means Mitchell can act as a primary creator. He is a crafty, smooth athlete who has found a niche at the highest level of competition.

[Weakness] Defensively, Mitchell is not elite but functional. Given his offensive contribution, his defense is more than serviceable. However, for Mitchell to reach his full potential, the defense needs to show up against elite level talent in later playoff rounds. A player with his length, frame, and athleticism possesses the capacity to defend the best guards in the league at a high level. That is his next step.

[Projection-verdict] A perennial All-Star linked with Devin Booker as the top Shooting Guard in the league. The ceiling is multiple All-NBA calls and a fringe chance at an MVP season if everything falls just right. Mitchell is good enough to anchor a championship team and is at the point in his career where he needs to show it.
```

**Dormant-vet verdict variant — Jackson sample (2026-05-02):**

Applies the §5.3 dormant-vet verdict-opener tense rule and the §4-B Max-POT-aware verdict-bound register (Jackson's Max POT 8.90 sits within 0.10 of the All-NBA credential floor, so "unlikely to become" + structural-gap-as-problem-to-solve framing replaces definitive "will not become"). Identity / Strength / Weakness follow the Mitchell template; only the Projection-verdict differs structurally.

```
[Projection-verdict] Jackson is a recent-vintage All-Star Switchable Big who missed time due to knee injury during the 2025-26 season. The character signals are durable: vocal locker-room leadership through the post-Bane Memphis era, USA Basketball commitments through team-level adversity. The projection waits on proof-of-return from the knee. The realistic ceiling is a return to the 2024-25 baseline: All-Star regular, All-Defensive Team defender on healthy minutes. Jackson is unlikely to become an All-NBA player; the lean frame and structural rebounding gap will need to find a solution for him to reach his upside potential.
```

---

## §6 — Anchor comp handling

- **Player names** used as comps stay verbatim. They are the public reference points readers debate and share ("the realistic floor is prime Andre Drummond"). Source of truth: [ANCHOR-LIBRARY.md](ANCHOR-LIBRARY.md).
- **Internal-cite anchors** (`Bridges precedent`, `Davion Mitchell precedent`, `S102-F03 anchor sweep`) are rewritten to plain language ("similar pattern to Mikal Bridges' playoff-shrink case") or stripped entirely if not load-bearing for a public reader.
- Misspelled anchor names are a Phase 4 stage 4 fact-extraction failure — Skill 7 is first-line check.

---

## §7 — One-line domain justification format

Per [PRODUCT_DESIGN_DECISIONS_v9.md §9](PRODUCT_DESIGN_DECISIONS_v9.md), every domain grade includes a one-line justification.

**Template:**
```
{Domain}: {score} — "{one-sentence justification, ≤25 words}"
```

**Rules:**
- Lead with the strength or the gap, not both.
- One affirmative clause + one balancing clause maximum.
- No semicolons inside the justification. No parentheticals. No R-codes.

**Worked examples (PDD v9 §9, verbatim):**
- Shooting: 7.2 — "Reliable catch-and-shoot option from the corners; off-dribble creation remains inconsistent"
- Defense: 8.1 — "Elite on-ball defender; help-side awareness needs development at NBA level"

---

## §8 — QC checklist (Skill 7 pre-write gate)

Run against the draft `_public.md` before saving. All seven must pass.

1. **Synthesis, not plagiarism.** No scout phrasing reproduced verbatim from the research packet.
2. **No cite codes.** Grep for `R\d`, `S\d{2,3}`, sub-domain id refs (`#\d{1,2}`), override flags.
3. **No internal flag language.** `CAPPED`, `SZ`, `structural zero`, `ambiguity flag`, `flagged`.
4. **Score numbers byte-equal to source.** Sub-domain (×26), domain (×8), composite, tier, projection POT/Min/Max/confidence preserved verbatim from `_profile.md`. Phase 4 pipeline enforces; Skill 7 is first-line check. **Carve-outs:** (a) numbers in the `## Career stats` appendix (§9) are independently sourced via Step 1.7 from `nba_api`/web-fallback and NOT compared against `_profile.md` (cross-check: career row reconciles against per-season rows for GP and PTS); (b) granular percentages and raw counts in narrative + sub-domain rationale come from Step 1.8's per-season + two-season-aggregate payload (or the §9 appendix) and are NOT compared against profile §3/§4 weighted figures. The substrate stays weighted internally; the public surface anchors to single seasons or raw aggregates per §5.3.
5. **R15 compliance.** No single-game references except championship-deciding clutch (per §3).
6. **Vecenie structure present.** Exactly four paragraphs, in Identity → Strength → Weakness → Projection-verdict order.
7. **Reconcilable temporal frame** (per §5.3). Every percentage and granular split in narrative + sub-domain rationale traces to one of: (a) a row in the `## Career stats` appendix, (b) `current_season` or `prior_season` in the Step 1.8 payload, or (c) the Step 1.8 `two_season_aggregate` framed with raw counts and explicit "since [year]" boundary. The 60/40 weighted blend as a flat number with no temporal frame is a fail. Regex first pass: any granular percentage with no adjacent season label, no raw count, and no "since" frame, that does not match a Career stats career-aggregate row, fails. Defense-in-depth check in `lint_profile.py` (flag-only on Wave-2 backfill, promotes to block-on-fail thereafter).

---

## §9 — Career stats appendix

Reference appendix appended to every NBA-vet and college-prospect public profile. Independently sourced at publish time; numbers do not pass through Skill 5 / Skill 6 and are NOT byte-equal-checked against `_profile.md` (carve-out per §8 QC4).

### §9.1 — Placement

Appended after `## NBA Comp(s)` as the final section of `_public.md`. Editorial choice: factual reference reads cleanly after the editorial product (narrative + scores + comps), mirroring the NBA.com page sequence (bio → narrative → stats).

### §9.2 — Format

- H2 heading: `## Career stats`
- H3 sub-section heading: `### Regular Season` (NBA vet) or `### College career` (college prospect)
- H3 sub-section heading: `### Playoffs` (NBA vet only) when `CareerTotalsPostSeason` is non-empty
- Each sub-section contains one markdown table — columns in this order: `Season`, `Team`, `GP`, `GS`, `MIN`, `PTS`, `REB`, `AST`, `STL`, `BLK`, `TOV`, `FG%`, `3P%`, `FT%`
- Career row bolded across every cell using `**…**`. The Season cell reads `**Career**`; the Team cell is empty for the bolded career row.

### §9.3 — Numeric format

- PerGame stats (`MIN`, `PTS`, `REB`, `AST`, `STL`, `BLK`, `TOV`) to 1 decimal: `27.1`, `7.5`, `0.7`. NBA.com convention.
- Percentages (`FG%`, `3P%`, `FT%`) to 3-decimal `.XXX` form with leading zero stripped: `.468`, `.346`, `.737`. Matches NBA.com convention. **Different from §5.3 in-narrative form** (`46.8%`) — the appendix is a reference table, not narrative prose.
- `GP`, `GS` as integer counts.
- Missing values render as `-` (single hyphen).

### §9.4 — Omission rules

- **HS profiles:** omit the entire `## Career stats` section. No heading, no empty placeholder.
- **College prospect with no source-table available** (web-fallback failure): omit the entire section. Log informational omission in the Phase B manifest.
- **NBA vet with empty `CareerTotalsPostSeason`** (never made playoffs): include `### Regular Season` only; omit the `### Playoffs` sub-section.

### §9.5 — Source

**Career stats appendix** (this section's table):
- **NBA:** `scripts/Public_Career_Stats.py` wrapping `nba_api.PlayerCareerStats` with `per_mode='PerGame'`. Trade-aware: TOT row used for season totals when present; team display joins non-TOT abbreviations with `/`.
- **College:** Skill 1 sub-agent (Sonnet 4.6) web-search of Sports-Reference college career table. Sub-agent emits markdown + structured JSON matching the same row schema (team = school name).

**Narrative + sub-domain rationale granular splits** (CAS 3PT%, mid-range%, rim FG%, OREB%, drives, etc. — metrics the appendix doesn't show):
- **NBA:** `scripts/Public_Narrative_Stats.py` orchestrates the 7 Skill-1 domain scripts as parallel subprocesses at publish time. Walks each script's `sb()`-shaped JSON output and emits three views per metric: `current_season`, `prior_season`, `two_season_aggregate` (sum/sum from raw counts, NOT the 60/40 weighted blend). The scoring substrate stays weighted; the publish-time payload is a separate display lens. Aggregate makes are reverse-computed from `pct × volume` (the source JSONs persist volume but not raw makes), introducing ±1 make of rounding error per season → ±0.1–0.5% drift on the aggregate value, well inside R14 dial tolerance.
- **College:** Skill 1 sub-agent fallback (Sonnet 4.6); coverage may be partial since Sports-Reference college tables don't expose all NBA-API metrics.
- **HS / web-fallback failure:** Step 1.8 emits an "omitted (no source)" flag. Narrative falls back to qualitative-only claims; specific percentages are not cited.

Both sources are independently sourced at publish time and are NOT byte-equal-checked against `_profile.md` (carve-outs per §8 QC4-(a) and §8 QC4-(b)).

---

*Created S151 (2026-05-06) as Phase 2 of the publishable-layer track. Phase 3 builds Skill 7 (`skills/scout-publish.md`) which loads this guide; Phase 4 builds the JSON export pipeline that consumes Skill 7's output. S175 pivot (2026-05-07): narrative authorship moves to Tyler; Claude assembles structured fields. §5.4 calibration sample replaced (Duren v2 → Mitchell). §5.3 universal rules updated (numerical numbers, em-dash prohibition, factual-trace, no overclaiming). See [docs/learnings/scout-publish-learnings.md](learnings/scout-publish-learnings.md) S174-F02. S177 Wave 1 retrospective (2026-05-07): §5.4 extended with Jackson dormant-vet verdict-paragraph variant alongside Mitchell healthy-vet sample, closing the S176-F02 deferred-until-JJJ-publish-exists trigger; two-anchor calibration set in place for Wave 2+. **Single-season-anchor pivot (2026-05-09):** §5.3 reconcilable-temporal-frame rule + §3 weighted-blend strip + §4-B per-element constraint + §8 QC7 + §9.5 narrative-stats source added. Inverts the prior eval-window-weighted-narrative policy. Curry (Wave 2) becomes the new §5.4 healthy-vet calibration sample post-publish; Mitchell + JJJ + Kawhi backfill in sequence under the new rule. See plan: `~/.claude/plans/we-need-to-address-staged-reddy.md`.*
