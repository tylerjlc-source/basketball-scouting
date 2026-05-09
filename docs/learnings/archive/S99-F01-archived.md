# S99-F01 — R13 Stage 2 is additive on credential-driven placement; strict convergence gate is protective against double-counting

**Status:** Superseded (promoted to SCORING-RULES.md R13 "Stage 2 application note — double-count protection" subsection, Session 99 2026-04-23)

**Original Date:** 2026-04-23
**Severity:** High
**Source file:** `docs/learnings/scout-composite-learnings.md`
**Applications before promotion:** 6 (S99 anchor recalibration sweep: SGA, Jalen Williams, Siakam, Mitchell, Brown, Thompson — Stage 2 did not fire in any case)

---

**Context:** SGA anchor recalibration surfaced that R13 Stage 2 modifiers stack on top of the composite produced by Steps 1–5 (including awards cross-check), not as a pathway to it. SGA's 2024-25 MVP + Finals MVP + championship credentials are already priced into the Step 4 awards cross-check (MVP + FMVP → Tier 4 floor 8.90+ compound, anchor comparison above Jokic at current level → 9.62). If R13 Stage 2 had fired at Defining (+0.20), the composite would have landed at 9.82 — tied with Kareem Abdul-Jabbar and above Kobe Bryant, not defensible for SGA's current career stage. Murray's library entry ("was 8.55; R13 Stage 2 moderate rise +0.10" → 8.65) confirms the additive mechanic. Tyler's call: keep R13 Stage 2 strict — the convergence gate ("statistical AND qualitative convergence") must be hard to clear precisely because championship/Finals-MVP credentials are already captured by the awards cross-check, and R13 Stage 2 is only meant to fire when playoff evidence shows something BEYOND what the credentials priced in.

**Learning:** R13 Stage 2 firing logic:
- **Mechanics:** Stage 2 applies AFTER Step 5 decimal placement. The credential-driven composite (Steps 1–5) already prices in awards (MVP, FMVP, All-NBA, DPOY). R13 Stage 2 is additive on top — use only to credit beyond-credential playoff signal.
- **Gate interpretation:** "Strong validation — multi-source statistical AND qualitative convergence" must be strict. Stat side must independently support the direction the qualitative side is pushing. Divergence (stat shrink + qualitative rise, or vice versa) means no Stage 2 fires, regardless of how prestigious the qualitative signal is. Finals MVP alone does not fire Stage 2 if TS% data says playoff shrink — the Finals MVP is already credited via awards cross-check.
- **Why strict:** Championship-era players routinely show star-level TS% drag in playoffs (-2 to -5 baseline per R13 note). If Stage 2 fires on qualitative alone, every Finals MVP winner gets double-credited (once via awards, once via R13), producing systematic overshoot at Tier 2+.
- **Archetype-primary stat substitution:** R13 allows DFGPOE or archetype-primary stats to substitute for TS%. This is a substitution of the stat signal, not a loosening of the gate. If PPG convergence is invoked, it must still be a genuine statistical rise signal matching the qualitative direction — not a backdoor past the convergence requirement.
- **When Stage 2 fires:** Reserved for cases where stat AND qualitative both push the same direction (Murray 2023 championship where TS% also rose vs baseline + qualitative rise = +0.10 moderate; Harden playoff shrink where both stat and qualitative declined = −0.10).

**Applies to:** Skill 4 Step 5.75 (R13 Stage 2 application). Governs NBA-vet re-scores where championship/FMVP credentials exist alongside mixed stat signals. Affects anchor library maintenance during drift recalibration sweeps.

**Promotion record:** S99-F01 was triggered by SGA's re-score in the S99 anchor recalibration sweep. Promotion flag specified promote-if-pattern-holds across remaining sweep re-scores. Pattern held 6/6 — Stage 2 did not fire in any sweep case. Promoted to SCORING-RULES.md as formal "Stage 2 application note — double-count protection" subsection.
