# Draft Class Generator — Project Roadmap & Task Checklist
**Living Document — Updated through Session 67**

---

## WHERE WE ARE

### The Three Products
1. **Real-world scouting tool** — AI-powered prospect discovery platform for scouts, agents, and college programs. Automates the broad coverage pass.
2. **Basketball ratings database** — public-facing player profile database. NBA, college, and high school. Longitudinal tracking from high school through the NBA. Indexed by the proprietary scouting rubric.
3. **2K draft class generator** — generates accurate, research-based custom draft classes for NBA 2K MyNBA. Currently deferred.

### Architecture

```
26 sub-domain scores → tier assignment → composite
```

- **26 sub-domains** scored 1–10 against a position-specific peer group
- **Domain scores** exist as readable profile summary only — not calculation inputs
- **Composite is assigned, not calculated** — tier table is the primary assignment tool
- **Archetype** identifies player type — identification only, not a calculation input
- **Non-negotiables gate** runs post-scoring — flags structural ceilings independently of composite

### Track Separation

**Track 1 — Layer 1 scouting and rating system**
The engine. Rubric, scoring protocol, archetype system, non-negotiables gate, tier assignment, composite. Every other product depends on this being validated.

**Track 2 — Public-facing ratings database**
Built on Track 1. Does not begin until Track 1 validation is complete.

**2K draft class generator**
Separate workstream. Deferred. Resumes when ~50 additional Layer 1 builds are available and translation tables have sufficient density.

---

## COMPLETED WORK

### Sub-Domain System
All 26 sub-domains defined, locked, and stored in SUB-DOMAINS_v3.md. R10 mandatory peer ranking step confirmed active. Content locked — no editorial changes without updating all dependent documents.

### Archetype System
25 archetypes across three positional groups. All weight tables built and confirmed in ARCHETYPE-WEIGHTS_v3.md.

- Guards (9): Jumbo Playmaker | Offensive Engine | All-Around Guard | 3-and-D Guard | Pure Point Guard | Microwave Scorer | Slasher | Shooting Specialist | Defensive Specialist
- Wings (10): All-Around Wing | Modern Four | 3-and-D Wing | 3-and-some-D Wing | Dribble Pass Shoot Wing | Secondary Playmaker | Score-First Wing | Shooting Specialist | Defensive Specialist | Defensive-Engine Playmaker
- Bigs (6): All-Around Big | Switchable Big | Rim Protector | Stretch Big | Versatile Scoring Big | Energy Big

Weight tables are qualitative reference only under the current architecture. Not formula inputs.

### Calibration Dataset
21 confirmed player targets scored across 5 positions and 15 archetypes. Full sub-domain profiles with confidence ratings. Stored in COMPOSITE_CALIBRATION_DATA_v5.md — to be migrated to anchor library in COMPOSITE-SCALE-AND-TIERS.md then archived.

### Position Scale — Guards
POSITION_SCALE_GUARDS_v1.md confirmed and active. Wings and Bigs scales pending.

### Architecture Pivot — Session 63
Formula-based composite retired permanently. New architecture locked: 26 sub-domain scores → tier assignment → composite. Composite is assigned, not calculated. Domain aggregation removed as calculation step. Full rationale in PRODUCT_DESIGN_DECISIONS_v9.md Section 2 and Section 14.

### Projection Output Block
Complete. Stored in PROJECTION-OUTPUT-BLOCK.md. Min < POT < Max structural rule confirmed. Bust%/Avg%/Boom% framework confirmed. Selective effort sub-category confirmed.

### Competitive Analysis and Product Design
Complete. All decisions locked in PRODUCT_DESIGN_DECISIONS_v9.md.

### scouting-rubric SKILL.md Rewrite — Session 65
All 2K language removed. Domain aggregation removed as calculation step. Rebuilt as standalone scouting tool. v3 active. No further changes required.

### Anchor Library — Session 66
COMPOSITE-SCALE-AND-TIERS.md fully rewritten. 87 confirmed players across tiers 1–10. Tier structure revised: top two bands tightened to 9.80–10.00 and 9.50–9.79; 0.20 redistributed to quality starter (7.90–8.29) and NBA starter/rotation (7.50–7.89) bands. Prospect pool context added to each band. Tier 8 label updated to "NBA starter / rotation player". Lower tiers restructured to reflect full prospect development pathway. Archetype corrections locked: Reaves → All-Around Guard; Pritchard → Microwave Scorer; Knueppel → Shooting Specialist; Dick → Shooting Specialist; Amen Thompson → Dribble Pass Shoot Wing. Tiers 11–13 anchor population deferred.

### Guard Validation Pipeline Complete — Session 89
All four guards through Layer A → B → C. Irving (8.78), Fox (8.51 confirmed), Smart (7.90), Hield (7.05 confirmed). Clean tier discrimination across four tiers (5, 6, 7, 9).

### 2K R&D — Manual 2027 Draft Class
67/67 confirmed builds complete. Position weight tables confirmed for all five positions. Calibration findings codified in draft-class-builder SKILL.md and Ground Truth. Deferred pending pipeline density.

### Pipeline Architecture — Session 82
Three-layer architecture confirmed:
- **Layer A — Data Collection (deterministic, no AI):** Python scripts hitting APIs (nba_api, Hoop-Math scraper, CBBpy), returning structured JSON per player covering all 26 sub-domains. Also runs web search pass collecting scouting report text tagged by sub-domain keyword matching. No judgment, no interpretation, no LLM calls.
- **Layer B — Intelligence (single Claude API call):** One Claude call with full system prompt (SKILL.md + SUB-DOMAINS + Position Scale + Source Map). Receives entire Layer A output. Scores all 26 sub-domains, assembles domain scores and full profile shape in one call.
- **Layer C — Assembly (deterministic, no AI):** Takes 26 scores. Computes domain scores using position weights. Suggests composite tier placement (human confirms during validation phase). Generates player card / database entry.

### First Automated Infrastructure — Session 82
finishing_data.py built and tested. Pulls Sub-Domain #1 (At-Basket Finishing) data for any NBA player via nba_api: restricted area FG%, % shots at rim, dunk rate, non-dunk rim FG%, FT%, FTA/game. Validated against four test guards (Irving, Fox, Smart, Hield). Domain 1 status: #1 validated, #2 partially validated, #3 baseline confirmed. Provisional scores assigned. Script update needed for #2 additions (drive rate, paint FG%, FTR) and missing #1 stats (% assisted at rim, finish rate against shot blockers).

### Precision Principle — Session 82
Documented standard: for every sub-domain, interrogate all primary and secondary stats before moving on. Test for each stat: would this change a score, or just confirm one? Stats that can move the needle are required for scoring. Stats that only confirm are enrichment — they increase confidence but don't block scoring.

### Domain-by-Domain Build Sequence — Session 82
Corrected sequence per domain: Research → Source Map → Script → Run Test Guards → Validate Discrimination → Score from Position Scale → Confirm Score Matches Expectation → Lock.

Phase ordering for guards:
1. Domain 1: Finishing — #1 validated, #2 partially validated, #3 baseline. Needs script update.
2. Domain 2: Shooting — Heaviest domain for guards (4 sub-domains). Research + source map + scripts.
3. Domain 3: Ball Skills — Handling, passing, turnovers. Moderate difficulty.
4. Domain 4: Playmaking — PnR data (Synergy access problem), transition, off-ball. Mixed difficulty.
5. Domain 5: Defense — 4 sub-domains, noisiest data. High difficulty.
6. Domain 6: Rebounding — Thin for guards. Quick build.
7. Domain 7: Athleticism — Mostly qualitative for NBA players. Minimal scripts.
8. Domain 8: IQ/Motor — Almost entirely qualitative. Minimal scripts.

After all 8 domains: run all four guards through complete pipeline (Layer A → B → C) and verify composite tier placement against anchor library.

---

## ACTIVE TASK SEQUENCE — TRACK 1

---

### Task S1 — Layer 1 Validation
**Status: Superseded as hard gate. Validation now happens inside S2 — domain-by-domain, against real players, as the pipeline is built.**

Original plan: formal validation as a standalone gate before pipeline work. What actually happened: the domain-by-domain build sequence (Session 82) validates stats AND scoring simultaneously. Four NBA test guards (Irving, Fox, Smart, Hield) serve as the validation set for each domain. Rubric fixes (S82-F01 co-primary, S77 stacking rule, S76 qualitative temper) are found and applied during builds, not in a separate validation pass.

Remaining S1 items that still apply (folded into S2 execution):
- [ ] Define pass standard for composite tier assignment accuracy
- [ ] Select prospect validation set (in addition to NBA test guards)
- [ ] Retrospective projection accuracy test — deferred to post-pipeline completion

---

### Task S2 — Data Retrieval Pipeline + Domain Validation
**Status: In progress. Current priority.**

Build the automated data pipeline domain by domain, validating each domain's stats against the four test guards before moving to the next. Each domain follows the confirmed build sequence: Research → Source Map → Script → Run Test Guards → Validate Discrimination → Score from Position Scale → Confirm Score Matches Expectation → Lock.

**Three-layer pipeline architecture (confirmed Session 82):**
- Layer A — Data Collection (deterministic, no AI): Python scripts + web search pass
- Layer B — Intelligence (single Claude API call): full rubric scoring in one call
- Layer C — Assembly (deterministic, no AI): domain scores, composite suggestion, player card

**Infrastructure Priorities (Session 81):**
- Sub-Domain Source Map — Domain 1 (Finishing) COMPLETE. Template confirmed. Domains 2-8 pending.
- Infrastructure builds identified: (1) Hoop-Math scraper, (2) CBBpy integration, (3) nba_api pipeline.
- Data subscriptions: EvanMiya + Cleaning the Glass (~$35/mo total).
- Partnership inquiries: deferred to post-proof-of-concept.

**2-season evaluation window (confirmed Session 83):**
- 60/40 recency weighting (current season / prior season) is the default for all NBA-level evaluation
- Volume-weighted percentages for shooting stats; simple weighted average for rate stats
- Both seasons queried independently with explicit season parameters — prevents ShotChartDetail cross-season bleed (S83-F05)
- Rookies or players who missed entire prior season: current season only

**Domain build status:**
- [x] Domain 1: Finishing — **LOCKED.** All four test guard scores final (#1: Irving 9.5, Fox 8.5, Smart 5.0, Hield 5.0 | #2: 7.0, 7.5, 5.5, 4.0 | #3: 2.5 all). Source map complete. finishing_data_v3.py built with 2-season window.
- [x] Domain 2: Shooting — **Scored (provisional).** Four sub-domains scored (#4-#7). Source map complete and integrated into SUB-DOMAIN-SOURCE-MAP. shooting_validation_v2.py built with 2-season window. Fox/Smart scores carry medium confidence pending clean 2-season re-pull.
- [x] Domain 3: Ball Skills — **LOCKED.** All three sub-domains scored (#8: Irving 9.5, Fox 8.0, Smart 5.5, Hield 4.5 | #9: 9.5, 7.0, 5.5, 6.0 | #10: 8.0, 7.0, 5.0, 6.5). Source map complete. ball_skills_validation.py built with 2-season 60/40 window. Expert-driven stat selection method formalized (S84-F01). Qualitative validation step confirmed mandatory (S84-F02).
- [x] Domain 4: Playmaking — **LOCKED.** All four sub-domains scored (#11: Irving 7.3, Fox 7.0, Smart 6.0, Hield 4.0 | #12: 7.5, 7.0, 6.0, 6.3 | #13: 7.8, 6.5, 5.5, 4.5 | #14: 6.5, 5.5, 3.5, 8.5). Source map complete. playmaking_validation.py built with 2-season 60/40 window. Expert-driven stat selection confirmed (S85-F01–F04). Scoring precision expanded to full decimal range (S85-F07).
- [x] Domain 5: Defense — **LOCKED.** All four sub-domains scored (#15: Irving 5.5, Fox 6.2, Smart 8.5, Hield 4.0 | #16: 5.2, 4.8, 8.5, 4.0 | #17: 2.5 all | #18: 2.5, 2.5, 5.5, 2.5). Source map complete. defense_validation.py built with 2-season 60/40 window. Deflections elevated to co-primary for #15 (S86-F01). DFGPOE confirmed as primary containment discriminator (S86-F04). Decimal precision applied (S85-F07).
- [x] Domain 6: Rebounding — **LOCKED.** Both sub-domains scored (#19: Irving 3.5, Fox 3.0, Smart 2.5, Hield 3.0 | #20: Irving 5.0, Fox 5.5, Smart 4.0, Hield 5.5). Source map complete. rebounding_validation.py v1 built (LeagueDashPlayerStats Advanced/Base + LeagueDashPtStats Rebounding + LeagueHustleStatsPlayer). S87-F01: Smart process-vs-output split on defensive rebounding.
- [x] Domain 7: Athleticism — **LOCKED.** All three sub-domains scored (#21: Irving 7.0, Fox 8.5, Smart 5.5, Hield 5.0 | #22: Irving 6.0, Fox 7.0, Smart 8.0, Hield 4.5 | #23: Irving 5.5, Fox 6.0, Smart 8.5, Hield 6.5). Source map complete. Combine data researched for all four guards. S87-F02: Smart width-based athletic profile. S87-F03: Fox/Irving opposite athletic archetypes.
- [x] Domain 8: IQ/Motor — **LOCKED.** All three sub-domains scored (#24: Irving 7.5, Fox 6.5, Smart 5.5, Hield 7.5 | #25: Irving 6.0, Fox 6.0, Smart 8.5, Hield 5.5 | #26: Irving 7.5, Fox 7.0, Smart 8.5, Hield 6.0). Source map complete. iq_motor_validation.py v1 built (LeagueDashPtShots closest defender + LeagueDashPlayerClutch + LeagueDashPtStats SpeedDistance). S88-F01: shot selection ≠ shot making. S88-F02: Smart inverse Domain 2/Domain 8 profile confirms archetype. S88-F03: hustle stat volume ≠ effort quality.
- **Note:** rebounding_validation.py v1 built and executed Session 87.
- **Note:** 26/26 sub-domains complete. Guard validation scoring is finished. Full pipeline run is next.
- **Pipeline issue flagged S88:** LeagueDashPtShots shot clock distribution — only "24-22" range returned data; all other ranges (Very Early through Very Late) returned null. Parameter investigation needed for correct shot clock range values in nba_api.
- **Documentation debt flagged:** Research & Methodology Log Entries 003-009 missing from some session close prompts — documentation present but may have gaps.
- [ ] Full pipeline run: all four guards through Layer A → B → C, verify composite tier placement against anchor library.

---

### Task S3 — Report Generation Layer
**Status: Not started. Depends on S2.**

Define and build the AI-generated scouting report system. The written report is the primary output of the product — not a secondary feature.

- [ ] Define prompt architecture: Layer 1 profile + raw data → narrative report
- [ ] Define output format: length, structure, tone, mobile readability
- [ ] Define data-sparse variant: how the report differs for thin-data international players
- [ ] Test against validation player set
- [ ] Calibrate tone against real scouting report samples

---

### Task S4 — Profile Design
**Status: Not started. Depends on S2.**

Design the public-facing player profile card. Mobile-first.

- [ ] Define layout hierarchy: what the user sees first, second, third
- [ ] Design confidence scoring range bar — prominent, not buried
- [ ] Define projection block display for draft-eligible players
- [ ] Define DNA comps display format
- [ ] Define one-line justification format per domain
- [ ] Define consensus range display alongside proprietary grade
- [ ] Prototype mobile layout

---

### Task S5 — Launch Profiles
**Status: Not started. Depends on S2, S3, S4.**

Build ~20–30 curated 2027 prospect profiles for pre-draft launch.

- [ ] Select final player list — archetype and data availability criteria
- [ ] Run full pipeline: data retrieval → Layer 1 → report generation → profile
- [ ] Quality review each profile before publish
- [ ] Target: profiles live before 2027 NBA Draft

---

### Task S6 — Frontend
**Status: Not started. Depends on S2 through S5.**

- [ ] Build public-facing site
- [ ] Profile search and display
- [ ] Confidence scoring visual — range bar
- [ ] Mobile optimization
- [ ] SEO foundations
- [ ] Domain decision: basketballratings.com vs hoopratings.com

---

## POST-LAUNCH TASKS

---

### Task S7 — Draft Ranking Module
**Status: Not started. Post-launch.**

Convert dimensional profiles into a ranked draft order with projected pick ranges. Reads directly from Layer 1 outputs — composite score, position, projection modifiers, confidence tier, age. Layer 2 is not involved.

- [ ] Cross-position normalization logic
- [ ] Consensus mock draft anchor
- [ ] Projection trajectory weighting
- [ ] Validate against current public consensus

---

### Task S8 — Scout-Facing Layer
**Status: Not started. Post-launch.**

- [ ] Shortlist generation feature
- [ ] Position-specific filtering
- [ ] Export functionality (CSV/HTML)
- [ ] Character profile layer
- [ ] Confidence scoring displayed transparently
- [ ] Team-specific fit analysis — Pro tier feature

**Monetization — Three-Tier Model (confirmed):**

| Tier | Access | Price |
|---|---|---|
| Free | Individual prospect profile, overall composite grade, domain breakdown, DNA comps, confidence scoring range bar, projected draft slot range, one-line justifications | Free |
| Pro | All free features + full draft class generation + team-specific fit analysis + real-time updates + comparison view + CSV/HTML export + API access | Subscription TBD |
| Scout/Agency | All Pro features + custom position filters + historical class archive + bulk export + white-label option | Enterprise TBD |

---

### Task S9 — Basketball Ratings Database
**Status: Not started. Post-launch. Depends on S2 through S6.**

- [ ] Named overall composite metric — must be decided before launch
- [ ] NBA tier coverage (450+ active players)
- [ ] College tier — Phase 2
- [ ] High school tier — Phase 3
- [ ] Public search interface
- [ ] SEO optimization
- [ ] Domain decision: basketballratings.com vs hoopratings.com

---

## DEFERRED WORKSTREAM — 2K GENERATOR

**Status: Deferred. Resume conditions below.**

What is built:
- 67/67 confirmed 2027 draft class builds in Ground Truth
- Translation tables built for all 8 domains (TRANSLATION_TABLES_v3.md — deferred)
- Development Modifier built (DEVELOPMENT_MODIFIER_v2.md — deferred)
- Layer B Position Relevance Filter built (deferred)
- Calibration Testing Log initialized (deferred)

Resume conditions:
- ~50 additional Layer 1 builds available
- Translation table density sufficient (minimum 3 data points per band per position)
- Layer 1 validated and locked

Pending when resumed:
- Step 1c — expand table density and validate
- Step 3 — Tier 2 and Tier 3 calibration testing
- Step 4 — full GT sweep
- Translation table Tier A / Tier B restructuring (SD-04)
- Phase 2 style modifier for multi-tool archetypes

---

## KEY ARCHITECTURAL DECISIONS (CONFIRMED)

| Decision | Resolution |
|---|---|
| Composite architecture | 26 sub-domains → tier assignment → composite. Assigned, not calculated. Formula retired permanently. |
| Domain scores | Readable profile summary only. Not calculation inputs. |
| Archetype system | Identification only. 25 archetypes across 3 groups. Not a calculation input. |
| Archetype weights | Qualitative reference only. ARCHETYPE-WEIGHTS_v3.md is not a formula input. |
| Non-negotiables gate | Position-based. Runs post-scoring. Failed gate flags structural ceiling and feeds Bust%. |
| Composite precision | Two decimal places. Earned from 26 sub-domain inputs. |
| R10 peer ranking | Mandatory before every sub-domain score. Rank is the input; scale description is the confirmation check. |
| Competition temper | Required for non-Power Conference and non-top-tier international stats. Not required for measured athleticism data. |
| Negative balance rule | Mandatory. Active search for negative signal on every build. Ceiling language maps to midpoint. |
| Projection Output Block | Min < POT < Max. Bust% driven by negative signals only — not data sparsity. |
| Selective effort | Distinct Bust% sub-category. +8–10% modifier vs +15–20% for general negative character. |
| DNA comp system | 2–3 comps per player. Position and archetype match required. Rookie TS% serves as Projection Midpoint validation cross-check (S98 unification). |
| Data pipeline | Option B — automated. AI-generated reports as proprietary output layer. |
| Longitudinal tracking | Core product vision. Requires automated pipeline. Task 5 engineering requirement. |
| Launch sequence | Track 1 (scouting tool + database) first. 2K generator deferred per SD-01. |
| Launch target | ~20–30 curated 2027 prospect profiles before the 2027 NBA Draft. |
| Monetization | Three tiers: Free / Pro / Scout-Agency. Team-specific fit is primary Pro upgrade trigger. |
| Named composite metric | Required before ratings database launch. Not yet decided. |
| 2K generator resume condition | ~50 additional Layer 1 builds required. Translation tables need density before generator is accurate. |

---

## OPEN QUESTIONS

1. What is the named overall composite metric?
2. Pro tier subscription price?
3. Scout/Agency tier pricing and white-label scope?
4. Domain: basketballratings.com vs hoopratings.com?
5. Is the ratings database a standalone product or a feature of the scouting tool?
6. What is the pass standard for S1 validation under the new architecture?
7. Wings position scale — when does POSITION_SCALE_WINGS_v1.md get built?
8. Bigs position scale — when does POSITION_SCALE_BIGS_v1.md get built?
9. Task S1 Phase 1: what is the pass standard for composite tier assignment accuracy? How many players, what error tolerance?
10. S89-O1: Domain score assembly redesign. Current raw average misrepresents profiles by including structural zeros. Fix: exclude N-weight sub-domains per archetype. Design decision needed before Wings/Bigs validation.
11. S89-O2: Output spec expansion. Full player profile needs: current season stats, career stats, player bio, scouting report, 26 sub-domain rationales, 8 domain rationales, composite rationale. Requires its own output specification document.
12. S89-O3: Architecture visualization corrections. Domain 7 has no dedicated script. SUB-DOMAIN-SOURCE-MAP governs both data sources and collection scripts.
13. Architecture restructuring plan adopted Session 89: scouting-rubric skill (554 lines) to be replaced by 5-skill chain (scout-research, scout-scoring, scout-profile, scout-composite, scout-output), each under 200 lines. Document splits planned: ARCHETYPE-WEIGHTS into 3 position-group files, COMPOSITE-SCALE-AND-TIERS into tier protocol + anchor library. Learnings system to be built from existing findings. Sessions 90–92 planned.

---

## PENDING DOCUMENT ACTIONS

| Document | Action | Status |
|---|---|---|
| COMPOSITE-SCALE-AND-TIERS.md | Rewrite — remove formula sections, add architectural statement, populate anchor library with all 21 player targets | **Complete — Session 66** |
| COMPOSITE_CALIBRATION_DATA_v5.md | Archive after migration confirmed complete | Session 64 Task 4 |
| ARCHETYPE-WEIGHTS_v3.md | Add qualitative-reference-only header label | Session 64 Task 5 |
| NON-NEGOTIABLES.md | Create standalone document — extract from POSITION-WEIGHTS-AND-NONNEG.md | Session 64 Task 6 |
| POSITION-WEIGHTS-AND-NONNEG.md | Archive after NON-NEGOTIABLES.md extraction confirmed complete | Session 64 Task 6 |
| scouting-rubric SKILL.md | Rewrite — remove domain aggregation, remove all 2K content, archive current version first | **Complete — Session 65** |
| POSITION_SCALE_WINGS_v1.md | Build from scratch | Pending |
| POSITION_SCALE_BIGS_v1.md | Build from scratch | Pending |
| TASK_S1_VALIDATION_LOG_v2.md | Create new — designed for new architecture | Task S1 Phase 1 |

---

*Last updated: Session 67*
