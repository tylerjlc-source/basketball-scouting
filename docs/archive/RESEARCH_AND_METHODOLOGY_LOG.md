# RESEARCH AND METHODOLOGY LOG
**Archived. Research log covering the architectural-build phase (Sessions 74–89). New external-research citations now live inline in the rule docs they ground (e.g., SCORING-RULES.md R3). Preserved here as audit trail for product credibility / methodology sourcing.**
**Started: Session 74**

---

## ENTRY 001 — R3 Competition Temper Redesign
**Session:** 74
**Decision:** Replace single-tier competition temper with a differentiated two-column system — full temper for shooting efficiency and turnover rate; minimal temper for assist rate, rebound rate, and block rate; steal rate reclassified as IQ proxy only.

**Research sources:**

1. Posting and Toasting (2022) — "Which statistics translate from college to the NBA?"
   - Dataset: All college/rookie season pairings from drafted rookies 2011–2019
   - Key finding: Rate stat correlations (NCAA → NBA): rebound rate 73%, assist rate 72%, block rate 70%, steal rate 23%
   - Key finding: Shooting correlations: FG% 40%, 3PT% 36%, FT% 27%
   - URL: https://www.postingandtoasting.com/2022/5/24/23139296/which-statistics-translate-from-college-to-the-nba

2. FloHoops (2018) — "How NCAA & EuroLeague Statistics Translate To The NBA"
   - Key finding: EuroLeague shooting stats are better NBA predictors than NCAA shooting stats
   - Key finding: Turnover rates remain high through year one and year two regardless of college or European origin — competition pressure increases at NBA level
   - Key finding: Blocks and rebounding translate well from both NCAA and EuroLeague (~60–80% explained)
   - URL: https://www.flohoops.com/articles/6253797-how-ncaa-euroleague-statistics-translate-to-the-nba-what-we-can-learn

3. Todd Schneider (2018) — "Assessing Shooting Performance in NBA and NCAA Basketball"
   - Dataset: 129,000 shots from 262 players appearing in both datasets
   - Key finding: Average FG% decline of ~4% on shots over 6 feet, and up to 15% on shorter shots, transitioning from college to NBA year one
   - URL: https://toddwschneider.com/posts/nba-vs-ncaa-basketball-shooting-performance/

4. Harvard Sports Analysis Collective (2020) — "Scouting NBA Three-Point Shooting"
   - Key finding: College FT% is a better predictor of NBA 3PT% than college 3PT% itself (34% vs 22% feature importance)
   - URL: https://harvardsportsanalysis.org/2020/10/scouting-nba-three-point-shooting/

5. Kevin Pelton / ESPN — "How My NBA Draft Projections Work"
   - Key finding: FT% rarely changes much in NBA transition; field goal percentages decline meaningfully
   - Key finding: Assists and steals per 100 team plays are used as direct translation inputs in his projection model — implying relative standing carries over
   - URL: https://www.espn.com/nba/story/_/id/16235135/explaining-kevin-pelton-nba-draft-projection-system

6. UNPLUGG'D / Aidan Berg (Medium, 2020) — "Steal Rates In College Just Might Be The Best Indicator Of NBA Success"
   - Key finding: College steal rate correlates with NBA success but not with NBA defensive statistics — players like Harden and Lillard had high college steal rates despite being poor NBA defenders; signals basketball IQ and anticipation, not defensive transferability
   - Key finding: Very high steal rates (e.g. Thybulle 6.7) can be inflated by system factors (Washington zone) — treat as signal with context, not direct translation
   - URL: https://medium.com/unpluggd-mag/the-relationship-between-steal-rates-and-nba-success-fbc8d668e9fa

**Reasoning:**
The research consistently shows that rate stats capturing positional skills (rebounding, playmaking, shot-blocking) transfer at 70–73% correlation from college to NBA. This is substantially higher than shooting efficiency stats (36–40%) and much higher than the 50% temper initially proposed. Applying a full competition temper to assist rate or rebound rate would meaningfully underweight skills that the data shows transfer almost intact. Turnover rate is treated as an efficiency stat because NBA transition consistently produces higher (not lower) turnover rates — the competition pressure increases, not decreases. Steal rate is reclassified entirely: the empirical evidence shows it predicts NBA success (IQ signal) but not NBA steal rate (skill signal), making it an unreliable direct input.

**Known limitation flagged at adoption:**
Positions that are rate-stat-heavy (PGs for assist rate, Cs for block/rebound rate) will receive lighter tempers on their primary skills relative to positions dependent on shooting efficiency. This may systematically produce higher composites for those positions at lower competition levels. Flag for review during validation testing — revisit if data shows systematic drift.

---

## ENTRY 002 — Qualitative Translation Temper (R3 Extension)
**Session:** 76
**Decision:** Extend R3 with a third column covering qualitative sub-domain observations. Seven sub-domains identified as requiring competition-level tempering before scores are assigned: #8 Handling/creation, #9 Touch/feel, #12 Decision-making, #13 Passing execution, #14 Off-ball movement, #15 On-ball pressure, #16 Help defense. Sub-domains grouped into four translation classes with different temper rates. #12 handled via scoring discipline rule rather than competition temper due to universal sub-domain status.

**Root cause this addresses:**
R3 tempers statistical inputs before they feed sub-domain scores. Qualitative sub-domain scores had no equivalent correction. A college player earning 8.0 on passing execution in the Big Ten was being treated as equivalent to an NBA player earning 8.0. Composite inflation of 0.25–0.40 points confirmed in Stirtz profile (Session 75). Qualitative sub-domain cluster identified as the source.

**Research sources:**

1. Playmakers League / Brian McCormick (sourced via web search, Session 76) — attributed to Brett Brown (Philadelphia 76ers): "while it's not uncommon for an NBA player to dramatically improve their shooting after they enter the league, very few seem to significantly improve their ball handling." Supports high translation rating for #9 (touch/feel) and physical component of #8 (handling). Establishes that mechanical skills are stable; creation quality requires separate treatment.

2. Posting and Toasting (2022) — same dataset as Entry 001. NCAA DRtg has ~0% correlation with NBA ORtg and only ~8% correlation with NBA DRtg. Single most important finding for #15 and #16. College defensive performance is nearly uninformative about NBA defensive output. Supports lower translation rating (upper end of temper range) for both defensive sub-domains.

3. Coates / Oguntimein, SAGE (2010) — "Assists in college translate one for one into assists per minute as a professional." Anchors assist rate translation. Distinct from execution quality — rate transfers; threading passes through NBA-level defensive traffic does not. Supports moderate translation rating for #13 (passing execution).

4. NFL Draft Diamonds (January 2026) — synthesising established basketball scouting frameworks: "Off-ball gravity, defensive rotations, and spacing awareness are portable across systems. These skills do not rely on usage rate or play-calling priority." Supports medium-high translation for #14 (off-ball movement). Same source: "Decision speed has proven more predictive of NBA success than raw assist totals" — supports the cognitive transferability component of #12.

5. No Ceilings NBA (December 2024) — G League scouting analysis: "Defensive statistics can be a mixed bag from player to player... I always encourage studying the defensive film." Confirms defensive sub-domains carry higher inflation risk than offensive qualitative sub-domains. Corroborates lower translation rating for #15 and #16.

**Sub-domain translation groups confirmed:**

| Group | Sub-domains | Translation | Temper at NCAA Power Conference |
|---|---|---|---|
| 1 — High | #9 Touch / feel | 90–95% | Lower end of column (5–10%) |
| 2 — Medium-high | #14 Off-ball movement | 85–90% | Lower-mid of column (10–15%) |
| 3 — Moderate | #8 Handling/creation; #13 Passing execution | 80–85% | Column value (15–20%) |
| 4 — Lower | #15 On-ball pressure; #16 Help defense | 75–80% | Upper end of column (20–25%) |

**#12 Decision-making — separate treatment:**
Universal sub-domain already scored against full NBA population. Problem is scoring discipline, not competition temper. Fix: scores above 7.0 for non-NBA players require in-session justification citing evidence of decision-making against advanced defensive schemes. Absence of justification caps #12 at 7.0.

**Known limitations flagged at adoption:**

- Qualitative temper values are first-generation estimates. No direct empirical dataset exists for qualitative sub-domain translation rates — values are inferred from adjacent statistical translation research and first-principles reasoning.
- Group boundaries (particularly Group 2 vs. Group 3) will require monitoring across validation builds. If systematic drift appears within a group, sub-domain may need reclassification.
- #12 scoring discipline rule effect on composite calibration not yet tested. Monitor across Stirtz revision and subsequent builds.

---

## Entry 003 — HS/EYBL Prospect Evaluation Test: R3 Temper Failure and Three Architectural Findings

**Session:** 77
**Test case:** Jordan Smith Jr. (Paul VI Catholic, VA → Arkansas commit, Class of 2026, 2027 draft eligible)
**Purpose:** First HS-level prospect evaluation through Layer 1 system. Tested R3 competition temper, R11 prospect ceiling, and Step 5.5 prospect gate against a data-sparse, high-school-only evidence base.

**Result:** Composite inflated to 7.65 (Tier 8 — NBA starter level) for a player who has not played a college game. System failed to produce realistic output at the HS competition level. Three specific architectural gaps identified.

**Finding 1 — Stacking rule lacks density and recency clause (CONFIRMED FIX — codified in SKILL.md v8)**

R3 Application Rule 3 states: "when a player has competed at multiple levels, the highest level achieved governs." Smith's handful of FIBA U17/U19 games (limited role-player minutes, prior summers) elevated his governing competition level from HS/EYBL (3.5–4.0) to FIBA U19 (5.5–6.0), nearly halving his temper. But 90%+ of his evidence base was current-season EYBL/HS.

Fix: The governing competition level is determined by where the majority of the most recent evidence comes from. "Most recent" = the current season. If early in a new season, the prior season. Alternatively: the most recent ~30 games. Higher competition levels achieved outside the current evidence window remain supplementary signals but do not govern the temper unless they represent the majority of current-season evidence.

Status: Confirmed by Tyler. Codified in SKILL.md v8.

**Finding 2 — Qualitative temper lacks mechanical scoring instruction (CONFIRMED CONCEPT — not yet codified)**

For statistical temper, the mechanism is clear: a percentage discount on an efficiency number. For qualitative temper, no equivalent instruction exists. "Elite HS defender after 35% temper" produced no clear scoring output — evaluator defaulted to judgment, which was biased upward by multi-source agreement.

Confirmed concept: Qualitative evidence places the player at a pre-temper score (capped at R11's 7.5 ceiling). The temper percentage is then applied as a multiplicative reduction from that pre-temper score. Formula: Tempered score = Pre-temper score × (1 − qualitative temper %).

Example: Elite HS defender → pre-temper 7.5 × (1 − 0.20) = 6.0 at Power Conference level. At FIBA U19 (30–35%): 7.5 × 0.675 = ~5.1. Physical sub-domains remain exempt.

Status: Concept confirmed by Tyler. NOT yet codified in SKILL.md — pending further validation across more prospect builds before committing to the multiplicative formula. Current SKILL.md qualitative temper language remains as-is until Tyler directs codification.

**Finding 3 — "Directional only" lacks scoring translation (OPEN)**

At HS/EYBL competition levels (3.5–4.0 and below), the R3 competition table reads "directional only" for qualitative sub-domain temper. The multiplicative concept from Finding 2 works for levels with a stated percentage but provides no instruction for directional-only levels. Open questions: (1) What does "directional only" translate to as a scoring range? (2) Can physical sub-domain support lift a directional-only score above midpoint? (3) Does character/motor evidence spanning multiple competition levels earn any exception?

Status: Open. Flagged as prerequisite for HS-level evaluation. Do not attempt HS prospect builds until resolved.

**Smith profile status:** Working draft — parked. Sub-domain scores embedded below as pre-fix baseline for comparison when architecture is corrected.

Pre-fix sub-domain scores (Session 77, pre-correction):
#1: 7.0 | #2: 6.5 | #3: 4.5 | #4: 4.0 | #5: 4.5 | #6: 5.0 | #7: 4.5
#8: 6.0 | #9: 6.0 | #10: 6.5 | #11: 5.5 | #12: 6.0 | #13: 5.5 | #14: 6.5
#15: 7.5 | #16: 7.0 | #17: 4.0 | #18: 5.5 | #19: 6.0 | #20: 7.0
#21: 7.5 | #22: 7.0 | #23: 7.5 | #24: 6.5 | #25: 7.5 | #26: 7.5
Pre-fix composite: 7.65 (inflated — confirmed)

**Sequence recommendation (confirmed by Tyler):**
1. Run more 2026 draft Guard prospects to validate R3 at different competition levels and archetypes
2. Build Wing and Big position scale documents (blocking all non-Guard evaluation)
3. Log Smith findings as architectural prerequisites for HS evaluation
4. Return to HS prospects only after Steps 1–2 produce calibration data

---

### Entry 004 — Sub-Domain Source Map Data Access Audit (Session 81)

**Research question:** For each sub-domain, what statistical sources exist, are they accessible, and can they be automated?

**Method:** Web search investigation of all potential basketball data sources — APIs, subscription sites, scraping targets. Evaluated access model, cost, coverage level, and API availability for each.

**Key findings:**

1. NBA-level data is largely solved via nba_api (free, automated). Restricted area FG%, play type data, player tracking — all available programmatically.

2. College-level data has three tiers:
   - Free + buildable: Hoop-Math (rim FG%, shot distribution), CBBpy (ESPN PBP with shot type labels), Basketball-Reference (box score stats)
   - Paid + manual: EvanMiya ($30/mo, opponent-adjusted stats, no confirmed API), Cleaning the Glass ($5/mo, NBA only, no API)
   - Inaccessible: Synergy/Sportradar (play-type data, requires B2B org relationship)

3. Synergy play-type data (post-up PPP, at-rim percentile, etc.) regularly appears cited in published scouting reports. Capturing these during web search research is a functional workaround for individual player builds.

4. Post offense (#3) is the most data-constrained sub-domain at the college level. The primary stat (post-up PPP) is locked behind Synergy. Absence of post-up data is itself a signal per SUB-DOMAINS.

5. Web search cannot surface zone-specific shooting data (restricted area FG%) — it lives in structured HTML tables. Validates the need for the nba_api pipeline as an infrastructure build.

6. EvanMiya's 2PT% is opponent-adjusted and usage-adjusted but blends rim with non-rim twos. Useful as a corroboration signal, not a primary for at-basket finishing specifically.

7. EvanMiya pricing confirmed: $29.99/mo or $179.99/yr. Cleaning the Glass: ~$5/mo. Total data subscription cost: ~$35/mo.

**Status:** Findings applied to SUB-DOMAIN-SOURCE-MAP_v1.md. Domain 1 complete. Domains 2-8 pending.

---

### Entry 005 — Domain 1 Validation: First Automated Pipeline Test (Session 82)

**Session:** 82
**Test case:** Four NBA guards (Kyrie Irving, De'Aaron Fox, Marcus Smart, Buddy Hield) — Sub-Domain #1 (At-Basket Finishing) and partial #2 (Contact Finishing / Foul Drawing).
**Method:** Built finishing_data.py using nba_api. Pulled restricted area FG%, % shots at rim, dunk rate, non-dunk rim FG%, FT%, FTA/game for 2024-25 season. Scored provisionally using POSITION_SCALE_GUARDS_v1.md with R10 peer ranking protocol.

**Finding S82-F01 — Rim FG% alone fails to discriminate among guards.**
Four-guard validation: Irving 67.6%, Fox 65.8%, Smart 65.4%, Hield 65.2% — only 2.4 percentage point spread across players who should be dramatically different finishers. Volume context (% of shots at rim + raw rim FGA) is the discriminator. Smart's 26 rim attempts across a full season at 21 MPG is definitive evidence of a non-finisher — not data sparsity. Volume elevated to co-primary alongside rim FG% in SUB-DOMAIN-SOURCE-MAP_v1.md.

**Finding S82-F02 — Dunk rate separates craft from athleticism.**
Irving at 0.5% dunk rate vs Fox at 8.6%. Non-dunk rim FG% reveals true finishing touch: Irving 67.4% vs Fox 62.6%. However, non-dunk rim FG% should NOT be elevated to primary because it would penalize legitimately athletic finishers (Giannis, Ja) whose dunking IS their finishing skill. Dunk rate is a style descriptor, not a quality ranking.

**Finding S82-F03 — Low volume at real minutes IS the signal.**
Smart's 26 rim attempts across a full season at 21 MPG is not data sparsity — it's definitive evidence that he's not a finisher. High confidence that he's a non-finisher. The absence is the data.

**Sub-Domain #2 partial validation (derived from existing data):**
FTR (FTA/FGA): Irving .228, Fox .293, Smart .251, Hield .083. Fox leads over Irving because he seeks contact; Irving finishes around it. Hield at sub-1 FTA/game across 82 games is definitive. Missing stats identified for script build: drive rate, paint FG%, AND1%.

**Provisional scores assigned (Session 82):**

| Sub-Domain | Irving | Fox | Smart | Hield |
|---|---|---|---|---|
| #1 At-Basket Finishing | 9.5 | 8.0 | 5.0 | 5.0 |
| #2 Contact Finishing | 7.0 | 7.5 | 5.5 | 4.0 |

Scores are provisional — may shift when additional stats (finish rate against shot blockers, drive rate, paint FG%, AND1%) are added to the pipeline.

**Pipeline architecture decided (Session 82):**
- Layer A — Data Collection: deterministic Python scripts hitting APIs, returning structured JSON. Also web search pass collecting scouting report text. No AI.
- Layer B — Intelligence: single Claude API call with full system prompt (SKILL.md + SUB-DOMAINS + Position Scale + Source Map). Receives entire Layer A output. Scores all 26 sub-domains in one call.
- Layer C — Assembly: deterministic. Computes domain scores, suggests composite tier placement, generates player card.

**Precision principle established:** For every sub-domain, interrogate all primary and secondary stats before moving on. Test for each stat: would this change a score, or just confirm one? Stats that can move the needle are required for scoring. Stats that only confirm are enrichment — they increase confidence but don't block scoring.

**Build sequence confirmed:** Research → Source Map → Script → Run Test Guards → Validate Discrimination → Score from Position Scale → Confirm Score Matches Expectation → Lock.

**Infrastructure finding:** stats.nba.com is blocked by Claude.ai's container egress proxy. Scripts must run in Claude Code or local Python environment. Web search cannot surface zone-specific shooting data — validates nba_api pipeline requirement.

**Status:** Domain 1 #1 validated, #2 partially validated, #3 baseline confirmed. Script update needed before Session 83. Domains 2-8 pending.

---

### Entry 006 — Session 83: Domain 1 Lock, Domain 2 Complete, Pipeline Architecture Update

**Date:** 2026-04-11
**Session:** 83

**Domain 1 — LOCKED**
Final scores for four test guards:

| Sub-Domain | Irving | Fox | Smart | Hield |
|---|---|---|---|---|
| #1 At-Basket Finishing | 9.5 | 8.5 | 5.0 | 5.0 |
| #2 Contact Finishing | 7.0 | 7.5 | 5.5 | 4.0 |
| #3 Post Offense | 2.5 | 2.5 | 2.5 | 2.5 |

Fox #1 elevated 8.0 → 8.5 based on drive volume (15.2/game), rim volume (243 FGA), and .658 rim FG%.

**Domain 2 — Scored (provisional, pending 2-season re-pull)**

| Sub-Domain | Irving | Fox | Smart | Hield |
|---|---|---|---|---|
| #4 CAS 3PT | 9.0 | 6.0 | 6.0 | 8.5 |
| #5 Off-Dribble | 9.3 | 5.5 | 3.5 | 3.0 |
| #6 Mid-Range | 8.5 | 7.5 | 3.0 | 3.5 |
| #7 Free Throw | 9.5 | 7.0 | 6.0 | 7.5 |

Fox and Smart data carries medium confidence due to multi-season data bleed (S83-F05). Scores may adjust after clean 2-season re-pull.

**Findings:**

S83-F01: Per-game FTR rounding causes drift. Totals-based FTR (total FTA / total FGA) is authoritative. All future FTR computations must use season totals.

S83-F02: nba_api cannot filter % assisted or defender distance to restricted-area shots only. Rim-specific assisted % and rim-specific contest data require Synergy access or manual film review. Known pipeline limitation.

S83-F03: Drive tracking data (drives/game, drive FG%, drive FTA) is the strongest new discriminator for both #1 and #2. Separates all four archetypes cleanly.

S83-F04: Fox #1 elevated 8.0 → 8.5. Drive volume, rim volume, and rim FG% support All-Star caliber finishing.

S83-F05 (revised): ShotChartDetail endpoint bleeds across seasons for traded players. Formalized as design decision: 2-season evaluation window with 60/40 recency weighting (current/prior) is the default for NBA-level evaluation. Single-season splits are too noisy for decimal-precision scoring.

S83-F06: Pull-up zone split (ShotChartDetail ACTION_TYPE classification) works. Confirmed as viable pipeline architecture for #5/#6 boundary. Pull-up 3s feed #5, pull-up mid-range feeds #6.

**Architectural decisions:**
- 2-season 60/40 window formalized for all NBA evaluation
- Pull-up zone split confirmed: pull-up 3PT → #5, pull-up mid-range → #6
- Volume-weighted percentages for shooting stats, simple weighted average for rate stats
- Domain 2 source map completed and integrated into SUB-DOMAIN-SOURCE-MAP

**Pipeline status:**
- finishing_data.py — needs v3 update for 2-season window
- shooting_validation.py — needs v2 update for 2-season window + clean season filtering
- Domain 1 source map — complete and locked
- Domain 2 source map — complete, pending integration via Claude Code
- Domains 3-8 source maps — not yet built

---

### Entry 007 — Session 84: Expert-Driven Stat Selection Method + Domain 3 Source Map + Scoring

**Date:** Session 84
**Topic:** Domain 3 (Ball Skills) source map build, data collection, and scoring

**Research conducted:**
- Web search for expert consensus on measuring ball handling, touch, and ball security
- BBall Index talent grade methodology (One on One grade uses driving data + Synergy ISO/Handoff)
- Counting the Baskets analysis: TOV per 100 touches vs standard TOV%
- Harvard Sports Analysis Collective: turnover percentage as preferred normalization
- Cleaning the Glass: TOV% and offensive overview methodology
- NBA tracking data (Wikipedia): touches, time of possession, dribbles per touch definitions
- Scouting report research for qualitative validation: Irving, Fox, Smart, Hield

**Findings:**
- S84-F01: Expert-driven stat selection method formalized. Chain: what do experts say best measures this skill → select those stats → source them.
- S84-F02: Qualitative validation step confirmed as mandatory for all players. Produces justifying sentence beside score.
- S84-F03: TOV per 100 touches is expert-preferred ball security metric. League average ~3.8.
- S84-F04: Smart ball security — 5.06 TOV/100 touches confirmed by multi-source scouting language. Defensive IQ ≠ offensive ball security.
- S84-F05: Play-type creation data (ISO PPP, PnR BH PPP, Handoff PPP) is primary for #8. Process metrics (TOP, drib/touch) are role descriptors only.
- S84-F06: Touch/feel (#9) is ~70% qualitative. FT% is primary proxy. Floater-range FG% (4–14 ft) is only net new data stream.
- S84-F07: Hield ball security — 2.62 TOV/100 touches is role-driven (catch-and-shoot), not skill-driven. Scored accordingly (6.5).

**Scores locked:**
- #8 Handling/Creation: Irving 9.5, Fox 8.0, Smart 5.5, Hield 4.5
- #9 Touch/Feel: Irving 9.5, Fox 7.0, Smart 5.5, Hield 6.0
- #10 Ball Security: Irving 8.0, Fox 7.0, Smart 5.0, Hield 6.5

**Script built:** ball_skills_validation.py — pulls play-type creation, tracking possessions, floater-range shots, TOV/touch, clutch data. 2-season 60/40 window.

---

### Entry 008 — Session 85: Expert-Driven Stat Selection for Domain 4 (Playmaking) + Source Map + Scoring

**Date:** Session 85
**Topic:** Domain 4 (Playmaking) source map build, data collection, and scoring

**Research conducted:**
- Web search for expert consensus on measuring court vision, decision-making, passing execution, and off-ball movement
- BBall Index Playmaking Talent methodology: 5 components (Passing Creation Volume, Passing Creation Quality, Passing Versatility, Passing Efficiency, On-Ball Gravity)
- BBall Index Off-Ball Movement grade: Synergy Cut + OffScreen play types + player tracking average velocity
- BBall Index passing stats guide: potential assists, secondary assists, FT assists, high-value assists, quick decision-making assists
- NBA Underground passing analysis: potential assists as teammate-independent creation metric, adjusted assist %, TOV/potential assists ratio
- Ben Taylor / Backpicks / Thinking Basketball: Box Creation, Passer Rating (1-10 scale using assists, offensive load, A:TO, height, turnovers²)
- Academic research: secondary assists correlate with team shot quality and spacing (Journal of Performance Analysis in Sport, 2022)
- SI.com, NBAstuffer: potential assist definitions and tracking methodology (Second Spectrum, since 2013-14)
- nba_api endpoint verification: LeagueDashPtStats (Passing, SpeedDistance), SynergyPlayTypes (Cut, OffScreen, Transition), LeagueDashPlayerStats (turnover type breakdown)
- Scouting report research for qualitative validation: Irving, Fox, Smart, Hield

**Findings:**
- S85-F01: Potential assists (not raw assists) are the expert-preferred primary stat for court vision. Removes teammate shooting quality dependency.
- S85-F02: Turnover type breakdown (bad pass TOV vs. lost ball TOV) is the primary statistical discriminator between decision-making (#12) and ball security (#10). nba_api provides this split.
- S85-F03: Passing execution (#13) is ~80% qualitative — no public stat directly measures pass accuracy, velocity calibration, or lob timing. FT assists are the strongest available proxy. Coherence rule established: #13 should track within ±1.0 of #9 (Touch/Feel).
- S85-F04: BBall Index Off-Ball Movement grade confirmed as methodological reference — uses Synergy Cut + OffScreen play types as primary inputs. Adopted for #14.
- S85-F05: Smart off-ball movement is zero — literally no cut or off-screen possessions across two seasons. Same "absence is the signal" pattern as Domain 1 finishing (S82-F03).
- S85-F06: Hield transition decisions (55th percentile, 9.3% TOV) outperform Irving (25.5th pctile) and Fox (33.5th pctile). Simple role = fewer decision errors. Role-driven performance, similar to S84-F07.
- S85-F07: Scoring precision expanded beyond .0/.5 increments. Scale supports one decimal place — finer placement used when data warrants (Irving #11 = 7.3, Hield #12 = 6.3, Irving #13 = 7.8, Smart #14 = 3.5).

**Scores locked:**
- #11 Court Vision: Irving 7.3, Fox 7.0, Smart 6.0, Hield 4.0
- #12 Decision-Making: Irving 7.5, Fox 7.0, Smart 6.0, Hield 6.3
- #13 Passing Execution: Irving 7.8, Fox 6.5, Smart 5.5, Hield 4.5
- #14 Off-Ball Movement: Irving 6.5, Fox 5.5, Smart 3.5, Hield 8.5

**Script built:** playmaking_validation.py — pulls passing tracking data, turnover breakdown, Synergy cut/off-screen/transition, speed/distance. 2-season 60/40 window.

---

### Entry 009 — Session 86: Domain 5 (Defense) Source Map + Scoring

**Date:** Session 86
**Topic:** Domain 5 (Defense) source map build, data collection, and scoring

**Research conducted:**
- Web search for expert consensus on measuring on-ball defense, help defense, rim protection, and post defense
- BBall Index defensive metrics methodology: On-Ball Defense, Matchup Difficulty, Perimeter Isolation Defense, Passing Lane Defense (deflections + intercepted passes), Help Defense Talent, Rim Protection, Defensive Playmaking, D-LEBRON, Defensive Positional Versatility, Defensive Roles
- BBall Index All-Defensive team write-ups (2022, 2025): Thybulle 1st in On-Ball Defense + Passing Lane Defense; Smart DPOY with elite Matchup Difficulty; McDaniels 98th percentile Matchup Difficulty + Perimeter Isolation Defense
- FiveThirtyEight DRAYMOND metric: opponent shooting-based, DFGPOE + DFGA Rate as primary components
- Best Ball Stats Tracking Defensive Plus Minus: deflections > steals for measuring defensive disruption; DFGPOE + DFGA Rate for shot contesting
- NBA.com Defensive Pressure Score (AWS partnership): 0-1 scale, frame-level tracking
- nba_api endpoint verification: LeagueDashPtDefend (6 DefenseCategory values confirmed), LeagueHustleStatsPlayer (contested shots/deflections/charges/loose balls/box-outs), SynergyPlayTypes (PostUp + Isolation defensive), LeagueDashPlayerStats (base + advanced)
- Scouting report research for qualitative validation: Smart (DPOY, multi-source elite consensus), Fox (tools without commitment), Irving (average), Hield (liability)

**Findings:**
- S86-F01: Deflections elevated to co-primary alongside opponent FG%/DFGPOE for #15 (On-Ball Pressure). Expert consensus: deflections are more reliable than raw steals for measuring defensive disruption because steals include loose ball recovery randomness.
- S86-F02: Help defense (#16) is the most qualitative defensive sub-domain. No single public stat captures rotations, weak-side positioning, or help-and-recover execution. Team DRtg on/off + hustle activity metrics are directional only.
- S86-F03: Rim protection (#17) and post defense (#18) confirmed near-baseline for all four test guards at high confidence. N/A returned for opponent FG% at rim for all guards — guards don't defend shots at the rim as closest defender. Same "absence is the signal" pattern as #3 and Smart's #14.
- S86-F04: DFGPOE (Defensive FG% Over Expected) is the single strongest discriminator for on-ball containment quality. Smart (-4.6%) is the only test guard with a negative value — the only one who actually makes opponents shoot worse. Irving (+1.1%), Fox (+2.1%), Hield (+2.9%) all make opponents shoot better.
- S86-F05: GUARD_VALIDATION_SCORES_v1.md had incorrect labels for #18-26. "Switchability" and "Steals/Passing Lane D" were listed as Domain 5 sub-domains but do not exist in SUB-DOMAINS_v3.md. Labels corrected to match the authoritative source. No scores were affected (all rows were Pending).
- S86-F06: LeagueDashPtDefend 3 Pointers and Greater Than 15Ft zone splits returned N/A for all four guards. The endpoint may not break out these categories at the individual player level for guards, or the data may require different query parameters. Flagged for pipeline investigation.
- S86-F07: Irving/Fox help defense flip — Fox is the better on-ball defender (#15: 6.2 vs 5.5) but Irving shows more help-side activity (#16: 5.2 vs 4.8). Different defensive profiles at similar overall levels.

**Scores locked:**
- #15 On-Ball Pressure: Irving 5.5, Fox 6.2, Smart 8.5, Hield 4.0
- #16 Help Defense: Irving 5.2, Fox 4.8, Smart 8.5, Hield 4.0
- #17 Rim Protection: Irving 2.5, Fox 2.5, Smart 2.5, Hield 2.5
- #18 Post Defense: Irving 2.5, Fox 2.5, Smart 5.5, Hield 2.5

**Script built:** defense_validation.py — pulls LeagueDashPtDefend (4 zone categories), LeagueHustleStatsPlayer, LeagueDashPlayerStats (base + advanced), SynergyPlayTypes (PostUp + Isolation defensive). 2-season 60/40 window.

**Discrepancy found and resolved:** SUB-DOMAINS_v3.md (locked, authoritative) defines Domain 5 as 4 sub-domains (#15-18). Opening prompt and GUARD_VALIDATION_SCORES had 5 defensive sub-domains (#15-19) with different names. Resolved: fix labels to match SUB-DOMAINS_v3. Domain 5 has 4 sub-domains, not 5.

---

### Entry S88-001: Shot Selection vs. Shot Making Distinction

**Session:** 88
**Sub-Domain:** #24 Shot Selection
**Finding:** Shot selection and shot making are distinct dimensions. Expert consensus (BBall Index, Second Spectrum) separates the two: selection = which shots you take, making = how well you convert. The primary statistical discriminator for selection quality is the closest-defender openness distribution (LeagueDashPtShots), not raw eFG% or TS%. Irving's 51.5% contested rate would indicate poor selection in isolation — but his elite conversion at tight-contest range (51.1% eFG) justifies the aggressive diet. Hield's 37.4% wide-open rate reflects excellent selection achieved through role discipline rather than creation skill.
**Status:** Codified in SUB-DOMAIN-SOURCE-MAP #24 Block A.

### Entry S88-002: Hustle Stat Volume vs. Effort Quality

**Session:** 88
**Sub-Domain:** #25 Effort/Motor
**Finding:** 82games.com research shows non-steal deflections negatively correlate with team winning. Deflection volume alone measures activity, not quality. Fox leads all test guards in deflections (3.33/g) and contested shots (4.37/g) but has documented defensive effort gaps and scores 6.0 on #25. The position-neutral effort signal hierarchy per expert research: deflections + loose balls (co-primary, least position-biased) > charges (sacrifice signal) > contested shots and box-outs (position-contaminated). Smart's 3x Hustle Award validates this hierarchy — he leads in charges and box-outs (sacrifice + positioning) despite not leading in raw deflections.
**Status:** Codified in SUB-DOMAIN-SOURCE-MAP #25 Block A.

### Entry S88-003: Competitive Character — Negative Signals More Predictive

**Session:** 88
**Sub-Domain:** #26 Competitive Character
**Finding:** Expert research (FanSided scouting factors study) confirms that outside observers struggle to predict competitive character in 19-20 year olds, but negative signals ("soft," "folds," "wilts") are more reliably predictive than positive signals ("tough," "competitor"). Our SUB-DOMAINS definition aligns: negative language overrides positive in multi-source contexts. For NBA evaluation, multi-source coach/teammate/opponent testimony is the highest-credibility signal. Statistical clutch data (LeagueDashPlayerClutch) is supplementary — confirms or contradicts the qualitative picture but doesn't independently establish character. Smart's profile (8.5) validated by convergence across 5+ independent sources (Stevens, Lue, Brown, Horford, Ainge). Irving's profile (7.5) demonstrates the off-court character flag ceiling — on-court big-moment performance is elite but multiple program disruptions cap below 8.0.
**Status:** Codified in SUB-DOMAIN-SOURCE-MAP #26 Block C weighing note.

---

### Entry S89-001: Guard Validation Pipeline — Full Run Confirmed

**Session:** 89
**Topic:** End-to-end guard validation pipeline execution and composite assignment

**Results:**
- All four test guards scored through complete Layer A → B → C chain
- Composite assignment via 6-step Tier Assignment Protocol validated
- Fox (8.51) and Hield (7.05) reproduced existing anchor placements — system self-validates
- Irving (8.78) and Smart (7.90) are fresh assignments confirmed by Tyler
- Key calibration finding: Irving's offensive skill concentration (9 sub-domains at 7.5+) is among the most elite guard profiles in the anchor library; defense/effort drag correctly places him upper Tier 5, not Tier 4
- Smart's placement moved from initial 7.85 to 7.90 after Lakers resurgence confirmed Tier 7 floor; DPOY skill set validated as current, not just historical
- Architecture restructuring plan adopted: 5-skill chain replacing single scouting-rubric skill; document splits; learnings system

**Status:** Guard validation complete. Architecture restructuring planned for Sessions 90–92.
