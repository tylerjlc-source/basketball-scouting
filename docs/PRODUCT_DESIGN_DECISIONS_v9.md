# Draft Class Generator — Product Design Decisions
**Decisions captured at the time made (last updated Session 64). For current-state rubric, scales, tier table, and archetype list, see the documents linked from CLAUDE.md DOCUMENT MAP. PDD records decision history and rationale; downstream docs are the current-state source.**
**Living Document — Resolved decisions only. Open questions live in the Roadmap.**

---

## PURPOSE

This document records every significant product and technical design decision made during development. Each entry logs what was decided, why, and what was explicitly rejected. The goal is to prevent relitigating resolved questions in future sessions and to give any new collaborator a clear picture of where the product stands and why.

---

## SECTION 1 — PRODUCT VISION AND TWO-PRODUCT ARCHITECTURE

**Two products. One rubric.**

**Product 1 — Real-world scouting tool**
An AI-powered prospect discovery platform for scouts, agents, and college programs. The broad coverage pass — who deserves deeper evaluation — is currently done manually. We automate it. The tool aggregates publicly available data: stats, biometrics, qualitative scouting reports, character descriptors, and social media signals. It generates structured prospect profiles faster and more consistently than any manual process.

**Product 2 — Public-facing ratings database**
Built on the same rubric. Covers NBA, college, and high school players. Longitudinal tracking from high school through the NBA — the same player followed across years, updated as new data arrives. Every number is explainable. The composite answers one question: how good are you at basketball, period. Not how good at your role. Not how good relative to your archetype. Overall basketball ability.

**The moat**
Every competitor has the same structural blind spot on international players. Video tools require footage that doesn't exist for most non-top-circuit players. Recruiting tools cover the US pipeline only. Draft media covers the consensus top 30. Our tool covers players when no competitor can. Confidence intervals are wider for data-sparse prospects — displayed transparently, not hidden. A wide-confidence structured profile is more useful than nothing.

**The engine (brief)**
Three signals: statistical comp model, qualitative signal processing, and rubric fallback. Confidence scoring drives Min/Max spread. More signals produce tighter ranges. Less data means wider spread and higher Bust% — shown openly.

**Long-term vision**
Longitudinal tracking from high school through the NBA. Same player, same system, same rubric across their entire career. Profile updates as new data arrives. This is only achievable with an automated pipeline.

---

## SECTION 2 — LAYER 1 SYSTEM ARCHITECTURE

**The architecture**

```
26 sub-domain scores → tier assignment → composite
```

Each of the 26 sub-domains is scored 1–10 against a position-specific peer group. Those scores feed directly into tier assignment. The composite is then assigned from the tier table — it is not calculated from a formula.

**Domain scores**
Domain scores still exist. They are a readable profile summary — a useful way to see where a player is strong and where they drag. They are not calculation inputs. Nothing downstream depends on them mathematically.

**Composite is assigned, not calculated**
The tier table in COMPOSITE-SCALE-AND-TIERS.md is the primary assignment tool. Every tier band is anchored by named confirmed examples. The evaluator reads the 26 sub-domain scores, identifies the tier the player fits, and assigns the composite from within that band. The anchor examples are the calibration mechanism.

**What was rejected and why**
A formula-based approach was tested through Session 63 across multiple designs. Every formula that worked for one player broke another. The root problem: a weighted average across 26 sub-domains compresses all profiles toward the middle. High-tier players with real weaknesses score lower than their basketball reality. Low-tier players with concentrated strengths score higher. No weighting scheme solved this without becoming player-classification-dependent — which is not scalable. The formula approach is permanently retired.

**What this changes**
The archetype weight tables in ARCHETYPE-WEIGHTS_v3.md are qualitative reference only. They describe what drives NBA value per archetype. They are not formula inputs. See Section 4.

---

## SECTION 3 — SCORING PROTOCOL

**R10 — mandatory peer ranking step**

Before assigning any sub-domain score, answer: among active players in this peer group, where does this player rank at this specific skill?

The ranking is the input. The scale description is a confirmation check. If the rank and the description conflict, the rank wins.

The ranking must integrate both quantitative signals (statistics, efficiency, volume, consistency) and qualitative signals (league-wide consensus, scouting reports, credible analyst and coach assessments). No single statistic determines the rank. If the ranking is driven by one statistic alone, identify at least one additional signal before assigning the score.

**Peer group and precision**
Peer groups are position-specific. Scores are expressed to one decimal place. Position-specific scales are loaded per evaluation — POSITION_SCALE_GUARDS_v1.md is confirmed. Wings and Bigs scales are pending.

**Evaluation window**
- Active player → rank current ability
- Retired player → rank at career median
- Injured player → rank based on last active season

**Talent vs. impact**
The rubric measures capability, not role production. A player in a bad system with low usage can still have elite grades. Impact data — box scores, on/off splits, advanced metrics — is a genuine signal. It measures what a player does with their talent. The discipline is contextualization, not rejection. Competition level, coaching system, and role are applied before impact data informs a grade.

**Competition temper**
Non-Power Conference and non-top-tier international stats require tempering before they inform a score. Measured athleticism data (wingspan, vertical, sprint times) requires no temper — it is position-independent physical evidence.

**Sourcing hierarchy**
Signal credibility ranking, highest to lowest:

1. Measured combine/biometric data
2. Multi-season Power Conference stats
3. Single-season Power Conference stats
4. Multi-circuit EYBL/AAU stats (with competition temper)
5. International stats (with competition-level temper)
6. Independent multi-source qualitative scouting reports
7. Single-source qualitative scouting report
8. Recruiting-context coach quotes (directional only)
9. Camp and combine performance (directional)
10. Social media and character signals (directional)
11. Age-relative developmental signals (directional)
12. Physical projection signals (directional)

**Negative balance rule**
Mandatory on every build. For every attribute set above position baseline, an active search for a negative signal is required. Where no negative signal exists, set the score at the midpoint of what positive sourcing supports — not the ceiling. Ceiling-framing language in scouting reports maps to the midpoint, not the ceiling. Recruiting-context quotes are directional only and never serve as primary justification for any score.

---

## SECTION 4 — ARCHETYPE SYSTEM

**Purpose**
Archetype identifies what kind of player this is. It is an identification step, not a calculation input. Nothing in the composite calculation depends on archetype. Archetype guides tier assignment by pointing the evaluator toward the most relevant anchor examples in the tier table — it narrows the comparison set, it doesn't run math.

**25 archetypes across three positional groups**

Guards (9):
Jumbo Playmaker | Offensive Engine | All-Around Guard | 3-and-D Guard | Pure Point Guard | Microwave Scorer | Slasher | Shooting Specialist | Defensive Specialist

Wings (10):
All-Around Wing | Modern Four | 3-and-D Wing | 3-and-some-D Wing | Dribble Pass Shoot Wing | Secondary Playmaker | Score-First Wing | Shooting Specialist | Defensive Specialist | Defensive-Engine Playmaker

Bigs (6):
All-Around Big | Switchable Big | Rim Protector | Stretch Big | Versatile Scoring Big | Energy Big

**Archetype identification**
Archetype is identified before scoring begins. It sets context — which sub-domains are structurally irrelevant for this player type, which anchor examples are the right comparison set, what the value profile looks like for players who project similarly. It does not change how sub-domain scores are assigned. R10 peer ranking applies regardless of archetype.

**ARCHETYPE-WEIGHTS_v3.md**
The weight tables in this document are qualitative reference only. They describe what drives NBA value per archetype — which skills matter most for each player type. They are useful context for tier assignment and for understanding a player's profile. They are not formula inputs and play no calculation role under the current architecture.

---

## SECTION 5 — NON-NEGOTIABLES GATE

**Purpose**
The non-negotiables gate is a hard check that runs independently of the composite. Certain skills are survival thresholds at each position. A player who fails them has a structural ceiling that the composite alone does not capture.

**Position-based, not archetype-based**
Gate thresholds are determined by position label, not archetype. The five position labels — PG, SG, SF, PF, C — determine which thresholds apply. Archetype does not modify the gate.

**When it runs**
After sub-domain scoring is complete, before composite assignment. The gate is a post-scoring check, not a scoring input.

**What a failed gate means**
A failed gate is flagged explicitly in the player profile. It does not zero out the composite. It caps the projection ceiling and feeds directly into Bust%. A player can have a strong composite and a failed gate simultaneously — the flag communicates that the ceiling is lower than the composite alone suggests.

**Relationship to the negative balance rule**
These are distinct mechanisms. The negative balance rule operates during scoring — it governs how negative signals affect individual sub-domain scores. The non-negotiables gate operates after scoring — it checks whether the finished profile clears position-specific survival thresholds. Both are mandatory. Neither replaces the other.

**Reference document**
Non-negotiables are stored in NON-NEGOTIABLES.md. Load this document for every evaluation. See Task 6 for the creation of this standalone document.

---

## SECTION 6 — COMPOSITE TIER ASSIGNMENT AND ANCHOR LIBRARY

**The tier table**

The tier table in COMPOSITE-SCALE-AND-TIERS.md is the primary assignment tool. 12 bands spanning 1.00–10.00. Every band is anchored by named confirmed players that define what a profile in that range looks like.

| Composite | Tier |
|---|---|
| 9.70–10.00 | All-time top 3 — generational standard-setters |
| 9.30–9.69 | All-time top 5–10 — era-defining franchise anchors |
| 9.00–9.29 | Perennial All-NBA First Team — elite franchise player |
| 8.70–8.99 | All-NBA caliber — clear franchise piece |
| 8.40–8.69 | Perennial All-Star — legitimate star |
| 8.10–8.39 | Genuine team star — All-Star capable |
| 7.70–8.09 | Quality starter — role-defining contributor |
| 7.20–7.69 | Rotation player — real NBA role |
| 6.50–7.19 | Fringe rotation — end of bench |
| 5.50–6.49 | G-League starter — fringe NBA |
| 4.00–5.49 | G-League rotation — developmental ceiling |
| 1.00–3.99 | Pre-pro developmental — no clear pathway |

**How assignment works**
The evaluator reads the completed 26 sub-domain profile and identifies which tier band the player fits. The anchor examples in each band are the comparison set. Archetype narrows which anchors are most relevant. The composite is then assigned from within that band — a specific value, to two decimal places.

**What the evaluator is looking for**
Profile shape matters more than any single score. The evaluator is reading: where are the strength clusters, where are the drag domains, how many structural zeros exist, how concentrated or distributed is the profile. A player with elite peaks and genuine weaknesses sits differently than a player with a uniformly solid profile at the same average. The anchor examples illustrate these distinctions concretely.

**Two decimal place precision**
Composites are expressed to two decimal places. This is earned precision — 26 sub-domain inputs at one decimal place each produce genuine separation between players. It is not false precision.

**Reference document**
The anchor library lives in COMPOSITE-SCALE-AND-TIERS.md. Every tier band must have at least one confirmed named example before the document is considered locked. Load this document for every evaluation.

---

## SECTION 7 — DNA COMP SYSTEM

**Purpose**
Every player profile includes 2–3 NBA player comparisons. The comp is not decoration — it is the empirical anchor for the evaluation. It communicates archetype, ceiling, and floor faster than any attribute table.

**How it works**
1. Prospect is tagged by position and archetype
2. Statistical similarity search run within the correct archetype bucket — a score-first guard matches against score-first guards only, not all guards
3. Top 3–5 closest comps returned from the NBA player database
4. Each comp's year-one NBA rating used as empirical anchor for the prospect's OVR range
5. 2–3 comps displayed on the profile with a brief similarity note

**Comp assignment rules**
- Position match required — a PF prospect does not comp to a center
- Style match required — archetype must align, not just position
- Recency preference — comps drawn from the last 10 years where possible
- No duplicate comps across the same draft class — each comp used maximum once per class

**Data source**
Comps currently anchor to 2K rookie ratings. Once the proprietary ratings database is live it replaces 2K as the source of truth — proprietary comps, not 2K comps.

**Relationship to the statistical comp model**
The DNA comp system and the statistical comp model are the same mechanism operating at two output levels. The statistical similarity search produces the comp list. The comp list produces the OVR anchor. The comp system is the Signal Layer 1 pipeline made user-visible.

---

## SECTION 8 — PROJECTION OUTPUT BLOCK

**Purpose**
POT/Min/Max and Bust/Avg/Boom% are produced together as a single block. They are complementary, not redundant. Separating them produces an incomplete picture.

- Min/Max defines the OVR range the player can reach
- POT is the expected peak within that range — always the middle value
- Bust/Avg/Boom% defines the probability distribution across outcomes within that range

**Inputs**
All inputs come from Layer 1:
- Composite score → OVR anchor
- Confidence tier → Min/Max spread width
- Age → development runway
- Projection modifiers (physical development, skill trajectory, character/work ethic) → distribution shape

**Structural rule**
Min < POT < Max. No exceptions. POT is always the expected outcome. Min is the floor — the bust scenario. Max is the ceiling — the boom scenario. Upside belongs in POT/Boom%/Max, not in the Day 1 composite.

**Bust% drivers — confirmed**
Bust% rises only when one or more of the following is present:
- Negative character signals
- Flat or declining skill trajectory
- Documented physical ceiling
- Injury history
- Anomalous data gap relative to peer group (e.g. a 21-year-old Power Conference junior with sparse stats)

**Critical rule — confidence and Bust%**
Wide confidence from expected data sparsity widens Min/Max spread. It does NOT raise Bust%. A high school senior with limited stats is evaluated in age-appropriate context — low data volume is normal for their tier and is not a bust signal. Bust% rises only when the data gap is anomalous for the player's context, or when a confirmed Bust% driver above is present.

**Selective effort sub-category**
Selective effort is a distinct sub-category within the Bust% modifier system. It applies when effort concern is directional — specific to one end, one role, or one context — and positive motor evidence exists independently in a different context.

- Selective effort Bust% modifier: +8–10%
- General negative character (multi-source) Bust% modifier: +15–20%

All three criteria must be met for selective effort classification: effort concern is directional, positive motor evidence exists in a different context, and source language does not include general "soft," "disengaged," or "not competitive" characterizations.

---

## SECTION 9 — USER-FACING PRODUCT DESIGN

**Confidence scoring — visual range bar**
Uncertainty is not hidden. Every profile displays a visual range bar showing Min/Max spread. A wide bar means less data. A narrow bar means high confidence. This is intuitive at a glance without requiring the user to interpret numbers. No competitor in the space visualizes uncertainty — the range bar makes confidence scoring a product differentiator visible on first contact.

**One-line justifications**
Every domain-level grade includes a one-line justification. Not a paragraph — one line. A bare number invites dismissal. A grade with justification invites debate and sharing. One line per domain is tractable at scale.

Example format:
- Shooting: 7.2 — "Reliable catch-and-shoot option from the corners; off-dribble creation remains inconsistent"
- Defense: 8.1 — "Elite on-ball defender; help-side awareness needs development at NBA level"

**Projected draft slot range**
Every prospect profile includes a projected draft slot range. Format: "Projected pick range: 15–22 | Current consensus: 18." Consensus calculated as median of last 5 published mocks. Spread reflects mock-to-mock variance. Stock movement between profile updates creates a reason to return.

**Consensus range alongside our grade**
Every profile shows where our grade sits relative to the broader scouting consensus. Where our grade diverges from consensus, the divergence becomes a talking point — which drives engagement and builds credibility over time.

**Team-specific fit analysis**
A Pro tier feature. For each prospect, identifies which NBA teams or 2K franchises represent ideal landing spots based on the player's profile and archetype. High compute cost, high value to the target Pro user — a clear free-to-Pro upgrade trigger tied to the core product.

**Ratings database UX — utility first**
One question, instant answer. Type a player name, get a clean grade immediately. No forced navigation, no sign-up walls on the free tier, no modal overlays on first visit. The free tier delivers: player name → overall composite grade + domain breakdown + DNA comps + one-line justifications. No account required.

**Named overall composite metric**
The composite needs a proprietary name before the ratings database launches. Named metrics become reference points audiences cite, search, and debate. Requirements: basketball-native, memorable, not tied to any specific player, distinct from existing metrics. Not yet decided — must be resolved before public launch.

---

## SECTION 10 — MONETIZATION

**Three-tier model**

| Tier | Access | Price |
|---|---|---|
| Free | Individual prospect profile, overall composite grade, domain breakdown, DNA comps, confidence scoring range bar, projected draft slot range, one-line justifications | Free |
| Pro | All free features + full draft class generation + team-specific fit analysis + real-time updates + comparison view + CSV/HTML export + API access | Subscription TBD |
| Scout/Agency | All Pro features + custom position filters + historical class archive + bulk export + white-label option | Enterprise TBD |

**The Pro upgrade trigger**
Team-specific fit analysis is the primary reason a free user upgrades. It is high value, high compute cost, and clearly tied to the core product — not an arbitrary paywall. Every free user who cares about where a prospect lands has a reason to upgrade.

**Pricing**
Pro and Scout/Agency pricing not yet decided. Must be resolved before public launch.

---

## SECTION 11 — DATA INFRASTRUCTURE AND SOURCING

**Pipeline architecture — Option B confirmed**
Automated pipeline. Web search pulls stats, scouting reports, news articles, and biometric data. AI-generated scouting reports are a proprietary output layer built on top of Layer 1 dimensional profiles. Confidence scoring handles data quality variance — wide confidence on data-sparse players is displayed prominently, not hidden. This is the only model that supports longitudinal tracking at scale.

**Longitudinal tracking requirement**
The pipeline must support recurring updates per player, not one-time profile generation. The same player is tracked from high school through college and into the NBA. Each profile update reflects current evidence. This is a Task 5 engineering requirement.

**Primary data sources by prospect tier**

| Prospect tier | Primary stats source | Primary qualitative source |
|---|---|---|
| Domestic HS | MaxPreps | 247Sports, On3 |
| College | Sports-Reference (CBB), EvanMiya.com | 247Sports, ESPN, The Athletic |
| International | FIBA, EuroLeague stats | NBADraft.net, international club sites |
| NBA | Basketball-Reference, EvanMiya.com | BBall Index, The Ringer |

**Source notes**
- MaxPreps is the confirmed ground-floor stat source for domestic HS prospects
- 247Sports and On3 are data sources, not competitors — their public scouting notes are a primary qualitative signal input for domestic HS and college prospects
- EvanMiya.com (evanmiya.com/?player_ratings) is a pipeline source for college and NBA player ratings
- HoopsHype is manual reference only — blocks automated scraping

---

## SECTION 12 — COMPETITIVE POSITIONING AND MOAT

**Talent vs. impact**
The rubric measures capability, not role production. This is the most important methodological decision in the product. Impact data — box scores, on/off splits, advanced metrics — is a genuine signal and is used. The discipline is contextualization, not rejection. Raw uncontextualized production is never used as a direct grade anchor.

This framing separates us from every stat-based tool in the space. A player in a bad system with low usage can have elite grades. A player putting up big numbers in a weak system does not automatically score high. The rubric reflects basketball reality, not circumstance.

**International coverage — the primary moat**
Every competitor has the same structural blind spot:
- Video tools (Synergy, Hudl) require footage that doesn't exist for most non-top-circuit international players
- Recruiting tools (247Sports, On3) cover the US pipeline only
- Draft media covers the consensus top 30 — international players outside the lottery are largely invisible

Our qualitative aggregation layer and rubric fallback cover players when no competitor can. Confidence intervals are wider for data-sparse international prospects — displayed transparently. A wide-confidence structured profile is more useful than nothing.

The moat timeline: 2–3 years minimum before a well-funded competitor closes this gap via licensed data. By that point the goal is a track record, a calibrated engine, and an audience.

**Transparent confidence scoring**
No competitor in the space visualizes uncertainty. The visual range bar makes this a product differentiator visible on first contact — not buried in a methodology note. Honest uncertainty builds more trust than false precision.

**Named composite metric**
A proprietary name for the composite metric is a long-term SEO and brand asset. Named metrics become reference points audiences cite, search, and debate. The name compounds into search value and recognition over time. Not yet decided — must be resolved before ratings database launch.

**The ratings database as SEO catchment**
The public-facing ratings database proves the rubric at scale. Every player profile is an indexed page. Every search for a player name is a potential entry point. The database is not just a product — it is the top-of-funnel for everything else.

---

## SECTION 13 — STRATEGIC LAUNCH SEQUENCE

**SD-01 — Launch sequence**
Launch the scouting tool and ratings database first. The 2K draft class generator launches later once the translation layer is accurate. Layer 1 is ready. Layer 2 is not — the translation table dataset is too sparse and most cells are single-point provisional. The international prospect coverage moat is a Layer 1 product. Premature 2K launch risks credibility.

**SD-02 — Layer 1 validation approach**
Validate Layer 1 accuracy against known NBA player career outcomes before any public launch. Score documented NBA players through the rubric. Check dimensional profiles against actual outcomes. Find errors, fix at Layer 1. Repeat until confidence is high. Website and monitoring infrastructure comes after validation, not before.

**SD-03 — Resolved product design questions**
Three decisions resolved:
- Data sourcing: Option B confirmed — automated pipeline, AI-generated reports as proprietary layer, confidence scoring handles data quality variance transparently
- Output format: composite grade + domain breakdown + confidence range bar + written scouting report + biometrics + statistical overview + DNA comps + projection block (draft-eligible players only)
- Database scope at launch: curated pre-draft soft launch — ~20–30 prospect profiles before the draft

**SD-04 — Translation table architecture (deferred)**
Translation tables need Tier A (prospect-era, L1-band keyed) and Tier B (NBA-tier, OVR-bracket keyed) restructuring. Deferred until 2K generator development resumes.

**SD-05 — Translation table density gap**
Approximately 50 additional Layer 1 builds required before translation tables are meaningfully accurate. Current dataset is too sparse. Primary driver of the SD-01 launch sequence decision.

**SD-06 — Launch target**
Curated pre-draft soft launch targeting the 2027 NBA Draft. Approximately 20–30 hand-selected prospect profiles published before the draft. This is the minimum credible debut — enough to establish the product, generate real feedback, and seed the audience before the 2027–28 recruiting season begins.

**SD-07 — AI-generated scouting reports**
The written scouting report is not a secondary feature — it is the primary output of the product. Structured data in → Layer 1 dimensional profile → AI-generated narrative report. The report generation layer is a core deliverable, not a Phase 2 add-on. Tone and format calibrated for scouts on mobile — not an academic writeup.

**SD-08 — Layer 1 validation plan**
Two test types before any public launch:
- Current-state accuracy: does the dimensional profile correctly describe what kind of player this is?
- Retrospective projection accuracy (NBA players only): using pre-draft data only, does the projection output match what the player actually became?

Player set is purpose-built — not reused from any prior calibration work. Systematic misses trigger Layer 1 rubric fixes. Isolated misses are logged and monitored.

**SD-09 — Longitudinal tracking**
The product is designed from the start to track a player from high school through college and into the NBA. Profile updates as new data comes in. The same player can be followed across years with each update reflecting current evidence. This is only possible with the automated Option B pipeline and is a Task 5 engineering requirement.

---

## SECTION 14 — WHAT IS DEPRECATED AND WHY

**Domain aggregation formula**
Retired permanently. A weighted average across 26 sub-domains compresses all profiles toward the middle. High-tier players with real weaknesses score lower than their basketball reality. Low-tier players with concentrated strengths score higher. Every formula design tested through Session 63 was mode-dependent — it worked for one player and broke another. No weighting scheme solved this without requiring player classification before application, which is not scalable. The composite is now assigned, not calculated.

**Domain arithmetic mean (display roll-up)**
Retired 2026-05-07. The unweighted mean of role-relevant sub-domains was kept as a readable display roll-up after the composite-formula retirement. In production this produced visible incoherence between composite (anchor-assigned, absolute) and domains (mean of peer-relative subs) — elite players showed composites in the 8.5+ tier with no domain rising above 7.5 because floor sub-domains pulled the mean down. Replaced by band-match assignment per DOMAIN-SCALE_v1.md, parallel to sub-domain and composite mechanics: peer-rank against the position group on the integrated capability the domain represents, then band-match the descriptor. Mandatory synthesis sentence preserves visibility of constraining sub-domains alongside the band assignment.

**Archetype weights as formula inputs**
Retired as calculation inputs. The weight tables in ARCHETYPE-WEIGHTS_v3.md describe what drives NBA value per archetype — they remain useful qualitative context for tier assignment and profile interpretation. They play no calculation role.

**Position weights as composite inputs**
Retired. The position weight system suppressed stretch-big archetypes structurally — confirmed multi-time All-Stars scored below prospects without NBA track records. Replaced first by the archetype weight system, then by the tier assignment architecture.

**TASK_S1_VALIDATION_LOG**
Archived. Built under the pre-pivot architecture. Validation methodology and pass standards were designed around domain scores and formula outputs. Not salvageable under the new architecture. A new validation approach will be designed when Layer 1 validation resumes.

**COMPOSITE_CALIBRATION_DATA_v5.md**
Archived after migration. The pre-pivot domain scores and raw composite columns are broken and must not be referenced. The 21 confirmed player targets are the only salvageable content — migrated to the anchor library in COMPOSITE-SCALE-AND-TIERS.md before archiving.

**POSITION-WEIGHTS-AND-NONNEG.md**
To be split. Position weights removed entirely. Non-negotiables extracted to a standalone NON-NEGOTIABLES.md document. The original file archived once extraction is confirmed complete.

---

## SECTION 15 — TRACK 1 / TRACK 2 SEPARATION

**Track 1 — Layer 1 scouting and rating system**
The engine that powers everything. The rubric, scoring protocol, archetype system, non-negotiables gate, tier assignment, and composite. Every other product depends on this being accurate and validated.

Current status:
- Architecture pivot complete — 26 sub-domains → tier assignment → composite
- Position scales: Guards confirmed (POSITION_SCALE_GUARDS_v1.md). Wings and Bigs pending.
- Anchor library: being built in COMPOSITE-SCALE-AND-TIERS.md. Every tier band requires at least one confirmed named example before the document is locked.
- Validation: Task S1 validation plan to be redesigned reflecting the new architecture before any public launch.

**Track 2 — Public-facing ratings database**
Built on top of Track 1. Covers NBA, college, and high school players using the same rubric. Longitudinal tracking from high school through the NBA. The broad coverage pass that scouts currently do manually, automated.

Current status: not started. Track 2 does not begin until Track 1 validation is complete. Quality of the database is only as good as the accuracy of the rubric underneath it.

**Sequencing**
Track 1 → Track 2. These are sequential, not parallel. Track 2 cannot launch on an unvalidated rubric — credibility risk on first contact.

**2K draft class generator**
A separate workstream. Currently deferred per SD-01. Resumes when approximately 50 additional Layer 1 builds are available and translation tables have sufficient density. Not part of Track 1 or Track 2.

---

*This document is append-only. Decisions are not removed — they are superseded by new entries if reversed.*
*Last updated: Session 64*
