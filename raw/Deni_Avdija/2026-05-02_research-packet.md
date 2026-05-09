# Research Packet — Deni Avdija — 2026-05-02

=== RESEARCH PACKET ===
PLAYER: Deni Avdija
POSITION: SF / PF (functional Wing; 2025-26 de facto primary ball-handler)
AGE: 25 (born 2001-01-03)
TEAM: Portland Trail Blazers
COMPETITION LEVEL: NBA
EVALUATION DATE: 2026-05-02

EVALUATION WINDOW: DEFAULT — 2025-26 (w=0.60) + 2024-25 (w=0.40). Both seasons healthy (66 GP / 33.3 MPG and 72 GP / 30.0 MPG respectively). No R12 trigger.

R13 STATUS: Below sample minimum (1 NBA playoff series — 2026 first round vs San Antonio, lost 4-1). Playoff_Track_Record.py NOT run. Qualitative playoff data captured below; classification = "below sample" per R13.

--- PHYSICAL PROFILE ---
Height:         6'8" (203 cm) — Basketball-Reference, ESPN
Wingspan:       6'9" to 6'9.5" (Blazer's Edge 2025-26 cites 6'9"; NBA Draft Room 2020 cites 6'9.5")
Weight:         228 lbs current (BBR 2025-26); 210 lbs at draft (2020)
Standing reach: unknown
Vertical:       unknown — no combine measurement found in any source
Lane agility:   unknown
Body type:      Filled-out NBA wing frame; +18 lbs since draft. Described 2020 as "average athlete by NBA standards" but with functional speed; "speed, strength and relentless drives" framing in 2025-26 (Portland beat aggregation)

================================================================================
DOMAIN 1 — FINISHING
================================================================================

[Statistical data — Domain_1_Finishing__Stats.py, weighted 60/40]

Sub-Domain #1 — At-Basket Finishing
- Rim FG% (weighted): 65.5% (current 65.7%, prior 65.1%)
- Rim FGA volume (weighted): 361.8
- % Shots at Rim (weighted): 37.2%
- Dunk Rate (weighted): 6.3%
- Non-Dunk Rim FG% (weighted): 63.5%
- % Assisted at rim (weighted): 52.4%

Sub-Domain #2 — Contact Finishing / Foul Draw
- FTR (weighted): 0.52 (current 0.573, prior 0.441) — meaningful YoY rise
- FT% (weighted): 79.6%
- Drives/G (weighted): 15.88
- Drive FG% (weighted): 52.7%
- Drive PPP (weighted): 0.543
- Paint non-RA FG% (weighted): 38.2%

[Qualitative signals]

Positives:
- "Avdija has a natural knack for creating contact and finishing despite it... aggressive mindset" (Last Word on Basketball, 2025-26)
- "He took 6.2 free throws per 36 minutes, which ranked 12th in the NBA, up from his prior season of 4.4 free throws per 36" (Ynet News, 2026)
- "Averaged 9.2 free throw attempts per game this season, second in the NBA behind only Luka Doncic" (Last Word on Basketball, Jan 2026)
- "He ranked near the top of the league in and-one plays" (Ynet News, 2026)
- "Added more patience near the rim: stopping, faking, shifting his body and throwing shot blockers off balance" (Ynet News, 2026)
- Floater/runner package: "part of his arsenal once he gets in the key and is met by a bigger defender" (NBA Draft Junkies; carry-over signal in 2025-26 via NBAScouting Live)

Negatives:
- **Left-hand limitation at the rim.** "The San Antonio Spurs forced Deni Avdija to the left throughout the playoff series, exposing a flaw in his skillset... San Antonio knows the star forward isn't as adept at driving with his left hand as he is with his right" (RipCity Project, April 2026). Confirmed across the 5-game series; "lack of a left hand" (Airalamo, April 2026).
- Foul-baiting controversy: Tari Eason viral comments after Avdija 41-pt / 15 FTA night; "the frequency of his free-throw attempts has received negative attention, leading to accusations about foul-baiting" (Last Word, Jan 2026). Not a skill knock per se, but a referee-environment flag.
- Playoff finishing deflation: "Attacks at the rim that would've generated whistles in the regular season just haven't been rewarded as frequently in the postseason" (SI.com Trailblazers, April 2026)
- Draft-era: "Prone to crashing towards a help defender from time-to-time" (Peachtree Hoops, Nov 2020) — mostly archival but still surfaces in TOV pattern

[Data gaps]
- No body-control / euro-step specific tracking
- Playoff splits cite "44/43/75" (Ynet) vs "8-of-28 first three games" (SI) — likely 3PT-specific or partial-series; reconcile is N/A pending series-level box scores

================================================================================
DOMAIN 2 — SHOOTING
================================================================================

[Statistical data — Domain_2_Shooting__Stats.py, weighted 60/40]

Sub-Domain #4 — Catch-and-Shoot 3PT
- CAS 3PT% (weighted): 35.8% (current 36.0%, prior 35.5%)
- Corner 3% (weighted): 33.6%
- Above-the-break 3% (weighted): 33.6%
- Total 3PA (weighted): 372.6

Sub-Domain #5 — Off-Dribble Shooting
- Pull-Up 3PT% LeagueDashPtStats (weighted): 28.8% (current 25.0%, prior 40.8% — prior figure flagged as small-sample/endpoint noise; ShotChart-derived PU Zone 3PT% weighted is 29.0%, which is the more reliable canonical)
- PU Zone Mid% (ShotChart wt): 49.2%
- ISO PPP (weighted): 0.986 (66.3 percentile)

Sub-Domain #6 — Mid-Range
- Mid-Range FG% (weighted): 42.2% (current 43.1%, prior 40.0%)
- Mid-Range FGA (weighted): 42.6

Sub-Domain #7 — Free Throw
- FT% (weighted): 79.6% (current 80.2%, prior 78.0%)
- FT% Career: 77.1%
- Clutch FT% (weighted): 83.1%

Overall shooting context (weighted): TS% 60.2%, eFG% 53.3%, 3PT% 33.5%

[Qualitative signals]

Positives:
- Catch-and-shoot framing: "He's become a knockdown 3-pointer shooter on spot-ups (40.7%)" (Blazer's Edge May 2025, reviewing 2024-25). **S105-F01 RECONCILE:** script CAS 3PT% 2024-25 alone = 35.5%, weighted = 35.8%. The 40.7% likely refers to broader Synergy Spot-Up play type (includes pump-fake mid-range), not the canonical CAS 3PT metric. Defer to script — Avdija is a respectable, NOT elite, CAS shooter.
- "His three-point percentage (38%) and free throw percentage (80.9%) are on track to be career bests" (Last Word, March 2025 — partial-season window for 2024-25). Weighted 3PT% per script = 33.5%; Avdija 2024-25 final 3PT% per Wikipedia ~36.5%. Article was a hot-stretch citation.
- "Reached career high...true-shooting percentage (60.5%)" (Ynet/Yahoo 2026) — converges with script's weighted TS% 60.2%

Negatives:
- **Off-dribble 3 is the largest skill weakness on offense.** Two independent Blazer's Edge cites: "puts up bricks when launching off the dribble (26.9%)" (May 2025) and "(25%)" (separate cite). Script confirms ~28-29% weighted. This is well below NBA average (~33-34%) and is a structural shot-creation ceiling.
- Slump pattern noted: "After two years of progress, Avdija fell back to 31.8% from beyond the arc... self-created 3-pointer largely disappeared" (slump-period article aggregation). 31.8% figure not confirmed as full-season; likely a stretch within 2025-26 (pre-back-injury). Flag.
- Draft-era jump-shot baseline: "30.6% on jump shots, 21% on jumpers off the dribble, 33% on 3-pointers" pre-draft (Peachtree Hoops 2020). Improvement over 5 NBA seasons is real but ceiling-limited.
- 2024-25 specific cite: "Three-point shot needs to be more bankable. He got open looks. He just wasn't completely consistent" (Blazer's Edge, May 2025 review)

[Data gaps]
- No Synergy spot-up PPP (different metric than CAS 3PT%); only inferred from articles
- Range distribution beyond ATB/corner unknown

================================================================================
DOMAIN 3 — BALL SKILLS
================================================================================

[Statistical data — Domain_3_Ball_Skills__Stats.py, weighted 60/40]

Sub-Domain #8 — Handling / Creation
- ISO PPP: 0.986 / FG%: 41.3% / TOV%: 11.7% / poss: 136 / 66.3 percentile
- PnR BH PPP: 0.911 / FG%: 46.2% / TOV%: 21.9% / poss: 363 / 64.3 percentile (heavy usage)
- Handoff PPP: 1.013 / poss: 70
- Touches/G: 76.1; Time of Poss: 4.9 min; Dribbles/Touch: 3.15; Points/Touch: 0.278
- Drives/G: 15.9; Drive FG%: 52.7%; Drive PTS/G: 8.5; Drive TOV%: 7.3%; Drive AST/G: 1.8
- USG%: 26.2% (script-canonical; article cited 23.8% "AST-included")

Sub-Domain #9 — Touch / Feel
- Floater FG% (4-14ft, weighted): 38.5% (current 39.9%, prior 35.1% — improving)
- Floater FGA (weighted): 212; Floater % of total FGA: 21.4%
- Non-Dunk Rim FG%: 63.5%
- FT% (touch proxy): 79.6%

Sub-Domain #10 — Ball Security
- TOV per 100 Touches: 4.4 (current 4.6, prior 4.2)
- Estimated TOV%: 12.8%
- A:TO Ratio: 1.62
- Raw season AST/TOV: 377 / 230 (weighted ratio 1.66)
- Clutch: 16 AST / 10 TOV in 110.6 clutch min

[Qualitative signals]

Positives:
- "The biggest stride in his game was creating for himself off the dribble to finish at the rim" (Ynet News, 2026)
- "He led the NBA this season in assists after drives" (Ynet/Yahoo, 2026) — 1.8 Drive AST/G is high for a wing
- Ambidextrous flash: "He can make shots with either hand off the dribble" (NBA Scouting Live)
- "Avdija emerged as a bona fide NBA star, leading the Blazers in nearly all statistical categories while taking on the roles of primary ball-handler, scoring option, and perimeter defensive stopper" (Last Word on Basketball)
- Floater touch: "Avdija has demonstrated the ability to use a pump fake off a dribble to score on a floater after dribbling in from the high post" (NBA Scouting Live)

Negatives:
- **Right-hand dominance at point of attack.** Spurs' 5-game scheme of forcing him left was effective enough to be a series-defining flaw. Indicates handle has a directional ceiling that playoff-caliber defenses can exploit.
- **Turnovers high.** "Third in the league in turnovers per 100 possessions with 5.4" (Blazer's Edge 2025-26). Raw TOV/G 3.8. PnR TOV% 21.9% is high for primary BH usage.
- "Struggled with his handle against pressure and was prone to crashing towards a help defender from time-to-time" (Peachtree Hoops, Nov 2020 — draft-era; element persists in TOV profile)

[Data gaps]
- No post-up usage data — sub-domain #3 (Post Offense) has no documented evidence at NBA level. Absence-as-data → baseline.

================================================================================
DOMAIN 4 — PLAYMAKING
================================================================================

[Statistical data — Domain_4_Playmaking__Stats.py, weighted 60/40]

Sub-Domains #11–13 — Vision / Decisions / Passing
- Passes/G (weighted): 52.7
- Potential AST (weighted): 11.4; Actual AST: 5.6; Conversion rate: 49.1%
- Secondary AST (weighted): 0.8; FT AST: 0.4; Adjusted AST: 6.7; Adj AST%: 12.7%
- AST Points Created (weighted): 14.7
- A:TO: 1.66 (current 1.76, prior 1.44 — improving)
- TOV / Potential AST: 0.30

Sub-Domain #14 — Off-Ball Movement
- Cut PPP (weighted): 1.335 / 55 poss / current 72 percentile (rose from 30 prior)
- OffScreen PPP: 0.855 / 69 poss / 36 percentile (current only — endpoint timeout for prior; partial signal)
- Transition PPP (weighted): 1.082 / 268 poss / current 55 pctile, prior 19 pctile (large YoY improvement)
- Avg Off-ball Speed: 4.60 mph (above-average wing speed)

[Qualitative signals]

Positives:
- "Excellent passer and a high-level decision-maker" (Ynet/Yahoo, 2026)
- "Led the NBA this season in assists after drives" (Ynet, 2026)
- Triple-doubles vs Bulls, Thunder, Spurs in 2025-26 (Last Word aggregation)
- Alley-oop chemistry with Donovan Clingan: "For much of the season, several possessions each night ended with Avdija throwing alley-oops to rookie center" (Ynet, 2026)
- Size + vision framing: "He checks all the boxes for a modern-day point guard with his size, ball-handling, speed, court vision, and floor spacing ability" (Blazer's Edge, 2026)
- Transition passing dexterity: "outlet passes, bullet passes in between defenders... darts to a shooter sprinting to the wing or the corner" (Peachtree Hoops 2020 — confirmed live by 2025-26 transition PPP rise)

Negatives:
- TOV volume is the persistent counter-signal. 2024-25 review: "Deni also led the team in turnovers, barely trailing Henderson... Paring those down would stake his claim to being a true table-setter" (Blazer's Edge, May 2025).
- Defenses scout the pass-first instinct: "Whenever Memphis doubles him, one of the important jobs will be helping the helper as Portland will naturally want to pass to the open target" (SI Grizzlies pre-game, 2026)
- 21.9% PnR BH TOV% is structurally high — decision-making-under-pressure ceiling is real

[Data gaps]
- OffScreen PPP missing for prior season (endpoint timeout); 36 pctile current alone is the only signal — sample of one season

================================================================================
DOMAIN 5 — DEFENSE
================================================================================

[Statistical data — Domain_5_Defense__Stats.py, weighted 60/40]

Sub-Domain #15 — On-Ball Pressure
- Opp FG% as closest defender: 48.6% (Overall)
- D_FGA/G: 12.1
- DFGPOE: +1.3% (slight negative — defenders shoot ~1.3% better than expected)
- Deflections/G: 1.6; STL/G: 0.9; Contested shots/G: 4.7 (Cont 3PT 1.7, Cont 2PT 3.0); PF/G: 2.5
- ISO Defense PPP: 0.883 / 2.2 poss 2-season (small sample); current 47 pctile, prior 73 pctile

Sub-Domain #16 — Help Defense
- Team DEF_RATING (on-floor): 115.0 (115.4 current, 114.5 prior)
- Charges drawn/G: 0.00; Def loose balls/G: 0.22; Def box-outs/G: 0.31
- BLK/G: 0.6; Deflections/G (cross-ref): 1.6

Sub-Domain #17 — Rim Protection
- Opp FG% at rim: N/A (D_FGA at rim endpoint NULL — known script gap, see SCRIPT-MAINTENANCE-BACKLOG.md)
- BLK/G: 0.6; Contested 2PT/G: 3.0
- Inferential only — wing not asked to rim-protect

Sub-Domain #18 — Post Defense
- PostUp Defense PPP: 1.249 / 0.9 poss 2-season (very small sample) / 13-15 percentile both seasons
- Def box-outs/G: 0.31

[Qualitative signals]

Positives:
- "Avdija stands with Camara as a true perimeter defender" (Blazer's Edge, May 2025)
- "Good middle-of-floor defender, something the Blazers don't always have on the perimeter" (Blazer's Edge, 2025-26)
- Portland defensive-system framing: "rangy, interchangeable wings, physical point-of-attack defenders" — Avdija central to this design
- EuroBasket 2025: "23 points, 8 rebounds, and 5 steals" vs France (FIBA, 2025) — active hands at international level
- Late-season hot stretch: "1.4 combined blocks and steals" over 8 games (search aggregation)

Negatives:
- DFGPOE +1.3% slightly negative (defenders shoot above expectation against him on closeouts/contests)
- "He doesn't really appear to have the typical defender mentality; his intensity level can wax and wane" (Peachtree Hoops, Nov 2020 — draft-era, no current-era explicit repeat but no overturning evidence either)
- Post defense PPP 1.249 (13-15 percentile) is very poor — mitigated by tiny 0.9 poss/season sample (rarely posted)
- Team transition D context: Portland gives up 16.6 fastbreak PPG (24th in league); Avdija's individual transition-D contribution unisolated

[Data gaps]
- No rim D_FG% endpoint (script null)
- No Opp 3PT% endpoint (null in current run)
- No matchup data (which positions he guards)

================================================================================
DOMAIN 6 — REBOUNDING
================================================================================

[Statistical data — Domain_6_Rebounding__Stats.py, weighted 60/40]

Sub-Domain #19 — Offensive Rebounding
- OREB/G (weighted): 1.26
- OREB% (weighted): 3.8%
- OREB chance%: 32.6% (adj); contested OREB% 50.0% (Avdija converts contested OREB chances at high rate when he attempts)
- OFF box-outs/G: 0.04 (very low)

Sub-Domain #20 — Defensive Rebounding
- DREB/G (weighted): 5.76
- DREB% (weighted): 17.6%
- DREB chance%: 66.5% (adj); contested DREB% 19.5%
- DEF box-outs/G: 0.31

Total: REB/G 7.06, REB% 9.8%, AVG_REB_DIST 6.1 ft (mid-range rebound positioning, consistent with wing/forward role)

[Qualitative signals]

Positives:
- "He rebounds at an impressive 11.7 per 100 possessions clip" (Blazer's Edge May 2025, reviewing 2024-25). Converges with weighted REB% of ~11.7% (per-100 ≈ REB% in this framing) — script-confirmed.
- 6.9 RPG career-high in 2025-26 across multiple sources
- EuroBasket: 9 reb vs Iceland, 8 reb vs France (FIBA 2025); 8.2 RPG at EuroBasket 2022 — consistent rebounding across contexts

Negatives:
- "The Blazers are putting a LOT of pressure on Clingan to generate rebounds for the team... The gap between him and everybody else is huge" (Blazer's Edge 2025-26) — implies Avdija's raw 6.9 RPG looks better in volume than rate; team rebounding leans heavily on Clingan
- No source highlights Avdija as a strong offensive rebounder or second-jump threat (absence-as-data → OREB% 3.8% is below-average for size)
- DREB chance% 66.5% is solid but not elite for a 6'8" / 228 lb wing

[Data gaps]
- None significant — script + EuroBasket converge

================================================================================
DOMAIN 7 — ATHLETICISM
================================================================================

[Statistical data — proxies from other scripts]

Sub-Domain #21 — Burst / Explosion
- Avg Off-ball Speed: 4.60 mph (above-average for wings)
- Drive FG%: 52.7% (top-tier conversion when getting downhill)
- Dunk Rate: 6.3% (modest — not a high-flyer)
- Total distance: 2.32 mi/G (high motor proxy)

Sub-Domain #22 — Lateral Quickness
- ISO Defense PPP 0.883 (small sample 2.2 poss)
- Deflections 1.6/G + STL 0.9/G — average hands-active markers
- No documented lateral agility / lane agility combine numbers

Sub-Domain #23 — Strength
- Weight: 228 lbs (current) vs 210 lbs (draft) — +18 lbs added muscle over 5 seasons
- "Speed, strength and relentless drives" framing (2025-26 portland beat aggregation)
- Drive FG% 52.7% on 15.9 drives/G implies functional finishing strength through contact

[Qualitative signals]

Positives:
- "Very fast in transition with the ball and a quick jumper off one and two feet... will be a tank in transition, being more functionally athletic than other kids with better empty-gym YouTube dunks" (NBADraft.net 2020)
- "He has good speed and quickness with the ball in his hands for his size, and he is very quick up and down the court" (NBADraft.net 2020)
- "Foundation of his rise is simple: speed, strength and relentless drives to the basket" (Portland beat, 2025-26)
- "Avdija leaves analysts and observers in awe when he has a full head of steam and a spread floor ahead of him" (Blazer's Edge, 2025-26)

Negatives:
- "Although Deni is athletic for Europe, he is an average athlete in the NBA" (NBADraft.net 2020). No current-era source explicitly upgrades or refutes this; consistent with 6.3% dunk rate.
- Left-side burst limited: Spurs forcing left for 5 games successfully (RipCity Project, April 2026) suggests directional first-step ceiling.
- No vertical jump measurement found in any source.

[Data gaps]
- No combine vertical, no lane agility, no shuttle, no bench
- No post-physicality quantitative data

================================================================================
DOMAIN 8 — IQ / MOTOR
================================================================================

[Statistical data — Domain_8_IQ_Motor__Stats.py, weighted 60/40]

Sub-Domain #24 — Shot Selection
- Defender distance distribution (2-season combined):
  - Very Tight (0-2 ft): 7.7% / Tight (2-4): 40.8% / Open (4-6): 28.7% / Wide Open (6+): 25.1%
  - Contested%: 48.5% (~half of all FGA contested — high for a high-usage primary)
- Shot clock distribution: 24-22 2.9% / VEarly 16.2% / Early 17.8% / Avg 48.2% / Late 7.6% / VLate 7.3%
- Shot-creation ratio: 1.44 PTS/FGA framing in 2024-25 review
- Mid-range usage 42.6 FGA at 42.2% — efficient shot selection within his ranges

Sub-Domain #25 — Effort / Motor
- Distance (weighted): 2.32 mi/G; Off 1.26, Def 1.10
- Avg Speed (weighted): 4.21 mph (Off 4.60, Def 3.83)
- Deflections 1.6/G; Def loose balls 0.22/G; Def box-outs 0.31/G
- Charges drawn: 0.00/G

Sub-Domain #26 — Competitive Character
- Clutch (weighted, 60 GP): 2.5 PTS, 47.2% FG, 36.0% 3P, 87.8% FT, +/- -0.6, 0.5 AST, 0.3 TOV
- Clutch FT 83.1% (sample for #7 cross-ref); Clutch FG% 47.2% — solid clutch shooting profile

[Qualitative signals]

Positives:
- "He is an excellent passer and a high-level decision-maker" (Ynet/Yahoo 2026)
- "He scored those points on just 11.7 field goal attempts per game. Nobody on the roster comes close to Deni's 1.44 point-per-shot ratio" (Blazer's Edge, May 2025)
- "While some of his younger teammates faded, he looked like a leader" in Spurs playoff series (Ynet, 2026)
- Maccabi: "Youngest MVP in Israeli league history" (multiple 2020 sources)
- "Competitive athlete with lots of skill and high basketball IQ" (NBADraft.net 2020)
- "He stopped opposing dribblers, rebounds at an impressive clip" (Blazer's Edge 2024-25 review)

Negatives:
- 5.4 TOV per 100 possessions (third-highest in NBA) — IQ counter-signal under pressure
- Off-dribble 3 selection issue: takes them at 25-29% — over-reliance on a low-efficiency self-created shot
- Playoff temper incident: held back from charging at De'Aaron Fox after a hard foul (Yardbarker, April 2026). Not disqualifying; signals emotional investment + composure-under-stress flag.
- Charges drawn 0.00/G (extreme low) — anti-correlate with defensive sacrifice metric

[Data gaps]
- No tracked screen-assist / hustle-charge data deeper than what's pulled
- No specific late-clock / late-game possession-by-possession breakdown beyond clutch aggregates

================================================================================
CHARACTER / PROJECTION SIGNALS
================================================================================

Work ethic evidence:
- Avdija quote: "I like to talk about things that I do for the younger generations to see, understand the work ethic, and what it takes to be at the highest level" (Eurohoops, 2025)
- "His leadership style was described as 'quiet, steady, built on work ethic and presence'" (Howard Blas, April 2025)
- Coach Veljko Perovic (formative): "He works hard... He gives smile, makes you laugh" (Sports Rabbi)
- +18 lbs added since draft (210 → 228) — durable physical investment

Competitive character evidence:
- Interim coach Tiago Splitter: "What Deni brings to the locker room is rare for a player his age. He's become our vocal leader in a time of uncertainty" (SI.com Trailblazers 2026)
- Avdija on team: "Our chemistry is amazing. It's one of the best chemistry teams that I've been on in a while"
- Self-doubt → determination arc: "Do I really belong here? Am I really going to be the basketball player I think I can become?" (Yahoo Sports 2026 reflective profile)
- Most Improved Player finalist (3rd in voting), first All-Star selection 2025-26, first Israeli All-Star in NBA history

Negative signals:
- Foul-baiting accusations (Tari Eason viral comments + league-wide narrative). Public-perception risk, not character indictment.
- Playoff temper episode (Fox confrontation). Single instance, restrained.
- 2020 draft-era: "Intensity level can wax and wane" (Peachtree Hoops). No current-era reaffirmation.

Trajectory:
- **IMPROVING** — every measurable area trending up. Wizards 2020-24 (gradual) → Portland 2024-25 (16.9/5.9/3.9) → Portland 2025-26 (24.2/6.9/6.7). Career-high in PPG, RPG, APG, USG, TS%, FTR, AST/G in 2025-26. Unanimous improvement narrative across sources.

================================================================================
PLAYOFF / BIG-GAME TRACK RECORD
================================================================================

NBA Playoffs:
- 2026 First Round: Portland vs San Antonio — lost 4-1 (Avdija's first NBA playoff series ever)
- Avdija series line: 22.2 PPG / 6.0 RPG / 4.6+ APG (Ynet); alt source cites 22.3/6.8/5.0 on 44/43/75 splits
- "Shot 8-of-28 through first three games" (SI April 2026) → likely 3PT-specific or partial-series; reconciled by series-end 44/43/75
- Spurs scheme of forcing him left held for 5 games → series-defining counter
- Leadership amid loss: "While some of his younger teammates faded, he looked like a leader" (Ynet 2026)
- Avdija: "This experience was needed" (Eurohoops post-elimination, 2026)

Below R13 sample minimum (1 series < 2-series threshold). **Classification: BELOW SAMPLE.** Recency status: ACTIVE (2026 playoff cycle). No R13 modifier applied; qualitative only.

International / FIBA:
- EuroBasket 2025: 20p/9r/3blk vs Iceland (W); 23p/8r/5stl vs France (W, upset). Israel's clear star, captain framing. Tournament-final placement not confirmed in available sources.
- EuroBasket 2022: 14.6 PPG / 8.2 RPG / 4.6 APG; Israel eliminated group stage (2-3)
- Maccabi Tel Aviv 2019-20: domestic title, playoff MVP, youngest in league history (19.2 PP40, 12 playoff appearances)

================================================================================
INJURY HISTORY
================================================================================

2024-25 (Portland Year 1):
- Multiple soft-tissue episodes — back (Dec 28-29), ankle (Jan 13-20, ~7 games missed), muscle/thigh (Feb 28–March 10), finger (April 6-13)

2025-26 (Portland Year 2):
- **Recurring lower-back injury (primary concern).** Left game vs Miami mid-season (Jan 2026). Missed 7 games. Returned. Aggravated Feb 22 vs Phoenix. "Missed 10 games over the past six weeks due to the injury and was clearly less than 100% in some of his seven appearances over that stretch" (SI March 2026). At one point "missed nine of Portland's last 12 games."
- Recovery: returned vs Indiana mid-March, 18 pts in 25 min; "the injury no longer appeared to be lingering" (Jerusalem Post)
- Played all 5 playoff games vs SAS — no postseason absence
- 66 RS games played (above 65-game threshold)

R9 (injury temper) — soft-tissue recurrence pattern documented but did not compromise the evaluation window. 66 / 72 GP across the 2 seasons, both healthy enough to anchor without R12. Worth noting as a long-arc durability flag but not a current-cycle scoring modifier.

R12 — NOT triggered.
R13 — Below sample (1 series).

================================================================================
DATA GAP INVENTORY
================================================================================

Sub-domains with STRONG support (3+ sources, script + qualitative):
- #1 At-basket finishing (script + 4+ sources)
- #2 Contact finishing (script + 5+ sources, FTR rise highly documented)
- #4 CAS 3PT (script + multiple article cites; reconciled S105-F01 — script canonical)
- #5 Off-dribble shooting (script + Blazer's Edge two-cite + draft baseline; convergent weakness)
- #7 Free throw (script + multiple)
- #8 Handling/creation (script + extensive Portland beat coverage of primary BH role)
- #10 Ball security (script + multiple TOV-volume cites)
- #11–13 Playmaking (script + 5+ sources, PPS/AST-after-drives lead cited multiple places)
- #20 Defensive rebounding (script + multiple)
- #25 Effort/motor (script + multiple)

Sub-domains with MODERATE support (2 sources):
- #6 Mid-range (script primarily; modest qualitative)
- #9 Touch/feel (script + scattered floater mentions)
- #14 Off-ball movement (Cut/Transition script strong; OffScreen partial — prior season endpoint timeout)
- #15 On-ball pressure (script + 2 qualitative cites)
- #16 Help defense (script + qualitative)
- #19 Offensive rebounding (script + absence-as-data)
- #21 Burst (proxies + qualitative)
- #22 Lateral quickness (proxies + qualitative)
- #23 Strength (proxies + draft-era + weight gain)
- #24 Shot selection (script + qualitative)
- #26 Competitive character (clutch script + multiple narrative sources)

Sub-domains with WEAK support (1 source / script-only / inferential):
- #17 Rim protection (script null at rim D_FG%; only BLK 0.6/G + cont 2PT 3.0/G — wing role makes this baseline-by-design)
- #18 Post defense (0.9 poss/season tiny sample, 13-15 pctile both seasons; PPP 1.249 directionally bad but non-decisive)

Sub-domains with NO direct evidence:
- #3 Post offense (no documented post-up usage at NBA level — absence-as-data → baseline)

Conflicting signals (S105-F01 reconciliations):
1. **CAS 3PT: 40.7% article (Synergy Spot-Up) vs 35.8% script (LeagueDashPtStats CAS)** — different metric definitions; defer to script for CAS sub-domain. Avdija is a respectable but not elite CAS shooter.
2. **Pull-Up 3PT 2024-25 raw 40.8% (PullUpShot endpoint)** vs **ShotChart PU Zone 29.0% weighted** vs **article 26.9% off-dribble** — endpoint quirk on PullUpShot prior; ShotChart + article converge in 26-29% range (CANONICAL).
3. **Playoff splits 8-of-28 first 3 games (SI) vs 44/43/75 series (Ynet)** — likely 3PT-specific partial vs total-series; both retained without override.
4. **31.8% 3PT slump cite** — sample window unspecified; not used as full-season anchor.
5. **TOV per-100 5.4 (Blazer's Edge) vs raw 3.8/G (multiple)** — different denominators; both consistent with a high-TOV primary BH.
6. **USG 23.8% (article, "AST-included") vs 26.2% (script base USG%)** — different metrics; both retained.

================================================================================
END RESEARCH PACKET
================================================================================
