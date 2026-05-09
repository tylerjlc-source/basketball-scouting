# scout-output — Learnings

Active calibration learnings for the scout-output skill. Loaded
just-in-time at skill invocation (P1). Governed by
SELF-LEARNING-PROTOCOL.md.

**Scope:** Category 3 findings scoped to this skill's execution.
Category 1 findings live in session logs. Category 2 findings live
in rule documents (see routing table in SELF-LEARNING-PROTOCOL.md).

---

## ACTIVE LEARNINGS

---

### S102-F02 — POT below composite is valid for post-peak NBA vets
**Status:** Superseded — structurally subsumed by S119 NBA-PROJECTION-OUTPUT-BLOCK.md design (archived 2026-05-03)

Full original entry preserved at `docs/learnings/archive/S102-F02-archived.md`. Applied 6 times (Sabonis S102, Vučević S104, Embiid S110, Giannis S116, KD S119, Curry S123) + 7 confirmed negative-controls — discrimination at the multi-condition gate was empirically clean across age range 22–38.

**Why archived:** The pattern was a workaround for the prospect-arc PROJECTION-OUTPUT-BLOCK.md Block 2 no-slot path defaulting POT above composite. The S119 NBA-PROJECTION-OUTPUT-BLOCK.md replaces that machinery entirely with anchor-based projection. The new POB's Step 3.1 ("POT cannot fall below the player's best observed season composite") plus Validation Check #2 (post-peak/late "should not exceed at all") encode post-peak handling natively — under the new POB, every one of this learning's 6 firings (POT below composite by −0.30 to −0.80) would be structurally impossible. The diagnostic value is preserved in the archive; future projection-doc changes that reintroduce a composite-to-POT band default should re-load the archived entry and re-evaluate.

---

### S96-F04 — NBA-vet adaptation for Comp + Projection frameworks
**Status:** Superseded then partially rescoped (promoted Session 101; rescoped Session 119)

Original entry archived at `docs/learnings/archive/S96-F04-archived.md`. Applied 6 times (Simons S94, Morant S96, Bogdanović S100, Anderson S100, Hauser S100, Kessler S101) — pattern held cleanly across all applications. Promoted to formal rule sections (NBA-COMP-METHODOLOGY.md § NBA-Vet Adaptation + PROJECTION-OUTPUT-BLOCK.md § State 4 Procedure) after promotion threshold reached at Kessler S101.

**S119 follow-up — partial demotion / rescope:** Multi-comp + age-comparable-season machinery scoped to prospects only. NBA vet evaluations now use a single lineage comp per NBA-COMP-METHODOLOGY.md § B — NBA VET LINEAGE COMP. The age-comparable-season selection logic — S96-F04's load-bearing complexity (Carmelo at 37 was bench scorer so use peak NYK; Paul George hasn't been 37 yet; etc.) — was the primary friction the rescope addresses. PROJECTION-OUTPUT-BLOCK.md § State 4 Procedure was retired in the same S119 cycle (replaced by NBA-PROJECTION-OUTPUT-BLOCK.md). KD S119 was the last evaluation under the legacy multi-comp + age-comparable-season model. Pattern noted for future: rules promoted from learnings sometimes need scoping later as the system matures and the original validation context evolves. (2026-05-03: "State 4" terminology retired across active routing — section name § B updated to "NBA VET LINEAGE COMP".)

---

## ENTRY FORMAT

See SELF-LEARNING-PROTOCOL.md for the canonical entry format. Each
active learning must include: ID, Date, Severity, Context, Learning,
Applies to, Status, Applications.

---

*Created Session 94. Empty scaffold.*
