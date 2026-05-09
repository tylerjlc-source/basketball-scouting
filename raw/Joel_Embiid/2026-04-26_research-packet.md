# Research Packet — Joel Embiid — 2026-04-26

```
=== RESEARCH PACKET ===
PLAYER:            Joel Hans Embiid
POSITION:          Center
AGE:               32 (born 1994-03-16)
TEAM:              Philadelphia 76ers
COMPETITION LEVEL: NBA
EVALUATION DATE:   2026-04-26
```

**Evaluation window flag (eval_window.py R12 trigger):**
Evaluation window: 2022-23 applied as primary per R12 — 2025-26 (38 GP, 31.6 MPG — fragment), 2024-25 (19 GP, 30.2 MPG — compromised), 2023-24 (39 GP, 33.6 MPG — fragment) all sub-healthy. Healthy anchor: 2022-23 (66 GP, 34.6 MPG, MVP season). Per Tyler's Skill 1 directive (option 2), 2025-26 statistical pull retained as worst-observation downside check; scoring numerically anchored on 2022-23, with worst-observation rule pulling sub-domain scores toward 2025-26 floor where the gap is material. R9 (injury temper) handled at composite stage.

---

## --- PHYSICAL PROFILE ---

```
Height:         7'1" (in shoes, private workout 2014); 7'0" listed playing height
Wingspan:       7'5.75" (private workout)
Weight:         280 lb listed (career range 250–300)
Standing reach: 9'5.5" (private workout — some observers question vs. standard combine)
Vertical:       Unknown (no combine measurement; skipped 2014 combine)
Lane agility:   Unknown
Body type:      Filled-out, frame-mature; weight has fluctuated significantly during rehab cycles
```

Source: NBA Big Board / Chad Ford private workout 2014; Basketball-Reference; Wikipedia. Note he skipped the 2014 NBA combine due to back injury — no official combine numbers.

---

## --- DOMAIN 1: FINISHING ---

**[Statistical — 2022-23 R12 anchor / 2025-26 worst-observation]**

| Metric | 2022-23 (anchor) | 2025-26 (worst-obs) | Delta |
|---|---|---|---|
| Rim FG% | 75.1% | (script bug — see gaps) | n/a |
| Non-Dunk Rim FG% | 71.8% | 67.5% | −4.3 |
| Dunk Rate | 19.4% | (0.0% script bug) | n/a |
| % Shots at Rim | 31.8% | (script bug) | n/a |
| FTR | 0.581 | 0.481 | −0.10 |
| FT% | 85.7% | 85.4% | −0.3 |
| Drives/g | 6.3 | 5.6 | −0.7 |
| Drive FG% | 57.8% | 46.0% | −11.8 |
| Drive PPP | 1.016 | 0.786 | −0.230 |
| Paint non-RA FG% | 49.0% | 46.6% | −2.4 |
| % Assisted | 62.6% | 64.8% | +2.2 |
| Post-up FG% (career playoff career mid-30s%) | — | — | — |

**[Qualitative]**
- "Embiid dominated the New York Knicks in the first round, averaging 35 points on 60.9% true shooting" — 2024 R1 vs Knicks, demonstrating elite contact-finishing under defensive resistance ([Fadeaway World](https://fadeawayworld.net/5-major-reasons-why-joel-embiid-is-one-of-the-worst-superstar-performers-in-playoff-history))
- "Notably, Embiid returned before the end of the regular season and put up a 50-point performance in Game 3 of Philadelphia's first-round series against the Knicks" ([ESPN/Basketball Network](https://www.basketballnetwork.net/latest-news/bill-simmons-on-joel-embiids-poor-showing-in-the-2024-playoffs))
- 2022-23 MVP season: 33.1 PPG on 65.5% TS — confirmed elite at-basket and contact finisher
- Foul-drawing: career-elite FTR (0.5+ in MVP windows). 2025-26 FTR drop to 0.481 reflects lower physical assertiveness post-knee
- 2025-26 mobility-related decline: "When Embiid has to quickly shift directions or move at pace, he's been detrimental" — affects drive efficiency directly ([Liberty Ballers Feb 2025](https://www.libertyballers.com/2025/2/17/24365038/joel-embiid-defense-nba-nurse-maxey-all-star-break-bucks-dame-pistons-raptors); language refers to 2024-25 post-return but trajectory carries into 2025-26)
- Drive FG% drop −11.8 points (57.8 → 46.0) is a cliff — physical-explosion indicator, not a skill regression

**[Data gaps]**
- Domain_1_Finishing__Stats.py rim metrics returned 0.0% / 0 attempts on the 2025-26 single-season override — likely a ShotChartDetail rim-zone extraction bug on partial-season data. Non-Dunk Rim FG% from Domain 3 (67.5%) used as substitute rim signal. Logging as new script bug for workstream-2 retrospective.
- Post-up volume/efficiency for 2025-26 not directly captured by Domain 1 script (post-up data lives in Domain 3 / Synergy); 2022-23 post-up framing was rare due to Nurse's face-up scheme — modest sample even at peak

---

## --- DOMAIN 2: SHOOTING ---

**[Statistical — 2022-23 R12 anchor / 2025-26 worst-observation]**

| Metric | 2022-23 | 2025-26 | Delta |
|---|---|---|---|
| TS% | 65.5% | 60.5% | −5.0 |
| eFG% | 57.3% | 52.7% | −4.6 |
| 3PT% overall | 33.0% | 33.3% | +0.3 |
| CAS 3PT% | 39.8% | 34.2% | −5.6 |
| Corner 3% | 25.0% | 25.0% | 0 |
| ATB 3% | 34.0% | 33.8% | −0.2 |
| 3PA total | 200 | 159 | (volume drop) |
| Pull-Up 3PT% | 22.4% | 25.8% | +3.4 (low volume both) |
| Mid-Range FG% | 48.7% | 46.3% | −2.4 |
| Mid-Range FGA | 351 | 214 | (volume drop) |
| FT% | 85.7% | 85.4% | −0.3 |
| Clutch FT% | 86.9% | 60.0% | −26.9 (small sample 2025-26) |

**[Qualitative]**
- "Embiid's improved face-up game" — Notre Dame Observer characterizing his Nurse-era shooting profile ([NDSM Observer](https://www.ndsmcobserver.com/article/2024/04/still-processing-joel-embiids-improved-face-up-game-solves-playoff-woes))
- Career FT% 83.0% — among the top FT shooters at the center position historically
- 2022-23 MVP season was an outlier high in CAS 3PT (39.8%); career 3PT% mid-30s. 2025-26 33% is regression to career baseline, not a step backward in stroke
- Mid-range elite at peak — the elbow/face-up pull-up has been a signature shot
- Clutch FT% drop to 60.0% in 2025-26 is small sample (2.0 PTS / GP, 20 GP clutch) but worst-observation flag for late-game finishing under fatigue/pressure

**[Data gaps]**
- Limited synergy on off-screen / off-ball shooting because Embiid is a primary handler/post player; 2025-26 OffScreen Synergy: 15 poss, 1.267 PPP (87th pctile) — small sample but positive
- Pull-up 3PT% sample very small both seasons (high volatility); not a signal load-bearing for off-dribble sub-domain

---

## --- DOMAIN 3: BALL SKILLS ---

**[Statistical — 2022-23 R12 anchor / 2025-26 worst-observation]**

| Metric | 2022-23 | 2025-26 | Delta |
|---|---|---|---|
| ISO PPP | 1.071 (80th) | 1.015 (77th) | −0.056 |
| ISO Poss | 434 | 131 | (volume drop, fewer games) |
| PnR BH PPP | 0.609 (11th) | 0.000 (no sample) | n/a (low-volume role) |
| Handoff PPP | 0.000 (0 poss) | 0.600 (20 poss) | (small sample) |
| Touches/G | 71.0 | 69.4 | −1.6 |
| Time of Poss | 3.1 min | 2.8 min | −0.3 |
| Dribbles/Touch | 1.18 | 1.17 | −0.01 |
| Points/Touch | 0.466 | 0.387 | −0.079 |
| USG% | 37.0% | 33.6% | −3.4 |
| Floater FG% (4-14ft) | 48.1% | 45.3% | −2.8 |
| Floater FGA | 455 | 201 | (volume) |
| TOV per 100 Touches | 4.8 | 4.1 | −0.7 |
| Estimated TOV% | 10.4 | 9.9 | −0.5 |
| A:TO Ratio | 1.21 | 1.38 | +0.17 |

**[Qualitative]**
- ISO 80th-percentile creator from the post and elbow at peak — face-up to spin, jab to mid-range pull-up, drives off the catch. Generates advantage on switches against guards and against most centers
- Touch / feel signature on the elbow / floater — among the more skilled big-man touch-shot profiles in the league at MVP peak
- 2025-26 USG drop (37 → 33.6) reflects Nurse's "passing culture" rebalancing toward Maxey + George ([Liberty Ballers — Nurse's offense](https://www.libertyballers.com/76ers-analysis/79022/nick-nurse-joel-embiid-sixers-new-offense-paul-george-tyrese-maxey))
- Points/Touch decline (−0.079) is a real efficiency-per-touch drop; ISO percentile barely moved (80th → 77th) — creation skill durability is intact, only finishing efficiency dropped
- Ball security improved: A:TO 1.21 → 1.38, TOV% 10.4 → 9.9, despite role dilution — suggests cleaner reads at lower volume
- "It's a bit of a departure away from the way he plays" — Nurse on Embiid in pass-first scheme; "some ups and downs" ([Liberty Ballers](https://www.libertyballers.com/76ers-analysis/79022/nick-nurse-joel-embiid-sixers-new-offense-paul-george-tyrese-maxey))

**[Data gaps]**
- PnR BH 2025-26 has zero possessions (dramatic role change vs. 23 poss in 2022-23) — reflects scheme/role, not skill loss
- Post-up creation volume for 2025-26 not separately surfaced; drives data is best proxy

---

## --- DOMAIN 4: PLAYMAKING ---

**[Statistical — 2022-23 R12 anchor / 2025-26 worst-observation]**

| Metric | 2022-23 | 2025-26 | Delta |
|---|---|---|---|
| AST/g | 4.2 | 3.9 | −0.3 |
| Potential AST/g | 6.3 | 7.1 | +0.8 |
| Conv rate (AST/Pot AST) | 66.7% | 54.9% | −11.8 |
| Secondary AST | 0.7 | 0.5 | −0.2 |
| FT AST | 0.1 | 0.5 | +0.4 |
| Adjusted AST | 4.9 | 4.9 | 0 |
| Adj AST % | 12.1% | 11.4% | −0.7 |
| AST Points Created | 10.8 | 10.5 | −0.3 |
| Passes/g | 40.5 | 43.0 | +2.5 |
| TOV/g | 3.4 | 2.9 | −0.5 |
| Cut PPP | 1.327 (55th) | 1.284 (44th) | −0.043 |
| OffScreen PPP | no data | 1.267 (87th, 15 poss) | new |
| Transition PPP | 1.211 (68th) | 0.985 (22nd) | −0.226 |
| Avg speed (mph) | 3.57 | 3.67 | +0.10 |
| Off speed | 3.69 | 3.78 | +0.09 |
| Def speed | 3.44 | 3.55 | +0.11 |

**[Qualitative]**
- Playmaking growth under Nurse is genuine — career-high 6.0 APG in 2024 reported, evolution to facilitator role ([Bleacher Report](https://bleacherreport.com/articles/10105219-76ers-joel-embiid-says-health-for-playoffs-more-important-than-2024-mvp-campaign))
- Potential AST UP in 2025-26 (6.3 → 7.1) — passes/G also up (40.5 → 43.0) — vision and willingness to read the floor have continued developing
- Conv rate drop (66.7 → 54.9) is the worst-observation tell: vision identifying reads, but receivers / surrounding finishing not converting (or some passes going through in heavier coverage)
- Transition PPP collapse (68th → 22nd pctile) is a mobility flag — old Embiid ran the floor enough to capitalize on transition; current Embiid is half-court anchored
- Off-screen PPP 87th pctile in 2025-26 (low sample) — suggests his off-ball setup work in Nurse's spaced offense is functional when used
- Speed metrics slightly UP in 2025-26 vs 2022-23 — interesting; suggests he's moving harder per touch in fewer minutes

**[Data gaps]**
- 2022-23 OffScreen had no Synergy sample; cross-season comparison limited for #14 off-ball movement
- Cut PPP percentile dropped 11 points but absolute PPP only −0.04 — league-wide Cut percentile shift may explain part of the percentile compression

---

## --- DOMAIN 5: DEFENSE ---

**[Statistical — 2022-23 R12 anchor / 2025-26 worst-observation]**

| Metric | 2022-23 | 2025-26 | Delta |
|---|---|---|---|
| Opp FG% (overall, closest defender) | 47.8% | 44.5% | −3.3 |
| D_FGA/g | 19.2 | 16.4 | −2.8 |
| DFGPOE | −1.8% | −4.2% | +2.4 (more suppression) |
| Deflections/g | 1.5 | 0.9 | −0.6 |
| STL/g | 1.0 | 0.6 | −0.4 |
| Contested shots/g | 10.2 | 8.1 | −2.1 |
| Contested 3PT/g | 1.7 | 1.9 | +0.2 |
| Contested 2PT/g | 8.5 | 6.2 | −2.3 |
| PF/g | 3.1 | 2.2 | −0.9 |
| ISO Defense PPP | 0.766 (82nd) | 0.979 (39th) | +0.213 (worse) |
| ISO Def poss | 1.2 (small) | 1.3 (small) | n/a |
| PostUp Def PPP | 0.800 (80th) | 1.500 (2nd) | +0.700 (sample 0.3 poss) |
| DEF_RATING | 110.2 | 113.2 | +3.0 (worse) |
| BLK/g | 1.7 | 1.2 | −0.5 |
| Charges drawn/g | 0.03 | 0.03 | 0 |
| Def loose balls/g | 0.35 | 0.16 | −0.19 |
| Def box-outs/g | 1.64 | 1.13 | −0.51 |

**[Qualitative]**
- "For the first time in his career, Joel Embiid's defense is doing more harm than help for Sixers" — Liberty Ballers Feb 2025 (refers to 2024-25 return; trajectory continuing into 2025-26) ([Liberty Ballers](https://www.libertyballers.com/2025/2/17/24365038/joel-embiid-defense-nba-nurse-maxey-all-star-break-bucks-dame-pistons-raptors))
- "When Embiid has to quickly shift directions or move at pace, he's been detrimental" (same source)
- "In pick-and-roll coverages, he's looked both dizzy and cement-footed" (same source)
- "His feet are slow enough that isolation defense is problematic" (same source)
- "He's too slow-footed to quickly contest shooters off screens, and the Sixers' defense has been at a disadvantage because Embiid makes wrong decisions and lacks the energy or explosiveness to correct them" (same source)
- COUNTER (rim protection holds): "In his early games after returning in early February 2025, opponents shot 21.9% worse than average on shots within 6 feet where Embiid was the closest defender, with opponents making just 41.4% of their shots when Embiid was the only obstacle between them and the rim. This was the best defensive mark for any center in that stretch" ([NBA.com Film Study](https://www.nba.com/news/film-study-sixers-joel-embiid-rim-protections))
- 2022-23 peak: All-Defensive consideration; ISO + post defense both 80th pctile
- 2025-26 split signal: opp FG% dropped (47.8 → 44.5) and DFGPOE improved (−1.8 → −4.2), BUT ISO def percentile collapsed (82nd → 39th) and DEF_RTG worsened (110.2 → 113.2). Reading: stationary contests still good (rim/post), perimeter mobility shot.
- Foul rate down 2025-26 — likely paired with reduced aggression / fewer rotations attempted, not improved discipline

**[Data gaps]**
- Rim protection at-rim stat (Opp FG% at rim) returned N/A both seasons — endpoint quirk
- ISO def sample only 1.2–1.3 poss — percentile swings are noisy; qualitative is the load-bearing signal
- Post-up Def 2025-26 sample 0.3 poss — too small for meaningful percentile; the 2nd-percentile reading is noise

---

## --- DOMAIN 6: REBOUNDING ---

**[Statistical — 2022-23 R12 anchor / 2025-26 worst-observation]**

| Metric | 2022-23 | 2025-26 | Delta |
|---|---|---|---|
| OREB/g | 1.7 | 2.0 | +0.3 |
| DREB/g | 8.4 | 5.7 | −2.7 |
| REB/g | 10.2 | 7.7 | −2.5 |
| OREB% | 5.7% | 6.3% | +0.6 |
| DREB% | 24.3% | 16.9% | −7.4 |
| REB% | 15.7% | 11.8% | −3.9 |
| OREB chances | 4.2 | 4.2 | 0 |
| DREB chances | 13.6 | 10.2 | −3.4 |
| OREB conv % | 40.6% | 47.2% | +6.6 |
| DREB conv % | 61.9% | 56.2% | −5.7 |
| Box-outs/g | 1.94 | 1.42 | −0.52 |
| Off box-outs/g | 0.30 | 0.29 | −0.01 |
| Def box-outs/g | 1.64 | 1.13 | −0.51 |

**[Qualitative]**
- 2022-23 elite DREB% (24.3%) — among the league's top defensive rebounders at peak
- 2025-26 DREB% collapse (24.3 → 16.9) is a major mobility/positioning indicator. Defensive box-out volume −31% (1.64 → 1.13)
- OREB% actually UP (5.7 → 6.3) — small sample but suggests offensive positioning intact, only the mobility-dependent DREB chase is degraded
- 2025-26 REB chances (DREB) down 25% — fewer opportunities, but conversion also down — both volume and efficiency degraded on defensive glass

**[Data gaps]**
- No qualitative scouting language specific to 2025-26 rebounding; relying on stats
- Career trajectory rebound% (per advanced stats) trends down with age + injury — hard to disentangle injury vs natural age decline

---

## --- DOMAIN 7: ATHLETICISM ---

**[Statistical / proxy — Domain 1, 3, 5 cross-references]**
- Standing reach 9'5.5" (private workout 2014); 7'5.75" wingspan
- Vertical: not measured at combine
- Drive FG% 57.8 → 46.0 (−11.8) implies severe burst loss between 2022-23 and 2025-26
- Speed metrics slightly up in 2025-26 (3.57 → 3.67 mph), but Drive PPP collapsed — reads as: covers similar floor in fewer minutes, but explosion off ground is reduced
- Dunk rate (2022-23) 19.4% of rim attempts; 2025-26 script returned 0% (script bug, but anecdotally dunk rate has dropped post-knee)

**[Qualitative — strength + size profile]**
- Frame is the single biggest reason he stayed productive in 2024-25 / 2025-26: 280-lb base lets him absorb contact even when explosion is gone
- Lateral quickness loss is the central scouting narrative on 2025-26 — confirmed multi-source ("dizzy and cement-footed" — Liberty Ballers; "feet are slow enough that isolation defense is problematic" — same)
- Strength remains an A-tier asset: posts up, walks back smaller defenders, rebounds in traffic
- Burst — formerly elite at MVP peak — clearly degraded post-Feb 2024 meniscus + Apr 2025 left knee scope. "Looking like a shell of himself" (2024-25 return, ESPN/Yahoo)

**[Data gaps]**
- No combine measurements for vertical / lane agility — strictly observational
- Pre-injury vs post-injury vertical decline magnitude not formally measured anywhere I could surface

---

## --- DOMAIN 8: IQ / MOTOR ---

**[Statistical — 2022-23 R12 anchor / 2025-26 worst-observation]**

| Metric | 2022-23 | 2025-26 | Delta |
|---|---|---|---|
| Defender contested% (0-4ft) | 48.6% | 42.0% | −6.6 |
| Wide open shot rate (6+ ft) | 14.5% | 18.2% | +3.7 |
| Shot clock late (<7s) | 27.8% | 24.2% | −3.6 |
| Shot clock very late (<4s) | 13.6% | 8.0% | −5.6 |
| Avg shot clock (15-7s zone) | 51.7% | 57.1% | +5.4 |
| Clutch GP | 36 | 20 | (volume) |
| Clutch PTS | 3.6 | 2.0 | −1.6 |
| Clutch FG% | 48.7% | 40.0% | −8.7 |
| Clutch +/− | +2.8 | +1.4 | −1.4 |
| Distance/g (mi) | 2.20 | 2.00 | −0.20 |

**[Qualitative]**
- Shot selection: more open looks in 2025-26 (wide open rate up 3.7 pp), fewer late-clock bailouts — Nurse's offense is generating cleaner attempts even with reduced primary creation
- Motor / character — see CHARACTER section below; major load-bearing qualitative signal
- Clutch FG% drop (48.7 → 40.0) is real worst-observation signal for late-game decision execution under fatigue; sample size 20 GP clutch is non-trivial
- Distance covered down 0.20 mi/g — fewer minutes, less floor coverage; not necessarily lower per-minute effort given speed metrics up

**[Data gaps]**
- Effort/motor evidence for 2025-26 is mostly inferred from physical metrics; very limited direct scouting language characterizing per-possession motor for current season
- Decision-making stats blend into Domain 4 conv rate, Domain 3 TOV — not a standalone read

---

## --- CHARACTER / PROJECTION SIGNALS ---

**[Work ethic evidence — multi-source]**
- "Embiid's work ethic has been questioned by some inside the organization, with reports indicating he hasn't always been a willing workout participant and has even blown off conditioning drills" ([Fadeaway World — professionalism questioned](https://fadeawayworld.net/nba/philadelphia-76ers/joel-embiids-professionalism-reportedly-questioned-nba-sixers-circles))
- "Criticisms of what was characterized as selfish behavior for not working on conditioning and proper eating, with questions raised about what role extra weight played in his numerous injuries" (same source)
- "Embiid gained more than 50 lbs in just over half a year while rehabbing an injury" — pattern of weight management failure during recovery cycles ([SI / 76ers](https://www.si.com/nba/76ers/onsi/news/doc-rivers-speaks-on-philadelphia-76ers-joel-embiid-issue-01jj2pc4dkqm))
- Doc Rivers public challenge: "Have you ever seen an out-of-shape MVP? It doesn't exist" ([NBC Sports Philadelphia](https://www.nbcsports.com/philadelphia/sixers/sixers-joel-embiid-doc-rivers-2021-nba-mvp))
- Pre-2024 playoffs partial counter: "Sixers' Joel Embiid drops weight, wants to be healthy for playoffs" ([ESPN](https://www.espn.com/nba/story/_/id/41533191/sixers-joel-embiid-drops-weight-wants-healthy-playoffs)) — shows capacity for short-window commitment when stakes high

**[Competitive character evidence]**
- "Always wanted to play that way" — Embiid endorsement of Nurse's pass-first scheme; suggests willingness to evolve role ([Sportskeeda](https://www.sportskeeda.com/basketball/news-always-wanted-play-way-joel-embiid-takes-subtle-dig-doc-rivers-lauding-nick-nurse))
- 2024 R1 vs Knicks: 35 PPG / 60.9% TS through Bell's Palsy + meniscus tear — competitive grit in hostile injury context
- 50-point Game 3 vs Knicks 2024 — heroic counter-evidence to "shrinks in big moments"
- Counter-balanced by: "15 points in an elimination game" (vs Boston 2023, MVP season elimination) — multi-source citation as low-water mark

**[Negative signals]**
- Multiple-source convergence on conditioning concerns (above)
- Injury frequency raises maintenance/conditioning question even if not directly causal
- "Embiid isn't Hurts… He never kept 'The Main Thing The Main Thing'" ([97.5 The Fanatic](https://975thefanatic.com/2024/11/19/joel-embiid-isnt-jalen-hurts/)) — local-media narrative, lower R2 weight but multi-outlet pattern
- "Joel Embiid's legacy is on the line and he has to finally tune out the noise" ([Liberty Ballers — Jun 2024](https://www.libertyballers.com/2024/6/4/24166480/nba-free-agency-paul-george-sixers-lebron-james-joel-embiid-injury-trade-rumors-jimmy-butler-ingram))

**[Trajectory: declining]**
- Multi-year health trajectory clearly declining post-Feb 2024 meniscus surgery; 2024-25 = 19 GP, 2025-26 = 38 GP through April with active appendectomy
- Skill durability (post-game touch, FT%, ISO PPP) holding up better than physical durability
- Career arc has been MVP → MVP-runner-up → consistent injury attrition

---

## --- PLAYOFF / BIG-GAME TRACK RECORD (R13) ---

**[Statistical — Playoff_Track_Record.py output]**

```
SAMPLE: 7 playoff seasons, 59 playoff games, 402 matched RS games
Career Playoff TS%:  58.0% (vs Reg Season 61.6%, delta −3.6)
Career Playoff PPG:  24.9 (vs RS 28.5, delta −3.6)
Career Playoff FGA:  17.2/g (vs RS 18.6/g)

LAST 3 PLAYOFF RUNS:
  2023-24  GP 6   TS% 59.2% (vs RS 64.4%, delta −5.2)  PPG 33.0
  2022-23  GP 9   TS% 56.1% (vs RS 65.5%, delta −9.4)  PPG 23.7
  2021-22  GP 10  TS% 59.0% (vs RS 61.6%, delta −2.6)  PPG 23.6

CLASSIFICATION HINT: moderate statistical shrink (career delta −3.6)
```

**[Qualitative — multi-source convergence]**
- "Embiid has been called one of the worst superstar playoff performers in history" ([Fadeaway World](https://fadeawayworld.net/5-major-reasons-why-joel-embiid-is-one-of-the-worst-superstar-performers-in-playoff-history))
- "As the only MVP winner in history without a Conference Finals appearance" (same)
- "Embiid's numbers have historically fallen off a cliff in May" (same)
- 2023 elimination Game 7 vs Boston: 15 points, MVP season ended early ([Basketball Network](https://www.basketballnetwork.net/latest-news/bill-simmons-on-joel-embiids-poor-showing-in-the-2024-playoffs))
- COUNTER: 2024 R1 vs Knicks 35 PPG / 60.9% TS, including 50-point Game 3 — strong rise within that series despite series loss
- Net qualitative reading: convergent multi-source language on shrink narrative; rise instances exist but get overwhelmed by elimination-game low-water marks (2022 vs MIA, 2023 vs BOS)

**[Classification — manual per R13 protocol]**
- Statistical: Career delta −3.6 TS% / −3.6 PPG → moderate shrink (statistical alone)
- Qualitative: Multi-source convergence on shrink narrative ("worst superstar playoff performer," "falls off a cliff in May," "only MVP without CF appearance")
- AND-rule check (R13 strong = stat AND qual): both conditions support shrink. Magnitude: career delta is moderate (−3.6, not −5+); multi-year qualitative is convergent and explicit
- **Classification: moderate shrink (leaning strong)** — stat magnitude says moderate, qualitative consistency leans strong; final call goes to Skill 4 with this evidence
- Recency: Last completed playoff = 2023-24 (2 yr gap). 2025-26 active in real-time (Sixers vs Celtics R1, currently 2-1 Boston) but Embiid has not played any 2026 playoff game (appendectomy April 9, 2026)
- **Active-injury dormancy flag: APPLIES** — documented injury (appendectomy + ongoing knee management) ruling Embiid out of Games 1, 2, 3; doubtful for Game 4 ([Yahoo Sports — Game 4 injury report](https://sports.yahoo.com/articles/full-injury-report-joel-embiid-210501315.html))
- Per R13: dormant status = treat playoff classification as historical-record only, applied with caution

---

## --- INJURY HISTORY ---

**[Documented injuries — chronological]**
- Pre-NBA: Right foot stress fracture (2014, pre-draft); back injury (skipped 2014 combine)
- 2014-15 / 2015-16: Two full seasons missed (right foot follow-up surgeries)
- 2016-17: Knee/foot issues; 31 GP
- 2017-18 to 2020-21: Generally available (60+ GP); plantar fasciitis chronic
- 2021-22 playoffs: Orbital fracture + concussion (Round 1 vs TOR)
- 2023: Right knee bone bruise (10 games missed); right knee meniscus tear (career history note)
- 2023-24: Left knee meniscus surgery (Feb 6, 2024); returned for playoffs through Bell's Palsy ([NY1/AP injury history](https://ny1.com/nyc/all-boroughs/ap-top-news/2025/02/28/injury-history-embiids-left-knee-latest-in-long-line-of-ailments-of-76ers-all-star-center))
- 2024-25: Left knee swelling, never more than 4 GP in a row; 19 GP total; foot issues Jan 2025; ruled out late February 2025 ([KU Sports](https://www2.kusports.com/joel-embiid/2025/mar/01/joel-embiid-will-miss-the-rest-of-the-season-for-treatment-and-rehabilitation-of-his-left-knee/))
- April 11, 2025: Second arthroscopic surgery on left knee (14 months after first) ([NBA.com](https://www.nba.com/news/sixers-joel-embiid-arthroscopic-surgery-left-knee))
- Sept-Oct 2025: Returned for training camp; preseason debut Oct 18, 2025
- 2025-26 season: 38 GP, 31.6 MPG; missed early back-to-backs as planned rest; right knee soreness reported in-season
- April 9, 2026: Appendectomy in Houston ([CBS Sports](https://www.cbssports.com/nba/news/76ers-joel-embiid-appendicitis-nba-playoffs/))
- 2026 R1 playoffs vs Boston: Missed Games 1, 2, 3 (recovery); Game 4 doubtful ([Inquirer Game 3 live](https://www.inquirer.com/sixers/live/philadelphia-sixers-boston-celtics-game-3-live-updates-joel-embiid-20260424.html))

**[R9 (injury temper) flag]**
- **R9 likely applies — strong temper warranted.** Embiid has now had two left knee surgeries in 14 months, ongoing in-season management of right knee soreness, and a fresh 2026 playoff-eve appendectomy. Career availability rate (career GP / possible) is well below 60%. Injury history is structural and recurring, not single-event recoverable.

**[R12 (injury evaluation window) flag]**
- **R12 fires. Already triggered above.** Both 2025-26 (38 GP fragment) and 2024-25 (19 GP compromised) sub-healthy. Anchored on 2022-23 (66 GP, 34.6 MPG, MVP season) per eval_window.py.

---

## --- DATA GAP INVENTORY ---

**[Sub-domains with strong support (3+ sources)]**
- #1 At-basket finishing: stats (2022-23 + 2025-26), career playoff record, multiple game-level scouting accounts
- #2 Contact finishing / FTR: career FTR + drive data + multi-source playoff scoring narratives
- #4 CAS 3PT, #6 Mid-range, #7 FT: multi-season stats + career FT% baseline + Nurse-era face-up scouting language
- #11 Court vision, #13 Passing execution: passing tracking + Nurse-era playmaking development articles + 2025-26 in-game evidence
- #15 On-ball pressure, #16 Help defense, #17 Rim protection: stats + Liberty Ballers post-injury defensive narrative + NBA.com film study
- #21 Burst, #22 Lateral quickness: multi-source qualitative ("dizzy and cement-footed," "feet too slow," "shell of himself") + drive efficiency stats
- #23 Strength: career-long durable signal — frame as primary asset
- #25 Effort, #26 Competitive character: multi-source narrative (work ethic concerns + 2024 R1 grit + playoff shrink language)

**[Sub-domains with moderate support (2 sources)]**
- #3 Post offense: career identity but limited 2025-26 isolated data (Synergy post-up sample sparse)
- #5 Off-dribble shooting: pull-up sample low both seasons; pull-up zone splits + face-up scouting language
- #8 Handling/creation: ISO percentile + USG context; PnR BH role-eliminated 2025-26
- #9 Touch/feel: floater stats + career FT% as touch proxy; minimal explicit scouting language for current season
- #14 Off-ball movement: Cut + transition stats; 2022-23 OffScreen had no sample
- #19 OREB, #20 DREB: stats both seasons; minimal qualitative language
- #24 Shot selection: defender distance + shot clock stats; no direct scouting commentary

**[Sub-domains with weak support (1 source)]**
- #10 Ball security: A:TO + TOV%, no direct narrative
- #12 Decision-making: indirect via assist conversion drop and TOV reduction; no clean isolated read
- #18 Post defense: 2025-26 sample 0.3 poss is essentially zero; reliance on 2022-23 + multi-year reputation

**[Sub-domains with no direct evidence]**
- None — every sub-domain has at least one signal

**[Conflicting signals between sources]**
- **Defense at rim vs. perimeter:** NBA.com film study credits elite rim protection (best-in-NBA shot suppression at <6ft) post-return; Liberty Ballers same-period article calls his overall defense net-negative due to mobility loss. Resolution: both true — rim anchor function intact, perimeter mobility shot. Sub-domain split: #17 holds, #15/#16 degrade
- **Conditioning narrative:** Doc Rivers + Fadeaway + SI converge on work-ethic concerns; Embiid's 2024-pre-playoff weight drop and Nurse-era role flexibility provide partial counter-evidence. Reading: real concern, with capacity for short-window commitment when stakes are high
- **Playoff shrink narrative vs. 2024 R1 vs Knicks:** 35/60.9% TS performance (50-pt Game 3) is genuine counter to "always shrinks." But series-by-series pattern shows shrink in elimination games specifically, not first-round games broadly. Both signals coexist
- **Script bug — Domain 1 rim metrics 2025-26:** Domain 1 returned 0.0% Rim FG% / 0 attempts on `--season-override 2025-26`. Domain 3 captures Non-Dunk Rim FG% 67.5% from same dataset. Reading: ShotChartDetail rim-zone extraction script bug for partial-season data; Non-Dunk Rim from Domain 3 used as substitute. Logged as new script-maintenance backlog entry for workstream-2 retrospective

---

## --- SPIKE INSTRUMENTATION (workstream-2 retro inputs) ---

**Skill 1 cost approximation:**
- Doc load (CLAUDE auto + scout-research.md + BASKETBALL-BRAIN + SCRIPT-REGISTRY + scout-research-learnings): ~36k chars input ≈ ~9k tokens
- Script outputs ingested: 8 scripts × 2 passes (where applicable) + Playoff_Track_Record + eval_window = 16 calls; estimated ~30k chars total output
- Web search + parse: 7 queries × ~3k chars avg = ~21k chars
- Packet body authored: ~22k chars output ≈ ~5.5k tokens
- **Skill 1 input/output rough estimate: ~85k chars in / ~30k chars out — meaningful cost but unavoidable for an established NBA player with 7+ playoff seasons of career to consolidate**

**Automation candidates spotted in Skill 1:**
1. R12 detection + path-decision (default vs override) is deterministic; gating user-confirm question could be a sub-prompt or auto-flag rather than full conversation turn
2. Playoff_Track_Record classification hint reliability problem (S100-F01) is now confirmed across 5+ players — the script's classification-hint logic should be deleted, not maintained, and the classification step moved entirely to Skill 4 with manual qual+stat AND-rule
3. Domain script `--season-override` two-pass is mechanical when R12 fires + Tyler's Option 2 selected — could be automated as a single R12_OPTION2 mode in eval_window.py
4. Script bug (Domain 1 rim-zone on partial season) could be deterministically detected (rim FGA == 0 for an active high-volume player) and flagged as substitute-needed
5. Web search query templates for established NBA veterans could be standardized — same 6-7 query patterns consistently produce the right qualitative threads
```

---

*Skill 1 complete. Handing off to Skill 2 (scout-scoring).*
