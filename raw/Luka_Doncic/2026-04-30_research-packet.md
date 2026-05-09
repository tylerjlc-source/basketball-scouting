# Research Packet — Luka Dončić — 2026-04-30

```
=== RESEARCH PACKET ===
PLAYER: Luka Dončić
POSITION: Guard (primary on-ball PG/SG; functional creator-guard)
AGE: 27 (DOB 1999-02-28)
TEAM: Los Angeles Lakers (acquired Feb 2, 2025 from Dallas Mavericks in Anthony Davis trade)
COMPETITION LEVEL: NBA
EVALUATION DATE: 2026-04-30

EVALUATION WINDOW (per eval_window.py):
  Mode: DEFAULT (no R12 trigger)
  Seasons used: 2025-26 (0.60) + 2024-25 (0.40)
  Detected: 2025-26 (64 GP, 35.8 MPG -- healthy), 2024-25 (50 GP per domain scripts, 35.4 MPG -- healthy)
  NOTE: eval_window.py reported 100 GP for 2024-25; this appears to be the S95-F07 TOT-row aggregation
  artifact (Dallas + Lakers rows summed). Domain scripts show 50 actual GP, which is the operative number.
  Both seasons cross the healthy threshold per auto-detection, so no R12 fires.
  R12 CANDIDACY (qualitative): Flagged for Skill 2/4 attention. 2024-25 included a ~2-month
  Dec-Feb calf-strain absence + post-trade recovery; 2025-26 ended April 2 with a Grade 2 hamstring
  (currently out for 2026 playoffs first round). Whether to apply Option 2 worst-obs pull is a
  Skill 2/4 judgment call -- script says no trigger.

--- PHYSICAL PROFILE ---
Height:         6'7" (201 cm) [Sportskeeda; Basketball-Reference]
Wingspan:       6'11" (211 cm) per most sources; 7'2" outlier flagged [Sportskeeda; Hoop Dojo]
Weight:         244 lb officially listed entering 2025-26 [Lakers PR; Heavy Sports; LWOS]
                  Eye-test framing: "weight listing doesn't match the eye test" -- looks
                  leaner despite higher number, attributed to added muscle [LWOS Sept 2025]
                  Prior listing 230 lb; +14 lb update followed visible offseason transformation
Standing reach: unknown (no combine data for European-prospect entry)
Vertical:       below-average; not a vertical-burst athlete [Stack; Bleacher Report]
Lane agility:   N/A (no combine data)
Body type:      "Wide-framed, 6-foot-7" [InsideHook]; legit small-forward size with
                guard skill [Bleacher Report]; mature adult frame
                Offseason 2025 transformation: 16-hr intermittent fasting 6 days/week,
                gluten-free / low-sugar, 250g protein/day [Men's Health; ESPN; CBS Sports;
                Al Jazeera]. Lakers source: "incredibly committed to his conditioning...
                dropped significant weight" [CBS Sports summer 2025].
                Self: "Just visually, I would say my whole body looks better" [ESPN Jul 2025]

============================================================
DOMAIN 1 — FINISHING
============================================================

[Statistical data — 2-season weighted 60/40]
  Sub #1 At-Basket Finishing:
    Rim FG% (weighted): 77.4% (current 81.6%, prior 70.9%)
    Rim FGA (weighted): 161.0
    % Shots at Rim: 12.9%
    Dunk Rate: 1.7%
    Non-Dunk Rim FG%: 77.0%
    % Assisted: 29.9%
  Sub #2 Contact Finishing / Foul Draw:
    FTR (weighted): 0.42 (current .443, prior .385)
    FT% (weighted): 78.1%
    Drives/game: 14.48
    Drive FG%: 58.0%
    Drive PPP: 0.731
    Paint non-RA FG%: 53.3%
    11.8 FTA/game in 2025-26 (NBA leader) [StatMuse; HoopsHype]

[Qualitative signals]
  At-rim:
    "Once he uses one of his tricks to get an edge, he is often fast enough to turn
    the corner" [Stack — athleticism profile]
    "Drives past the defender and goes to his floater game" when contact too close
    [The Stepien draft profile, retained pattern]
    Negative balance: relies on craft/footwork/body/deceleration to finish below the rim;
    no "explosive rim finisher" language found across reviewed sources. Rim FG% historically
    lags when conditioning slips.
  Contact / foul-draw:
    LeBron: "Luka who's very good at it... they've figured out a way to get in a rhythm"
    [Athlon Sports / Yahoo, 2025-26]
    Truehoop "Luka Rules": "took his time getting to the left side of the rim while
    his defender hopelessly tried to get back into position... nearly two seconds elapsed
    from when Dončić decided to drive until he laid it up while getting his defender to foul him."
    Negative balance: foul-draw framed as gamesmanship by some critics (Dan Patrick called
    parts "selfish") [BasketballNetwork]; NBA-wide free-throw decline framing flags
    diminishing returns risk [Diggin' Basketball].

[Data gaps]
  Drive PPP of 0.731 looks low against a 58.0% drive FG% and 11.8 FTA/g profile -- worth
  cross-checking against StatMuse for sanity (S105-F01 hot-stretch check passed: 33.5/7.7/8.3
  HoopsHype line is full-season, not small-sample).

============================================================
DOMAIN 2 — SHOOTING
============================================================

[Statistical data — 2-season weighted 60/40]
  Sub #4 CAS 3PT:
    CAS 3PT% (weighted): 38.1% (current 38.6%, prior 36.9%)
    Corner 3% (weighted): 23.8%   <-- low; flag for Skill 2
    ATB 3% (weighted): 37.6%
    Total 3PA (weighted): 801.2
  Sub #5 Off-Dribble:
    Pull-Up 3PT% (weighted): 35.9% (current 35.8%, prior 36.0%)
    PU Zone 3PT% (ShotChart): 35.6%
    PU Zone Mid%: 39.8%
    ISO PPP: 1.128 (90.4 percentile)
  Sub #6 Mid-Range:
    Mid-Range FG% (weighted): 42.6% (current 44.3%, prior 38.9%)
    Mid-Range FGA (weighted): 203.8
  Sub #7 Free Throw:
    FT% (weighted): 78.1% (current 78.0%, prior 78.2%)
    Clutch FT%: 84.4%
    Career FT%: 75.5%
  Overall:
    TS%: 60.4%, eFG%: 55.2%, 3PT%: 36.7%

[Qualitative signals]
  CAS 3PT:
    Older Mavs-era framing: "26.9% catch-and-shoot 3s" [The Ringer 2020] -- this
    is stale; script's 38.1% weighted CAS is the operative datum.
    "It may be more comfortable for Doncic to shoot in rhythm off the bounce" [Ringer]
  Off-dribble:
    Step-back signature shot. "Step-back threes hovering over 37%" [Sky Sports]
    Mechanism: "generates power when his lower half is lengthened... uses 'eccentric force'
    to create separation" [InsideHook]; "stepping 'across the chest' to make it more
    difficult for the defender to block" [Sky Sports]
    "Knack for changing his release point... high, low, or even on the side, keeping
    defenders guessing" [rubycom analysis]
    49-pt opening night vs MIN with five 3s [NBA.com 40-40 club]
  Mid-range:
    "Versatile on the offensive end, displaying proficiency in shooting three-pointers,
    mid-range jump shots, floaters and shots in the post" [The Stepien]
    "Can shoot the mid-range pull-up jumper or floater depending on what the defense gives"
    Jeremy Lin: "He reads feet like a book" [Basketball Network — Deep Bag breakdown]
    Post fadeaways and one-foot faders cited as repeatable counters when posting smaller
    guards [Smoking Cuban]
  FT:
    11.8 FTA/g. "Getting to the line at that level, and converting them at a career
    high... is a big reason... why he has remained the NBA's top scorer despite
    struggling with his three point shot" [Diggin' Basketball]

[Data gaps]
  Corner 3 sample at 23.8% looks like a low-volume artifact -- he rarely takes corner
  threes. Flag for Skill 2 (likely directional, not a real liability).
  S105-F01 hot-stretch check: 36.6% / 36.7% 3PT figures across sources match script
  weighted aggregate. No inflation detected.

============================================================
DOMAIN 3 — BALL SKILLS
============================================================

[Statistical data — 2-season weighted 60/40]
  Sub #8 Handling / Creation:
    ISO PPP: 1.128 (258 poss, 90.4 pctile, 44.0% FG, 7.6% TOV)
    PnR BH PPP: 0.996 (483 poss, 81.5 pctile, 44.7% FG, 14.9% TOV)
    Handoff PPP: 1.219 (45 poss)
    Touches/G: 85.2 | Time of Poss: 7.1 min | Dribbles/Touch: 4.15 | Pts/Touch: 0.367
    Drives/G: 14.5 | Drive FG%: 58.0% | Drive PTS/G: 10.5 | Drive TOV%: 6.7% | Drive AST/G: 1.7
    USG%: 36.8%
  Sub #9 Touch / Feel:
    Floater FG% (4-14 ft): 51.6% (current 53.1%, prior 48.1%)
    Floater FGA: 403 (31.1% of total FGA)
    Non-Dunk Rim FG%: 77.0%
    FT% (touch proxy): 78.1%
  Sub #10 Ball Security:
    TOV per 100 Touches: 4.5 (current 4.5, prior 4.4)
    Estimated TOV%: 10.1
    A:TO Ratio: 2.10
    Touches/G: 85.2
    Raw season: 471 AST / 224 TOV
    Clutch: 17 AST / 3 TOV in 78.4 clutch min

[Qualitative signals]
  Handle:
    "Mesmerizing display of footwork and finesse" creating space; "deep bag of crossovers,
    step-backs, up-fakes" [Sky Sports]
    "Master of deceleration to control his defenders" [Stack; Mavs Moneyball]
    Eccentric force / change-of-pace, not raw speed: "decelerating rated better than more
    than 90% of... NBA players who have tested at P3's facility" [Stack]
    "92nd and 93rd percentiles for eccentric force output and eccentric rate of force
    development" [Stack]
  Touch:
    Floater game; "deceleration helps him create space for floaters and mid-range jumpers"
    [Mavs Moneyball]
    Post fadeaway / one-foot fader cited as a go-to with mismatches [Smoking Cuban]
    "Crazy 3" / circus-shot reputation [ESPN circus shot game-winner]
  Ball security:
    2025-26 TOV: 4.0/g [StatMuse]; led Lakers in turnovers by wide margin [LakeShowLife]
    "All nine of his turnovers in a game against the Suns resulted in steals... most live-ball
    turnovers by any player in a game that season" [Rolling Out, Dec 2025]
    Trend improvement: "averaging just over three turnovers per game since the start of
    February, versus well over four from October to January... Lakers have recorded the
    second-best turnover rate in the league since All-Star break" [LakeShowLife]
    Vulnerability: "opposing teams have been making him play in a crowd on the perimeter
    and pressuring his ball-handling, which has left him vulnerable to losing the ball
    off the dribble" [LakeShowLife]
    Bulls game: 7-turnover loss with public self-criticism [Yahoo Sports]

[Data gaps]
  Handoff sample (45 poss) is small; ignore for primary scoring weight.
  Live-ball vs pass-out TOV split not isolated -- qualitative pull suggests live-ball
  turnovers under perimeter pressure are the primary failure mode. Confirm directionally
  in Skill 2.

============================================================
DOMAIN 4 — PLAYMAKING
============================================================

[Statistical data — 2-season weighted 60/40]
  Sub #11 Court Vision + Sub #13 Passing Execution:
    Passes/game: 52.2
    Potential AST: 13.5 | Actual AST: 8.1 | Conv rate: 59.9%
    Secondary AST: 1.1 | FT AST: 0.7
    Adjusted AST: 9.9 | Adj AST%: 18.9%
    AST Points Created: 20.1
  Sub #12 Decision-Making:
    AST: 8.1 | TOV: 3.8 | A:TO: 2.10
    TOV / Potential AST: ~0.28
    Transition PPP: 1.070 (224 poss weighted, 33-52 pctile bands)
  Sub #14 Off-Ball Movement:
    Cut: 19 poss weighted, 1.453 PPP (78-87 pctile, very low frequency 1.3-1.7%)
    OffScreen: 85 poss weighted, 1.016 PPP (current 48 pctile, prior 99 pctile but
      very small-sample 25 poss in 24-25)
    Off speed: 4.09 mph (offensive distance 1.30 mi/g) -- low for primary creator
    Total dist: 2.30 mi/game

[Qualitative signals]
  Vision:
    Popovich: "Magic Johnson-like... he sees the floor in that same way"
    [Silver Screen and Roll, retained]
    Carlisle: "Larry Bird and Jason Kidd" comp for "playmaking and court vision"
    [Silver Screen and Roll, retained from Mavs era]
    "Master manipulator who sets the floor as he wants it" [The Ringer]
    2024 ESPN feature on his "TD passes" driving Mavs WCF run vs. Wolves
  Decisions:
    "Master of reading and manipulating the paint... time their drives when defenders
    are forced to vacate" [mybasketballacademy]
    Self-aware on overload: "I'm just trying to balance that rhythm between getting
    a better shot or just some crazy shot. Obviously, I need to work on that" [Yardbarker]
    Reaves: "every now and then it's a curse to think you can make every shot" [Yardbarker]
    Negative balance: 4.0 TOV/g and the Suns 9-live-ball-TO game indicate decisions
    break down under perimeter pressure / late-clock hero plays.
  Passing execution:
    "Elite at orchestrating four-on-three situations" out of doubles [Wikipedia synthesis]
    Self: "my passes are faster than feet" [Silver Screen and Roll]
    8.3 APG in 2025-26
    ESPN 2024 piece details lobs and skips driving Wolves WCF win
  Off-ball movement:
    NO off-screen role language found across reviewed 2025-26 / 2024-25 sources.
    Implicit confirmation per The Ringer: "if Tim Hardaway Jr. or Seth Curry doesn't
    spring open as intended, [Doncic] can freelance to create a decent look against
    a dwindling shot clock" -- team designs off-ball action for others, not Luka.
    ABSENCE-AS-DATA: off-ball movement remains structurally minimal; pure creator role.
    OffScreen 99-pctile prior season is a 25-poss small sample -- not load-bearing.

[Data gaps]
  Most current quote material is JJ Redick (Lakers) or carryover Carlisle (former Mavs).
  Fresh top-coach playmaking quotes from the Lakers era are sparser. Flag for Skill 2
  source-recency weighting.

============================================================
DOMAIN 5 — DEFENSE
============================================================

[Statistical data — 2-season weighted 60/40]
  Sub #15 On-Ball Pressure:
    Opp FG% (overall): 47.5% | D_FGA/g: 15.9 | DFGPOE: +0.5%
    Deflections/g: 3.2 | STL/g: 1.7 | Contested shots/g: 4.9
    Contested 3PT/g: 2.7 | Contested 2PT/g: 2.2 | PF/g: 2.4
    ISO Defense PPP: 0.842 (3.2 poss 2-season -- very small sample, scheme-driven)
  Sub #16 Help Defense:
    DEF_RATING (on-court): 113.6 (current 115.6, prior 110.5)
    Charges drawn/g: 0.16 | Def loose balls/g: 0.36 | Def box-outs/g: 0.33 | BLK/g: 0.5
    Deflections/g (cross-ref): 3.2
  Sub #17 Rim Protection:
    Opp FG% at rim: N/A (script bug per S100-F01 / SCRIPT-MAINTENANCE-BACKLOG)
    BLK/g: 0.5
    Contested 2PT/g: 2.2
    Functional: not a rim protector; structural ceiling.
  Sub #18 Post Defense:
    PostUp Defense PPP: 1.118 (1.3 poss 2-season -- very small sample)
    Def box-outs/g: 0.33

[Qualitative signals]
  On-ball:
    "Lack of lateral quickness, poor foot positioning, and inconsistent effort on
    closeouts" [Fadeaway World — recurring]
    "Struggles to stay in front of quicker guards and can be beaten off the dribble"
    [Ftp Bills isolation deep dive]
    Counter (2025-26): "When he switches onto the ball, it's the lowest of any of
    the Lakers' perimeter guys in terms of points per possession, and he's shown
    that he can contain the basketball" [Yahoo / Silver Screen and Roll]
    NEGATIVE FLOOR: "Allowed nine blow-bys on 16 defended drives, the most by any
    player in a single playoff game during the 2025 postseason" [Fadeaway World —
    Wolves Game 5 elimination]
  Help / off-ball:
    "Inconsistent effort and limited quickness" [Diggin' Basketball]
    "In star-heavy lineups without true rim protection, opponents hunt mismatches
    relentlessly — guards drag Dončić into action, forcing late rotations" [LakersNation]
    Positive: "Generates steals and deflections" — passing-lane disruption is real
    [Silver Screen and Roll; Yahoo]
  Rim:
    Length is 6'11" wingspan but "not very long-armed or explosive" [Bleacher Report].
    No rim-protector language identified. Lakers ranked 20th defensive rating, 28th
    opponent 3PT% in 2025-26 [LakersNation] -- broader structural issue, not Luka alone.
  Post:
    Mostly "checks bigger wings where his size comes into play" [The Stepien]
    "Excellent rebounder for a guard... advanced metrics (EPM, RAPM, DARKO) consistently
    portray him as an above-average defender" [Fadeaway World; Diggin' Basketball]
    Negative balance: post defense as primary assignment is rare -- schemed away from
    it. No 2025-26 source describes him anchoring post coverage.

  2025-26 trajectory:
    "Dončić has taken steps forward defensively in recent games that his coaches have
    noticed" [ESPN]
    Redick: "he was right. You got to get a little bit more, especially from the star
    players. So that's on us. That's on me" [ESPN — accountability framing]
    "Better-conditioned Dončić should have more energy on defense" [Silver Screen and Roll]
    Counter: NBA Cup loss to Spurs -- "second time he hasn't gotten back on defense"
    [Heavy Sports / Van Gundy quote]; Lakers announcer Macdonald: "Luka — again he's
    complaining — gotta get back on defense" [Heavy Sports]

[Data gaps]
  Rim D_FGA/D_FG% N/A is the known LeagueDashPtDefend "Less Than 6Ft" endpoint bug
  (S100-F01 / SCRIPT-MAINTENANCE-BACKLOG B5). Score #17 at lower confidence and lean
  on qualitative + DEF_RATING context.
  ISO Defense and PostUp Defense samples are tiny (3.2 and 1.3 poss weighted) and
  scheme-driven -- not real signal for sub-domain scoring; lean qualitative.
  Defensive improvement framing is real but soft -- "improving" / "underrated piece"
  headlines exist alongside Lakers' 20th DRtg, NBA Cup transition lapses, and the
  2025 elimination-game tape. Treat improvement as directional, not transformational.

============================================================
DOMAIN 6 — REBOUNDING
============================================================

[Statistical data — 2-season weighted 60/40]
  Sub #19 OREB:
    OREB/g: 0.68 | OREB%: 2.1%
    Off box-outs/g: 0.02 -- effectively absent
  Sub #20 DREB:
    DREB/g: 7.22 | DREB%: 19.6%
    DREB Chance %: ~66%, Adj %: ~71%
    Avg DREB Distance: 5.3-5.7 ft
    Def box-outs/g: 0.27-0.42

[Qualitative signals]
  OREB:
    No specific offensive-rebound craft language identified across reviewed sources.
    ABSENCE-AS-DATA: not a meaningful OREB factor; he's the initiator above the action.
  DREB:
    "Defensive rebound percentage is 19.5, meaning he rebounds like a forward while
    most guards rebound at lower rates" [Diggin' Basketball]
    "One of the best wing defensive rebounders in the NBA" [Silver Screen and Roll]
    "Rebounds at an elite rate for his position" [Fadeaway World]
    Pattern: secures DREB then immediately initiates fast break — outlet/grab-and-go
    is a defined skill [Fadeaway World]
    7.7 RPG in 2025-26 [HoopsHype]

[Data gaps]
  None significant. DREB at guard position is a clear strength; OREB is a clean baseline.

============================================================
DOMAIN 7 — ATHLETICISM
============================================================

[Statistical data — proxy / no dedicated script]
  Dunk rate: 1.7% (Domain 1 cross-ref) -- low for primary creator
  Drive volume: 14.5/g (Domain 3 cross-ref)
  Avg offensive speed: 4.09 mph (Domain 4 cross-ref) -- low among primary creators
  Total distance: 2.30 mi/game

[Qualitative signals]
  Sub #21 Burst:
    Self: "Not everything is jumping high. I think I'm very athletic in other stuff.
    Balancing, controlling my body, what I do when I stop, slowing down" [Yahoo / BasketballNetwork]
    "Doesn't have burst in the traditional sense, but once he uses one of his tricks
    to get an edge, he is often fast enough to turn the corner" [Stack]
    P3 testing: "decelerating rated better than more than 90% of... NBA players"
    [Stack]; "92nd and 93rd percentiles for eccentric force output and eccentric
    rate of force development" [Stack]
    Offseason 2025: "first step seems notably quicker, particularly after his recent
    physical transformation" [LakeShowLife]
    Signal: deceleration / eccentric force is the elite trait, not vertical pop
    or first-step burst.
  Sub #22 Lateral:
    "Doncic does not possess the lateral quickness or foot speed that certain elite
    defenders make a living from" [Ftp Bills]
    "Inherent athletic limitation" [Fadeaway World]
    2025-26 improvement language: "early reactions showed clear signs of improvements
    in areas such as lateral agility, the quickness of his first step, and the sudden
    nature with which he could change directions" [LakeShowLife]
    Negative floor: 9 blow-bys in 2025 playoff Game 5 elimination [Fadeaway World]
  Sub #23 Strength:
    "Wide-framed, 6-foot-7 player" [InsideHook]
    244 lb listed -- physical, "bullies smaller defenders in the post" [Smoking Cuban]
    "Exceptionally good at controlling his hips and trunk during deceleration" [Stack]
    Mature adult frame; not a draft-era projection.

[Data gaps]
  No NBA Combine data (European prospect entry). Wingspan reported variance (6'11"
  most-cited vs. 7'2" outlier) is a flag.

============================================================
DOMAIN 8 — IQ / MOTOR
============================================================

[Statistical data — 2-season weighted 60/40]
  Sub #24 Shot Selection:
    Defender distance distribution: VeryTight 3.8% / Tight 34.9% / Open 50.6% /
      WideOpen 10.7% (Contested% 38.7%)
    Shot clock distribution: 24-22 0.7% / VEarly 10.1% / Early 19.5% / Avg 51.3% /
      Late 8.9% / VeryLate 7.3%
    Note: 2025-26 "Average" band returned 0 rows due to script timeout (S100-F01
    partial endpoint timeout). Operative reading is the 2024-25 + 2-season weighted
    combined which is intact.
    Shot zone distribution captured via Domain 2 (rim 12.9%, mid-range volume,
    floater-range 31.1%, 3PA volume 801.2 weighted).
  Sub #25 Effort / Motor:
    Total dist: 2.30 mi/g (low among primary creators)
    Avg speed: 3.74 mph | Off 4.09 | Def 3.39 (def speed near league average)
  Sub #26 Competitive Character:
    Clutch (2-season weighted 47 GP): 2.5 PTS / 41.7% FG / 34.3% 3PT / 77.1% FT
      / +/- 2.1 / 0.7 AST / 0.1 TOV
    Clutch FT%: 84.4% (well above season FT%)
    Two career game-winning 3-pointers in final 5s of a playoff game (joins LeBron,
    Lillard, Reggie Miller, Robert Horry per play-by-play era) [clutchpoints]

[Qualitative signals]
  Shot selection:
    Coaching green light is real: "routinely attempts wild shots, sometimes even
    early into a shot clock, due to the green light he has from his coaching staff"
    [Yardbarker]
    "Tends to go overboard in taking tough shots, especially the one-legged three
    with multiple defenders on him" [Yardbarker]
    Reaves intervention: "every now and then it's a curse to think you can make
    every shot" [Yardbarker]
    Self-aware: "I'm just trying to balance that rhythm between getting a better
    shot or just some crazy shot... Sometimes those are too much" [Yardbarker]
    Counter: 47.6% FG, 61.6% TS in 2025-26 -- efficiency holds despite the variance
    [HoopsHype]. The volume of "wild shots" has not collapsed efficiency -- but
    the shot diet is shaped by trust in his shot-making, not pristine selection.
  Effort / motor:
    Transition defense: "Luka is so bad in transition" -- recurring fan/analyst frame
    [Heavy Sports]
    "Argues with referee, leading to a 4-on-5 situation on the other end" [Jim Jackson]
    Van Gundy on ESPN broadcast: "That's the second time he hasn't gotten back on
    defense" [Heavy Sports]
    Conditioning-driven motor caveat: "appearing to have more energy late in games
    and stepping up on defense" post-2025 reset [LakeShowLife]
    NEGATIVE BALANCE: motor narrative is the most stable critique -- recurring
    across Mavs era and into 2025-26 even with conditioning gains.
  Competitive character:
    Big-game presence: Worthy: "I don't think we've ever seen one as consistent
    and as dominant as Luka Doncic" [Yahoo on Lakers' clutch performers]
    Kyrie: "He's prepared for these moments, and he's built for these moments"
    [clutchpoints]
    Negative balance: referee tantrums / tech-foul pattern is durable. "At least
    15 technicals in every season from 2021 to 2024" [recurring across multiple
    Mavs/Lakers writeups]; 2025-26 LA-Knicks "money gesture" toward officials drew
    league scrutiny [beIN Sports; Yahoo]
    Self-awareness present: "I gotta stop this, I know it's not right" [Fadeaway
    World, retained framing]

[Data gaps]
  2025-26 "Average" shot-clock band returned 0 rows due to API timeout. Operative
  reading still complete via 2024-25 + 2-season weighted combined.

============================================================
CHARACTER / PROJECTION SIGNALS
============================================================

Work ethic:
  Bifurcated trajectory:
    Through 2024-25: repeated reporting of poor conditioning habits and weight
    noncommitment; "fourth calf strain in about 18 months" by Christmas Day 2024
    [ESPN/MacMahon]; this drove the trade.
    Through 2025-26: repeated reporting of disciplined diet/training and visible
    improvement. 2025 offseason transformation -- 16-hr intermittent fasting, gluten-free,
    250g protein/day; Lakers source "incredibly committed" [CBS Sports; ESPN; Al Jazeera;
    Men's Health]. "Just visually, I would say my whole body looks better" [Doncic, Jul 2025].
    READ: real change, but recency-bias flag -- one offseason's discipline does not
    erase the prior pattern. Sustained over multiple offseasons is the real test.

Competitive character (positive):
  Clutch reputation, three-time scoring champion trajectory, multiple deep playoff runs,
  team leader on offense. "Built for these moments" framing convergent across multiple
  sources.

Competitive character (negative):
  Referee complaints / tech-foul pattern (15+ techs annually 2021-2024).
  Body language ("optically… doesn't look good" — Jim Jackson).
  Transition disengagement when frustrated.

Trade context (Dallas → LA, Feb 2, 2025):
  Harrison's stated reasoning per ESPN's MacMahon: "leaked that he would trade Luka
  Doncic if he didn't improve his conditioning following the Christmas Day game in
  2024," referencing "fourth calf strain in about 18 months" and "always the same
  problem regarding Luka's conditioning."
  Harrison framing to ownership: "the deal would be an awful investment, pointing
  to Doncic's conditioning concerns, poor off-court habits and recurring calf strains,
  predicting that his body would break down" [SI Mavericks].
  READ: Multi-source convergence on conditioning + off-court habits package as
  trade driver. Even though the trade has aged poorly for Dallas in basketball
  outcome, the character signals embedded in the pre-trade reporting are real.

Trajectory: improving (current season) following a documented reset; structural
  lower-body durability remains an open question (see injury history below).

============================================================
PLAYOFF / BIG-GAME TRACK RECORD (R13 sample minimum met -- 5 playoff seasons, 55 GP)
============================================================

[Statistical data — Playoff_Track_Record.py output]
  Sample minimum: Met (5 playoff seasons)
  Recency status: Active (last playoff: 2024-25, gap: 1 year)
    NOTE: 2025-26 playoffs in progress as of 2026-04-30; Doncic OUT for first round
    vs. Houston due to Grade 2 hamstring. Active-injury dormancy flag candidate
    for R13 -- defer to Skill 4 on whether this shifts recency status.
  Career playoff vs regular season (matched-season basis):
    Playoff TS%: 57.3% (55 GP / 5 seasons) | Regular TS%: 59.1% (312 GP / 5 seasons)
    Delta TS%: -1.8 (neutral / normal playoff efficiency drag)
    Playoff PPG: 30.9 | Regular PPG: 29.5 | Delta: +1.4
    Playoff FGA: 23.3/g | Regular FGA: 21.4/g
  Last 3 playoff runs:
    2024-25 (LAL vs MIN, lost 4-1): GP 5, TS% 60.8% (+2.1 vs RS), PPG 30.2
    2023-24 (DAL Finals run, lost 4-1): GP 22, TS% 55.6% (-6.1 vs RS), PPG 28.9
    2021-22 (DAL WCF run): GP 15, TS% 57.7% (+0.6 vs RS), PPG 31.7

[Qualitative signals]
  2024 NBA Finals (DAL vs BOS, lost 4-1):
    Series averages: 29.2 PPG / 8.8 RPG / 5.6 APG
    Game 1: 30/10 -- first 30-point double-double in Finals debut since Tim Duncan 1999
    Game 2: 32/11/11 -- first Maverick Finals triple-double
    Game 3: fouled out final minutes on controversial call; 27/6/6
    Game 4: 29 in 122-84 blowout win
    Game 5: 28/12/5/3 stl in close-out loss
    ESPN frame: "Luka Doncic has yet to truly grasp what defined Jordan, LeBron --
    and these Celtics" [ESPN, Jun 2024] -- directional negative; Finals stage rise
    within a series-loss frame, champion-gap framing.
  2025 Playoffs (LAL vs MIN, lost 4-1, first round):
    30.2 PPG / 7.0 RPG / 5.8 APG
    4Q struggles: "20 points on 5 of 15 shooting in the fourth quarter of the Lakers'
    four losses" [Basketnews]
    Game 5 defensive collapse: 9 blow-bys on 16 defended drives -- single-game
    postseason worst in 2025 [Fadeaway World]
    Charles Barkley public criticism after series [Basketnews]
    "Honeymoon-over" framing [FOX Sports]
  2026 Playoffs (LAL vs HOU, in progress, LAL up 3-1):
    Doncic OUT due to Grade 2 hamstring; per Shams "not expected to return during
    the first round" [Bleacher Report; Heavy]
    Active recency: zero 2026 playoff sample.

[Classification suggestion -- DEFER TO SKILL 4]
  Mixed track record with a clear negative recent beat. 2024 Finals showed rise
  within a series-loss frame; 2025 first-round exit features documented 4Q collapse
  and elimination-game defensive disaster; 2026 absent due to injury.
  Career stat delta (-1.8 TS%) is neutral / normal drag.
  Multi-source convergence supports neither "clear riser" nor "clear shrinker" --
  directional shrinkage in 2025 specifically.
  Per R13: "strong" requires statistical AND qualitative; "moderate" requires either.
  Most defensible frame: NEUTRAL by stats, with a flagged moderate-shrink signal
  on the most-recent qualifying run (2025 1st-round exit). Active-injury dormancy
  is also a candidate flag pending 2026 1st-round close-out.

[Recency status]
  Active (1-year gap to most recent playoff appearance), but candidate for
  active-injury dormant flag if 2026 1st round closes out without him playing.

============================================================
INJURY HISTORY
============================================================

  Calf strain cluster (2023-2024): "fourth calf strain in about 18 months" by
  Christmas Day 2024 [ESPN/MacMahon].
  2024-25 mid-season calf strain: cost ~2 months Dec-Feb; trade arrival to LAL
  delayed; post-trade played ~28 regular-season games for Lakers + 5 playoff games.
  2025-26 preseason hamstring strain: no regular-season time missed [SI].
  April 2, 2026: Grade 2 LEFT HAMSTRING strain vs OKC -- spin move near paint
  [NBA.com; SI]; ended regular season at 64 GP (one short of 65-game rule, costing
  awards eligibility).
  Treatment: traveled to Madrid for stem cell treatment [Yahoo].
  Status as of 2026-04-30: out indefinitely; not expected back for first round vs.
  Houston (Lakers up 3-1); "may even miss the second round against the Thunder"
  [Shams via Heavy Sports; Eurohoops].
  Aggregate framing flag: SI fantasy tracker reports "five hamstring injuries since
  2024" -- possibly conflating calf + hamstring; the distinct lower-leg injury
  cluster (calf + hamstring across 2023-2026) is the directional signal, not the
  precise count. Lower-body durability is a real long-term concern.

  R12 EVALUATION:
    Per eval_window.py (DEFAULT mode): no R12 trigger; both 2024-25 (50 GP healthy)
    and 2025-26 (64 GP healthy) cleared the threshold.
    Per qualitative reading: 2024-25 included a 2-month mid-season calf gap; 2025-26
    closed early with hamstring and currently dormant for playoffs.
    Recommendation: TREAT THE SCRIPT AS GOVERNING (no R12 fire), but flag the calf+
    hamstring durability pattern as a Skill 2 floor consideration (per memory
    feedback_r12_option2_worst_obs_pull -- only invoke Option 2 when R12 actually fires).

  R9 (injury temper) candidacy: Possibly applicable for current-season finish;
  consider whether 2025-26 sub-domain scores need any temper given the season
  ended on injury rather than completing 82.

============================================================
DATA GAP INVENTORY
============================================================

[Sub-domains with strong support (3+ sources / strong stats)]
  #1 At-rim, #2 Contact/foul-draw, #4 CAS 3PT, #5 Off-dribble, #6 Mid-range,
  #7 FT, #8 Handle, #9 Touch, #10 Ball security, #11 Vision, #12 Decisions,
  #13 Passing execution, #14 Off-ball movement (absence-as-data), #20 DREB,
  #24 Shot selection, #25 Motor, #26 Competitive character.

[Sub-domains with moderate support (2 sources or stats + qualitative)]
  #15 On-ball pressure (DFGPOE +0.5 + 2025-26 Lakers improvement framing vs.
  2025 elimination-game floor), #16 Help defense (DRtg + qualitative),
  #18 Post defense (small Synergy sample + scheme-context qualitative),
  #19 OREB (stats only -- absence-as-data on craft), #21 Burst (P3 testing
  + self/scout language), #22 Lateral (qualitative + 2025 elimination tape +
  2025-26 improvement signals), #23 Strength.

[Sub-domains with weak support / known data limitations]
  #17 Rim protection: D_FGA at rim N/A from script (S100-F01 / B5 backlog);
  not a meaningful rim protector at this size/profile -- baseline or below.

[Sub-domains with no direct evidence]
  None. All 26 have at least directional evidence.

[Conflicting signals]
  Wingspan: 6'11" (mainstream) vs. 7'2" (outlier) -- defer to 6'11".
  Weight: 244 lb listed vs. eye-test "looks lighter" [LWOS]. Treat 244 as
    operative; treat eye-test as scout-level commentary on body composition.
  CAS 3PT: stale Mavs-era Ringer "26.9%" framing vs. current 38.1% weighted CAS%.
    Defer to script -- the older framing is no longer load-bearing.
  Lower-leg injury count: "5 hamstring injuries since 2024" [SI fantasy] vs.
    "fourth calf strain in 18 months by Dec 2024" [ESPN] -- likely conflating calf
    and hamstring. Treat the distinct lower-body durability cluster as the
    directional signal.
  Defensive improvement: real but soft -- "improving" headlines coexist with
    Lakers 20th DRtg, NBA Cup transition lapses, 2025 elimination tape. Treat
    improvement as directional, not transformational.
  S105-F01 hot-stretch check: 36.6%-3PT season figures across articles match
    weighted 36.7% -- no inflation flag.

[eval_window discrepancy flagged for backlog]
  eval_window.py reported 100 GP for 2024-25; domain scripts show 50 GP. Likely
  S95-F07 PlayerCareerStats TOT-row aggregation summing DAL + LAL + TOT rows.
  Operative GP = 50. Add to SCRIPT-MAINTENANCE-BACKLOG if not already tracked.
```
