# S96-F04 — NBA-vet adaptation for Comp + Projection frameworks (ARCHIVED)

**Status:** Superseded — promoted to NBA-COMP-METHODOLOGY.md § NBA-Vet Adaptation and PROJECTION-OUTPUT-BLOCK.md § State 4 Procedure, Session 101.

**Archive note:** This is the original learning body preserved for provenance. Active guidance lives in the two rule documents above. Do not apply this file directly — it is not loaded.

---

### S96-F04 — NBA-vet adaptation for Comp + Projection frameworks
**Date:** 2026-04-22
**Severity:** Medium
**Context:** Ja Morant was the second NBA veteran through the full 5-skill chain (first was Anfernee Simons in S94). Two framework gaps surfaced: (1) NBA-COMP-METHODOLOGY.md specifies "Rookie TS%" as the comp anchor, but for an established 26-year-old vet, comparing Ja's current TS% to a comp's rookie-year TS% produces a bad mismatch; (2) PROJECTION-OUTPUT-BLOCK.md's States 1-4 cover draft-year prospects primarily — State 4 ("Not in draft year") technically covers NBA vets but some Block 1 formula fields assume comp anchor = rookie TS%. For Ja, comps (Wall, Westbrook, Rose) were run at age-comparable seasons (2016-17, 2015-16, 2014-15) rather than rookie seasons, and Block 1 used the age-comparable comp TS% as anchor. Tyler approved adaptation in-session.
**Learning:** For active NBA-vet evaluations (State 4), adapt the frameworks as follows:
- **NBA Comp (Section 10):** Run NBA_Comp_Stats.py with `--season YYYY-YY` targeting the comp's age-comparable season (same age as subject during the evaluation anchor window), not `--rookie`. Statistical matching uses current-state stats on both sides, preserving the "comparable-career-stage" comparison that makes the comp meaningful.
- **Projection Midpoint (Block 1):** For an active vet, Midpoint equals the current rubric composite directly (per POB Block 1 under the unified composite scale, S98). The age-comparable comp's rookie TS% serves as a validation cross-check — flag when it implies a materially different entering-the-league level. Comp does not numerically shift the Midpoint.
- **POT (Block 2):** Use the no-slot path (Composite band → POT range). Apply projection modifiers normally. Min/Max widens per the no-slot rule.
- **Block 4 Bust/Avg/Boom%:** Omitted per State 4 spec.
- **Sleeper criteria:** N/A for NBA vets.
Document the adaptation explicitly in the Projection Output Block output and comp similarity notes.
**Applies to:** Skill 5 Section 9 (Projection Output Block) and Section 10 (NBA Comp) — specifically the active-NBA-vet case (State 4). Does not affect prospect evaluations.
**Status:** Active
**Applications:** 6 (Simons S94, Morant S96, Bogdanović S100, Anderson S100, Hauser S100, Kessler S101)

**Promotion history:**
- S96 creation: learning authored after Morant Skill 5 surfaced the two framework gaps.
- S100 batch 1: applications 3, 4, 5 (Bogdanović, Anderson, Hauser) confirmed the pattern held for NBA vets across diverse archetypes (Wing 3-and-some-D, Wing Secondary Playmaker, Wing Shooting Specialist).
- S101 Kessler: 6th application, first Big under adaptation. Promotion threshold reached.
- S101 promotion: formalized in NBA-COMP-METHODOLOGY.md § NBA-Vet Adaptation and PROJECTION-OUTPUT-BLOCK.md § State 4 Procedure. Active learning entry replaced with superseded pointer.
