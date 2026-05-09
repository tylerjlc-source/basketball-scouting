# Research Packet — Myles Turner — 2026-04-25

```
=== RESEARCH PACKET ===
PLAYER: Myles Turner
POSITION: Center
AGE: 29 (born 1996-03-24)
TEAM: Milwaukee Bucks (signed 4yr / $108.9M July 2025)
COMPETITION LEVEL: NBA
EVALUATION DATE: 2026-04-25

EVALUATION WINDOW (eval_window.py):
  Mode: DEFAULT
  Seasons: 2025-26 (0.60), 2024-25 (0.40)
  Detected: 2025-26 (71 GP, 26.9 MPG -- healthy), 2024-25 (72 GP, 30.2 MPG -- healthy)
  No R12 trigger.
  Single-team current season (Bucks) — no eval_window TOT-row aggregation bug risk.

ROSTER CONTEXT:
  - 2015–2025: Indiana Pacers (10 seasons; franchise blocks leader; 2025 NBA Finals run)
  - 2025–present: Milwaukee Bucks (replaced Brook Lopez alongside Giannis Antetokounmpo)

--- PHYSICAL PROFILE ---
Height:         6'11" with shoes (6'9.75" without per 2015 combine)
Wingspan:       7'4" (224 cm)
Weight:         250 lbs current (238.6 at 2015 combine)
Standing reach: 9'4" (2nd longest at 2015 combine)
Vertical:       No official no-step vertical recorded; scouts described as "not a particularly flashy athlete" pre-draft
Lane agility:   No recorded combine value
Body type:      Long, leaner-than-listed for a 250-lb 5; length-dominant rather than mass-dominant. "You can't teach the kind of length that Turner possesses" (Basketball Beacon).

--- DOMAIN 1 — FINISHING ---

Statistical (2-season weighted 60/40):
  Sub-domain #1 At-basket finishing:
    Rim FG%: 67.6% (curr 65.6 / prior 69.5)
    Rim FGA: 148 weighted volume; % shots at rim 20.6%
    Dunk rate: 26.5%; Non-dunk rim FG% 60.3%
    % Assisted: 88.4% (set up by others — pick-and-pop cuts/dunks, not self-create)
  Sub-domain #2 Contact finishing / foul draw:
    FTR: 0.282 weighted (curr 0.274 / prior 0.293) — modest for a 5
    FT%: 75.6% weighted; career 76.9%
    Drives/g: 1.44; Drive FG% 39.8%; Drive PPP 0.738
    Paint non-RA FG%: 40.3%
  Sub-domain #3 Post offense:
    No script play-type post-up output (volume too low to register in domain script)
    Post-up qualitative: "Only takes a shot or two out of it a game"; "above-average scorer when he uses it" (8 Points 9 Seconds)

Qualitative signals:
  - "Pops way more often than he rolls" after setting screen (Brew Hoop, 2025-04-21)
  - "His main job is guarding the rim, not cleaning up the miss" — frames offensive role as spacer first (iPacers, 2024-11-17)
  - Self-acknowledged: "those guys [back-to-basket bigs] kind of became extinct because you had to be able to, one, guard at a high level, and two, be able to stretch the floor" (Basketball Network)
  - 2025-26 Bucks: "scoring contribution did not materialize as hoped under Doc Rivers' coaching scheme" — 11.9 PPG, down from 17.0 in Pacers years (Brew Hoop end-of-season review)
  - 2024-25 Pacers: 16.7 PPG / 9.6 FGA, more central offensive role pre-trade

Data gaps:
  - Post-up volume below script's reporting threshold (no PPP returned) — qualitative only
  - Drive efficiency (39.8% FG, 0.738 PPP) below league average for primary drivers but he isn't a drive creator — directional only

--- DOMAIN 2 — SHOOTING ---

Statistical (2-season weighted 60/40):
  Sub-domain #4 CAS 3PT:
    CAS 3PT%: 39.7% (curr 39.3 / prior 40.2)
    Corner 3%: 45.9%; ATB 3%: 37.4%
    Total 3PA: 388 weighted volume — high-volume stretch big
  Sub-domain #5 Off-dribble:
    Pull-up 3PT%: 31.9% (curr 30.0 / prior 35.3) — well below CAS
    PU Zone Mid%: 36.1%
    ISO PPP: 0.929 (58.9 pctile)
  Sub-domain #6 Mid-range:
    Mid-range FG%: 48.3% weighted (curr 42.3 / prior 54.8) — large drop curr/prior
    Mid-range FGA: 60 weighted volume — limited use
  Sub-domain #7 Free throw:
    FT% weighted: 75.6%; career 76.9%
    Clutch FT%: 71.0%
  Overall context:
    TS%: 59.5%; eFG% 56.3%; 3PT% 38.8%

Qualitative signals:
  - "Career-best 39.6%" 2024-25 with Pacers — articles' figure reconciles with script's 40.2% prior weighted (S105-F01 check passes; consistent narrative)
  - "He really stretches the floor with his shooting range, and has great instincts offensively" (multiple stretch-five rankings)
  - "Leading all centers in total threes made this season by a wide margin" (Bucks-era, 2025-26)
  - 5.5 3PA/g 2024-25 — high volume for a center; 2025-26 still strong volume per script (388 weighted total)
  - "Spaces the floor, opens driving lanes, keeps opposing bigs honest" — gravity descriptor, multiple sources
  - Defender distance distribution (script): 4.7% very tight / 27.3% tight / 25.2% open / 42.7% wide open — 67.9% of shots at open or wider, normal for spacer big
  - Shot clock distribution: 53.2% in 15-7 average band — set offense / off ball flow, not late-clock creation

Data gaps:
  - Pull-up 3PT volume modest enough that 31.9% should weight toward "limited self-create" rather than "weak mechanic"
  - No specific corner-3 vs ATB-3 split on prior-season; current corner% is 45.9% which is strong

--- DOMAIN 3 — BALL SKILLS ---

Statistical (2-season weighted 60/40):
  Sub-domain #8 Handling / creation:
    ISO PPP 0.929 / 14 poss / 38.3% FG / 7.4% TOV / 58.9 pctile
    PnR BH: 0 poss (script returned zero — confirms not a PnR ball-handler)
    Handoff PPP: 1.153 / 13 poss — efficient when DHO action runs through him
    Touches/G: 35.5; Dribbles/Touch: 0.58 (low — quick decision processing)
    Drives/G: 1.4 (drive volume reflects spacer not creator)
    USG%: 19.1%
  Sub-domain #9 Touch / feel:
    Floater 4-14ft FG%: 41.1% (curr 39.3 / prior 42.7)
    Floater FGA: 132 — moderate volume short-range pop
    Non-dunk rim FG%: 60.3%
    FT% (touch proxy): 75.6%
  Sub-domain #10 Ball security:
    TOV per 100 touches: 3.9 (curr 3.7 / prior 4.2) — low rate per opportunity
    A:TO ratio: 1.07
    Estimated TOV%: 9.7
    Clutch TOV: 5 in 93.2 clutch min (low)

Qualitative signals:
  - Not a self-creator; built around connectivity actions (DHO, pick-and-pop, transition trail)
  - "Quick decision processing" implied by 0.58 dribbles/touch — touch-and-go big
  - Floater 41% is decent for the volume — supports legitimate touch in floater range

Data gaps:
  - No PnR ball-handler script output (volume too low)
  - Handoff sample (13 poss) is small — directional signal only

--- DOMAIN 4 — PLAYMAKING ---

Statistical (2-season weighted 60/40):
  Sub-domain #11 Court vision:
    Potential AST/g: 2.2 (modest)
    AST Points Created: 3.8/g
  Sub-domain #12 Decision-making:
    AST/TOV: 1.07
    Adj AST%: 8.0%
    AST/PotAST conv rate: 68.2% (efficient when he does pass)
  Sub-domain #13 Passing execution:
    AST: 1.5 / TOV: 1.4 / Passes/G: 22.6
    Secondary AST: 0.2
  Sub-domain #14 Off-ball movement:
    Cut: 85 poss weighted, 1.272 PPP (46th pctile curr / 40th prior — elite efficiency, modest percentile due to volume normalization)
    OffScreen: 10 poss curr only, 1.100 PPP, 72nd pctile (small but efficient)
    Transition: 87 poss weighted, 1.225 PPP (70th pctile)
    Avg off-ball speed: 4.45 mph (in line with active 5s)

Qualitative signals:
  - Limited pass volume (1.5 AST/g) consistent with non-hub 5
  - Cut PPP 1.272 confirms strong rim-rolling/cutting touch when he commits to roll vs pop
  - Transition 1.225 PPP / 70 pctile → fills lanes effectively in trail/sprint roles

Data gaps:
  - No D4 hub-passing language (he is a connector, not a hub) — consistent with Skill 3 archetype expectations

--- DOMAIN 5 — DEFENSE ---

Statistical (2-season weighted 60/40):
  Sub-domain #15 On-ball pressure:
    Opp FG% (Overall): 48.6%
    DFGPOE: -0.2% (right at expected — neutral on contest)
    Deflections/g: 1.6; STL/g: 0.7
    Contested shots/g: 8.3 (6.4 2PT + 1.9 3PT)
    PF/g: 2.6 (under career 2.9 — manageable)
    ISO Defense PPP: 0.955; pctile current 46.6 / prior 38.1 — average to slightly below
  Sub-domain #16 Help defense:
    DEF_RATING: 114.1 (curr 115.8 / prior 111.5 — uptick this year is concerning for an anchor)
    BLK/g: 1.8 weighted (script); 1.6/g 2025-26 standalone per articles; 2.0/g 2024-25 standalone
    Charges drawn: 0.00 (he doesn't take charges — verticality model)
    Def loose balls/g: 0.16
    Def box-outs/g: 1.28
  Sub-domain #17 Rim protection:
    Opp FG% at rim (DFGPOE rim split): N/A — script endpoint returned None for this player
    BLK/g 1.8 weighted is the strong residual signal
    Contested 2PT/g: 6.4 — high contest volume at the rim
  Sub-domain #18 Post defense:
    PostUp Defense PPP: 0.764 weighted (curr 0.72 / 89 pctile; prior 0.831 / 79 pctile)
    Post poss volume: 1.2 (very low volume — modern role does not invite frequent post attacks)
    PF/g cross-ref 2.6

Qualitative signals:
  - "Halts post-ups, deters players from even shooting, forces players to miss" — death sentence at rim (FOX Sports / Basketball Beacon)
  - "From 6 feet and in with Turner as the primary defender, opponents shoot 9.1% worse than expected" — top-5 league figure (BBall Index)
  - "Opp shoots <50% in the post; slightly above league average there" — solid but not elite vs old-school post
  - 2024-25 Pacers anchor: on/off DRtg gap 9.5 pts (104.3 on / 113.8 off)
  - 2025 Finals: 5 blocks Game 3 (most in Finals game in 3 years); 1.4 BLK/g across 7 Finals games — elite single-game spikes, modest game-to-game floor
  - "Aggressive pick-and-roll defense (jumping out on 52% of screens vs 20% in Games 1-2)" — scheme-flexible; can play higher than drop when needed (Pro Football Network)
  - Drop coverage: "incredible at these coverages" — 0.837 PPP roll-man defense (69 pctile), 0.727 PPP ball-handler defense (BBall Index)
  - Lateral quickness: "lacks great, or even good, lateral quickness"; "clearly lost a step of lateral quickness" as of March 2026 — age 29 decline signal (Behind the Buck Pass; Basketball Beacon)
  - Bucks 2025-26: "his expected defensive prowess... did not materialize as hoped" — at-rim impact has dipped from Pacers peak (Brew Hoop)
  - Foul tendency: "still has a tendency to bite on pump fakes as well as be overly aggressive with his hands at times" — recurring critique (8 Points 9 Seconds)

Data gaps:
  - Opp 3PT% as closest defender, Opp FG% >15ft, and DFGPOE-at-rim split all returned N/A from script for both seasons (endpoint quirk; not player-specific failure — consistent with S100-F01 NBA endpoint pattern though different field)
  - Charges drawn = 0.00 reflects rule scheme, not effort
  - 2025-26 on/off DRtg specific to Bucks not pulled in script — would refine help/anchor judgement

--- DOMAIN 6 — REBOUNDING ---

Statistical (2-season weighted 60/40):
  Sub-domain #19 Offensive rebounding:
    OREB%: 4.1% weighted (curr 3.9 / prior 4.3) — below average for a 5
    OREB/g: 1.18; OREB chances 2.5/g curr; OREB conversion 43.9% curr (improving prior 41.3%)
    Off box-outs: 0.21/g
  Sub-domain #20 Defensive rebounding:
    DREB%: 15.9% weighted (curr 15.2 / prior 16.9) — modest for a 5
    DREB/g: 4.7; DREB chances 9.2 curr / 10.7 prior; DREB conversion 47.6% curr (chance-pct adjusted 56.1%)
    Def box-outs: 1.17/g curr / 1.44/g prior
    Avg DREB distance: 5.2 ft — gathers within his radius, doesn't chase
    DREB contest%: 37% (most of his rebounds are uncontested)

Qualitative signals:
  - "Rebounding has long received the most criticism of Turner's traits" — chronic narrative (8 Points 9 Seconds)
  - "Poor work on the glass on both ends added up to the second-worst total rebounding percentage of his career at only 11.9%" — recent decline, age signal (iPacers)
  - "Hurt his rebounding chances: positioned above the arc to stretch the defense; main job is guarding the rim, not cleaning up the miss" — scheme cost framing, partially mitigates raw rate (iPacers)
  - "Bad defender that can't rebound and gets outplayed by opposing big men every night" — most aggressive critic framing (8 Points 9 Seconds historical)

Data gaps:
  - DREB% gap by lineup (with Giannis vs without) not pulled in script
  - Hustle box-out conversion ratios reasonable signal — supports "engaged box-outs but limited gather rate" read

--- DOMAIN 7 — ATHLETICISM ---

(No script — proxies + scouting language)

Statistical proxies:
  - Standing reach 9'4" (2nd longest 2015 combine) — primary defensive lever
  - Wingspan 7'4" — elite length
  - Dunk rate 26.5% (script Domain 1) — moderate for a center; not above-the-rim dominant
  - Drives 1.4/g — limited explosive perimeter creation
  - Avg defensive speed 3.97 mph (script Domain 8) — average for active 5s
  - On-ball ISO Defense pctile current 46.6 / prior 38.1 — slipping with age
  - Foul rate 2.6/g — under career 2.9, indicates cleaner-than-historic body control this window

Qualitative signals:
  - Sub-domain #21 Burst/explosion: "Not a particularly flashy athlete in terms of running and jumping" — scouts pre-draft (Bright Side of the Sun)
  - Sub-domain #22 Lateral quickness: "Lacks great, or even good, lateral quickness"; "lost a step" March 2026 (Basketball Beacon; Behind the Buck Pass)
  - Sub-domain #23 Strength: 250 lbs listed; "doesn't bully into the paint"; can use "size and finesse" (8 Points 9 Seconds) — functional rather than dominant strength

Data gaps:
  - No combine vertical or lane agility recorded
  - No published in-NBA timing data (3/4 court sprint times etc.)

--- DOMAIN 8 — IQ / MOTOR ---

Statistical (2-season weighted 60/40):
  Sub-domain #24 Shot selection:
    Defender distance: 4.7% very tight / 27.3% tight / 25.2% open / 42.7% wide open
      → 67.9% taken at open or wider — high-quality shot diet for spacer
    Shot clock: 2.0% / 7.3% / 19.9% / 53.2% / 9.4% / 8.1% (24-22 / vEarly / Early / Avg / Late / vLate)
      → ~70% taken in first half of clock (early to average) — flow-of-offense looks
    Mid-range FGA only 60 weighted total — disciplined avoidance of midrange
  Sub-domain #25 Effort / motor:
    Total dist: 2.06 mi/g; Off speed 4.45 / Def speed 3.97
    Hustle stats: deflections 1.6/g; def box-outs 1.17–1.44/g; def loose balls 0.16/g
    Contested shots 8.3/g
    Def speed 3.97 mph and total distance 2.06 mi are middle-of-the-pack for active 5s
  Sub-domain #26 Competitive character:
    Clutch 2-season: 58 GP, 1.4 PTS, 59.0% FG, 58.8% 3PT, +1.2 net, 0.1 AST, 0.1 TOV
    → Tiny per-game offense in clutch (low usage), but elite conversion when shots come

Qualitative signals:
  - "Loyal, hard-working and mature teammate" — Pacers scouting language since college (Rick Barnes' Texas program), consistent through career
  - Players' Tribune ("It Took Me 10 Years to Write This") — own framing emphasizes work, durability, professionalism
  - Putting in body work documented since 2018 (iPacers)
  - 2024 Pacers media day: "unfazed by contract situation, ready to do more"
  - Leadership: "elder statesman of the team... everybody kind of follows what I do in this city"
  - 2025-26 Bucks comments: Giannis publicly defended Turner from boos — positive ally framing
  - Negative framing: 2025-26 "did not play up to the contract"; one source says "worst season as a professional"; another says "Bucks have a massive Myles Turner problem that's impossible to fix" (decline framing)
  - No off-court character flags surfaced in search; no transfer/coach drama; long single-franchise run before age-29 free agency

Data gaps:
  - No quantified peer/opponent testimony
  - Bucks-fit qualitative is recent and mostly disappointment-coded — separate decline-on-court from Doc Rivers usage critique

--- CHARACTER / PROJECTION SIGNALS ---

Work ethic evidence:
  - Pacers scouts identified "loyal, hard-working, mature" at Texas; consistency through 11-year NBA career (multiple sources)
  - Documented body-work commitment since 2018 (iPacers)
  - Players' Tribune piece frames career as professional grind

Competitive character evidence:
  - Clutch FG% 59.0%, 3PT% 58.8% (2-season) — elite shot-making in late-game situations
  - Pacers franchise blocks leader after a decade — durability + commitment marker
  - Self-identified leadership tone post-Pacers ("everybody follows what I do")
  - Pre-Finals 2025: stated desire to win championship; followed through with mostly-uneven Finals output but Game 3 5-block performance was a signature defensive performance

Negative signals:
  - 2025-26 narrative: "disappointing first year in Milwaukee"; "worst season as a professional" per one Bucks blog; "decline" framing repeated
  - Lateral quickness explicitly said to have declined as of March 2026
  - Aggressive hands → pump-fake bites → fouls (recurring)
  - Rebounding effort/positioning critique chronic across career — cannot be separated from spacer-role frame

Trajectory: Plateaued / mild decline. Career-best shooting volume year (2024-25) immediately followed by step back in usage and impact (2025-26 in Bucks system). Age 29 — typical 5 aging curve from this point: floor protection holds for 2-3 more years before more visible drop. Not a rising trajectory.

--- PLAYOFF / BIG-GAME TRACK RECORD (R13) ---

Sample minimum: Met (66 GP across 7 playoff seasons / 12 series).
Recency: Active (last playoff 2024-25 NBA Finals; gap 1 year is current-season-not-yet-played, not historical-only).

Statistical rise/fall vs regular-season baseline (Playoff_Track_Record.py output):
  Career playoff TS%: 59.5% / Regular TS%: 58.4% / Delta TS%: +1.1
  Career playoff PPG: 13.8 / Regular PPG: 13.8 / Delta: +0.0
  Career playoff FGA: 10.2/g / Regular FGA: 10.4/g
  Most recent runs:
    2024-25: 23 GP, TS% 60.7% (vs RS 61.2, delta -0.5), PPG 13.8 — neutral run despite Finals appearance
    2023-24: 17 GP, TS% 63.7% (vs RS 62.6, delta +1.1), PPG 17.0 — positive
    2019-20: 4 GP, TS% 61.7% (vs RS 56.6, delta +5.1), PPG 15.8 — strong on small bubble sample

Qualitative rise/fall language:
  - 2025 Finals: "5 blocks in Game 3 (most in Finals game in 3 years)"; "first teammates with 5+ blocks and 5+ steals in Finals game since Iverson/Mutombo 2001" — high-leverage defensive moment (Pro Football Network)
  - 2025 Finals: "10.6 PPG, 4.4 RPG, 37.7 FG%, 21.4% 3PT" — modest box-score; Pacers fans noted "Turner's defense regressed last season, and he struggled heavily in the NBA Finals"
  - "Bucks will soon make a Myles Turner realization Pacers fans figured out in NBA Finals" — implies Finals exposed limits visible to Pacers fans (8 Points 9 Seconds)
  - Career framing absent of either "rises to the moment" or "disappears" — neutral-coded language predominates
  - Cross-source convergence: split. Defensive moments (blocks, scheme-flex jump-out) trend positive; offensive efficiency in Finals 2025 trends down

Classification (R13 manual):
  - Statistical: +1.1 TS% career delta = Moderate magnitude (not "strong"; "strong" typically requires ≥+2.0 TS% or comparable cluster of metrics)
  - Qualitative: Mixed — strong defensive moments paired with offensive shrink in 2025 Finals; no consistent "rises" language across multiple sources
  - Per R13: "strong" requires statistical AND qualitative; "moderate" requires either
  - **Final classification: Moderate statistical rise** (statistical qualifier met at boundary, qualitative is not strongly confirmatory; script's "strong" hint overridden per S100-F01)
  - Recency: Active (2024-25 Finals + 2025-26 active season)

--- INJURY HISTORY ---

Documented injuries:
  - 2015-16 (rookie): Left thumb fracture surgery, missed 21 GP (Nov-Dec)
  - 2017-18: Concussion + sore neck (Oct 2017)
  - 2018-19: Right elbow injury, missed 9 GP (January)
  - 2021-22: Stress reaction in foot (Jan 14, 2022) — ended season
  - Various: Back, neck, toe issues (day-to-day status, undocumented duration)
  - 2025-26 (per Pacers tweet referenced in search, may be mislabel): concussion evaluation Feb 2026 — full GP count of 71 suggests no extended absence

Eligibility window check:
  - 2024-25: 72 GP / 30.2 MPG — clearly healthy (≥58 GP threshold per R12)
  - 2025-26: 71 GP / 26.9 MPG — clearly healthy
  - **No R12 trigger.** No R9 injury temper applies.

--- DATA GAP INVENTORY ---

Sub-domains with strong support (3+ sources):
  - #1 At-basket finishing (script + multiple scouting reports + box scores)
  - #4 CAS 3PT (script + multiple stretch-five rankings + Bucks/Pacers narrative)
  - #15 On-ball pressure / #17 Rim protection (script proxies + BBall Index analytical piece + Brew Hoop scheme breakdowns + Finals coverage)
  - #18 Post defense (script PPP + multiple analytical pieces)
  - #25 Effort / motor (script hustle suite + multi-source character framing)
  - #26 Competitive character (clutch script + Players' Tribune + leadership quotes)

Sub-domains with moderate support (2 sources):
  - #2 Contact finishing (script + drive narrative)
  - #5 Off-dribble (script + general "not a self-creator" framing)
  - #8 Handling / creation (script + connector role narrative)
  - #14 Off-ball movement (script + DHO/cut framing)
  - #16 Help defense (script + Pacers on/off framing)
  - #19/20 Rebounding (script + chronic critique narrative)
  - #21–23 Athleticism (combine measurements + decline framing)

Sub-domains with weak support (1 source):
  - #3 Post offense — script returned no PPP, qualitative is single-source above-average framing
  - #6 Mid-range — script only; no qualitative deep dive (sample is also small)
  - #11–13 Playmaking trio — script + general non-hub framing only

Sub-domains with no direct evidence:
  - None — every sub-domain has at least script proxy or qualitative framing

Conflicting signals between sources:
  - 2025-26 defensive impact: script DRtg up to 115.8 (decline) vs. ongoing identity as elite anchor — reconcile via "decline within still-positive band" read
  - "Strong statistical rise" Playoff_Track_Record hint vs. R13 manual classification (boundary case requires AND-qualitative; landed Moderate per S100-F01 protocol)
  - Career-best 39.6% 3PT (multiple articles citing 2024-25) vs. script's 40.2% prior weighted — reconciles cleanly (S105-F01 check passes; no hot-stretch deception)
  - Rebounding: chronic critique vs. scheme-cost defense (positioning above arc, primary task is rim) — both true; rate is genuinely modest, scheme frame partially explains
```

