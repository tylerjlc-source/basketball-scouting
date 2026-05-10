---
name: scout-publish
description: "Generate the public-facing editorial version of a completed player profile. Reads the latest output/[Player]/[YYYY-MM-DD]_profile.md, applies pull policy and voice transforms per docs/PUBLIC-LANGUAGE-GUIDE.md, and writes output/[Player]/[YYYY-MM-DD]_public.md. Manual-only trigger: 'publish [Player]'. Editorial step — never modifies scores, structure, or upstream artifacts. Output feeds the JSON export pipeline (Phase 4)."
---

# Skill 7 — Scout Publish

**Job:** Editorial transform — produce the public-facing `_public.md` from the canonical `_profile.md`. One player per invocation.
**Position in chain:** Seventh, manual-trigger only. Parallel branch from Skill 5; does not depend on Skill 6.
**Output:** `output/[Player_Name]/[YYYY-MM-DD]_public.md` (BRANCH-symmetric per SCHEMA-SPEC §10-A).

---

## LOADING INSTRUCTIONS

Loads execute as a single parallel batch in Phase A — see P8.

Always load:
1. **This file (SKILL.md)** — publish workflow, pull policy reference, QC checklist
2. **docs/PUBLIC-LANGUAGE-GUIDE.md** — transform spec. Surgical read — load §§1–§4, §5.1, §5.2, §5.3, §6, §7, §8, §9 (everything except §5.4 calibration sample). The §5.4 calibration sample is deferred to the reviewer sub-agent (Step 3-C / Subagent V) and loaded on-demand by Step 3-T only if the draft surfaces a voice question that the truncated guide cannot answer.
3. **docs/validation/PUBLIC-VOICE-CALIBRATION.md** — voice spec. Surgical read — load **only** §8 (Patterns Across the Best of Them), §9 (Pitfalls to Avoid), §10 (Ranked Voice Recommendation). The writer-exemplar excerpts §§1–7 are heavy and load only inside the reviewer sub-agent's context (it gets the calibration evidence; the writer gets the codified rules and pitfalls).
4. **docs/SIGNATURES.md** — Signature roster, tiers, descriptions, and assignment rules. Loaded for Step 3 sub-domain Signature column derivation (universal, runs every invocation).

Inputs required (must already exist):
5. **output/[Player_Name]/[YYYY-MM-DD]_profile.md** — the canonical Skill 5 deliverable. Locate the latest by listing the directory and taking the lexicographically last filename. Read fully.

**NOT loaded** (P1 enforcement):
- `docs/SCORING-RULES.md` — scores pass through byte-equal; rules unused at publish time
- `docs/SUB-DOMAINS_v3.md` — names byte-equal from profile; definitions unused
- `docs/POSITION_SCALE_*.md` — scoring scales unused at publish time
- `docs/ANCHOR-LIBRARY.md` + `docs/anchors/Tier_*.md` — anchor names pass through; library not consulted
- `docs/ARCHETYPE-WEIGHTS-*.md` — archetype name byte-equal from profile
- `docs/DOMAIN-SCALE_v1.md` and `docs/DOMAIN-SCORE-ROLE-RELEVANCE.md` — only consumed by the Step 1.5 recompute-gate **sub-agent**; main Skill 7 context never loads them. See Step 1.5 below.

If the profile is missing, stop and flag — do not synthesize from memory.

---

## EXECUTION PATTERN — PHASE-BATCHED

The workflow steps below cluster into **3 execution phases. Each phase runs in a single turn** — see P8.

| Phase | Steps | Turn shape |
|---|---|---|
| A | 1–3.5 (Locate, recompute gate, career-stats pull, narrative-stats pull, validate, assemble, lint pre-flight, scout-review handoff) | One turn — parallel reads (this file + PUBLIC-LANGUAGE-GUIDE + PUBLIC-VOICE-CALIBRATION + SIGNATURES + profile) plus the Step 1.7 career-stats Bash call AND the Step 1.8 narrative-stats Bash call (both parallelize with reads — player name is the only input on each). Step 1.5 marker pre-check runs in-line on the loaded profile; if the marker is absent, a recompute-gate sub-agent fires with its own context (DOMAIN-SCALE_v1 + DOMAIN-SCORE-ROLE-RELEVANCE never enter the main window). Validate, then Step 3-T (Tyler-iterated path) OR Step 3-C → 3.4 (cheap lint pre-flight) → 3.5 (invoke `scout-review` sub-skill — V + F parallel + revise-against-V happen inside scout-review's context, not here). Structured fields are always Claude-assembled regardless of narrative path. |
| B | 4 (Diff manifest preview) | One turn, no tools — present manifest to Tyler. |
| — | (Approval gate) | Tyler confirms. |
| C | 5–7 (Write, QC, confirmation) | One turn — single Write call + QC analysis + confirmation in same response. |

**Three turns total per publish is the budget.** Per S174-F02, narrative authorship defaults to Step 3-T (Claude drafts → Tyler edits → Claude redrafts the final); Step 3-C (Claude-only, no Tyler edit) is the fallback when Tyler does not engage the edit loop.

---

## PUBLISH WORKFLOW

### Step 1 — Locate and load (Phase A entry)

**This step initiates Phase A — issue all loads from LOADING INSTRUCTIONS items 1–5 in parallel within a single response.** (DOMAIN-SCALE_v1 / DOMAIN-SCORE-ROLE-RELEVANCE are NOT in this batch; they live only in the Step 1.5 sub-agent's context if it fires.)

Confirm via Phase A reads:
- `output/[Player_Name]/` directory exists with at least one dated profile (`[YYYY-MM-DD]_profile.md`).
- Latest profile = lexicographically last filename (same logic as Skill 6 Step 1).
- No existing `[YYYY-MM-DD]_public.md` for the same date — if one exists, stop and flag (P6).

### Step 1.5 — Domain-mechanic recompute gate (Phase A continued)

**Universal — every publish invocation runs this gate.** The band-match mechanic (DOMAIN-SCALE_v1.md, shipped 2026-05-07) replaced arithmetic-mean domain derivation. Profiles built before that date use arithmetic means in §5; the public layer cannot ship arithmetic-mean domains alongside band-matched composites without breaking score-coherence.

**Marker pre-check (in-line, no extra load).** Skill 7 already loaded the profile in Step 1. Scan it for the line:
`Domain-mechanic recompute: arithmetic mean → band-match per DOMAIN-SCALE_v1.md`
appearing in any dated footer entry.

- **Marker present →** skip the gate entirely. Profile already on band-match. No sub-agent fires; no DOMAIN-SCALE_v1 / DOMAIN-SCORE-ROLE-RELEVANCE load happens. Proceed to Step 2.
- **Marker absent →** spawn the recompute-gate sub-agent (below). The two reference docs load only inside the sub-agent's isolated context window; the main Skill 7 turn never carries them.

**Sub-agent: recompute-gate.** Spawn via the Task tool. Prompt lives at [docs/subagent-prompts/recompute-gate.md](../docs/subagent-prompts/recompute-gate.md) — load that file and pass its prompt block verbatim to the Task tool, substituting the absolute profile path into `{ABSOLUTE_PATH_TO_PROFILE_MD}`. Inputs handed to the sub-agent: the absolute path to the source `_profile.md`. The sub-agent reads profile + DOMAIN-SCALE_v1 + DOMAIN-SCORE-ROLE-RELEVANCE, edits the profile in place, and returns a confirmation summary listing per-domain old → new scores, credentialed-star carve-out status, and the footer line written.

**After the sub-agent returns**, the main turn re-reads the profile (one cheap read of the now-corrected file) so subsequent steps operate on the post-recompute state. The sub-agent's summary is folded into the Phase B manifest preview as informational context.

**Calibration-correction scope (per `feedback_branch_layout_scope`):** This is a calibration correction — same dated `_profile.md`, no new file spawned. Mirrors the §1/§8 composite-correction precedent already accepted by Step 2 carve-out below.

**P1 enforcement note (post-decomposition):** DOMAIN-SCALE_v1.md and DOMAIN-SCORE-ROLE-RELEVANCE.md are explicitly **NOT** loaded in the main Skill 7 context. They live only inside the recompute-gate sub-agent's window, and only when the marker pre-check determines the gate must fire. On marker-present publishes (the steady-state case once a profile has been touched once), neither file loads at all. This is a deliberate inversion of the prior "always-loaded" policy: the per-publish savings (~3–5K tokens) materially relieve the Phase A budget without changing the gate's correctness guarantee.

---

### Step 1.7 — Career stats pull (Phase A continued)

**Universal — every publish invocation runs this step.** Pulls the player's career per-game stats for the `## Career stats` reference appendix at the end of `_public.md` (display spec: PUBLIC-LANGUAGE-GUIDE §9). Routing is fall-through on script error — the NBA path's `ValueError: No player found` is the route signal to drop into the college fallback.

1. **NBA path (default attempt).** Run `python scripts/Public_Career_Stats.py "[Player]"`. Capture stdout (markdown tables ready to paste into `_public.md`) and read `scripts/public_career_stats_output.json` for the structured payload. The Bash call parallelizes with the Phase A read batch — player name is the only input. Both active and retired NBA players resolve here; `PlayerCareerStats` returns full history regardless of active status.

2. **College fallback** (NBA script raises `ValueError: No player found`). Spawn the Skill 1 sub-agent (Sonnet 4.6, per `project_skill1_subagent_active`) with a self-contained prompt asking for a Sports-Reference-style college career career-totals table. Sub-agent returns markdown table(s) + structured JSON matching the `career_stats_row` schema, keyed `college_career` instead of `regular_season`. Single-call; no Playoffs sub-section.

3. **HS / web-fallback failure** (sub-agent returns nothing or no Sports-Reference page found). Omit the `## Career stats` section entirely. Log "career stats: omitted (no source)" in the Phase B manifest preview as informational. Do not block publish.

**Output handoff.** Step 1.7 produces two artifacts consumed at Step 5 (Write):
- Markdown block to append after `## NBA Comp(s)` in `_public.md`.
- Structured payload (JSON) attached to the export-pipeline reconciliation surface; not pasted into `_public.md`.

**P1 enforcement note:** No new doc loaded by Step 1.7. Script and sub-agent are JIT data sources, not loadable references. PUBLIC-LANGUAGE-GUIDE §9 (the display spec) is already in the Phase A read batch. The QC4 carve-out for these numbers is documented at Step 6 and PUBLIC-LANGUAGE-GUIDE §8.

---

### Step 1.8 — Public narrative stats pull (Phase A continued)

**Universal — every publish invocation runs this step.** Pulls per-season + two-season-aggregate granular splits for use in the 4-paragraph narrative and the sub-domain rationale table. The 60/40 weighted blend (the scoring substrate) is NOT surfaced; the public artifact anchors numbers to a temporal frame the reader can reconstruct (PUBLIC-LANGUAGE-GUIDE §5.3, §8 QC7). Routing mirrors Step 1.7: NBA path default, college fallback, HS / web-fallback omission.

1. **NBA path (default attempt).** Run `python scripts/Public_Narrative_Stats.py "[Player]"`. The script orchestrates the 7 Skill-1 domain scripts in parallel as subprocesses (no scoring substrate edits — it consumes their existing JSON outputs), walks each `sb()`-shaped block, and emits three views per metric: `current_season`, `prior_season`, `two_season_aggregate` (sum/sum from raw counts, not the 60/40 blend). Captures stdout (markdown handoff block organized by sub-domain) and reads `scripts/public_narrative_stats_output.json` for the structured payload. The Bash call parallelizes with the Phase A read batch and with Step 1.7 — player name is the only input. Wall-clock ~1–2 minutes (longest single domain script) since the 7 subprocesses run concurrently.

2. **R12 mode handling.** The script honors the eval-window classification surfaced in the source profile's flag template:
   - `DEFAULT` (60/40 two-season window) — emit all three views per metric.
   - `R12_ANCHOR` (single healthy season) — emit `current_season` only; skip `prior_season` and `two_season_aggregate`. The anchor IS the most-recent meaningful sample.
   - `R12_AGGREGATE` (two compromised seasons aggregated) — emit both seasons individually with GP context in the structured payload; narrative cites each season explicitly with GP framing per PUBLIC-LANGUAGE-GUIDE §10.
   - `ROOKIE` / `OVERRIDE` — single-season emit, same shape as R12_ANCHOR.

3. **College fallback** (NBA script returns `ValueError: No player found`). Spawn the Skill 1 sub-agent (Sonnet 4.6, per `project_skill1_subagent_active`) with a self-contained prompt asking for per-season granular splits for the player's most-recent two college seasons. Sub-agent returns markdown + structured JSON matching the same three-view schema where data permits; per-domain coverage may be partial (Sports-Reference college tables don't expose all NBA-API metrics).

4. **HS / web-fallback failure** (no source available). Omit the granular-stats payload. Narrative falls back to qualitative-only claims (no specific percentages). Log "narrative stats: omitted (no source)" in the Phase B manifest preview as informational.

**Output handoff.** Step 1.8 produces two artifacts consumed at Step 3 (Assemble draft):
- Markdown handoff block — Tyler / Claude reads at draft time as the canonical source for any granular percentage cited in narrative or sub-domain rationale rewrite.
- Structured payload (JSON) — attached to the export-pipeline reconciliation surface; not pasted into `_public.md`.

**Aggregate rounding caveat.** The orchestrator reverse-computes per-season makes from `pct × volume` because the source domain JSONs persist volume but not raw makes. ±1 make per season of rounding error → ±0.1–0.5% drift on the two-season aggregate value vs. the true sum/sum. Well inside R14 dial tolerance and visually equivalent for narrative purposes; documented in the script docstring and at PUBLIC-LANGUAGE-GUIDE §9.5.

**P1 enforcement note:** No new doc loaded by Step 1.8. Script is a JIT data source. The QC7 check is documented at Step 6 and PUBLIC-LANGUAGE-GUIDE §8 / §5.3.

---

### Step 2 — Format-validate the profile (fail-loud)

**Pre-flight linter (mandatory).** Run `python scripts/lint_profile.py output/[Player_Name]/[YYYY-MM-DD]_profile.md`. The linter is the single source of truth for canonical-format conformance — same script invoked at Skill 5 QC6. Exit 0 = clean; exit 1 = drift (block publish, report drift to Tyler with file path + line numbers; fix in source profile before re-invoking publish); exit 2 = fatal parse error.

Additional post-linter checks (defense-in-depth, mostly already covered by linter):
- All canonical sections present (per SCHEMA-SPEC §10-G: §1–§10 main + §11 Anchor Library Entry).
- Each section heading uses H2 form: `## Section N — Title`.
- Section 1 contains: Player, Position, Group, Archetype, Composite, Tier (bold field names + bold Composite value per scout-output.md §1 template).
- Section 8 composite matches Section 1 composite (cross-check) — see calibration-correction carve-out below.

**Calibration-correction carve-out.** If §1 composite ≠ §8 composite AND the profile footer documents a dated in-place calibration correction (per the BRANCH-layout-scope pattern — calibration corrections edit `_profile.md` in place rather than spawning a new dated file) AND the latest `wiki/evaluations.jsonl` row for this player matches §1 composite — accept §1 as canonical, treat §8/§11 prose as internal-only, and do not block publish. The pull policy (§4-A) already SKIPS §8 and §11; §9 POT/Min/Max pull through byte-equal regardless of internal anchor staleness. Capture the encounter as a calibration finding in [docs/learnings/scout-publish-learnings.md](../docs/learnings/scout-publish-learnings.md). Linter must be configured to allow this divergence (or the operator approves the lint-1 exit on the basis of the carve-out documented above).

If any check fails (and the carve-out does not apply): **stop**. Report the drift and recommend a Skill 5 format-fix before re-invoking publish. Do not proceed to draft with a malformed profile — `_public.md` is downstream of the JSON pipeline and contamination is hard to clean up.

### Step 3 — Assemble draft per pull policy (Phase A analysis)

Apply PUBLIC-LANGUAGE-GUIDE §4-A pull policy. Read selectively:

| Pulled | Skipped |
|---|---|
| §1 Header (structured fields) | §6 Profile shape |
| §2 Physical (height/wingspan/weight only, prose) | §7 Non-negotiables gate |
| §3 Narrative (source for Vecenie 4-paragraph rewrite) | §8 Composite rationale (absorbed by Vecenie verdict) |
| §4 Sub-domain scores (numbers byte-equal; rationales rewritten) | §11 Anchor library entry |
| §5 Domain summaries (numbers byte-equal; one-line justifications) | QC1–5 (already absent from canonical profiles) |
| §9 Projection (narrow — POT/Min/Max/confidence + Bust/Avg/Boom for prospects) | |
| §10 NBA Comp (player + tier + similarity prose ≤2 sentences) | |

#### Step 3-T — Tyler-iterated narrative path (DEFAULT per S174-F02)

Three-step iteration:

1. **Claude drafts** the 4-paragraph narrative (Identity → Strength → Weakness → Projection-verdict). Inputs: source profile §3 (scouting narrative as scoring rationale, NOT the source of stat values), source profile §9 NBA POB block (read the `TENSE` token — `past` / `present` / `mixed` — and apply the [PUBLIC-LANGUAGE-GUIDE §5.3](../docs/PUBLIC-LANGUAGE-GUIDE.md) dormant-vet tense rule when ≠ present), Step 1.7 Career stats table (per-season + career-aggregate basics), Step 1.8 narrative-stats payload (per-season + two-season-aggregate granular splits). Apply the same strip / rewrite / re-voice / anchor rules as Step 3-C below. Stats anchor to the Step 1.8 payload and Step 1.7 table — never the profile §3 weighted numbers.
2. **Tyler edits** the draft and returns the edited prose. Tyler's edit pass is canonical for voice, sentence structure, and word choice.
3. **Claude redrafts the final** by integrating Tyler's edits. This is a typo-fix and structural reconciliation pass only — preserve Tyler's voice and word choice exactly. Hyphenation/punctuation normalization (e.g., "All Star" → "All-Star") is allowed if surfaced explicitly in Phase B. Do NOT polish for flow, do NOT replace clauses with "better" phrasing.

**Skip Step 3.5 reviewer pass on the narrative.** Tyler's edit IS the canonical voice gate; the rubric is defense-in-depth, not gate. Run Step 3.5 only on Claude-assembled structured fields (sub-domain rationales, domain one-lines, projection prose, comp prose).

Phase B manifest shows the post-integration final draft with Tyler's edit pass marked, plus any normalization fixes called out explicitly.

#### Step 3-C — Claude-only narrative path (FALLBACK)

When Tyler does not engage the edit loop, Claude produces the final draft alone. Inputs same as Step 3-T step 1 (profile §3, source profile §9 `TENSE` token, Step 1.7 table, Step 1.8 payload). Apply [PUBLIC-LANGUAGE-GUIDE](../docs/PUBLIC-LANGUAGE-GUIDE.md) in order: §3 (strip) → §4-B (rewrite) → §5 incl. §5.1 / §5.3-P / §5.3-G (re-voice + percentage syntax + acronym glossary) → §6 (anchor comps) → §7 (one-line domains).

Calibration target: [PUBLIC-LANGUAGE-GUIDE §5.4](../docs/PUBLIC-LANGUAGE-GUIDE.md) Mitchell sample (Tyler-authored, S175). Upstream voice exemplars in PUBLIC-VOICE-CALIBRATION are reference inspiration only — match the §5.4 target, not the upstream writers (per S174-F02; Lowe-imitation by Claude failed across four iterations).

**Structured fields are always Claude-assembled** regardless of narrative path. Sub-domain rationales (including the Signature column derived from the byte-equal sub-domain score per [docs/SIGNATURES.md](../docs/SIGNATURES.md) §3–§4), domain one-lines, projection prose, and comp prose follow the §4-B and §5.3 rules whether Tyler authors the narrative or not. Signature derivation is mechanical, not editorial — reconciliation at JSON export is fail-loud.

### Step 3.4 — Lint pre-flight (Phase A continued)

**Cheap mechanical check before reviewer fires.** The Step 3.5 V + F subagents are expensive; bare-percentage drift is mechanically detectable. Catch it here in O(milliseconds) instead of paying for a reviewer turn.

Pipe the assembled draft text from Step 3 into `lint_public.py --stdin --strict`. Per [PUBLIC-LANGUAGE-GUIDE §5.3-P](../docs/PUBLIC-LANGUAGE-GUIDE.md), every percentage in narrative + sub-domain rationale must carry a season anchor (`20YY-YY` / `since 20YY` / `[season] season`), a paren-count anchor (`(N attempts` / `(N of`), an N-of-M aggregate (`N of M`), or a `career` qualifier within ~60 chars. Any bare percentage exits non-zero.

**Invocation (PowerShell):**
```
$draft | python scripts/lint_public.py --stdin --strict
```

**Invocation (Bash):**
```
echo "$draft" | python scripts/lint_public.py --stdin --strict
```

**Exit handling:**
- **Exit 0 (clean):** proceed to Step 3.5.
- **Exit 1 (drift):** revise the draft in place against the linter's per-line findings (each finding names section + line + offending percentage). Re-run the pre-flight; only proceed to Step 3.5 once clean. The pre-flight is a writer-side discipline — Tyler does not see the loop unless the writer cannot resolve drift, in which case surface in the Phase B manifest as a flag.
- **Exit 2 (fatal parse error):** stop and report; the draft is structurally malformed.

**P1 enforcement note.** No new doc loaded by Step 3.4. Script is a JIT mechanical check, not a loadable reference.

### Step 3.5 — Invoke scout-review (Phase A continued)

**Runs only on the Claude-only path** (Step 3-C) and on Claude-assembled structured fields when Step 3-T is active. **Skipped for the Tyler-iterated narrative** per Step 3-T (Tyler's edit IS the canonical voice gate).

Spawn the [scout-review](scout-review.md) sub-skill via the Task tool (`subagent_type=general-purpose`). The sub-skill spawns Subagent V (PUBLIC-RUBRIC, PASS gate) and Subagent F (FACT-CHECK-RUBRIC, shadow-mode) in parallel against the draft, applies V's critique to revise the draft, and returns the revised text plus both verdicts. Steps 3.5 and 3.6 of the pre-Phase-B.5 workflow now live entirely inside `scout-review`.

**Handoff contract — what scout-publish hands to scout-review:**
- The draft text from Step 3-C (full text), or the structured-fields slice when Step 3-T is active.
- Absolute path to the source `_profile.md` (scout-review reads §§1, 2, 3 for V and §§1, 3, 4, 9 for F itself).
- Path to `scripts/public_career_stats_output.json` (Step 1.7 payload, F input).
- Path to `scripts/public_narrative_stats_output.json` (Step 1.8 payload, F input).

**Handoff contract — what scout-review returns:**
- Revised draft text (post-V-critique application).
- V verdict (PASS / FAIL) and verbatim critique per PUBLIC-RUBRIC output format.
- F verdict and verbatim critique per FACT-CHECK-RUBRIC output format, labeled `[F shadow]`.
- Un-revisable flags (if any) — V failures the writer could not fix without source-fidelity loss.

The revised draft replaces the in-context draft for Step 4 manifest assembly. V and F verdicts plus any flags fold into the manifest under their labeled blocks per Step 4 below. Phase A turn-budget unchanged: scout-review is a single Task call inside the same turn that spawned Step 1's parallel reads.

### Step 4 — Diff manifest and approval gate (Phase B)

Present an enumerated operation manifest. Format:

```
=== PUBLISH PLAN — [Player Name] ===
Source: output/[Player_Name]/[YYYY-MM-DD]_profile.md
Target: output/[Player_Name]/[YYYY-MM-DD]_public.md

Pull policy applied (PUBLIC-LANGUAGE-GUIDE §4-A):
  PULLED:  §1, §2, §3, §4, §5, §9, §10
  SKIPPED: §6, §7, §8, §11, QC

Editorial decisions to confirm:
  Vecenie 4-paragraph narrative — full draft below.
  Sub-domain rationale rewrites — before/after table for all 26.
  Domain one-line justifications — full set of 8.

Composite + all scores: byte-equal preserved (see Step 6 QC).
```

Then surface the actual content:
- Full 4-paragraph Vecenie narrative draft. **Step 3-T (Tyler-iterated):** show post-integration final with Tyler's edit pass marked + any normalization fixes called out. **Step 3-C (Claude-only):** show post-revise prose returned by `scout-review` plus the V verdict (PASS gate) and a clearly labeled `[F shadow]` block carrying F's punch-list + verdict (informational only during shadow-mode rollout — Tyler reads to spot factual drift V missed and may edit in response).
- Sub-domain rationale before/after table (the editorial decision surface).
- Domain one-line justifications (8 lines).
- Projection rewrite + comp similarity rewrite.

Wait for Tyler's explicit approval. If Tyler edits any section, regenerate the relevant slice and re-confirm. Do not proceed to write on partial approval.

### Step 5 — Write the public artifact (Phase C)

Single `Write` call to `output/[Player_Name]/[YYYY-MM-DD]_public.md`. Date matches the source `_profile.md` filename.

### Step 6 — Run QC checklist (Phase C analysis)

Per PUBLIC-LANGUAGE-GUIDE §8 — all seven must pass:
1. **Synthesis, not plagiarism.** No scout phrasing reproduced verbatim.
2. **No cite codes.** Grep the draft for `R\d`, `S\d{2,3}`, sub-domain id refs (`#\d{1,2}`), override flags.
3. **No internal flag language.** `CAPPED`, `SZ`, `structural zero`, `ambiguity flag`, `flagged`.
4. **Score numbers byte-equal.** Sub-domain (×26), domain (×8), composite, tier, projection POT/Min/Max/confidence appear identically in `_profile.md`. **Carve-outs:** (a) numbers in the `## Career stats` appendix are independently sourced via Step 1.7 and not compared against `_profile.md` (cheap sanity check: career row GP and PTS reconcile against per-season rows); (b) granular percentages and raw counts in narrative + sub-domain rationale are sourced from Step 1.8 (or the Step 1.7 appendix) at publish time and are not compared against `_profile.md` §3/§4 — the substrate stays weighted, the public surface anchors to single seasons or two-season raw aggregates. First-line check; Phase 4 pipeline re-enforces with the same scope carve-outs.
5. **R15 compliance.** No single-game references except championship-deciding clutch.
6. **Vecenie structure present.** Exactly four paragraphs in Identity → Strength → Weakness → Projection-verdict order.
7. **Reconcilable temporal frame.** Every percentage and granular split in narrative + sub-domain rationale traces to one of: (a) a row in the `## Career stats` appendix (per-season or career-aggregate), (b) a specific named season in the Step 1.8 payload (`current_season` or `prior_season`), or (c) the Step 1.8 `two_season_aggregate` framed with raw counts and explicit "since [year]" boundary. The 60/40 weighted blend cited as a flat number with no temporal frame is a fail. Regex first pass: any granular percentage adjacent to no season label, no raw count, and no "since" frame, that does not match a Career stats appendix career-aggregate row, fails. Defense-in-depth re-asserted in `lint_profile.py` (flag-only on first three backfills; promotes to block-on-fail per the implementation plan).

If any check fails, fix in place before reporting confirmation. A failed QC means the draft did not pass approval cleanly — re-loop through Step 3 if substantive.

### Step 7 — Confirmation

Report back per the OUTPUT block.

---

## OUTPUT — PUBLISH CONFIRMATION

```
=== PUBLISH COMPLETE — [Player Name] ===
File written: output/[Player_Name]/[YYYY-MM-DD]_public.md
QC: 1✓ 2✓ 3✓ 4✓ 5✓ 6✓ 7✓
Open items: [QC failures fixed in place, or "None"]
```

---

## TEMPLATE — `_public.md` output shape

Canonical template + variant rules live at [docs/PUBLIC_MD_TEMPLATE.md](../docs/PUBLIC_MD_TEMPLATE.md). Skill 7 emits the exact shape documented there; the pipeline parser ([scripts/export_public_json.py](../scripts/export_public_json.py)) cross-checks the produced artifact at Phase 4 stage 1 and the `PUBLIC_MD_TEMPLATE` Python constant in that script is the implementation echo. Deviations fail loud.

---

## RULES

**P1 — One player per invocation.** Skill 7 publishes exactly one profile. Catchup runs are sequential invocations, each with its own approval gate.

**P2 — Editorial only.** Never modify scores, sub-domain ids, archetype, tier, comp tier text, or projection numbers. PUBLIC-LANGUAGE-GUIDE §2 lists what is byte-equal preserved.

**P3 — Format drift fails loud.** A malformed profile blocks publish. Cross-ref Skill 6 Step 2. Do not warn-and-proceed; downstream JSON export is the wrong place to absorb upstream defects.

**P4 — Approval gate is mandatory.** No `Write` before Tyler confirms the Step 4 diff manifest. Editorial drift compounds at the JSON pipeline (Phase 4 fact-extraction) — gate it here.

**P5 — Manual trigger only.** Skill 7 does not auto-chain after Skill 5 or Skill 6. Editorial rewrites require human-driven invocation (`publish [Player]`).

**P6 — BRANCH layout invariant.** Output to `output/[Player_Name]/[YYYY-MM-DD]_public.md` per SCHEMA-SPEC §10-A. Never overwrite an existing dated public artifact. A re-run requires explicit Tyler authorization to delete the prior file.

**P7 — Synthesis, not plagiarism.** Cross-ref `scout-output.md` O3. Take what scouts observed in §3, process through the Vecenie 4-paragraph structure, write in the system's own words. Never reproduce another scout's phrasing.

**P8 — Phase-batched execution is mandatory.** 3 turns total: Phase A (parallel reads + draft assembly + lint pre-flight + scout-review handoff), Phase B (manifest preview, no tools), approval gate, Phase C (Write + QC + confirmation). Sequential single-tool turns within a phase trigger the same quadratic session-cost mechanic that scout-ingest I8 calls out.

**P9 — Sub-skill: scout-review.** The reviewer pass is a distinct job — fresh-context review of an editorial draft against a binary rubric — and lives in [skills/scout-review.md](scout-review.md). scout-publish hands a draft + profile path + payload paths to scout-review at Step 3.5; scout-review returns a revised draft + V verdict + F shadow report. The split landed Phase B.5 (2026-05-09) after Phase B grew the prior monolithic skill past 460 lines (the pre-split P9 RULE explicitly named "revisit if the skill grows further" as the trigger). Post-split: scout-publish at 314 lines (1.6× the P3 200-line ceiling), scout-review at 111 lines (under the ceiling). The residual 114-line gap on scout-publish is the orchestration weight (Steps 1.5/1.7/1.8/2/3/3.4 plus the Phase B manifest format and the Phase C QC checklist) — recognized as an ongoing exception per ARCHITECTURAL_PRINCIPLES.md ENFORCEMENT clause; further reductions wait on whether reasoning-pattern repetition emerges that earns another extraction. See plan: `~/.claude/plans/we-need-to-examine-joyful-pearl.md`.

**P10 — Narrative authorship is Tyler-iterated; rubric is defense-in-depth, not gate.** Per S174-F02 (with workflow correction 2026-05-09), the 4-paragraph narrative defaults to Step 3-T: Claude drafts → Tyler edits → Claude redrafts the final. Step 3-C (Claude-only, no Tyler edit) is the fallback when Tyler does not engage the edit loop. PUBLIC-RUBRIC PASS does NOT guarantee Tyler approval — the rubric tests surface markers; Tyler's edit pass IS the canonical voice gate, and Tyler approval at Phase B is the final gate. Mitchell v4-rev2 PASSed §§1–6 of the rubric and was rejected by Tyler as grade-6-fail prose; §§7–11 were appended after that failure to widen rubric coverage but the necessary-but-not-sufficient relationship to Tyler approval is structural and permanent. Structured fields (sub-domain rationales, domain one-lines, projection prose, comp prose) are always Claude-assembled and always run through scout-review's V/F subagents regardless of narrative path.

---

*Skill 7 of the scouting chain. Built S151 (2026-05-06) as Phase 3 of the publishable-layer track; writer/reviewer split added S175 (2026-05-07); narrative-authorship pivot to Tyler-default same session per S174-F02 after Mitchell v1–v4 voice failures; Step 3-T workflow corrected to three-step iteration (Claude drafts → Tyler edits → Claude redrafts) and Step 1.8 narrative-stats pull added 2026-05-09 to anchor public stats to a reconcilable temporal frame. Manual-trigger editorial step; no auto-chain. Phase 4 (JSON export pipeline) consumes the `_public.md` artifact this skill produces. See [docs/learnings/scout-publish-learnings.md](../docs/learnings/scout-publish-learnings.md) S174-F02 for the pivot context.*
