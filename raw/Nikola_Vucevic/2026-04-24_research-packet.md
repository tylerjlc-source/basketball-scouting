# Research Packet — Nikola Vucevic — 2026-04-24

=== RESEARCH PACKET ===
PLAYER: Nikola Vučević
POSITION: Center
AGE: 35 (born 1990-10-24)
TEAM: Boston Celtics (traded from Chicago Bulls at 2026 deadline; Simons/Vucevic + 2nd-round pick swap)
COMPETITION LEVEL: NBA (15th pro season; 14+ yr vet)
EVALUATION DATE: 2026-04-24

--- EVALUATION WINDOW ---
Mode: DEFAULT (2-season, no R12 trigger)
- 2025-26 (w=0.60): 64 GP, 28.4 MPG — healthy; split Bulls (pre-Feb deadline) + Celtics (post-trade, reduced role, missed 14 games mid-March to early April for fractured right ring finger, surgery 2026-03-07, returned 2026-04-05)
- 2024-25 (w=0.40): 73 GP, 31.2 MPG — healthy; Bulls starter; primary hub role
**Flag (S100-F01):** eval_window.py reported 128 GP for 2025-26 — bug (inflated by TOT row aggregation from mid-season team change). Actual GP 64 per domain-script queries. Scoring proceeds on corrected GP.

--- PHYSICAL PROFILE ---
Height:         6'10.25" no shoes / 6'11.75" w/ shoes (2011 NBA Draft Combine)
Wingspan:       7'4.5" (+3.5" over standing; solid for C, not elite)
Weight:         ~260 lbs (259.8 at combine; playing weight consistent; thick-framed)
Standing reach: 9'4.5"
Hands:          10.25" width / 9.25" length
Vertical:       unknown (not listed in combine data)
Lane agility:   unknown
Body type:      Thick-framed traditional center; finesse skill set layered over limited foot speed / mobility

--- DOMAIN 1 — FINISHING ---

**Statistical (weighted 2-season):**
- Rim FG%: 65.6% (65.4 cur / 65.9 prior); Non-Dunk Rim 64.3%
- Rim FGA: 220.2 volume (~ 1.1/g)
- % Shots at Rim: 24.4% (LOW for C — stretch profile, many attempts outside paint)
- Dunk Rate: 6.6% (very low — finesse finisher, plays below rim)
- % Assisted at Rim: 81.7% (doesn't self-create rim shots)
- FTR: 0.127 (low; avoids contact, finesse style)
- Drive FG%: 53.2% on 3.04 drives/g (efficient but rare)
- Paint non-RA FG%: 55.1% (strong short-range / floater range)
- Drive PPP: 0.573

**Qualitative:**
- "Elite back-to-the-basket scorer. While he doesn't always get optimum position down low, Vucevic's footwork, intelligence and soft touch make him a reliable low-post scorer" (Film Room: Vucevic's Strengths, NBA.com/Magic — career compilation)
- "In the post, Vucevic has good footwork and touch, showing the ability to go over both shoulders. Vucevic's signature turnaround hook shot is the biggest weapon in his offensive repertoire" (NBA.com/Magic)
- "Post touch... elite" — per multi-source scouting convergence
- "Soft shooting touch that enables him to score efficiently in various situations" (Sports Forecaster player profile)
- "Finesse finisher... plays below the rim... post touch and footwork carry the scoring" (BlogABull / CHGO Sports cluster)
- "If defenders double on a drive, he pops out for an open three; if they send their big up to the level of the screen, he rolls hard and finds an easy bucket in the restricted area" (Raptors Republic PnR breakdown)

**Data gaps:**
- Post-up PPP/Synergy offense: Domain 1 script did not dump Synergy PostUp offense block in 2025-26 output — sub-domain #3 (Post offense) stats gap. Qualitative language strong enough to score but at moderate confidence.
- Self-created vs assisted rim breakdown is captured, but half-court vs transition rim splits not broken out.
- Current-season foul-drawing trajectory with Celtics not separately captured.

--- DOMAIN 2 — SHOOTING ---

**Statistical (weighted 2-season):**
- CAS 3PT%: 38.4% (37.2 cur / 39.9 prior) — strong for C
- Corner 3%: 32.6% | ATB 3%: 39.0% (above-break is his bread-and-butter)
- Total 3PA volume: ~453.6 (weighted) — high-volume stretch big
- Pull-Up 3PT%: 20.0% on tiny sample (0%/50%; not a threat off dribble)
- Mid-Range FG%: 42.5% (41.6 cur / 43.5 prior) on 89.4 FGA — quality mid-range
- FT%: 82.0% (82.8 cur / 80.5 prior); career 77.3%
- Clutch FT%: 73.8%
- TS%: 58.9% | eFG%: 57.0% | 3PT%: 37.8%

**Qualitative:**
- "He shot over 40 percent from beyond the arc for only the second time in his career while attempting at least four shots per game from long range for a fourth straight year" (2024-25 — RotoWire / Pippen Ain't Easy)
- "35.1 percent on 3-point shots with the Celtics... 37.3 percent for the whole season" (BostonGlobe 2026-04-10 — slight decline post-trade)
- "His work in pick-and-roll and pick-and-pop situations is perfect" (Raptors Republic — historical but pattern persists)
- "Very competent as a short roll passer, combining the shooting and passing of a Marc Gasol with the finishing ability of a Jonas Valanciunas" (Raptors Republic)
- "Knock down open threes off the catch... one of the best ways for a lower-usage player to make an impact" (BostonGlobe — Celtics role shift)
- "He is one of the league's premier screen setters... tactical in his body placement... creating extra space for teammates" (CHGO Sports)
- Off-dribble signal ABSENT — no scouting language describing creation from a live dribble; all shooting evidence is CAS/PnP/PnR-rolling

**Data gaps:**
- Pull-up 3PT on thin sample (PU Zone 3PT 40% but only from ShotChart zone weighting — low attempts).
- Off-screen (shooting variant) PPP lives in Domain 4 not Domain 2 (reporting artifact); 1.38 PPP weighted, 74–98 pctile — supports shooting strong signal.

--- DOMAIN 3 — BALL SKILLS ---

**Statistical (weighted 2-season):**
- ISO PPP: 0.907 (49.2 pctile) on 13 possessions — occasional, modest
- PnR BH PPP: 0.000 / 0 possessions (not a ball-handler)
- Handoff PPP: 0.000 / 0 possessions (script reports zero — likely endpoint classification; Vucevic is frequent DHO hub qualitatively; flag)
- Touches/G: 61.5 (HIGH for C — offensive hub usage)
- Time of Possession: 1.5 min | Dribbles/Touch: 0.59 | Points/Touch: 0.267
- Drives/G: 3.0 | Drive FG%: 53.2% | Drive TOV%: 4.4% | Drive AST/G: 0.3
- Floater FG% (4–14ft): 53.6% (52.1 cur / 55.4 prior) on 337 FGA — **37.8% of total FGA** (floater range is core shot diet)
- Non-Dunk Rim FG%: 64.3%
- TOV per 100 Touches: 2.3 (current 2.2 / prior 2.5)
- Estimated TOV%: 7.7 | A:TO Ratio: 2.37
- Clutch MIN 101.2 | Clutch TOV 5 / AST 8

**Qualitative:**
- "Touch / feel" upper-tier language across sources — "soft touch," "signature turnaround hook"
- Hand-off hub role: "screening away from the ball or just acting as a facilitation hub at the elbow" (SI Bulls — Donovan on Vucevic)
- Ball security: no multi-source concern with turnovers; A:TO 2.37 strong for hub big
- No dribble-drive creation language — consistent with null PnR BH PPP

**Data gaps:**
- Handoff PPP = 0 from Synergy endpoint despite heavy qualitative DHO usage; may be endpoint classification inconsistency (DHO hub actions sometimes booked as "off screen" or "post up" rather than "handoff"). Flag but do not override — cross-check via Domain 4 OffScreen data (1.38 PPP, strong).
- No live-dribble creation evidence — properly zero for this profile.

--- DOMAIN 4 — PLAYMAKING ---

**Statistical (weighted 2-season):**
- Passes/G: 45.2 | Potential AST: 5.7 | Actual AST: 3.4
- Conv rate (AST / Potential AST): 59.3% — strong for C
- Secondary AST: 0.3 | FT AST: 0.1
- Adjusted AST: 3.9 | Adjusted AST %: 8.6%
- AST Points Created: 8.7/g
- A:TO: 2.38 | TOV: 1.4
- Cut PPP: 1.314 (38 cur / 65 prior pctile) on 95 poss weighted — middling as cutter
- OffScreen PPP: 1.383 (74/98 pctile) on 31 poss — strong off-screen/DHO finisher variant
- Transition PPP: 1.205 (58/73 pctile) on 116 poss — solid
- Off speed: 4.16 mph | Off distance: 1.04 mi/g (typical for a non-mobile big)

**Qualitative:**
- "Short-roll playmaking is one of the most crucial aspects of NBA offenses and perhaps Vucevic's best skill. Vucevic is second to Jokic in secondary assists among centers and sixth in potential assists" (CHGO Sports — 2024-25 framing)
- "The Bulls use him as an offensive hub for their half-court sets. Coach Billy Donovan noted they've been 'able to do more things where he's kind of initiating actions from the elbows'" (SI Bulls)
- "Connective tissue and playmaking hub behind the league's fifth-best offense" (CHGO — Bulls 2024-25 role framing)
- "Vucevic is averaging five post touches a game, and not only is he a scoring threat from the block, but he is also a passing threat from there"
- "Passing and shooting of a Marc Gasol with the finishing of a Jonas Valanciunas" (Raptors Republic)
- "We're not asking him to score, we're asking him to play basketball" — Mazzulla, post-trade role redefinition (Hardwood Houdini)
- Off-ball movement: minimal self-generation; hub role keeps him at elbow/top-of-key. Cut-frequency 10% is role-appropriate but middling PPP.

**Data gaps:**
- Decision-making quality under pressure (sub #12) is directional only; no dedicated Synergy turnover-type breakdown in output (script reported "Found TOV-related columns... TOV, TOV_RANK" without error-type split).
- Celtics-era playmaking usage smaller sample (reduced role; harder to isolate skill from context).

--- DOMAIN 5 — DEFENSE ---

**Statistical (weighted 2-season):**
- #15 On-Ball Pressure:
  - Opp FG% (Overall): 48.3% | D_FGA/g: 16.6 | DFGPOE: −1.1% (below-average on-ball)
  - Deflections: 1.5/g | STL: 0.7/g | Contested shots: 8.1/g (2.7 3PT / 5.4 2PT)
  - PF/g: 2.1
  - ISO Defense PPP: 0.878 on tiny sample (3.2 poss 2-season)
- #16 Help Defense:
  - DEF_RATING: 115.3 (poor; 114.8 cur / 116.0 prior — consistent across bad Bulls team contexts)
  - Charges drawn: 0.01/g (virtually never) | Def loose balls: 0.13/g | Def box-outs: 1.63/g
  - BLK/g: 0.6
- #17 Rim Protection:
  - **Rim-specific endpoints (Opp FG% at rim, D_FGA at rim, DFGPOE at rim) all returned N/A** — endpoint gap in this run. Flag.
  - BLK/g: 0.6 (cross-ref; **very low for a starting C**)
  - Contested 2PT/g: 5.4 (cross-ref)
- #18 Post Defense:
  - PostUp Defense PPP: 0.803 (72 cur / 90 prior pctile) on 1.4 poss/g — strong-looking PPP, but small possession sample
  - Def box-outs/g: 1.63 (cross-ref)

**Qualitative — heavily convergent NEGATIVE signal:**
- "Vucevic offers extremely limited rim protection and practices a general 'no touching' philosophy" (Pippen Ain't Easy)
- "Vucevic has been a weak rim protector, and the Bulls' defense has struggled in the paint" (Pippen Ain't Easy)
- "Vucevic lacks the foot speed and agility to reliably switch out onto the perimeter or hedge much in defensive coverage. As a result, Vucevic simply cannot do any coverage except drop. If he were to contest in the open court, it would result in an easy blow by to the rim" (BlogABull)
- "Of the 34 big men with 1000+ minutes played, Vucevic has the 6th worst dFG% vs expected" (BlogABull, 2024-25 context)
- "He allowed opponents to shoot 56 percent at the rim, manifesting itself into a mediocre block rate" (BlogABull)
- "It's hard to protect the paint effectively in today's NBA without a shot-blocking center, and Vucevic does not fit the bill" (Last Word on Basketball — Matas Buzelis piece framing)
- "Bulls' biggest interior defensive weakness" repeated framing 2024-25 and 2025-26 across Pippen Ain't Easy / Blog A Bull / CHGO Sports
- Limited POSITIVE: Post defense PPP metric is decent; he does not consistently lose 1-on-1 post matchups, and post defense is reduced league-wide so sample is small

**Data gaps:**
- Rim-specific DFGPOE endpoints returned N/A — blocks me from confirming the "56% at rim allowed" qualitative claim with script output. Trust convergent qualitative.
- Celtics-era defensive context is small sample and role-limited; hard to separate scheme improvement from Vucevic skill change.
- Switch/hedge coverage breakdown not isolable from the aggregate Opp FG% figure.

--- DOMAIN 6 — REBOUNDING ---

**Statistical (weighted 2-season):**
- REB/g: 9.08 | OREB/g: 2.16 | DREB/g: 6.88
- OREB%: 7.1% | DREB%: 21.8% | REB%: 14.7%
- Contested rate: 40% (contested 3.4 / total 8.5 per 2025-26)
- Defensive rebound chance %: 63.6 cur / 67.3 prior (strong finishing rate when contested)
- OREB chance %: 46.6 cur / 50.9 prior
- Avg REB distance: 5.1 ft (cur) / 5.2 ft (prior) — typical paint rebounder
- Box-outs/g: 1.98 (cur) / 2.14 (prior); heavily weighted defensive (80% DEF, 20% OFF)

**Qualitative:**
- "Cemented his reputation as a prolific rebounder, possessing the 10th best rebounding rate last season (27.6 percent)" (player profile framing — note source-reported REB% higher than script; may be per-48 or older season)
- "Able to manipulate some matchups... set great screens... able to keep Drummond and Bona off the glass" — Mazzulla post-Game 1 (2026 playoffs) (Boston Globe)
- Consistency: "Averaged at least 10 rebounds in seven consecutive campaigns" (RotoWire)
- No negative rebounding language found across sources

**Data gaps:**
- Second-jump/effort rebounding qualitative depth is thin; metrics-based only.
- Tip-out vs secure-and-hold breakdown not isolable.

--- DOMAIN 7 — ATHLETICISM ---

**Statistical (weighted 2-season, movement proxies):**
- Avg speed: 3.96 mph | Off: 4.16 | Def: 3.77 — BELOW average for movement, typical for traditional C
- Distance/g: 2.02 mi (modest)
- Dunk Rate: 6.6% (very low — plays below rim)
- Drives/G: 3.04 (modest; drive FG% 53.2%)

**Qualitative:**
- "Lacks the foot speed and agility to reliably switch out onto the perimeter" (BlogABull)
- "Plays below the rim... finesse finisher... doesn't get above" multi-source convergence
- Strength: "fundamentally strong footwork" and post leverage (NBA.com/Magic); able to hold post position but not bully
- "One of the league's premier screen setters" — implies mass + angle manipulation, not vertical/explosive athleticism
- Age-related: "He is 35 and one of the oldest players in the NBA" (Pippen Ain't Easy)

**Data gaps:**
- No combine vert / lane agility / shuttle published (2011 Combine didn't record or didn't publish).
- No recent measured vert; in-game proxies consistent with non-athletic finesse C.
- Strength (#23) inferred from body-mass + screen-setting acclaim; no direct bench-press or measured strength data.

--- DOMAIN 8 — IQ / MOTOR ---

**Statistical (weighted 2-season):**
- Shot clock distribution: 6.1% 24-22 | 8.6% V.Early | 20.3% Early | 49.3% Average | 8.4% Late | 7.3% V.Late — healthy shot-clock distribution (avg-heavy, low late/very-late)
- Defender distance: Very Tight 6.5% | Tight 39.8% | Open 21.0% | Wide Open 32.8% | Contested %: 46.3% (near league average)
- Clutch (2-season weighted, 59 GP): 1.9 PTS, 50.0% FG, 40.0% 3P, 76.7% FT, +/− −0.2, 0.3 AST, 0.1 TOV — solid-ish clutch scorer
- Hustle: 1.5 deflections/g, 1.63 def box-outs/g, 0.13 loose balls/g, 0.01 charges/g

**Qualitative:**
- "Hard worker who is always looking to improve his game. Positive influence in the locker room, setting an example with his dedication" — respected professional framing across Eurohoops / CelticsBlog / SI Bulls historical
- Mentoring role: Celtics' Neemias Queta "isn't squandering the opportunity of sharing a locker room with the 15-year veteran's expertise" (CelticsBlog)
- "He just wants to win" — Mazzulla endorsement (CelticsBlog)
- **Recent negative motor signal:** "It's been a stretch of up-and-down effort for Chicago's starting center, and the fanbase is understandably frustrated" (Pippen Ain't Easy, 2025-26) — tied to Bulls' losing stretch + trade-rumor fatigue
- Reading the game: "intelligence... connective tissue... manipulate some matchups" — multi-source positive on basketball IQ
- Shot selection: low contested% (46.3 vs league avg) and heavy "Average" shot-clock window are healthy indicators

**Data gaps:**
- Motor signal is mixed — mostly positive career view, but recent Bulls-era motor concerns. Needs weighing against role/context.
- Competitive character in playoff / high-leverage moments: sample thin; 2025-26 playoffs is small role off bench.

--- CHARACTER / PROJECTION SIGNALS ---

**Work ethic evidence:**
- Multi-source: "consummate professional," "hard worker," "positive locker room presence"
- 7 straight seasons of 17/10/3 — durability & consistency
- 5 straight seasons of 70+ GP — availability is a career pattern

**Competitive character evidence:**
- Mazzulla: "He just wants to win"
- Celtics mid-season acquisition framing: "excited at the potential for first deep playoff run" (Yahoo Sports)
- Career playoff TS% delta −1.6 (neutral R13 classification) — does not elevate or collapse in playoffs

**Negative signals:**
- Bulls 2025-26 motor dips during losing stretches — fanbase/beat criticism
- Trade-market framing: "the Bulls were reportedly holding out for a first-round pick in exchange for an aging center with one year left on his contract, whose game doesn't fit anymore" (Newsweek/Hoops Rumors) — league-wide decline perception
- Bulls-era benching incident: Donovan briefly benched Vucevic for Zach Collins (CHGO Bulls podcast headline)
- Defense-side effort/capability gap is long-standing and structural, not a motor issue per se

**Trajectory: flat-to-declining**
- 2024-25: career-year 23.4/11.7/3.8 @ 48/40/84 (age 34)
- 2025-26 (pre-trade Bulls): ~18.5/10.5/3.5 @ 53/40 (aug-window role data)
- 2025-26 (post-trade Celtics): ~13 PPG, smaller role, 35.1% 3P — role-driven decline; hard to parse skill erosion from usage shift
- Career TS% still 58.9% weighted — no statistical cliff visible, but usage/role trajectory is DOWNWARD

--- PLAYOFF / BIG-GAME TRACK RECORD (R13 applies) ---

**Sample:** Met (5 playoff seasons: 2010-11 SIX, 2018-19 ORL, 2019-20 ORL, 2021-22 CHI, 2025-26 BOS)
**Recency status:** Active (last playoff 2025-26, gap 0; in ongoing 2026 playoffs as Celtics reserve)

**Statistical (matched-season basis, Playoff_Track_Record.py):**
- Playoff TS%: 53.5% (18 games / 5 seasons)
- Regular TS%: 55.1% (330 matched-season games)
- Delta TS%: −1.6 (modest shrinkage; neutral-range drag)
- Playoff PPG: 17.0 | Regular PPG: 16.4 | Delta +0.6 (volume stable)
- Playoff FGA: 15.1/g | Regular FGA: 14.0/g (volume maintained)

**Recent 3 playoff runs:**
- 2025-26 (BOS): 2 GP, TS% 55.1% (vs RS 57.4%, −2.3), 6.0 PPG — reserve role, small sample
- 2021-22 (CHI): 5 GP, TS% 52.0% (vs RS 53.3%, −1.3), 19.4 PPG — starter role, mild shrinkage
- 2019-20 (ORL bubble): 5 GP, TS% 60.4% (vs RS 54.9%, **+5.5**), 28.0 PPG — strong rise

**Qualitative:** No "Mr. June" language; no "disappears in big games" language. Multi-source framing is neutral — playoff career largely on bad/overmatched teams (Magic 2019-20 bubble, Bulls 2021-22 first round). No convergent big-moment narrative either way.

**Classification (manual, per R13):**
- Stat signal: Career matched delta −1.6 TS% = neutral-range drag
- Qualitative signal: neutral (no converging rise OR shrink language)
- **R13 classification: NEUTRAL (active recency)** — script's "neutral" hint aligns with manual per-R13 read this time. No override.
- Script's Playoff_Track_Record classification hint is trusted here, but per S100-F01 learning the hint remains a known-bug class; confirmed independent alignment.

--- INJURY HISTORY ---

**2025-26 recent:**
- **Fractured right ring finger**, March 6, 2026; **surgery March 7**; missed 14 consecutive games (March 8 – April 3); returned April 5; 4 games pre-playoffs + Game 1/Game 2 first-round action (BOS vs PHI)
- No known lingering effect; not on playoff injury report

**Career:**
- Broadly durable — 70+ GP in 5 straight seasons prior
- Two missed early-20s developmental seasons at Sixers / Magic due to limited role, not injury

**R9 / R12 assessment:**
- R9 (injury temper): NOT triggered. Finger injury is minor, not chronic, not role-altering. No composite temper warranted.
- R12 (both-seasons-compromised): NOT triggered. Neither 2025-26 (64 GP healthy outside 14-game finger absence) nor 2024-25 (73 GP healthy full season) qualifies as compromised. Default 60/40 eval window stands.

--- DATA GAP INVENTORY ---

**Strong support (3+ sources):**
- Physical profile (combine data solid)
- Shooting / CAS 3PT / pick-and-pop (stats + 3+ scouting sources)
- Playmaking / short-roll / elbow hub (stats + 3+ sources incl. coach quotes)
- Post-up scoring touch and footwork (scouting language strong, historical + current)
- Screen setting (3+ sources, league-recognized)
- Rim protection WEAKNESS (overwhelming convergent negative; stats align)
- Drop-only coverage / can't switch (convergent, 3+ sources)
- Rebounding (stats + consistency + box-out framing from Mazzulla)

**Moderate support (2 sources):**
- Character / professionalism (multi-source positive; recent motor dip context)
- Celtics role adjustment / lower-usage fit
- Trade-market perception of decline
- Off-screen / Off-movement finisher PPP

**Weak support (1 source or thin sample):**
- ISO defense PPP (2-season total 3.2 possessions — very small)
- Post defense PPP (1.4 poss/g — small sample; PPP looks strong but volume thin)
- Pull-up 3PT (trivial sample, 0%/50% split)
- ISO offense (13 poss total weighted)

**No direct evidence:**
- Vertical leap / lane agility / bench press (2011 combine did not publish; no current measured data)
- Sub-domain #22 (lateral quickness) direct measurement — inferred from "lacks foot speed" consensus

**Conflicting signals:**
- Shooting: 40.2% on 3s in 2024-25 vs 35.1% post-trade with Celtics — resolvable as role/shot-diet shift (lower usage → different look mix), not mechanics; career 3PT trend is upward
- Effort/motor: respected-professional career narrative vs recent Bulls-era motor critiques — context-dependent (losing team + trade rumors)

**Script output bugs flagged (S100-F01 family):**
- eval_window.py: 128 GP 2025-26 incorrect (TOT row aggregation from mid-season trade); use domain-script GP values (64)
- Playoff_Track_Record.py: classification hint ("neutral") ALIGNS with manual R13 read this run; no override required, but known-bug awareness maintained
- Domain 1 script: Synergy PostUp offense block not printed in output — sub-#3 (Post offense) stats gap; qualitative evidence compensates
- Domain 5 script: rim-specific endpoints (Opp FG% at rim, DFGPOE at rim) returned N/A — sub-#17 (Rim Protection) stats thin; qualitative convergence very strong, offsets
- NBA_Comp_Stats.py (deferred to Skill 5; BLK%/STL% endpoint None may recur)

=== END RESEARCH PACKET ===
