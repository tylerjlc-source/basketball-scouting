# FACT-CHECK RUBRIC — Skill 7 fresh-context fact reviewer

Binary checklist applied to every `_public.md` draft by **Subagent F** (fact-checker), the parallel partner to **Subagent V** (voice / [PUBLIC-RUBRIC.md](PUBLIC-RUBRIC.md)) in Skill 7 Step 3.5. Loaded only by F's subagent invocation — not by the writer agent, not at session open, not by V.

**Status.** Created Phase B (2026-05-09) of the basketball-scouting super-user-practices plan. **Shadow-mode** for the first three publishes — F's punch-list appears in the Phase B manifest as informational only; V remains the PASS gate. Promote F to PASS-required after 3 publishes if signal-to-noise holds.

**Scope.** F is the authority on **factual** claims and **authoring-discipline syntax** ([PUBLIC-LANGUAGE-GUIDE §5.3-P](PUBLIC-LANGUAGE-GUIDE.md) percentage syntax + [§5.3-G](PUBLIC-LANGUAGE-GUIDE.md) acronym glossary + dormant-vet tense rule). V's §8 fact-cross-reference and §12 acronym scan remain in place during shadow mode; redundancy is intentional. On promotion, V §8 / §12 may be stripped.

---

## Inputs handed to F

The subagent receives **only**:
- The `_public.md` draft text (Step 3-C output, or the structured-fields slice when Step 3-T is active).
- Source profile **§1 Header**, **§3 Scouting narrative**, **§4 Sub-domain scores** (rationales + scores), **§9 Projection Output Block** (TENSE token + POT/Min/Max).
- `scripts/public_career_stats_output.json` (Step 1.7 payload — career per-season + career-aggregate basics).
- `scripts/public_narrative_stats_output.json` (Step 1.8 payload — `current_season` / `prior_season` / `two_season_aggregate` views per metric).
- This file ([docs/FACT-CHECK-RUBRIC.md](FACT-CHECK-RUBRIC.md)).

F does **not** receive: profile §§2, 5, 6, 7, 8, 10, 11; PUBLIC-LANGUAGE-GUIDE; PUBLIC-RUBRIC; PUBLIC-VOICE-CALIBRATION; the writer's reasoning. Fresh-context fact-check per the writer/reviewer pattern.

---

## §F1 — Trace-percent

For every percentage in narrative + sub-domain rationale, declare its source row. Three legitimate sources:
- **Career stats appendix row** — bolded `**Career**` row OR a per-season row in §9 of the draft (sourced from `public_career_stats_output.json`).
- **Step 1.8 named-season payload** — `current_season` or `prior_season` view for the cited metric in `public_narrative_stats_output.json`.
- **Step 1.8 two-season aggregate** — `two_season_aggregate` view with explicit "since [year]" frame in the prose AND raw-count anchor (paren `(N attempts` or `N of M` form per [PUBLIC-LANGUAGE-GUIDE §5.3-P](PUBLIC-LANGUAGE-GUIDE.md)).

Any percentage that does not map to one of these three sources is a fail. Bare percentages with no temporal frame are a fail.

Target: 0 untraced. Quote each percentage with the closest payload row OR "no source row" if none exists.

## §F2 — Credentials

Every credential claim in the draft narrative — All-Star count, All-NBA team + year, All-Defensive team + year, FMVP / MVP / DPOY / 6MOTY year, championship year, draft pick — must appear in profile §1 (header) or §3 (scouting narrative). Fabricated counts ("7x All-Star" when profile shows 6) and miscited years are fails.

Target: 0 mismatches. Quote each credential with the matching profile statement or "not present in §1 / §3".

## §F3 — Comp containment

Cross-player names appear only in two places: (a) `## NBA Comp(s)` table and its similarity prose, (b) anchor references woven into Identity / Strength / Weakness / Projection-verdict that already appear in profile §3 (the writer is allowed to surface a §3 cross-player anchor in the narrative). Any cross-player name in narrative prose that does NOT appear in profile §3 is a fail.

This catches comp-leakage drift — a §10 comp name escaping into the narrative as a soft analogy without source-profile grounding.

Target: 0 leaks. Quote each cross-player narrative mention with profile §3 status.

## §F4 — POT / Min / Max byte-equal

The `## Projection (public)` prose preserves POT, Min, Max from profile §9 byte-equal. Confidence label byte-equal from §9 `Confidence:` line. Any drift (rounded, modified, paraphrased numerics) is a fail.

Target: 0 drift. Quote each value with the profile §9 source line.

## §F5 — Raw-count anchoring

Raw-count claims ("attempted 412 threes", "220 turnovers in 71 games", "251 of 623") must carry a season anchor — single named season (`in 2025-26`) OR a `since [year]` boundary OR an explicit "career" qualifier where the count reconciles to the §9 Career row.

Catches the inverse of §F1: a raw count cited without a season frame is just as unreconcilable as a bare percentage. Mirrors [PUBLIC-LANGUAGE-GUIDE §5.3-P](PUBLIC-LANGUAGE-GUIDE.md) raw-counts-beat-opaque-rate-units rule.

Target: 0 unanchored. Quote each raw count with adjacent frame status.

## §F6 — Acronym scan

Scan for the pinned glossary acronyms ([PUBLIC-LANGUAGE-GUIDE §5.3-G](PUBLIC-LANGUAGE-GUIDE.md)): DFGPOE, PPP, A:TO, FTR, OREB%, DREB%, TS%, USG, TOV/100, CAS 3PT%, PnR, DHO, ISO, plus credential acronyms DPOY / MVP / FMVP / 6MOTY. Within each scan-standalone group (4-paragraph narrative; sub-domain rationale table; domain one-line table; comp similarity column), each acronym must be expanded inline at first use. Subsequent mentions inside the same group may use the bare acronym.

Target: 0 unexpanded first-uses. Quote each occurrence with group + first-use status.

## §F7 — Tense scan

Read profile §9 `TENSE:` token (per [skills/scout-output.md](../skills/scout-output.md) §9 NBA-vet template).
- **`Tense: past`** ⇒ dormant-window claims (the season the player missed) read past tense; today-state opener still reads present (e.g., "Jackson is …"). Flag any in-progress "currently out for [year]" framing or any present-tense claim about the missed season.
- **`Tense: mixed`** ⇒ dormant window in past tense, active claims in present tense. Flag the same in-progress framing.
- **`Tense: present`** ⇒ default register; nothing to check here.

If profile §9 has no `TENSE:` line (legacy profiles predating the field), default to `present` and skip this check.

Target: 0 violations. Quote each violating sentence with the §9 token.

---

## Output format

```
=== FACT-CHECK CRITIQUE ===
§F1 Trace-percent (target 0 untraced): [N found] — [list with closest payload row]
§F2 Credentials (target 0 mismatches): [N found] — [list with profile-source quote]
§F3 Comp containment (target 0 leaks): [N found] — [list with profile §3 status]
§F4 POT/Min/Max byte-equal (target 0 drift): [N found] — [list with profile §9 source]
§F5 Raw-count anchoring (target 0 unanchored): [N found] — [list with frame status]
§F6 Acronyms (target 0 unexpanded first-uses): [N found] — [list with group]
§F7 Tense (target 0 violations): [N found] — [list with §9 TENSE token]

VERDICT: PASS / FAIL
```

PASS = §F1=0 AND §F2=0 AND §F3=0 AND §F4=0 AND §F5=0 AND §F6=0 AND §F7=0. FAIL = anything else.

**Shadow-mode note (Phase B initial rollout):** F's verdict is informational only in the Phase B manifest. V (PUBLIC-RUBRIC) remains the PASS gate. After 3 publishes, evaluate F's punch-list signal-to-noise — if F catches real drift V missed without surfacing noise, promote to PASS-required and (optionally) strip V §8 / §12 to remove redundancy.

---

*Created Phase B (2026-05-09) of the basketball-scouting super-user-practices plan. Shipped in shadow-mode; promotion criterion documented above. Loaded only by Subagent F invocation in scout-publish.md Step 3.5. See plan: `~/.claude/plans/we-re-working-on-the-warm-dream.md`.*
