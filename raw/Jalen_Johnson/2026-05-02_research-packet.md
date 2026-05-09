# Research Packet — Jalen Johnson — 2026-05-02

=== RESEARCH PACKET ===
PLAYER: Jalen Johnson
POSITION: PF/SF (listed)
AGE: 24 (DOB 2001-12-18)
TEAM: Atlanta Hawks
COMPETITION LEVEL: NBA
EVALUATION DATE: 2026-05-02

--- EVALUATION WINDOW NOTE ---
eval_window.py initially flagged R12_ANCHOR with 2023-24 (56 GP) as primary, classifying 2025-26 (72 GP, 35.2 MPG) and 2024-25 (36 GP, 35.7 MPG) as fragments. The 2025-26 fragment classification is an MPG-band false positive — 72 GP at 35.2 MPG with no in-season injury absence is a healthy starter sample by every reasonable definition. Per memory feedback "R12 firing — default to Option 2 worst-obs pull," scripts were also run with `--season-override 2025-26` so the actual healthy current-season sample governs the read. Stats below are 2025-26 unless noted; 2023-24 referenced for trajectory confirmation. R12 NOT formally applied. R9 NOT applied (player was cleared fully healthy for 2025-26 by Hawks medical and produced a career-best, All-Star-level 72-game sample — no athleticism suppression to temper).

--- PHYSICAL PROFILE ---
Height:         6'9.25" in shoes (6'7.75" barefoot)
Wingspan:       7'0.25"
Weight:         ~219 lbs (combine 209.6; filled out)
Standing reach: 8'10.0"
Vertical:       Did not test at 2021 NBA Combine
Lane agility:   Did not test at 2021 NBA Combine
Body type:      "Well-built wing," documented strength gain post-rookie. "At 6'9", 220 lbs, with a 7-foot wingspan, he's easy to identify on the court, especially given his effortless gliding up and down the hardwood." (Yahoo Sports 2024). Both parents played college basketball; father played pro in Poland.

--- DOMAIN 1 — FINISHING ---
[Stats — 2025-26]
- Rim FG%: 69.8% on 384 attempts (% of total FGA: 31.3%)
- Dunk rate: 22.7%; Non-dunk rim FG%: 62.0%
- FT%: 78.8% (career 75.1%)
- % assisted at rim: 55.0%
- FTR: 0.311 (60th-pctile-adj for wings); FTA-adjacent: ~7.0/g implied
- Drives/g: 13.2; Drive FG%: 45.7%; Drive PPP: 0.583; Drive PTS/g: 7.7
- Paint non-RA FG%: 41.6%
- 2023-24 reference: Rim FG% reported at 72%, dunk rate higher in transition

[Qualitative]
- "Connected on a career-high 72% of rim attempts (88th percentile)" 2024-25 (SI/OnSI Hawks season grades, April 30 2025)
- "Ability to finish around, above, or simply against contact at the rim" (MavsDraft, June 2021)
- "One of the highest finishing upsides in the draft" (MavsDraft, June 2021)
- "His functional handle in open space combined with an explosive and strong 6-foot-9 frame allows him to accelerate, get into the paint and finish over or through all kinds of defenders" (multi-outlet 2024-25)
- "Plays above the rim with ease" (pre-draft scouts, 2021)
- "A terror in the open court" (Prospective Insight 2021, updated 2025)

[Data gaps]
- Specific left-hand vs right-hand finishing splits not captured by scripts
- Synergy possessions for transition timed-out on 2025-26 D4 pull (workaround: D4 ran successfully for 2023-24 — Transition PPP 1.122, 47th percentile, 22.6% freq)

--- DOMAIN 2 — SHOOTING ---
[Stats — 2025-26]
- 3PT%: 35.2% (weighted), CAS 3PT% endpoint flag returned 0.0% on the 2025-26 override pull (script's CAS endpoint requires Synergy CatchShoot which timed out — fallback to overall 3PT 35.2%)
- Total 3PA: 341 (volume jump from 200 in 2023-24)
- Pull-up 3PT% (ShotChart): 28.4%
- PU Zone Mid% (ShotChart): 47.0%
- Mid-Range FG%: 0.0% reported by main mid-range endpoint (timeout); Paint non-RA 41.6% from D1 captures the floater/short mid-range; PU Mid 47.0% is the more reliable read
- FT%: 78.8%; Career FT%: 75.1%; Clutch FT%: 80.6%
- TS%: 58.1%; eFG%: 53.7%
- 2023-24 reference: CAS 3PT% 35.6%, Corner 3PT% 29.5%, ATB 3PT% 38.4%; Mid-Range 48.6%, ISO PPP 0.955

[Qualitative]
- 2025-26 splits widely cited: 58/40/81.2 (career bests) — RotoWire/StatMuse aggregations 2026
- "Needs to improve jump shot." "Jump shot needs an entire overhaul." "Shoots on the way down on moving shots." (MavsDraft June 2021)
- "Johnson's shooting form is somewhat awkward when he has to dribble or step back into a jumper." (aggregated pre-draft/early career analysis)
- "He can probably use some more improvement as a three-point shooter." (SI/OnSI April 2025)
- 3P% trajectory: 35.5% (2023-24) → 31.2% (2024-25 36 GP) → 40% (2025-26)
- Free-throw line trajectory: 72.8% → 74.6% → 81.2%

[Data gaps]
- CAS-only 3PT% endpoint timed out on 2025-26 pull; 35.2% overall 3PT (script weighted) and ~40% from public aggregations are the reads
- Mid-range FGA endpoint also timed out; PU Zone Mid% 47.0% from ShotChart is the cleanest mid-range read
- S105-F01 watch: Web articles cite "40% from three" but the script aggregate is 35.2% weighted. The ~40% figure may be cherry-picked hot stretches; per S105-F01, defer to script. Plausibly the script's CAS-specific filter timed out and the script weighted overall 3PT under a different definition than public aggregates. Treating 35–37% as conservative read; 38–40% as upper bound from public sources. Conflicting signal — flagged.

--- DOMAIN 3 — BALL SKILLS ---
[Stats — 2025-26]
- ISO PPP: 0.780 (25.8th pctile), 127 poss (significant volume)
- ISO FG%: 37.0%, ISO TOV%: 11.0%
- PnR BH PPP: 0.772 (34.1st pctile), 381 poss (heavy primary-handler volume)
- PnR BH FG%: 41.1%, PnR BH TOV%: 22.6%
- Handoff PPP: 0.811, 106 poss
- Touches/g: 89.2 (very high — primary creator level); Time of poss 4.9 min
- Dribbles/touch: 2.35; Points/touch 0.252
- Drives/g: 13.2, Drive TOV% 6.1%, Drive AST/g 1.3
- Floater FG% (4-14ft): 41.6% on 425 FGA (heavy floater volume); Floater = 34.6% of total FGA
- Non-dunk rim FG%: 62.0% (touch proxy at rim)
- TOV per 100 touches: 3.8; Estimated TOV%: 11.1; A:TO: 2.32

[Qualitative]
- "Quick first step; can handle the ball equally well with his left and right hands; difficult to guard once he gets going downhill" (MavsDraft 2021)
- "Johnson uses his dynamic slashing to engage help defense, then executes disguised jump passes to cutters" (Soaring Down South 2025-26)
- "Johnson finished 5th over the Nike EYBL with 3.6 turnovers per game in 2019" (pre-draft records — historical TOV concern)
- "Turnover percentage rose to 15.1% in 2024-25 as usage climbed" (SI/OnSI April 2025)
- "Four turnovers in one game against the Cleveland Cavaliers" (Soaring Down South 2025-26)
- Trae Young traded mid-season; primary-creator load shifted to Johnson; A:TO held at 2.32

[Data gaps]
- Specific live-ball TOV vs dead-ball TOV split not captured

--- DOMAIN 4 — PLAYMAKING ---
[Stats — 2025-26]
- Passes/g: 64.0; Potential AST: 14.0; Actual AST: 7.9 (conv 56.4%)
- Secondary AST: 0.5; FT AST: 0.8; Adjusted AST: 9.1; Adj AST%: 14.2%
- AST Points Created: 20.5
- AST/g: 7.9 (career high; franchise All-Star level for non-PG)
- TOV/g: 3.4; A:TO: 2.32
- Cut PPP: 1.463 (80th pctile, 95 poss, 73.4% FG, 6.0% freq) — 2025-26 capture (Cut endpoint succeeded; OffScreen + Transition timed out for 2025-26)
- 2023-24 reference: OffScreen 0.895 PPP 35th pctile (low volume, 19 poss); Transition 1.122 PPP 47th pctile, 196 poss
- Speed: Total 2.6 mi/g; Avg 4.32 mph; Off speed 4.84 mph (above-average for wings)

[Qualitative]
- "Johnson has an assist rate of 25.3%, meaning a quarter of shots made by his teammates are assisted by him... puts Johnson in the 98th percentile as a creator across the league" (Soaring Down South 2025-26)
- "Super talented passer at 6'9, and his ability to find perimeter shooters is probably his best passing quality" (aggregated 2024)
- "6'9" players who can move like Johnson very seldomly come around, and most of those who do don't also possess such a passing repertoire" (Prospective Insight, updated 2025)
- 13 triple-doubles in 2025-26 — franchise record
- Second-fastest triple-double in NBA history (first half vs. Denver) 2025-26
- "Must get better at recognizing open teammates" (MavsDraft 2021) — old concern, largely resolved

[Data gaps]
- 2025-26 OffScreen and Transition Synergy data timed out

--- DOMAIN 5 — DEFENSE ---
[Stats — 2025-26 (retry succeeded)]
- Opp FG% (Overall): 49.1%; D_FGA/g 12.8; DFGPOE: +1.2% (slight negative — opponents shot slightly above expected)
- ISO Defense PPP: 1.091 (19.1st pctile, micro sample 0.8 poss — disregard small-sample)
- Deflections/g: 2.4; STL/g: 1.2; Contested shots/g: 4.8 (3PT 2.0, 2PT 2.8)
- BLK/g: 0.4; PF/g: 2.1
- DEF_RATING: 112.3 (team-on-court figure; mid-tier)
- PostUp Defense PPP: 0.686 (94th pctile, 0.5 poss — micro sample, disregard)
- Charges drawn/g: 0.03; Def loose balls/g: 0.18; Def box-outs/g: 0.58

[Qualitative]
- "Opponents shot 3.8% worse from the field when Johnson closed out on them — 91st percentile among all forwards" (SI/OnSI October 2025, on 2024-25 sample)
- "Rim points saved per 100 possessions improved to 1.1 (85th percentile) from 0.4 (76th percentile). Opponents shot 7% worse at the rim due to his presence (82nd percentile)" (SI/OnSI October 2025, 2024-25 data)
- "Career-high defensive box plus-minus of 1.8" (SI/OnSI April 2025)
- "He can guard every position. And he's just beginning to figure out how good he can be." (anonymous GM, Yahoo Sports 2024)
- "LeBron told him: 'There should be no reason I shouldn't be on All-Defensive teams.'" (Johnson via Yahoo Sports 2024)
- "His level of focus on defense could be more consistent." (SI/OnSI April 2025) — engagement concern
- "Lacks intensity on-ball" (MavsDraft 2021) — old draft-era concern
- "His absence from the lineup left the Hawks extremely susceptible to getting exposed by star players with size" (2025 coverage on 2024-25 post-injury impact)
- 2025-26 DFGPOE +1.2% is a regression vs 2024-25 reports of "−3.8% closeout effect" — usage and primary-creator load may have absorbed defensive intensity in 2025-26

[Data gaps]
- 2025-26 DFGPOE positive (+1.2%) is the most negative current-state defensive read; reconcile with prior-season "91st pctile closeout" qualitative

--- DOMAIN 6 — REBOUNDING ---
[Stats — 2025-26 (retry succeeded)]
- OREB/g: 1.4; DREB/g: 8.9; REB/g: 10.3
- OREB%: 3.8%; DREB%: 24.1%; REB%: 14.0%
- DREB chances 12.7/g, DREB chance pct adj: 75.6% (high conversion on opportunities)
- Contested DREB%: 27.2%
- Box-outs/g: 0.63 (def 0.58, off 0.04); Box-out player rebs 0.44
- 2023-24 reference: OREB% 3.6%, DREB% 21.1%

[Qualitative]
- "Elite rebounder for his position" (MavsDraft 2021)
- "Defensive rebound percentage: 10.8 per game (100th percentile, 'one of the best in the league')" (SI/OnSI April 2025, on 2024-25 sample)
- "Elite defensive rebounder; his ability to grab a defensive rebound and take off fuels the Hawks' transition offense" (multi-outlet 2024-26)
- 10.3 RPG in 2025-26 — top-of-position output
- "Catches the ball at the apex" — vertical leverage on rebounding (pre-draft 2021)

[Data gaps]
- None — strong stat coverage AND qualitative convergence

--- DOMAIN 7 — ATHLETICISM ---
[Stats]
- No combine vertical / lane agility on file — DNP at 2021 Combine
- 2025-26 speed/distance: 4.32 mph avg, 4.84 mph offensive (above-average for wings)
- Drive volume: 13.2/g (high for size — burst signal)
- Dunk rate: 22.7% (functional vertical translation)
- DREB chance conversion 75.6% adj (pursuit + vertical)
- 2023-24 reference: Avg speed 4.31, off 4.70 — slight uptick in motor in 2025-26

[Qualitative]
- "A terror in the open court... truly special functional athleticism" (Prospective Insight 2021/2025)
- "Phenomenal athlete" (MavsDraft 2021)
- "Plays above the rim with ease" (2021 scouts)
- "Lateral quickness is a strength; slides his feet well on defense and has the ability to get down and cover guards" (pre-draft 2021)
- "Boundless motor, constantly running the floor" (Yahoo 2024)
- Strength: "Filled out," "well-built," documented offseason weight-room work; 220 lbs at 6'9" with 7'0" wingspan = above-average wing strength profile

[Data gaps]
- No measured vertical / lane agility (DNP at combine)

--- DOMAIN 8 — IQ / MOTOR ---
[Stats — 2025-26]
- Shot zone: 23.0% Early clock 50.7% FG; 44.5% Average 44.3% FG; 6.9% Late 45.9%; 5.6% Very Late 36.2%
- Clutch: 34 GP, 2.9 PTS, 51.6% FG, 35.0% 3P, 80.6% FT, +/- 0.0, 0.7 AST, 0.4 TOV
- TS% 58.1% on 24.0% est USG (above-average wing efficiency at high usage)
- Estimated USG ~24% (script reported 0.0% but cross-referenced with public aggregations: 22.5 PPG / 7.9 APG / 10.3 RPG with high touches reflects elevated usage)

[Qualitative]
- "He's a starter now, he's getting everything he wants, and he's still unsatisfied" (Chris Johnson, trainer; Yahoo 2024)
- "He has a boundless motor, constantly running the floor" (Yahoo 2024)
- "I watch a lot of guys who do everything. That's my mindset. I don't want to have there be a lapse of why I can't finish out a game." (Johnson 2024)
- "There's a hunger and an openness to want to be pushed" (Quin Snyder, roundtable.io 2025)
- "Inconsistency muddled some of Johnson's season... before exploding for huge performances" (Prospective Insight 2021)
- Shot selection self-acknowledged: "I feel like I could have taken better shots to put us in a better position" (Johnson post-game 2025-26)
- Series vs Knicks 2026 R1: "Johnson has struggled in this series" before Game 3 turnaround (SI/OnSI May 2026)

[Data gaps]
- USG% endpoint timed out on D3 (2025-26); inferred from public sources

--- CHARACTER / PROJECTION SIGNALS ---

Work ethic — strong multi-source positive:
- Trainer Chris Johnson: "He's a starter now... he's still unsatisfied" (Yahoo 2024)
- Quin Snyder: "There's a big part of him that wants to be really, really good. And if he's running into the wall sometimes, he's got to figure out not to run through it, but to run around it" (Yahoo 2024)
- Quin Snyder: "He's worked." "Sometimes you see something in a player, and it's not just what they do on the court. In his case, there's a hunger and an openness to want to be pushed." (roundtable.io 2025)
- Johnson: "Hard work really does pay off, and I'm a firm believer in that. The work is what really separates the ones that want to be something in this league." (Andscape 2025)

Competitive character:
- LeBron took him under wing; mentioned All-Defensive aspiration
- 13 triple-doubles in 2025-26 — sustained engagement across full season
- Elite-output games: 31/18/14/7stl vs Utah; 43/11/9 vs Charlotte (career-high); second-fastest triple-double in NBA history first half vs Denver
- Playoff series 2026 vs NYK — "best game" Game 3 (24/10/8/2stl in W); but uneven across the 6-game series; B grade from analysts; "It just sucks" exit-interview tone (post-loss). Did not fold — closed series with 21/8/6 in Game 6 even amid 51-point loss. Mature post-series language.

Trajectory: clearly improving year-over-year.
- 2021-22 rookie: 22 GP, 2.4 PPG (G League heavy)
- 2022-23: 70 GP, 5.6/4.0/1.2
- 2023-24 breakout: 56 GP, 16.0/8.7/3.6, 51.1/35.5/72.8 (MIP candidate; first triple-double; signed 5yr/$150M extension Oct 2024)
- 2024-25 interrupted: 36 GP, 18.9/10.0/5.0/1.6/1.0, 50.0/31.2/74.6 (MIP track before shoulder)
- 2025-26 ascent: 72 GP, 22.5/10.3/7.9/1.2, 58/40/81.2 (1st All-Star, MIP top-4 candidate, franchise cornerstone after Trae trade)

Negative signals (multi-source, historical):
- Pre-Duke "character/motor concern after leaving multiple programs" (MavsDraft 2021) — IMG departure (sr. year HS), Duke opt-out Feb 2021. Slid from projected top-5 to #20.
- Johnson self-acknowledged in 2025: "I didn't understand how to look at it from a bigger picture point of view. I let a lot of outside noises kind of distract me from what's really important."
- Snyder "coached him pretty hard" early — narrative now framed as resolved
- Defense focus consistency flagged in 2024-25 review

--- PLAYOFF / BIG-GAME TRACK RECORD ---

Sample status: 1 NBA playoff series (2025-26 R1 vs NYK) + brief Play-In appearance 2022-23. Below R13 sample minimum (≥2 series across different years). Classification: BELOW SAMPLE — playoff data is directional only, not yet primary input to #26.

NCAA tournament: Johnson did not play in NCAA tournament (Duke missed it 2020-21 season; Johnson opted out Feb 2021). No prospect-side R13 sample available.

2025-26 vs NYK (lost 2-4):
- Series: ~19.5 PPG / 7.7 RPG / 5.2 APG
- Game 2 (W): 17 PTS, 8 REB, 3 AST, 1 STL — 36 min
- Game 3 (W): 24 PTS, 10 REB, 8 AST, 1 BLK, 2 STL — 38 min ("probably the best game of the series for Johnson"; "first player in Atlanta franchise history to record those minimums in a single game" — SI/OnSI May 2026)
- Game 5 (L 126-97): 18 PTS, 10 REB, 6 AST — 35 min (team-high)
- Game 6 (L 140-89, 51-pt blowout home): 21 PTS, 8 REB, 6 AST, 1 BLK — 32 min (sustained output despite team collapse)

Recency: Active (within last 2 playoff cycles).

R13 status: Below sample minimum; playoff sample treated as directional confirmation (positive — sustained output, mature post-series tone) rather than primary modifier. R13 Stage 1/2 modifier: 0 (insufficient sample).

--- INJURY HISTORY ---

Pre-NBA:
- Senior HS (2019-20): Left IMG Academy mid-year; played only 9 games at Nicolet (return to home program). Reasons not fully documented; possible undisclosed factor.
- December 2020 (Duke): Foot injury; missed 3 games; returned but opted out Feb 15 2021.
- 2021-22 rookie season-end: non-surgical left knee procedure.

NBA career:
- January 23 2025 (mid-2024-25 season): Left shoulder dislocation while blocking a Scottie Barnes layup vs Toronto. Diagnosis: torn labrum. Surgery late January / early February 2025 at Emory Sports Medicine Complex. Missed remainder of 2024-25 (36 of 39 GP played pre-injury).
- Recovery: Hawks GM Onsi Saleh declared Johnson "fully healthy" entering 2025-26 (October 2025). Confirmed by 72-GP 2025-26 sample with no in-season absences.

R9 / R12 evaluation:
- R12 not formally applied — 2025-26 is a healthy 72-GP sample (the script's MPG-band fragment classification appears to be a false positive given his 2022-23 lower-MPG qualifying year skewing rotation_mpg). Script-side override warranted on this case.
- R9 not applied — full healthy-clearance 2025-26 sample is the eval anchor; no athleticism suppression to temper.

Durability projection note: His 2025-26 was first complete (>70 GP) season since junior year of HS. Multi-program / multi-year injury / DNP pattern weighed in the past; clean 2025-26 is positive signal but durability remains a watchpoint, not a current liability.

--- DATA GAP INVENTORY ---

Strong support (3+ sources):
- Physical (combine measurements) — primary signal; not re-projectable
- D1 At-basket finishing — 2025-26 stats + 2024-25 SI 88th pctile + multi-source qualitative
- D4 Court vision + Passing — full stat suite + Soaring Down South 98th pctile creator + MavsDraft + Snyder + multiple outlets
- D6 Defensive rebounding — 24.1% DREB% + 100th pctile language (2024-25) + multi-outlet convergence
- D8 Effort/motor + Competitive character — Snyder + trainer + Andscape + Yahoo + LeBron mention + sustained 2025-26 production
- Injury history — official Hawks announcement + AJC + multi-outlet confirmation

Moderate support (2 sources):
- D2 CAS 3PT — script (35.2% weighted) + public aggregations (~38–40%) — flagged S105-F01 conflict
- D2 FT — script + multi-season trend
- D3 Handling — 2025-26 stats + multi-outlet
- D5 On-ball + Help — 2025-26 stats + 2024-25 SI percentile language
- D7 Burst / Lateral — qualitative-only without combine numbers; speed/distance + drive volume serve as proxies
- D7 Strength — body type + free throw rate + qualitative

Weak support (1 source):
- D2 Off-dribble shooting — stats only (PU Zone 28.4%); no specific qualitative language captured beyond general "creates" notes
- D2 Mid-range — limited specific qualitative (PU Mid 47.0% the cleanest read)
- D3 Post offense — no documented post role; absence is data

No direct evidence:
- Sub-domain #3 Post offense — no script support and minimal qualitative; "absence is data" — baseline read

Conflicting signals:
- 2025-26 3PT% 35.2% (script weighted) vs ~40% (public aggregations); per S105-F01, defer to script as conservative anchor
- 2025-26 DFGPOE +1.2% (mid-negative) vs 2024-25 SI "91st pctile closeout effect" — usage / role expansion in 2025-26 likely traded some defensive sharpness for primary-creator role load

=== END RESEARCH PACKET ===
