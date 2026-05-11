# PUBLIC RUBRIC — Subagent V (Voice)

Binary checklist applied to every `_public.md` draft by **Subagent V** (voice / structure reviewer) invoked from [skills/scout-review.md](../skills/scout-review.md) Step 1. Loaded only by V's subagent invocation — not by the writer agent, not at session open.

**Status.** Created S175 (2026-05-07) as part of the writer/reviewer split for Skill 7. Phase B (2026-05-09) split the reviewer pass into V (this rubric) + F (FACT-CHECK-RUBRIC, shadow-mode). Phase B.5 (2026-05-09) lifted Steps 3.5 + 3.6 into the dedicated [skills/scout-review.md](../skills/scout-review.md) skill. Phase C (2026-05-10) lifted F out of scout-review into the user-invoked [skills/fact-audit.md](../skills/fact-audit.md) skill; scout-review is now V-only. **V remains the PASS gate** for scout-review's pre-publish pass.

---

## Inputs handed to V

The subagent receives **only**:
- The `_public.md` draft text (Step 3-C output, or the structured-fields slice when Step 3-T is active).
- Source profile **§1 Header**, **§2 Physical**, **§3 Scouting Narrative** — passed alongside to support §8 fact-check.
- This file ([docs/PUBLIC-RUBRIC.md](PUBLIC-RUBRIC.md)).
- [docs/validation/PUBLIC-VOICE-CALIBRATION.md](validation/PUBLIC-VOICE-CALIBRATION.md) (voice spec — reference inspiration only per S174-F02).
- The Mitchell sample from [PUBLIC-LANGUAGE-GUIDE §5.4](PUBLIC-LANGUAGE-GUIDE.md) (system-output target).

V does **not** receive: profile §§4–§11 (rubric scores not within review scope); PUBLIC-LANGUAGE-GUIDE outside §5.4; the writer's reasoning. Fresh-context review per the writer/reviewer pattern.

---

## How to use

Read the draft once end to end. Then walk through the rubric. For each item: quote the offending line (or "none found"), mark Y/N or the count. Output the structured response below — no prose preamble, no softening. The rubric is the writing-equivalent of a test suite; pass or fail is the only valid answer.

**Status (S175).** Per S174-F02, the rubric is **defense-in-depth, not gate**. Tyler approval supersedes any PASS verdict. Mitchell v4-rev2 PASSed on §§1–6 and was still rejected as grade-6-fail prose; the additions §§7–11 below were appended after that failure to widen coverage. PASS still does not guarantee Tyler approval — it guarantees only that the listed surface markers are clean. The reviewer subagent also runs primarily on Claude-assembled structured fields when Tyler authors the narrative directly; in that case the 4-paragraph narrative bypasses the rubric per scout-publish.md Step 3-T.

---

## §1 — Worst line

Quote the single worst line in the draft and explain in ≤25 words. "Worst" = most generic, most hedged, most rubric-flavored, most cliché, most overclaiming, most violating of [PUBLIC-VOICE-CALIBRATION.md](validation/PUBLIC-VOICE-CALIBRATION.md) §8 patterns or [PUBLIC-LANGUAGE-GUIDE.md](PUBLIC-LANGUAGE-GUIDE.md) §5.3 universal rules.

## §2 — Hedge-phrase scan

List every occurrence of: "might," "perhaps," "potentially," "shows flashes of," "has the potential to," "is poised to," "projects as a," "could become," "tends to," "can be" (used as soft commitment).

Target: 0. Quote each occurrence with line context.

## §3 — Stat load-bearing test

For every numeric value in the draft, declare load-bearing or cosmetic. Load-bearing = removing it breaks the sentence's argument. Cosmetic = the sentence still says the same thing without the number.

Target: 0 cosmetic stats. List each cosmetic stat with line context.

## §4 — Specific moment count per paragraph

For each of the 4 paragraphs, count specific moments. A specific moment = named play type (drop coverage, isolation, pick-and-roll), named game state (clutch, end-of-quarter), named opponent matchup where the detail is load-bearing, or named possession.

Target: ≥1 per paragraph (≥4 total). Below this, the prose is reading from rubric attributes, not film.

## §5 — Archetype-projection close

Does the final paragraph project an archetype or role at the close (per [PUBLIC-VOICE-CALIBRATION.md](validation/PUBLIC-VOICE-CALIBRATION.md) §8.5)? Tells the reader what the player *will be*, not just what skills they have. Reference: Duren v2 final sentence ("the most plausible candidate to evolve the archetype further than Drummond ever did").

Target: Y. If N, quote the actual final sentence.

## §6 — AI-tell scan

Scan for two categories:
- **Rubric vocabulary at the public surface:** "Tier N," "All-NBA caliber," "structural zero," "composite," "modifier," "domain score," "sub-domain," "non-negotiable" (as system phrase), "franchise piece" (as system label).
- **Source attribution:** "scouts say," "according to ESPN," "reports indicate," "analysts have noted," "the consensus view."

Target: 0 of each. Quote every occurrence.

## §7 — Em-dash count

Count em-dash characters (—, U+2014) in the narrative prose. Hyphens (-) and en-dashes (–) do not count. Title separators ("Player Name — Public Profile") and structural separators are ignored; only narrative-paragraph em dashes are counted.

Target: 0. Quote each occurrence with line context. Per S174-F02, em dashes produce stilted prose at this register; the calibration target uses zero.

## §8 — Factual accuracy cross-reference

The reviewer subagent receives the source profile §1 (Header), §2 (Physical), §3 (Scouting Narrative) alongside the draft. For each factual claim in the draft narrative — credentials, counts, percentages, comp names, team state — verify it traces to or is consistent with the source profile. Flag any claim that does not trace, contradicts the profile, or extrapolates beyond stated framing.

Target: 0 mismatches. Quote each mismatched claim with the conflicting profile statement.

## §9 — Overclaiming detection

Flag sentences that attribute team state (record, standing, success, conference position) to a single player's named action. Examples of overclaiming: "Cleveland finished with the best record in the East with him running the pick-and-roll." "The Pistons climbed to the top three on defense because of his rim protection." Single-player credit must be load-bearing for an individual claim, not a team claim.

Target: 0. Quote each occurrence.

## §10 — Repetition detection

Each of the following items may appear at most once across the 4-paragraph narrative, ideally in Identity only: height, weight, wingspan, position, archetype name, primary comp player. If any repeats outside its first mention, flag.

Target: 0 out-of-Identity repetitions. List each repeated item with paragraph location.

## §11 — Cliché-construction detection

Flag canonical writerly clichés:
- "Young version vs current version" / "the X he was in [team]"
- "A name that does not appear on [Y]"
- "The kind of frame [that does X]"
- "The proof that [X]"
- "The credential that would close the case" / similar verdict-flavored sweeps
- "Off the bounce" used as filler rather than as named off-dribble play type
- "What he will be, instead, is [grand projection]" stacked with multiple credential clauses
- Power-position cross-comparisons forced onto the wrong position ("guard with power-forward strength")

Target: 0. Quote each occurrence.

## §12 — Acronym and jargon scan

Scan for opaque metric acronyms at the public surface: DFGPOE, PPP, A:TO, FTR, OREB%, DREB%, USG, TOV/100, and similar internal shorthand. Each must be translated inline or named explicitly per [PUBLIC-LANGUAGE-GUIDE.md](PUBLIC-LANGUAGE-GUIDE.md) §5.3.

Target: 0. Quote each occurrence with line context.

## §13 — Signature column format compliance

Scan the sub-domain rationales table's Signature column. Each filled cell must match `[Name] ([Tier])` exactly — one space before the parens, capitalized Signature name, capitalized tier label drawn from {Proven, Elite, Superstar, Iconic, Generational}. Empty cells must be the em-dash `—` (U+2014). No additional commentary, hedging, or prose within the column.

The reviewer cannot validate Name/Tier against the underlying score (profile §4 is not loaded); derivation correctness is enforced at JSON-export reconciliation per [PUBLIC-LANGUAGE-GUIDE.md §4-B](PUBLIC-LANGUAGE-GUIDE.md). This check verifies surface form only.

Target: 0 format violations. Quote each malformed cell with row number.

---

## Output format

```
=== REVIEWER CRITIQUE ===
§1 Worst line: "[quoted]" — [reason]
§2 Hedges (target 0): [N found] — [list]
§3 Cosmetic stats (target 0): [N found] — [list]
§4 Specific moments per ¶: [P1: N | P2: N | P3: N | P4: N] — flag any < 1
§5 Archetype close: [Y/N — if N, quote final sentence]
§6 AI-tells (target 0/0): [rubric vocab: N | source attribution: N] — [list]
§7 Em-dashes (target 0): [N found] — [list]
§8 Fact-check (target 0 mismatches): [N mismatches] — [list with profile-source quote]
§9 Overclaiming (target 0): [N found] — [list]
§10 Repetition (target 0 out-of-Identity): [N found] — [list]
§11 Clichés (target 0): [N found] — [list]
§12 Acronyms (target 0): [N found] — [list]
§13 Signature format (target 0): [N found] — [list]

VERDICT: PASS / FAIL
```

PASS = §2=0 AND §3=0 AND §4 every paragraph ≥1 AND §5=Y AND §6=0/0 AND §7=0 AND §8=0 AND §9=0 AND §10=0 AND §11=0 AND §12=0 AND §13=0. FAIL = anything else. **PASS does not guarantee Tyler approval — the rubric tests surface markers; Tyler approval is the gate.**

---

*Created S175 (2026-05-07) as part of Skill 7 writer/reviewer split. Status revised same session per S174-F02: rubric is defense-in-depth, not gate; §§7–11 added (em-dash count, factual accuracy, overclaiming, repetition, cliché) after Mitchell v4-rev2 PASSed §§1–6 and was still rejected. Loaded only by the reviewer subagent in scout-publish.md Step 3.5. Reviewer now also receives source profile §1–§3 alongside the draft to support §8 fact-check. See [docs/learnings/scout-publish-learnings.md](learnings/scout-publish-learnings.md) S174-F02. Update when patterns emerge that warrant new checks; aim for binary verifiability per check.*
