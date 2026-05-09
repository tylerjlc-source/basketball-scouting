# Research Packet — Jimmy Butler — 2026-05-05

```
=== RESEARCH PACKET ===
PLAYER: Jimmy Butler III
POSITION: SF / wing
AGE: 36 (born September 14, 1989)
TEAM: Golden State Warriors (acquired from Miami at Feb 2025 trade deadline)
COMPETITION LEVEL: NBA vet (≥25 NBA games — lineage-comp track per S119; NBA-PROJECTION-OUTPUT-BLOCK at Skill 5)
EVALUATION DATE: 2026-05-05
```

---

## EVALUATION-WINDOW NOTE

`eval_window.py` returned **DEFAULT (60/40 across 2025-26 / 2024-25)**, no R12 trigger. Two caveats to surface for Skill 2:

1. **eval_window.py reported 2024-25 as `110 GP, 31.7 MPG -- healthy`. Domain scripts confirm actual 2024-25 RS = 55 GP, 31.7 MPG.** The 110 GP figure is an aggregation artifact of the MIA→GSW mid-season trade (likely TOT row + individual MIA + individual GSW rows summed). Per S95-F07 (PlayerCareerStats TOT-row handling), this is a known pattern. **Treat 2024-25 as 55 GP for sample-quality reasoning, not 110.**

2. **2025-26 is now a CLOSED 38-GP fragment, not an in-progress sample.** Butler tore his right ACL on January 19, 2026 vs. Miami; surgery Feb 9, 2026; return projected mid-2026-27. The 38-GP sample IS the entire 2025-26 evaluation contribution — no further data will arrive. R12 single-season step-back was not triggered by the script because 2024-25 was misclassified as "healthy 110 GP", but for human reasoning: 2024-25 (55 RS + 11 playoff GP, two-team season, three suspensions) is itself non-canonical. Default 60/40 weighting is defensible because the 38 GP pre-injury 2025-26 sample is statistically meaningful and reflects the GSW environment that is the player's current truth — but **flag for Skill 2 that both seasons carry compromise tags.**

R9 (injury temper) is **forward-looking** for this player, not backward-looking — the 38 GP were played healthy; injury is a Skill 5 projection input, not a Skill 2 scoring suppressor.

R13 sample minimum is **easily met** (9+ playoff seasons across multiple years: CHI 2014/15/17, MIN 2017-18, PHI 2018-19, MIA 2020/22/23/24, GSW 2024-25). Recency status: **active** (2024-25 GSW playoffs within last cycle). 2025-26 playoff absence due to ACL injury — classify R13 status as "active with injury dormancy on current cycle."

---

## --- PHYSICAL PROFILE ---

| Field | Value | Source |
|---|---|---|
| Height (with shoes) | 6'7.75" | 2011 NBA Combine (Tankathon, topendsports.com) |
| Weight | 222 lbs combine / ~230 lbs listed playing weight | 2011 Combine; Heat/GSW listings |
| Wingspan | 6'7.5" — **average/below-average for position, nearly 1:1 with height** | 2011 Combine |
| Standing reach | Not documented in 2011 Combine results pulled | gap |
| Vertical (max) | 39.0" at age 21 (2011 Combine) | topendsports.com |
| Body composition (combine) | 5.40% body fat | 2011 Combine |
| Body type | Strong, durable lower-body build; physical wing — historically a contact player rather than a vertical leaper | scouting consensus |

**2025-26 athleticism observations (qualitative, age-36 + post-trade):**
- "He'd routinely get near the bucket and pump fake several times in search of a foul because he didn't trust his vertical lift." — SI.com Warriors, 2025
- "He surrendered blow-by drives a little more often than was comfortable during his previous season." — Golden State of Mind, 2024-25 review
- "Butler was entering his age-36 season looking like a guy who had racked up a lot of brutal miles." — SI.com Warriors, 2025 pre-season
- ACL tear at 36: "only the second oldest player to tear his ACL in the last 20 years." — HITC, Jan 2026

---

## --- DOMAIN 1 — FINISHING ---

**Statistical (60/40 weighted, 2025-26 + 2024-25):**
- Rim FG%: **69.7%** (current 69.7%, prior 69.7%)
- Non-Dunk Rim FG%: **63.9%** — strong craft finishing
- Dunk rate: 17.3% — modest but non-zero, athletic finishing still in the toolkit
- % of shots at rim: **42.7%** — heavy rim diet
- FTR: **0.635** weighted (current 0.621, prior 0.657) — elite foul-draw, vintage Butler
- Drives: **11.7/g** weighted volume
- Drive FG%: **51.8%**
- Drive PPP: 0.538
- Paint non-RA FG%: 41.7%
- FT%: **85.0%** weighted (career 84.4%) — elite
- % Assisted on rim: 55.5% — meaningful self-creation share

**Qualitative:**
- "Since 2019-20, there hasn't been a soul in the league who has matched Butler's combination of high usage and a free throw attempt rate of .609 — a higher rate over six seasons than even prime Shaq on the Lakers." — Last Word On Basketball, Sept 2024
- "31.7% of Jimmy Butler's points were scored from the FT line in '23-'24, highest of any player in the NBA, and Jimmy drew FTs on 27.7% of his ISO possessions, most in the NBA." — Fanduel/StatMuse
- "He'd routinely get near the bucket and pump fake several times in search of a foul because he didn't trust his vertical lift." — SI.com Warriors, 2025 (relevant to evolution from athletic finisher → contact-craft finisher)
- 2025 playoffs Game 4 vs. Rockets: "23 of his 27 points in the second half, 14 in the fourth quarter, and put the Warriors up for good with three free throws after Dillon Brooks committed a silly touch foul on a 3-point attempt." — Al Jazeera, April 2025

**Data gaps:** None material — finishing sub-domains have full statistical + qualitative coverage.

---

## --- DOMAIN 2 — SHOOTING ---

**Statistical (60/40 weighted):**
- TS%: **63.8%** — career-tier efficiency, but heavily lifted by FT volume + rim share, not jumper
- eFG%: 54.5%
- 3PT%: **33.4%** weighted overall
- CAS 3PT% (catch-and-shoot): 38.2% — but only current season has data; prior season N/A from script
- Corner 3%: 40.2%
- Above-the-break 3%: 29.8%
- Total 3PA: 134.2 weighted attempts — **low volume for a wing**
- Pull-Up 3PT%: **32.5%** (current 32.0%, prior 33.3%) — average
- Mid-Range FG%: **34.1%** weighted (current 32.9%, prior 35.6%) — **declining trajectory in his historical signature area**
- Mid-Range FGA: 76.8 weighted — significantly reduced volume from his Heat-era alpha years
- FT%: 85.0% weighted; clutch FT% 81.8%; career FT% 84.4%

**Qualitative:**
- 3PT volume + accuracy reconciliation: "Butler shot 41.4 percent from deep on 2.4 three-point attempts per game in 2023-24 but only 30.8 percent from beyond the arc in 2024-25." — StatMuse / multiple outlets. (Per S105-F01: defer to script weighted 33.4% for current evaluation window.)
- "Kerr made clear that Butler would dictate the tempo and be more involved in half-court decision-making, allowing him to orchestrate from the elbow." — NBC Sports Bay Area, 2025-26 preview (the elbow/mid-post ISO is his role context now)
- 2020 Bubble Finals signature: "first player to score 40 points in a Finals game without a 3-point attempt since Shaquille O'Neal." — NBA.com — historical baseline of low-volume 3PT identity
- **Absence — no documented 3PT volume expansion in GSW system across 38 GP 2025-26.** Catch-and-shoot infrastructure exists (Curry/Kerr offense) but Butler did not adopt it.

**Data gaps:** Prior-season CAS 3PT% returned N/A from script (endpoint timeout or data pull issue). Mid-range script returned full data; 3PT splits partial.

---

## --- DOMAIN 3 — BALL SKILLS ---

**Statistical (60/40 weighted):**
- ISO PPP: **0.962** (64th pctile), 105 weighted poss, ISO FG% 40.6%, ISO TOV% 12.4%
- PnR ball-handler PPP: **1.112** (95th pctile), 80 poss, PnR FG% 54.9%, PnR TOV% 13.3% — **ELITE**
- Handoff PPP: 0.800 (low volume — 10 poss)
- Touches/g: 63.8 — high
- Time of possession: 4.0 min/g
- Dribbles per touch: 2.56
- Points per touch: 0.298
- USG%: **21.7%** — significantly reduced alpha role at GSW
- Floater FG% (4-14ft): **42.3%** weighted (current 43.9%, prior 40.6% — TRENDING UP)
- Floater FGA: 169 weighted — 32.7% of total FGA, signature shot
- Non-dunk rim FG%: 63.9%
- TOV per 100 touches: **2.3** — excellent ball security
- A:TO ratio: **3.46** weighted — elite for a wing
- Clutch TOV: 1 (in 55.3 clutch min)
- Raw season AST/TOV: 230 / 65

**Qualitative:**
- "Golden State often isolates Butler, who rarely turns the ball over." — Fansided, 2025
- Steve Kerr: "Every time he puts the ball on the floor and pivots and makes a pass, it's not spectacular, but it just makes the game flow." — Yardbarker, 2025
- "When the Warriors first acquired Butler, the coaching staff examined tape from his Heat days, where Miami ran a similar offense predicated on off-ball screens to blend with Butler's isolation game." — Fansided, 2025
- "Lineups with Butler but not Curry have an 8.6 net rating." — Databallr, cited in Fansided
- "The Warriors often dumping the ball to Butler along the baseline or post to let him isolate mismatches, slicing into the paint and either scoring or kicking out." — Golden State of Mind, Feb 2025

**Data gaps:** 2024-25 ISO Synergy data partial (script timed out on retries); PnR + handoff full.

---

## --- DOMAIN 4 — PLAYMAKING ---

**Statistical (60/40 weighted):**
- AST/g: 5.1 weighted
- Potential AST: 10.8 weighted
- Secondary AST: 0.8
- FT AST: 0.5
- Adjusted AST: 6.3
- AST Points Created: 14.0
- AST/PotAST conversion: 47.1%
- A:TO: **3.45**
- Transition PPP: **1.395** weighted (84 weighted poss, 91st-98th percentile across two seasons) — **ELITE**
- Cut PPP: 1.325, 57th pctile (40 poss prior season)
- Off-screen PPP: 0.546 — **very low volume (13 poss weighted), 3rd-16th pctile** — not an off-ball mover
- Distance: 2.28 mi/g weighted; off-speed 4.45 mph (average)
- Note: 2025-26 speed/distance N/A (tracking pulls didn't fire for current season — likely due to mid-season ACL ending the season)

**Qualitative:**
- "Butler is averaging 6.1 assists per game as a Warrior, 1.8 more than his career average." — Yardbarker, 2025
- "His knack for scanning the floor from the high post and making the right read has been a transformative asset for the Warriors." — Yardbarker, 2025
- "Butler has developed a sub-identity as somewhat of a stretch-five whisperer who almost always looks for either Horford or Post as a passing target out on the perimeter." — Golden State of Mind film breakdown
- "Butler's playmaking has alleviated a good chunk of playmaking/ball-handling responsibilities from Curry, allowing Curry to focus on what he does best as an off-ball movement shooter." — Fansided, 2025
- 2020 Bubble Finals: averaged 26.2 points / 9.8 assists / 8.3 rebounds across 6 games. — StatMuse / Sky Sports
- 2023 Heat ECF MVP run: 24.7 / 7.6 / 6.1 / 2.6 stl across 7 games. — Bleacher Report / NBA.com

**Data gaps:** 2025-26 speed/distance N/A from script.

---

## --- DOMAIN 5 — DEFENSE ---

**Statistical (60/40 weighted):**
- Opponent FG% (overall closest defender): **49.1%**
- D_FGA/g (overall): 10.3
- **DFGPOE (overall): +2.4%** weighted (current +3.2%, prior +1.1%) — **opponents shoot ABOVE expected vs. Butler in both seasons** — directionally negative
- Deflections/g: 2.7 (current 2.45, prior 2.98) — solid, mild decline
- STL/g: 1.4 — solid for wing
- Contested shots/g: 2.8 (current 2.37, prior 3.41) — declining
- PF/g: 1.1 — disciplined
- ISO Defense PPP: 1.519 on 0.8 weighted poss — tiny sample, 0.8 pctile — bad rate but unstable
- Post-up Defense PPP: 1.364 on 0.3 weighted poss — tiny sample
- DEF_RATING: 109.4 (current 109.2, prior 109.6)
- BLK/g: 0.2 — typical for wing
- Charges drawn/g: 0.03
- Def loose balls/g: 0.36
- Def box-outs/g: 0.47
- 3PT closeout, rim contests, >15ft contests: **N/A** — endpoint timed out (LeagueDashPtDefend 3-Pointers / Less-Than-6-Ft / Greater-Than-15Ft all returned "None" or partial)

**Qualitative:**
- "From Butler's first game to end of the season last year, the Warriors had the No. 1 defensive rating in the NBA (109.0). This year [2025-26], it ranks 10th (112.2)." — SI.com Warriors, November 2025
- Butler and Draymond Green "had the second- and sixth-lowest defensive ratings of the 101 players averaging at least 30 minutes per game since the trade deadline [Feb–May 2025]." — The Ringer, March 2025 — *positive on/off signal during 2024-25 GSW window*
- "Defensively, Butler brings versatility that allows Kerr to experiment again with lineups that switch across positions." — Golden State of Mind, 2025
- "He surrendered blow-by drives a little more often than was comfortable during his previous season." — Golden State of Mind — on-ball decline signal
- Butler publicly criticized GSW defense Nov 2025: "We're just not guarding anybody... From what I can tell, I haven't been here long, but that's never been the formula here." — Yahoo Sports / Yahoo, Nov 2025

**Conflicting signals:** DFGPOE +2.4% (negative) vs. team DRtg #1 with Butler 2024-25 + #2-#6 individual DRtg post-deadline (positive). Resolution: Butler's individual closest-defender numbers are mediocre, but his rotational/help-side IQ + team scheme integration produce strong on-court team defensive impact. The on-ball matchup data shows age-36 decline; the team DRtg shows residual value as a connector and high-IQ help defender.

**Absence — no documented post-defense or post-help-side rotation language for 2025-26 pre-ACL window.** Sub-domain #18 (post defense) has only the 1.364 PPP / 0.3 poss script row plus residual #16 (help defense) cross-references.

**Data gaps:** Rim D, 3PT D, >15ft D all script-N/A (endpoint timeouts). Sub-domain #17 (rim protection) has no script data — must rely on BLK/g (0.2) and contested 2PT/g (1.4) cross-references plus baseline wing-rim-protection assumption.

---

## --- DOMAIN 6 — REBOUNDING ---

**Statistical (60/40 weighted):**
- OREB/g: **2.3** weighted
- DREB/g: **3.1** weighted
- REB/g: 5.4 weighted
- OREB%: **7.2%** — strong for a wing
- DREB%: **10.1%**
- REB%: 8.7%
- OREB chance% (adjusted): 46.3% — collects when in position
- DREB chance% (adjusted): 63.4% — solid
- Avg REB distance: 6.9 ft — perimeter rebound profile
- Box-outs/g: 0.74
- Off box-outs/g: 0.32
- Def box-outs/g: 0.42
- Off Box-out% of total: 42.9% — meaningful offensive glass effort

**Qualitative:**
- 2025-26 (38 GP pre-injury): 5.6 REB/g
- 2025 playoffs Game 1 vs. Timberwolves: 11 rebounds while serving as the primary initiator in Curry's absence. — Pro Football Network
- "Butler brings rebounding prowess from the guard spot, with Draymond, Moses, and Jimmy throwing around hard boxouts to enable other players to clean up the glass." — The Swish Theory, 2025
- Team context: GSW DREB ranked 23rd 2025-26. — SI.com Warriors

**Data gaps:** None material.

---

## --- DOMAIN 7 — ATHLETICISM ---

**(No script — sourced via biometrics + cross-domain proxies)**

**Biometric anchors (2011 Combine, age 21):**
- Max vertical: 39.0" — above-average wing leap baseline
- Body composition: 5.40% body fat — elite conditioning at draft
- Strength: durable wing build, contact-tolerant

**2025-26 cross-domain proxies:**
- Dunk rate 17.3% on 220 weighted rim FGA — non-zero but reduced
- Drive volume 11.7/g — high volume drive game intact
- Drive FG% 51.8% — efficient at the rim
- Speed 4.22 mph (2024-25 only — 2025-26 N/A)

**Qualitative — age-36 decline signals:**
- "He'd routinely get near the bucket and pump fake several times in search of a foul because he didn't trust his vertical lift." — SI.com Warriors, 2025 — **explicit vertical-lift trust decline**
- "He surrendered blow-by drives a little more often than was comfortable." — GSoM — **lateral decline signal**
- "Butler was entering his age-36 season looking like a guy who had racked up a lot of brutal miles." — SI.com Warriors, 2025
- ACL tear Jan 19, 2026 (age 36) — second-oldest in 20 years per HITC. **Forward-looking durability collapse, not retroactive scoring suppressor.**
- Strength as physical weapon remains: "embraces contact, dictates the final minutes with calm, physical control." — Sportscasting, 2025-26 preview

**Wingspan caveat:** 6'7.5" wingspan against 6'7.75" height = **near 1:1 ratio**, structurally below average for a wing. Has always limited true rim deterrence and shot-contesting.

**Data gaps:** No 2025-26 vertical/lane agility/speed measurement. 2025-26 LeagueDashPtStats SpeedDistance returned N/A (likely tracking-data fragment incomplete for the partial season).

---

## --- DOMAIN 8 — IQ / MOTOR / COMPETITIVE CHARACTER ---

**Statistical (60/40 weighted):**
- Defender distance distribution: 8.9% Very Tight, **49.9% Tight**, 25.6% Open, 13.3% Wide Open — **Contested%: 58.8%** — high-difficulty shot diet (alpha/star territory)
- Shot clock distribution: 5.6% 24-22, 13.4% Very Early, 11.7% Early, 44.9% Average, 12.9% Late, 14.0% Very Late — moderate late-clock burden
- Clutch (2-season weighted): 37 GP, 2.0 PTS, **41.9% FG, 73.3% 3P (small sample), 79.3% FT, +/- 0.2, 0.5 AST, 0.1 TOV** — clutch FG% modest, but elite TOV control + decent +/-
- Speed (2024-25 only — 2025-26 N/A): avg 4.22 mph, off 4.40, def 4.03 — average movement

**Shot selection note:** 32.7% of FGA are floaters (4-14ft) — a lot of touch-shot diet. Mid-range FGA 76.8 weighted (down from peak Heat era). Heavy rim diet (42.7%). 3PA 134.2 weighted (low). The shot diet is paint-heavy and FT-leveraged — a structurally efficient profile that does not require shot-volume or jumper accuracy to function.

**Qualitative — Effort / Motor:**
- "Miami trainer says he had workouts with Jimmy Butler at 3:30 AM: 'He likes to be uncomfortable because the game is supposed to be easy.'" — Yahoo Sports, Jan 2025
- Butler on Miami culture early in his tenure: "In order to thrive here, you gotta have a crazy-ass work ethic." — Yahoo Sports archive
- "Butler is proof of how willpower and charisma can vault a player into the highest echelons of basketball, among players more talented but nowhere near as insistent." — The Ringer / Hot Hot Hoops, Jan 2025

**Qualitative — Competitive character (Playoff Jimmy):**
- Draymond Green: "Playoff Jimmy is a real thing." — April 17 2025, GSoM
- Unnamed NBA scout: "No one will want to play them in the playoffs. Jimmy with fresh legs and motivation... honeymoon-phase Jimmy is a motherf--ker." — Bleacher Report, March 2025
- "We're going to bring hell: The Warriors are embracing the full Jimmy Butler experience." — Fox Sports, 2025

**Qualitative — Negative signals (Negative Balance Rule):**
- Three Heat suspensions in January 2025; walked out of practice; Riley statement: failed "to give best efforts during recent games" and was "combative in meetings with management and ownership." — ESPN/CBS Sports, Jan 2025
- ESPN career retrospective: "14 seasons, 4 teams and a list of clashes." — ESPN, Jan 2025
- The Ringer: "What Is Jimmy Butler After?" — framing the question of whether competitive drive turned corrosive — Jan 7 2025
- Butler GSW friction with Kerr over defense, Nov 2025: "An irate Steve Kerr dismisses Jimmy Butler's take on the Warriors' defense, 'Don't care.'" — HITC, Nov 2025
- Post-Game 5 elimination 2025: "No excuse for how I played, how we played." — self-assessment after Wolves series eliminated GSW (Curry-out games)
- Jay Williams (ESPN) on 2025 Wolves elimination: "You weren't asked to win the war, you were asked to hold the damn line." — NBC Sports Bay Area

**Data gaps:** 2025-26 speed/distance N/A; some shot-clock late ranges N/A for current season.

---

## --- CHARACTER / PROJECTION SIGNALS ---

**Work ethic:**
- 3:30 AM workouts; "uncomfortable because the game is supposed to be easy." — multiple sources, longstanding pattern.
- Pre-ACL 2025-26 38-GP sample: averaging 20.0 points / 5.6 REB / 4.9 AST / 1.5 STL on 51.9% shooting — best efficiency of his career, consistent with high-IQ GSW environment.

**Competitive character:**
- Dual-edged: galvanizing in playoffs (2020 Bubble, 2023 ECF MVP) but Pat Riley publicly accused him of failing to give best effort and being combative with management; three suspensions in one month.
- GSW assessment (post-trade): Locker room embraced his directness; system gives him the elbow/high-post role and reduced USG (21.7% vs Heat-era 28%+); Kerr/Curry/Draymond all publicly endorse the fit. But mid-season Kerr-Butler defensive disagreement (Nov 2025) shows friction does follow him into new environments.
- Butler's framing of his Miami exit: "I want to see me get my joy back from playing basketball... Probably not [in Miami]." — The Ringer, Jan 2025 — explicit emotional/environmental dependency on competitive infrastructure.

**Negative signals (full):**
- Heat saga 2024-25: combative with management, missed flights, walked out of practice, three suspensions. Whether GSW's stronger leadership infrastructure (Curry, Kerr, Green) mutes this is the open projection question.
- Athletic decline at 36: vertical lift trust decline, blow-by lateral decline, and now ACL tear.
- 3PT volume never expanded; remains structurally low-volume shooter.
- 2025 Wolves Game 4-5: 31 total points on 20 FGA across two elimination losses with Curry sidelined — broke the "Playoff Jimmy carries the load" narrative when asked to be the actual #1.

**Trajectory:**
- **Pre-injury 2025-26:** flat-to-slightly-up — efficient role-tier All-Star caliber within GSW system, reduced USG, reduced volume, maintained playmaking, increased 3PT volume modest.
- **Post-injury (forward):** ACL recovery 9-12 months pushing return to mid-2026-27 at age 37. Historical comp class is small and unfavorable — second-oldest ACL in 20 years.
- Net: **declining** when projection horizon is included.

---

## --- PLAYOFF / BIG-GAME TRACK RECORD (R13 sample met) ---

**Sample minimum:** 9+ unique playoff seasons across multiple years (CHI 2014/15/17, MIN 2017-18, PHI 2018-19, MIA 2020/22/23/24, GSW 2024-25). Recency: 2024-25 within last 2 cycles → **active**, with 2025-26 dormancy due to ACL.

**Playoff_Track_Record.py:** Failed two consecutive runs with read-timeout on PlayerCareerStats endpoint at 30s default. Likely API rate-limit on Butler's high-volume career data. Manually compiling from web evidence below.

**Statistical / qualitative rise vs. regular-season baseline:**

- **2020 Bubble Finals (MIA):** 26.2 PPG / 9.8 AST / 8.3 REB across 6 Finals games. Game 5 — 35/12/11/5 stl, 12-for-12 FT. Game 3 — 40-point triple-double, "first player to score 40 points in a Finals game without a 3-point attempt since Shaquille O'Neal." Source: NBA.com, Sky Sports.
- **2023 First Round vs. Bucks (MIA, 8-seed):** 56-point game (19-28 FG, 15-18 FT, 9 REB) — fourth-best playoff scoring performance in NBA history. Followed with 42-point closeout. — ESPN, April 2023
- **2023 ECF MVP run (MIA):** 24.7 / 7.6 / 6.1 / 2.6 stl across 7 games vs. BOS. Joined LeBron and Wade as only Heat to put up 500 PTS / 100 REB / 100 AST in single postseason. Game 7: 28/7/6/3 stl. Full 2023 playoffs: **31.9 PPG**. — Bleacher Report, NBA.com
- **2025 Round 1 vs. Rockets (GSW):** Game 1 — 25 / 7 / 6 / 5 stl in 42 min. Game 4 (return from pelvic injury) — 27 points with "23 of 27 in the second half, 14 in the fourth quarter" to take 3-1 lead. Series upset. The Athletic: "Warriors validate Jimmy Butler trade." 2025 playoffs overall: **19.2 / 6.6 / 5.2** in 11 games.
- **2025 Round 2 vs. Timberwolves (GSW, Curry sidelined):** Game 1 — 20/11/8 (carried, GSW won). Game 4-5 — **31 total PTS on 20 FGA across two elimination losses**. NBA.com: "Butler didn't live up to his 'Playoff Jimmy' moniker in Golden State's final two losses." Series lost 4-1. Butler self-assessment: "No excuse for how I played, how we played."

**Classification:**
- Through 2023: **strong rise** — multi-source convergence on "Playoff Jimmy" with an 8-seed Finals run and an ECF MVP.
- 2025 playoffs (one-cycle update): **mixed** — strong vs. Rockets, neutral-to-shrink vs. Wolves when asked to carry as the actual #1 with Curry out.
- **Net R13 verdict for current evaluation:** moderate rise, with active-cycle softening — historical anchor evidence remains but the most recent playoff data point introduces a counter-signal worth weighting in Skill 4 (composite) and Skill 5 (NBA-vet projection POT modifier).

**Recency status:** active (2024-25 within window) / **active-injury dormant on current 2025-26 cycle**.

---

## --- INJURY HISTORY ---

- **Pre-2024-25 durability pattern:** "Has not played over 65 games since 2016-17." Long-standing availability concern.
- **2023-24 Heat:** 60 GP. MCL sprain in April 2024 play-in vs. PHI; missed second play-in.
- **2024-25 (split season):**
  - MIA pre-trade: 25 GP, three suspensions in January 2025 (administrative absences, not injury), trade Feb 5, 2025.
  - GSW post-trade: 30 GP regular season + 11 GP playoffs. Pelvic injury cost 1 game in Round 1.
  - Total: 55 RS GP + 11 playoff GP.
- **2025-26 GSW:** 38 RS GP. **Right ACL tear, January 19, 2026** vs. MIA — "Leaped to grab an entry pass in the middle of the paint and collided with Davion Mitchell, and his right knee appeared to twist on the landing." Surgery Feb 9, 2026. Return projected: "nine to 12 months" — won't return until "middle of the 2026-27 campaign."
- **Age context:** "36-year-old Jimmy Butler is only the second oldest player to tear his ACL in the last 20 years."

**R9 (injury temper):** **Forward-looking only.** The 38 GP played in 2025-26 were healthy; the injury terminated the season but does not retroactively suppress sub-domain scores. R9 will apply at Skill 5 (NBA-vet projection block) as a major durability/ceiling input.

**R12 flag:** Not formally triggered by `eval_window.py` (script saw 2024-25 as 110 GP "healthy"). Manual reasoning: 55 RS GP + 11 PO GP is below "healthy" threshold given Butler's career availability profile, but is statistically usable. **Recommend Skill 2 use default 60/40 weighting and treat both seasons as compromised-but-usable, per the EVAL-WINDOW NOTE at top.**

---

## --- DATA GAP INVENTORY ---

**Strong support (3+ sources, statistical + multi-source qualitative):**
- #1 At-basket finishing
- #2 Contact finishing / foul draw
- #4 CAS 3PT (current season only — prior N/A)
- #6 Mid-range
- #7 Free throw
- #8 Handling / creation
- #9 Touch / feel
- #10 Ball security
- #11 Court vision
- #13 Passing execution
- #14 Off-ball movement (note: structurally low-volume — script + qualitative absence both point to "not his game")
- #15 On-ball pressure (overall closest-defender data; but DFGPOE conflicts with team context)
- #19 Offensive rebounding
- #20 Defensive rebounding
- #24 Shot selection
- #25 Effort / motor
- #26 Competitive character

**Moderate support (2 sources):**
- #3 Post offense (no script; high-post elbow ISO described qualitatively but not "post-up" PPP — likely low volume)
- #5 Off-dribble shooting (script + scouting reports)
- #12 Decision-making (A:TO + clutch TOV + qualitative Kerr quotes)
- #16 Help defense (DEF_RATING + box-outs + qualitative versatility)
- #18 Post defense (1.364 PPP on 0.3 weighted poss — tiny sample; minimal qualitative)
- #21 Burst / explosion (cross-domain proxies + qualitative decline language)
- #22 Lateral quickness (cross-domain proxies + qualitative blow-by language)
- #23 Strength (qualitative + body type + contact game)

**Weak support (1 source or partial):**
- #17 Rim protection — no rim D script data; only BLK 0.2/g + contested 2PT 1.4/g + general wing baseline. Has historically not been a rim deterrent.

**No direct evidence:**
- None at "zero" — every sub-domain has at least cross-domain proxy or qualitative coverage.

**Conflicting signals:**
- DFGPOE +2.4% (negative individual closest-defender) vs. team DRtg #1 with Butler post-trade 2024-25 + #2-#6 individual DRtg post-deadline (positive). → resolve via "individual matchup defense declining; help/scheme/IQ defense still strong."
- 3PT% 2023-24 41.4% vs. 2024-25 30.8% vs. 2025-26 fragment — narrative-stat divergence per S105-F01. Defer to script weighted aggregate (33.4%) for the evaluation window.
- "Playoff Jimmy" historical anchor vs. 2025 Wolves Game 4-5 collapse with Curry sidelined.

**Script gaps:**
- Playoff_Track_Record.py: 2 timeouts on PlayerCareerStats endpoint. Manual web compilation substituted; structured delta summary would be desirable but not blocking.
- Domain 5: 3PT-defense, rim-defense (Less Than 6Ft), and >15ft-defense endpoints all returned partial/None due to LeagueDashPtDefend timeouts. Sub-domain #17 (rim protection) confidence is low as a result.
- Domain 4 + 8: 2025-26 SpeedDistance returned N/A (likely a partial-season tracking issue post-ACL).
- Domain 8: 2025-26 shot-clock middle ranges (18-15 Early, 15-7 Average, 7-4 Late) all N/A — likely same partial-season issue; 2024-25 data is full.

---

## --- HANDOFF NOTES TO SKILL 2 ---

1. **Eval window** is default 60/40 (2025-26 / 2024-25). Treat both seasons as compromised-but-usable per EVAL-WINDOW NOTE. Do not invoke R12; rely on R9 forward-looking at Skill 5.
2. **Position group:** Wing (per CLAUDE.md group definitions and Butler's positional history).
3. **Independent scoring directive (per Tyler's session opener + memory `feedback_legacy_anchor_independent_scoring.md`):** Score blind. No reference to any external composite, public ranking, or prior eval anchor. Surface divergence transparently.
4. **Critical R14 reminder:** Use full .0–.9 decimal range. Don't cluster at .0/.5.
5. **Critical Negative Balance reminder:** Butler's positive evidence is heavy and well-documented; the negative evidence (vertical decline, lateral decline, low 3PT volume, mid-range erosion, Heat exit dysfunction, 2025 Wolves Game 4-5 shrink) requires equal weighting.
6. **Pre-ACL stat lines do not retroactively temper.** R9 is a Skill 5 input for projection only.

---

*End of research packet.*
