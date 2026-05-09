# scout-publish — Learnings

Active calibration learnings for the scout-publish skill. Loaded
just-in-time at skill invocation (P1). Governed by
SELF-LEARNING-PROTOCOL.md.

**Scope:** Category 3 findings scoped to this skill's execution.
Category 1 findings live in session logs. Category 2 findings live
in rule documents (see routing table in SELF-LEARNING-PROTOCOL.md).

---

## ACTIVE LEARNINGS

---

### S174-F01 — In-place calibration corrections cause §1↔§8 cross-check drift
**Date:** 2026-05-06
**Severity:** Low (process gap, not output corruption)
**Context:** First Wave 1 publish — Donovan Mitchell. Profile §1 Header reads composite **8.95** (canonical, matches `wiki/evaluations.jsonl` row); §8 Composite Rationale, §9 POT block ("CURRENT (composite): **8.92**"), and §11 Anchor Library Entry all reference **8.92**. Cause: 2026-05-05 top-30 cohort audit revised the composite 8.92 → 8.95 via in-place edit per the BRANCH-layout-scope pattern (calibration corrections are not new evaluations and don't spawn a new dated file). Footer at line 245 documents the correction. §9 POT/Min/Max (9.02 / 8.62 / 9.06) were not re-run — POT 9.02 derives from prior DEP 8.92 + 0.10 Peak buffer; under DEP 8.95 the buffer would be 9.05 (3-hundredths drift, well within R14 tolerance).
**Learning:** Skill 7 Step 2 strict cross-check ("§8 composite matches §1") fails on every profile that has been calibration-corrected in place. The cross-check was designed for malformed profiles, not the documented in-place pattern. Carve-out added to scout-publish.md Step 2: accept §1 as canonical when (a) §1 ≠ §8, (b) footer documents calibration correction, and (c) latest ledger row matches §1. §8/§11 prose stays internal-only per pull policy; §9 POT/Min/Max byte-equal-pulled regardless of internal anchor staleness.
**Applies to:** Skill 7 Step 2 format-validate. Will likely fire on every Wave 1–4 player whose composite was touched by the 2026-05-05 cohort audit. Memory `feedback_branch_layout_scope` is the upstream authority for the in-place pattern.
**Status:** Active — carve-out applied 2026-05-06 (S174). Re-evaluate after Half A: if firing rate is high (>30% of launch-30) consider promoting to a formal SCHEMA-SPEC §10-A clause covering in-place calibration cascades and downstream-section staleness expectations.
**Applications:** Mitchell 2026-05-06 (this entry).

---

### S174-F02 — Reviewer-rubric PASS doesn't guarantee acceptable prose; Tyler-authored narrative is the workable pattern
**Date:** 2026-05-07
**Severity:** Medium (architecture pivot for Skill 7 narrative authorship)
**Context:** Mitchell publish drafts v1–v3 (S174) and v4 + v4-rev2 (S175) all rejected. v4-rev2 PASSed PUBLIC-RUBRIC after one revision pass — zero hedges, zero cosmetic stats, ≥1 specific moment per paragraph, archetype-projection close, zero AI-tells. Tyler rejected anyway: factual error (7th vs 6th consecutive All-Star at 2024-25 breakout), em dashes throughout (em-dash prohibition flagged twice prior), prose-form numbers when numerical was wanted, contrived "power-forward strength" comparison, weight restated as paragraph subject, "young version / current version" cliché stack, overclaiming Cleveland's regular-season record on Mitchell's pick-and-roll work. Rubric passed grade-6-fail prose because PUBLIC-RUBRIC tests surface markers (banned phrase lists, count thresholds) and not factual accuracy, em-dash count, numerical form, overclaiming, repetition, or sentence-construction cliché. Root cause: PUBLIC-VOICE-CALIBRATION conflated upstream voice EXEMPLARS (Lowe, who uses em-dashes as "workhorse") with the system's actual published-output target (Duren v2, which uses zero em-dashes). The voice spec drove Claude toward Lowe-imitation at sentence level, which Claude cannot sustain at acceptable quality. Tyler then hand-wrote the Mitchell narrative in five minutes; his prose beat all four Claude iterations.
**Learning:** LLM-generated literary prose at scout-publish register is below the project's quality bar. PUBLIC-RUBRIC binary checks are necessary but not sufficient — they catch surface markers, not bad writing. Skill 7 pivots to Tyler-as-author for the 4-paragraph narrative; Claude assembles structured fields (sub-domain rationales ≤30 words, domain one-lines ≤25 words, projection prose ≤2 sentences, comp prose ≤2 sentences) where tight constraints match Claude's actual capacity. Reviewer subagent stays as a defense-in-depth check on Claude-authored fields, not as a gate on the narrative. Mitchell's hand-written narrative replaces Duren v2 as PUBLIC-LANGUAGE-GUIDE §5.4 calibration sample. Em-dash prohibition restored explicit. Numbers numerical (not prose form). New PUBLIC-RUBRIC checks queued: em-dash count (target 0), factual-accuracy cross-reference against source profile, overclaiming detection, repetition detection, cliché-construction detection.
**Applies to:** All Wave 1–4 publish runs (29 remaining after Mitchell). When Tyler authors narrative, skip Step 3.5 reviewer pass (canonical author). When Claude assembles structured fields, reviewer rubric still applies but Tyler approval supersedes any PASS verdict.
**Status:** Active — pivot decided 2026-05-07 (S175). Doc edits to PUBLIC-LANGUAGE-GUIDE / PUBLIC-VOICE-CALIBRATION / PUBLIC-RUBRIC / scout-publish.md pending Tyler confirmation. Re-evaluate after Wave 1 close: if Brown + JJJ also require Tyler-authored narratives, the system has effectively pivoted to "Tyler writes prose, Claude writes structured fields" and Skill 7 docs should be normalized to that model as the primary path rather than the writer/reviewer subagent pattern.
**Applications:** Mitchell 2026-05-07 (this entry).

---

### S176-F01 — Brown publish surfaced four codification gaps in the public-language spec
**Date:** 2026-05-07
**Severity:** Medium (writer-side rule additions; reviewer-side scan added)
**Context:** Wave 1 #2 publish — Jaylen Brown. Tyler-authored narrative cleanup of profile §3 surfaced four patterns the system had not codified: (1) opaque metric acronyms (DFGPOE, PPP, A:TO, FTR, OREB%, DREB%) leaked into both narrative and structured fields; (2) rate stats with non-intuitive units (TOV/100 touches at 5.0) were unreadable without translation; (3) in-narrative cross-player comparisons used as system triangulation ("score-first but not Curry-efficient") leaked into prose where comps belong in §10; (4) system recency-window framing ("two-season evaluation window", "within recency") leaked into the Projection-verdict register. Tyler had to flag each by hand; reviewer rubric did not catch them because the surface markers weren't on the scan list. The same Brown publish also surfaced a comp-quality issue (Wiggins under-rated Brown's archetypal shape; swapped to Butler at Skill 7 publish via in-place §10 calibration correction) — adjacent finding documented in the profile footer, not codified here because comp-quality is a Skill 5 judgment, not a Skill 7 language rule.
**Learning:** PUBLIC-LANGUAGE-GUIDE §3 (strip list) extended with two categories — system-internal cross-player comparisons in prose; system recency-window framing. PUBLIC-LANGUAGE-GUIDE §5.3 (universal operational rules) extended with two rules — acronyms translated inline; raw counts beat opaque rate units. PUBLIC-RUBRIC §12 added — binary acronym/jargon scan, with PASS condition and output format updated. Codification finalized between Brown ship and JJJ kickoff so JJJ inherits the rules from the doc, not from session context.
**Applies to:** All Wave 1–4 publish runs. Reviewer subagent now has §12 acronym scan; writer (Claude or Tyler) has expanded §3 strip list and §5.3 rules.
**Status:** Active — codified 2026-05-07 (S176).
**Applications:** Brown 2026-05-07 (this entry).

---

### S176-F02 — JJJ publish surfaced three more codification gaps: structured-field acronym re-expansion, dormant-vet verdict-opener tense, Max-POT-aware verdict-bound register
**Date:** 2026-05-07
**Severity:** Medium (writer-side rule additions)
**Context:** Wave 1 #3 publish — Jaren Jackson Jr. Tyler-directed narrative authorship surfaced three patterns S176-F01 did not capture: (1) acronym re-expansion at first use within structured-field groups — narrative's "Defensive Player of the Year" expansion did not propagate to sub-domain rationale tables that scan standalone (reviewer caught DPOY in #16 Help defense); (2) dormant-vet verdict-opener tense — initial draft used in-progress "currently out for the 2025-26 season" framing; Tyler corrected to past-tense "who missed time due to knee injury during the 2025-26 season" because by publish time (2026-05-07) the regular season is past, not in-progress; (3) Max-POT-aware verdict-bound register — initial draft used definitive "He is not going to become an All-NBA player"; Tyler corrected to "Jackson is unlikely to become an All-NBA player; the lean frame and structural rebounding gap will need to find a solution for him to reach his upside potential" because JJJ's Max POT 8.90 sits within 0.05 of the All-NBA credential floor (~8.85), making definitive "will not become" overcommitted. Each pattern was Tyler-flagged in narrative review; reviewer rubric did not catch (1) until explicit Step 3.5 acronym scan, did not catch (2) or (3) at all because they are judgment calls on register, not surface-marker scans.
**Learning:** PUBLIC-LANGUAGE-GUIDE §5.3 acronym rule extended — first-use applies per structured-field group (sub-domain rationale tables, domain one-line tables, comp tables that scan standalone) even when narrative has established the acronym upstream. Credential acronyms (DPOY, MVP, FMVP) follow the same rule. PUBLIC-LANGUAGE-GUIDE §5.3 new bullet — dormant-vet verdict-opener tense rule for any R13-dormant or active-injury vet at publish time. PUBLIC-LANGUAGE-GUIDE §4-B Projection narrative row extended — verdict-bound language modulates with Max POT proximity to next-tier credential floor (~0.10 buffer to 8.85 All-NBA, 7.90 All-Star); use "unlikely to become" + structural-gap-as-problem-to-solve framing inside that band, definitive "will not become" only when Max POT is clearly below the credential. JJJ verdict paragraph itself becomes a candidate dormant-vet calibration sample for §5.4 (deferred until JJJ public.md exists post-Phase-C).
**Applies to:** All Wave 1–4 publish runs (27 remaining after JJJ ships). The dormant-vet opener rule directly governs the 7 remaining R13-dormant launch profiles (Durant, Edwards, Luka, Haliburton, Kyrie, AD, Lillard). The Max-POT-aware verdict-bound rule applies wherever the verdict carries a "will/will not become" clause — most of the 27.
**Status:** Active — codified 2026-05-07 (S176).
**Applications:** Jackson 2026-05-07 (this entry).

---

### S178-F01 — "word form" doc-fidelity drift across three downstream files
**Date:** 2026-05-08
**Severity:** Low (informational — canonical rule and actual practice agree; only the downstream copies are wrong)
**Context:** Building the Signatures system, grepped for "word form" and found four files containing the phrase. PUBLIC-LANGUAGE-GUIDE §5.3 (canonical) explicitly says "Numbers in numerical form ('40.7%', '6'10\"', '9.02')... not word form" and §4-B repeats "Numbers in numerical form ('40.7%', '85th percentile'), not word form" — both correct. Three downstream files contradict by stating "numbers in word form": (1) `skills/scout-publish.md` line 262 — sub-domain rationale row template comment says "[≤30 words, numbers in word form per PUBLIC-LANGUAGE-GUIDE §5.3]"; (2) `docs/schema/public-profile.schema.json` line 173 — `rationale_public.description` says "Rewritten public rationale per PUBLIC-LANGUAGE-GUIDE §4-B: ≤1 sentence, ≤30 words, numbers in word form"; (3) `scripts/export_public_json.py` line 587 — Stage 4b symbol_number cross-check note says "Symbol-form number not in profile (language guide §5.4 says use word form)" — also has the wrong section number (§5.4, not §5.3). Existing public profiles (Mitchell, JJJ, Brown) all use numerical form, confirming the canonical rule is the actually-applied one. The audit-note in (3) is doubly wrong — its message says "should be word form" but its trigger flags exactly the symbol-form numbers that are in fact correct per §5.3. The check itself appears not to fire in practice (numerical form is what we use), so the audit-note string is dormant.
**Learning:** Three pure-typo drifts of the same false claim (canonical → "numerical"; drifted copies → "word") plus one wrong section number. Per memory `feedback_doc_fidelity_drift_propagation`, when fixing one, grep for the others and bundle the patch — captured here so the next docs maintenance pass picks up all four edits in one go: skill template comment, schema description, script audit-note string, and the script's §5.4 section reference (should be §5.3). No production behavior changes; the canonical rule is already the actual practice.
**Applies to:** Skill 7 sub-domain rationale authoring (template comment), public-profile JSON schema descriptions, export-script audit-note text. No impact on JSON output, schema validation, or fact-extraction (the affected fields are all human-readable copy/comments, and the export-script symbol-number check's trigger is correct even though its note text is wrong).
**Status:** Captured 2026-05-08 (S178). Recommend bundling fix in next docs maintenance pass — out of scope for the Signatures build that surfaced it. Single 4-edit patch when picked up.
**Applications:** None yet (informational capture during Signatures build).

---

## ENTRY FORMAT

See SELF-LEARNING-PROTOCOL.md for the canonical entry format. Each
active learning must include: ID, Date, Severity, Context, Learning,
Applies to, Status, Applications.
