# Research Packet — Bam Adebayo — 2026-05-01

```
=== RESEARCH PACKET ===
PLAYER: Edrice Femi "Bam" Adebayo
POSITION: Center (Big)
AGE: 28 (born July 18, 1997)
TEAM: Miami Heat
COMPETITION LEVEL: NBA
EVALUATION DATE: 2026-05-01
EVALUATION WINDOW: 2025-26 (0.60) + 2024-25 (0.40) — both healthy, no R12 trigger
```

---

## PHYSICAL PROFILE

| Metric | Value | Source |
|---|---|---|
| Height (shoes) | 6'9.75" | 2017 NBA Combine (NBADraft.net) |
| Height (barefoot) | 6'8.75" | 2017 NBA Combine |
| Wingspan | 7'2.75" | 2017 NBA Combine |
| Standing reach | 9'0" | 2017 NBA Combine |
| Weight | 242.6 lbs (combine); listed 255 currently | 2017 NBA Combine; current Heat listing |
| Hand length | 9.5" (tied longest at 2017 combine) | NBADraft.net |
| Body fat | 5.2% (combine) | 2017 NBA Combine |
| Max vertical | 38.5" | 2017 NBA Combine |
| Lane agility / shuttle | Not surfaced | — |

**Body type / build language:**
- "Powerful and quick leaper who has a really good combination of length, strength and quickness. He's a high level dunker who plays with his head above the rim." — RevUpSports.com
- "Remarkably quick feet and arms that could best be described as uber-long." — FiveThirtyEight
- "Undersized from his position [center] and relied on length and athleticism to affect the game around the rim." — NBADraft.net (2017 combine recap)

**Physical archetype:** undersized but athletically elite center; lateral quickness and recovery explosion are the differentiating traits.

---

## DOMAIN 1 — FINISHING

### Statistical (2-season weighted, 60/40)

| Metric | Value | Current | Prior |
|---|---|---|---|
| Rim FG% | 69.0% | 68.3% | 70.0% |
| Rim FGA (window total) | 279 | — | — |
| % Shots at Rim | 24.7% | — | — |
| Dunk Rate | 35.1% | — | — |
| Non-Dunk Rim FG% | 56.9% | — | — |
| FT% | 77.4% | — | — |
| % Assisted at rim | 67.8% | — | — |
| FTR | 0.339 | 0.369 | 0.295 |
| Drives/G | 6.1 | — | — |
| Drive FG% | 46.0% | — | — |
| Drive PPP | 0.726 | — | — |
| Paint non-RA FG% | 42.4% | — | — |

### Qualitative

- **2023-24 paint volume:** "NBA leaders in Points in the Paint, 2023-24: 1. Brunson 138, 2. Sengun 122, **3. Adebayo 120**, 4. Jokic 118." — Tommy Beer (X), Feb 2024.
- **2024-25 first-half struggles → second-half recovery:** "Until the new year, Adebayo's touch inside of 15 feet was off… Over his first 43 games he averaged 15.6 PPG with 45.4 percent FG, the lowest mark of his career by nearly 10 percentage points… Career-worst 48.5% clip from the field… first time in his career under 50% through an entire season." — Hot Hot Hoops, 2024-25 Player Review.
- **Second-half rebound:** "21.0 PPG on 51.3/43.2/81.1 since the start of February — Heat's best player in the second half." — Hot Hot Hoops.
- **2025-26 closing stretch:** "Final 42 games: 22.8 PPG, 10.3 RPG, 3.6 APG, 1.4 SPG on 43.9 FG%, 31.8 3P%." — Hot Hot Hoops, 2025-26 Review.
- **83-point game (Mar 10, 2026 vs WAS):** "31 of Heat's 40 first-quarter points… set NBA records for FTM (36) and FTA (43) in a single game; seven 3PM." — NBA.com / Wikipedia.
- **Foul-drawing in 2023 Finals (per The Ringer, June 7, 2023):** Led Miami in touches (87.5), points (23.5), shot attempts (19.5), rebounds (11) — generated 1.295 PPP on 56 combined handoffs/picks (vs Jokic 0.971 on same actions).
- **Contact context:** Plays with consistent rim aggression but draws fouls more by leverage than vertical attack.

### Data gaps
- Synergy post-up PPP not pulled by current scripts (Sub-domain #3 sourced from web search per registry; not surfaced in qualitative either — log as gap).
- No specific contact/and-1 rate split.

---

## DOMAIN 2 — SHOOTING

### Statistical (2-season weighted, 60/40)

| Metric | Weighted | Current 2025-26 | Prior 2024-25 |
|---|---|---|---|
| CAS 3PT% | 31.4% | 31.4% | N/A in script (script bug — "prior N/A") |
| Pull-Up 3PT% | 32.3% | 32.3% | N/A in script (bug) |
| PU Zone 3PT% (ShotChart) | 28.9% | — | — |
| Total 3PA (window) | 88.4 | — | — |
| Mid-Range FG% (script) | **0.0% — script bug** | 0.0% | N/A |
| Mid-Range FGA (script) | **0 — script bug** | — | — |
| FT% (Domain 2) | 76.5% | 0.0% (bug) | 76.5% |
| FT% (Domain 1 cross-ref) | 77.4% | — | — |
| Clutch FT% | 68.6% | — | — |
| TS% (script value) | **22.4% — clearly bugged output** | — | — |
| eFG% (script value) | **20.8% — clearly bugged output** | — | — |
| Overall 3PT% (script) | 35.7% | — | — |

**SCRIPT BUG FLAGS** (log under Data Gap Inventory): Domain 2 produced TS% 22.4% / eFG% 20.8% / Mid-Range FGA = 0 — all impossible for Adebayo whose mid-range is the signature shot. Likely the same script-maintenance backlog issue (LeagueDashPlayerShotLocations zone allocation or a per-mode flag). Treat numeric outputs for mid-range and TS%/eFG% as unreliable; rely on qualitative + cross-reference from Domains 1 and 3.

### Qualitative

- **Mid-range volume / efficiency (signature shot):** "Over his last four seasons, he's graded in the 96th percentile or greater (amongst other big men) in mid-range frequency and 95th percentile or greater in short mid-range (~4-14 ft.) frequency, which are largely contested looks." — Basketball News.
- **Mid-range volume context (script): 51.3% of 2024-25 shot clock allocation in 15-7 sec band** (per Domain 8 shot clock distribution — implies a lot of late-clock mid-range looks).
- **3PT career arc — historical absence to credible volume:**
  - "Adebayo has been noted for his 'non-existent three-point shot' throughout much of his career."
  - 2023-24 3PT%: **35.7%** on low volume — Basketball-Reference.
  - "He says he will shoot at least 100 3-pointers in 2024-25." — Hot Hot Hoops, Oct 4, 2024.
  - **2024-25 progression:** "For the season, he's taking nearly 20 percent of his shots (19.4) from deep, a huge uptick from 4.1 percent 3-point rate last season."
  - **2024-25 second half explosion:** "Post-Jan 1, Adebayo shot 39.7% from 3 on 2.9 attempts/game; 43.5% over his final 35 games. Among all centers, his 3-point shooting ranked in the 81st percentile post-Jan 1." — multiple outlets.
  - **2025-26 sustained:** "Final 42 games: 31.8 3P%, ~3.0 attempts." Career 3PM total surpassed 127 by season end (third on team). "Since Jan. 25 [2026], Adebayo is averaging 22.4 PPG, 11.4 RPG, 4.6 APG on 53.4% FG and 41.8% from 3."
- **Free throw shooting:** 75.5% (2023-24); 81.1% over 2024-25 second half; 36/43 (83.7%) in 83-point game; career-trend stable mid-70s-low-80s.
- **C&S vs pull-up split:** Script shows pull-up 3PT 32.3%, CAS 31.4% — close to even. Qualitative confirms a mix; many of his 3PA come on rotated-to-corner kicks but he is also taking pull-up trail 3s in transition.
- **Off-dribble shooting context (#5):** Script ISO PPP 0.738, ISO percentile 21.6% — modest as an isolation scorer, but his off-dribble shot is mostly a complement to his roll/face-up game, not a primary engine.

### Data gaps
- Mid-range FG% and FGA from script unusable (script bug). Per qualitative, mid-range frequency is 96th+ percentile among bigs but specific FG% for window not surfaced — flag as moderate-confidence.
- Domain 2 FT% career trend N/A from script. Career FT% can be cross-checked from Domain 1 (77.4%) and Basketball-Reference manually.

---

## DOMAIN 3 — BALL SKILLS

### Statistical (2-season weighted, 60/40)

| Metric | Value |
|---|---|
| ISO PPP / Poss / FG% / TOV% / Pctile | 0.805 / 129 poss / 36.8% / 10.0% / 34.7th |
| PnR BH PPP / Poss / FG% / Pctile | 0.431 / 15 poss / 19.4% / 4.1% TOV / 37.3th |
| Handoff PPP / Poss | 0.000 / 0 (Adebayo hands off; rarely receives) |
| Touches/G | 60.1 |
| Time of Poss | 2.7 min |
| Dribbles/Touch | 1.67 |
| Points/Touch | 0.322 |
| Drives/G / FG% / TOV% / AST | 6.1 / 46.0% / 5.1% / 0.3 |
| USG% | 24.2% |
| Floater FG% (4-14ft) | **0.0% — script bug, FGA = 0** |
| Non-Dunk Rim FG% | 56.9% (cross-ref Domain 1) |
| FT% (touch proxy) | 77.4% |
| TOV per 100 Touches | 3.0 (current 2.8 / prior 3.2) |
| Estimated TOV% | 7.9% |
| A:TO ratio | 1.99 (Domain 3) / 2.00 (Domain 4) |

### Qualitative

- **Handle in space:** "Against switching defenses, his handle allows him to dribble from the perimeter into the post." — Lockdown Coaching Blog.
- **Face-up / DHO fake:** "Big threat to punish opposing bigs who jump out to the DHO too early, executing a quick DHO fake to attack the basket with his drive." — Lockdown Coaching Blog.
- **Post moves:** "Footwork and post moves are key to his success, with Bam demonstrating different footwork and post moves around the basket to score in the paint." — Lockdown Coaching Blog. Featured in NBPA "Post Moves with Bam Adebayo" instructional series.
- **Touch / floater language:** "Until the new year [2024-25], Adebayo's touch inside of 15 feet was off." — Hot Hot Hoops. 83-point game: "attacked a closeout and hit a bizarre running half-hook floater" — The Athletic.
- **Ball security:** A:TO of ~2.0 with 60+ touches/game and 24.2% USG is strong for a big; TOV/Potential AST 0.33 (Domain 4) is solid.
- **TOV context:** "His turnover rate is high at 3.0 per game, though his much-increased usage rate and far greater role in the passing game of the half-court offense is a big part of why."

### Data gaps
- Floater FG% from script bugged (FGA = 0). Likely same shot-zone allocation issue as mid-range. Treat as gap; qualitative confirms touch is real but variable.

---

## DOMAIN 4 — PLAYMAKING

### Statistical (2-season weighted, 60/40)

| Metric | Weighted | Current | Prior |
|---|---|---|---|
| Passes/game | 39.5 | 36.6 | 43.9 |
| Potential AST | 5.6 | 4.8 | 6.9 |
| Actual AST | 3.6 | 3.2 | 4.3 |
| Conversion rate | 64.5% | 66.7% | 62.3% |
| Secondary AST | 0.4 | 0.5 | 0.3 |
| FT AST | 0.2 | 0.2 | 0.2 |
| Adj AST | 4.3 | 3.9 | 4.8 |
| Adj AST % | 10.8% | 10.7% | 10.9% |
| AST Points Created | 9.6 | 8.4 | 11.4 |
| A:TO | 2.00 | — | — |
| TOV/PotAST | 0.33 | — | — |
| Cut PPP / Poss / Pctile | 1.256 / 121 / 30th-45th band | 1.221 / 77 / 30th | 1.278 / 187 / 45th |
| OffScreen PPP / Poss | 0.978 / 37 | 1.051 / 39 / 65th | 0.853 / 34 / 34th |
| Transition PPP / Poss | 1.036 / 243 | 1.064 / 297 / 35th | 0.957 / 161 / 17th |
| Avg offensive speed (mph) | 4.71 (current only — prior timed out) | — | — |
| Off distance (mi/G) | 1.20 (current only) | — | — |

### Qualitative

- **Premier passing big:** "Adebayo is one of the premier NBA passing bigs, comparable to Nikola Jokic and Marc Gasol. The Heat employ him as a hub for their DHO heavy offense." — Lockdown Coaching Blog.
- **DHO hub specifics:** "Duncan Robinson and Adebayo remain the NBA's most dangerous handoff combo… 1.273 PPP across 13 actions in 2023 Finals." — Basketball News / The Ringer.
- **Heat offense yield through Bam:** "The Heat are scoring an absurd 1.56 points per possession when Adebayo receives the ball and shoots or passes it to someone who shoots." — Basketball News.
- **Elbow / high-post passing:** "Adebayo showed his playmaking prowess by dissecting Charlotte's zone from the elbows and the high post — a spot where the Heat frequently give Adebayo the ball." — Five Reasons Sports Network.
- **PnR roll/short-roll:** "He's at his best when operating in pick-and-rolls. Adebayo toggles between bone-crushing picks and early slips, depending on the defensive coverage… scoring at an absurd clip on rolls while making teams pay with the pass in short-roll situations." — Basketball News.
- **2023 Finals:** "Led Miami in touches (87.5/G); struck balance between scoring and playmaking with improved decision-making." — The Ringer.
- **Decision-making (#12):** Conversion rate 64.5% is strong; A:TO ~2.0 reflects controlled decisions; Heat OffRtg with Bam on the ball cited above.
- **Off-ball movement (#14):** Cut percentile dropped from 45th (prior) to 30th (current); OffScreen percentile rose from 34th to 65th. Off-ball usage is moderate — he is the offensive hub, not a cutter primarily. Avg off-speed 4.71 mph current is moderate (Domain 4 timed out on prior season speed).

### Data gaps
- Speed/distance for 2024-25 timed out (script). Cross-reference Domain 4 prior-season pull-up frequencies if needed.
- TOV breakdown (bad pass vs lost ball) for 2024-25 timed out — only TOV total available for prior season.

---

## DOMAIN 5 — DEFENSE

### Statistical (2-season weighted, 60/40)

| Metric | Value | Current 2025-26 | Prior 2024-25 |
|---|---|---|---|
| Opp FG% (Overall, closest defender) | 46.2% | 45.6% | 47.4% |
| D_FGA/G | 14.2 | 14.97 | 13.13 |
| **DFGPOE (Overall)** | **−2.5%** | −3.1% | −1.6% |
| Opp 3PT FG% / D_FGA / DFGPOE | N/A (endpoint timed out — backlog item) | — | — |
| Opp FG% >15ft | N/A | — | — |
| ISO Defense PPP / Poss | 0.743 / 2.0 (low sample) | 0.826 / 1.3 / 71st pctile | 0.618 / 0.7 / 92.7th pctile |
| PostUp Defense PPP / Poss | 1.071 / 0.8 (very low sample) | 1.097 / 0.4 / 35.7th | 1.032 / 0.4 / 44.8th |
| **DEF_RATING (on-court)** | **110.9** | 111.0 | 110.8 |
| Deflections/G | 2.7 | 2.38 | 3.06 |
| STL/G | 1.2 | 1.2 | 1.3 |
| Contested shots/G | 6.4 | 6.84 | 5.77 |
| Contested 3PT/G | 2.3 | — | — |
| Contested 2PT/G | 4.1 | — | — |
| BLK/G | 0.7 | — | — |
| PF/G | 1.9 | — | — |
| Charges drawn/G | 0.02 | — | — |
| Def loose balls/G | 0.27 | — | — |
| Def box-outs/G | 2.04 (cross-ref Domain 6) | — | — |
| **At-rim FG% allowed** | **N/A from script (endpoint bug) — qualitative: 70.6% (worst among qualifying centers)** | — | — |
| **Heat on/off DRtg differential** | "+5.4 (Heat best)" — qualitative | "112.5 with vs 117.9 without (89th pctile)" | — |

### Qualitative

#### #15 On-ball pressure / switch defense
- **Switchability — single most cited trait:** "Despite being an undersized center, Adebayo's one of the few players who can legitimately defend 1 thru 5 on a nightly basis — as well as play drop effectively, hard hedge or even blitz (and recover) on the perimeter." — LastWordOnSports, Mar 7, 2026.
- "On defense Bam was still the best switching big in the league by a wide margin during the 2024-25 season. He was noticeably better than every other big on switches this season in the data." — Hot Hot Hoops, 2024-25 Review.
- "Bam Adebayo currently leads the NBA in PnR switches (34) and the Heat are allowing roughly 64 points per 100 possessions on those trips." — Hot Hot Hoops.
- "Only one center in the league has switched into a one-on-one matchup with a guard more often than Adebayo." — FiveThirtyEight (baseline).
- "His elite athleticism and lateral quickness against opposing wings are fairly uncommon traits for players his size."
- **ISO Defense data:** 0.743 PPP weighted, with prior season 92.7th percentile and current 71st — elite isolation defender numerically (sample is low at 2.0 weighted poss, but signal is strong).

#### #16 Help defense
- "His ability to protect the rim, switch on guards, and anchor rotations makes him one of the league's most respected defenders." — LastWordOnSports.
- 2023 Finals: "When benched for 16 minutes, Miami was outscored by 19 points." — The Ringer.
- 2025-26: "Adebayo finished in the 89th percentile in on-off differential on defense; the Heat surrendered 112.5 points per 100 possessions when he was on the floor compared to 117.9 when he was off, with his 5.4 on-off differential defensively being a team-high." — Hot Hot Hoops, 2025-26 Review.
- Charges/G 0.02 and Def loose balls/G 0.27 — modest hustle volume; box-outs 2.04 (Domain 6 cross-ref).

#### #17 Rim protection (THE WEAKNESS)
- **Explicit headline criticism:** "Bam Adebayo Is The Worst NBA Center In Defending The Rim This Season — defending the rim at an abysmal 70.6%, the worst among all qualifying centers in the league." — Fadeaway World / Yardbarker (2024-25 reference window).
- "He has faced 160 contests at the rim, allowing 113 made field goals [70.6%]. For comparison, elite rim protectors like Wembanyama and Allen are holding opponents to 48.9% and 50%. Even Vucevic (69.6%), KAT (67.9%), and Sabonis (68.9%) — not traditionally known for rim defense — are performing better."
- "The Miami Heat often deploys him in schemes that require him to guard on the perimeter, leaving him vulnerable to late rotations when contesting shots at the rim."
- **Block rate:** 0.7 BPG (script). Career has typically hovered 0.8-1.0 BPG — modest for a primary-five.
- **2025-26 partial mitigation:** "Adebayo got back to his pre-2024 days of switching most actions with [Kel'el] Ware protecting the rim at an adequate level, particularly when he shared the floor with teammate Kel'el Ware." — Hot Hot Hoops, 2025-26 Review.

#### #18 Post defense
- Script PPP 1.071 (35-45th percentile) on tiny sample — directionally weak but small-N caveat.
- Post defense was historically a relative strength (Jokic assignment in 2023 Finals: "fast-moving brick wall… preventing entry passes to Jokic" — The Ringer). Sample drop reflects modern league shift away from post-up volume.

### All-Defensive selections (career arc)
- 2019-20 → 2022-23: All-Defensive **Second Team** (4 straight)
- 2023-24: All-Defensive **First Team** (peak), 3rd in DPOY voting (behind Gobert, Wembanyama)
- 2024-25: **Dropped off entirely** — first miss since 2018-19. Placed 12th overall (1 first-team vote, 16 second-team).
- "Among centers who defended at least 500 shot attempts, Adebayo slipped down to 26th in defensive field-goal percentage allowed at 47.4." — Yahoo Sports, May 2025.
- "The Heat fell from fifth in defensive rating in 2023-24 to ninth this past season." — Clutch Points.

### Data gaps
- At-rim FG% allowed not produced by script (known endpoint issue per SCRIPT-MAINTENANCE-BACKLOG; qualitative surfaced 70.6% for 2024-25 — backed by multiple outlets).
- 3PT defense splits N/A from script (timed out — but recovered on retry; partial. Some splits still showing N/A in retry — endpoint may not be configured for `Less Than 6Ft` or `>15Ft` in this script).
- Synergy ISO and PostUp samples are very low (2.0 / 0.8 weighted poss) — directionally suggestive but not statistically definitive.

---

## DOMAIN 6 — REBOUNDING

### Statistical (2-season weighted, 60/40)

| Metric | Weighted | Current 2025-26 | Prior 2024-25 |
|---|---|---|---|
| OREB/G | 2.16 | 2.0 | 2.4 |
| DREB/G | 7.68 | 8.0 | 7.2 |
| REB/G | 9.84 | 10.0 | 9.6 |
| OREB% | 6.3% | 5.9% | 6.9% |
| DREB% | 22.7% | 23.6% | 21.4% |
| REB% | 14.5% | 14.6% | 14.1% |
| OREB Chance % | — | 44.6% | 47.8% |
| DREB Chance % | — | 70.5% | 65.1% |
| OREB Contest % | — | 59.7% | 64.9% |
| DREB Contest % | — | 26.6% | 30.9% |
| Box-Outs / G | — | 2.11 | 2.76 |
| Def Box-Outs / G | — | 1.84 | 2.33 |
| Off Box-Outs / G | — | 0.27 | 0.42 |
| Avg DREB Distance | — | 5.6 | 5.7 |
| Avg OREB Distance | — | 7.1 | 6.6 |

### Qualitative

- Career rebounding line: 8.9-10.4 RPG over last 5 seasons — consistent.
- 2025-26 standout games: 30/12 vs SAS (Feb 1, 2025); 19/15 vs WAS (Mar 3, 2025); 11.4 RPG since Jan 25, 2026.
- Box-outs dropped from 2.76 (prior) → 2.11 (current) — slight decline in mechanical effort metrics; consistent with Heat playing him more on the perimeter in 2025-26 with Ware as rim partner.

### Data gaps
- No specific qualitative scout language on box-out technique surfaced — gap is informational, not load-bearing (script data is comprehensive).

---

## DOMAIN 7 — ATHLETICISM

### Statistical proxies

- Combine vertical: 38.5" max (2017).
- Body fat: 5.2% at combine.
- Weight: 242.6 lbs combine; listed ~255 currently.
- Drive volume 6.1/G with 46.0% FG (Domain 1/3 cross-ref) — sustained athletic attack volume at age 28.
- Dunk rate 35.1% (Domain 1) — meaningful but not freak-of-nature; finishes through contact more than over.

### Qualitative

#### #21 Burst / explosion
- "He's a powerful and quick leaper who has a really good combination of length, strength and quickness." — RevUpSports.
- "He's a high level dunker who plays with his head above the rim." — RevUpSports.
- "Even when he gets beat, he has great recovery speed and the ability to get off the ground incredibly quickly to block or alter a shot." — Various.

#### #22 Lateral quickness (DIFFERENTIATING TRAIT)
- "What he lacks in the verticality department, Bam makes up for with a combination of agility and lateral mobility that would make almost any big man in the NBA jealous." — FiveThirtyEight.
- "His elite athleticism and lateral quickness against opposing wings are fairly uncommon traits for players his size."
- "He can stay in front of players who are quick off the bounce more often than not."

#### #23 Strength
- 5.2% body fat at 242 lbs (combine) — elite functional strength composition.
- 9.5" hand length (tied longest at combine) — secondary strength signal (grip / contact finishing).
- No specific recent strength criticism surfaced; he holds position vs centers despite undersized standing reach.

### Data gaps
- No 2017 lane agility / shuttle / bench reps specifics surfaced.
- No updated post-2017 biometric measurements confirmed.

---

## DOMAIN 8 — IQ / MOTOR

### Statistical (2-season, 60/40 where complete)

| Metric | 2025-26 | 2024-25 |
|---|---|---|
| Defender distance: Very Tight (0-2ft) | 5.7%, 40.0% FG | N/A (timed out) |
| Defender distance: Tight (2-4ft) | 38.2%, 50.2% FG | N/A (timed out) |
| Defender distance: Open (4-6ft) | 28.4%, 39.2% FG | N/A (timed out) |
| Defender distance: Wide Open (6+ft) | 27.6%, 41.9% FG, 58.3% eFG | 19.2%, 44.4% FG, 58.4% eFG |
| Shot clock 24-22 | 5.2%, 50.8% FG | 4.2%, 63.8% FG |
| Shot clock 22-18 | N/A | 6.3%, 58.6% FG |
| Shot clock 18-15 | N/A | 12.5%, 46.8% FG |
| Shot clock 15-7 | N/A | 51.3%, 49.6% FG |
| Shot clock 7-4 | N/A | 12.5%, 45.3% FG |
| Shot clock 4-0 | N/A | 13.2%, 39.5% FG |
| Clutch (2025-26 only): GP, PTS, FG%, +/- | 29 GP, 1.5 PPG, 27.8% FG, −0.9 | N/A (timed out) |
| Clutch (2-season weighted) | 29 GP, 0.9 PPG, 16.7% FG, 12.8% 3P, 48.0% FT, −0.5 +/-, 0.1 AST, 0.0 TOV |

**Note:** 2-season weighted clutch line shows poor numbers because the 2024-25 pull failed. 2025-26 clutch alone is 29 GP, 1.5 PPG, 27.8% FG — modest. Qualitative suggests his clutch profile is mixed (see below).

### Qualitative

#### #24 Shot selection
- 51.3% of 2024-25 shots came in the 15-7 sec band — late-clock mid-range volume is heavy. Mid-range frequency 96th+ percentile among bigs.
- 19.4% 3PA share in 2024-25, up from 4.1% in 2023-24 — diet rebalanced significantly.
- Defender distance: 5.7% at very tight, 38.2% at tight — 43.9% of his shots are contested (both seasons combined). This is consistent with his role taking tough mid-range looks.

#### #25 Effort / motor
- "Repeatedly gushed about Bam's work ethic, motor and athleticism." — Spoelstra/Riley pre-draft, 2017 (Hot Hot Hoops).
- "Ain't nobody can question anything Bam says because he's literally our hardest worker." — Udonis Haslem.
- 2024-25 hustle: 3.06 deflections/G prior → 2.38 current — drop in the activity layer (could reflect role/scheme change with Ware).

#### #26 Competitive character
- **Pre-draft Heat workout (foundational story):** During pre-draft drills, "Adebayo turned to Heat brass, including Pat Riley and Erik Spoelstra, and shouted: 'Oh, you got me f—ing confused! You got me f—ed up!'" Juwan Howard: "To have the balls to say that in front of Pat Riley… that's a Heat guy." — Playmaker HQ.
- "We feed off his emotion, we feed off his leadership, we feed off his voice, we feed off his inspiration." — Spoelstra, Clutch Points.
- "Though he wasn't playing his best basketball, he was still leading. That was a big step for him." — Spoelstra, 2024-25.
- **Spoelstra disagreement (2024-25):** "Bam Adebayo Speaks Out on Disagreement With Erik Spoelstra After Heat's Blowout Loss to Spurs" — Yardbarker (negative signal — friction, not durable).

### Data gaps
- 2024-25 defender-distance bands timed out (only Wide Open band recovered).
- 2024-25 clutch stats timed out (one season only).
- 2024-25 speed/distance timed out.

---

## CHARACTER / PROJECTION SIGNALS

### Work ethic
- Spoelstra (pre-draft): "athleticism… toughness, motor, defensive mindset, all of these things that we value." — Hot Hot Hoops.
- Haslem: "literally our hardest worker."
- Pat Riley (2024 contract extension): "He's a caretaker now for this culture. He carries the baton, now and into the future."
- "Miami Heat star Bam Adebayo has been working hard in the gym all summer and according to him, the results have been astounding." — Clutch Points (offseason transformation language, recurring).
- 3-year, $166M extension signed June 2024, beginning 2026-27 — franchise commitment.

### Competitive character
- Foundational pre-draft Riley/Spoelstra/Howard workout story (above) — multi-source corroborated.
- 5x All-Star (2021, 2022, 2023, 2024 — snubbed 2025); 2x All-NBA appearance window.
- "I'm always looking to improve everything — it's not just one thing specifically. It's decision making, reading the game, communicating with Spo." — Adebayo, Yahoo Sports.
- Range extension (3PT) is a multi-year, self-driven project — strong character signal of trajectory ownership.

### Negative signals
- **Offensive passivity criticism (M. Beasley, March 2026):** "The only reason why Bam isn't a 30-point scorer is that the Heat system doesn't allow him to do so… he doesn't play aggressive or look for shots because of the system." — Basketball Network.
- **Jimmy Butler reportedly told Adebayo not to press offensively** (SI headline, full quote not captured — directional).
- **Spoelstra disagreement** (2024-25, post-Spurs blowout loss) — Yardbarker.
- **All-Star miss 2024-25** — first miss in three years.
- **All-Defense miss 2024-25** — first miss since 2018-19.
- **83-point game scrutiny:** "Adebayo's feat drew scrutiny due to his doing so against one of the league's worst squads, the Washington Wizards… called him out for stat padding." Bill Simmons: one of "the weirdest moments in NBA history."

### Trajectory
- **Defense:** rose to All-D 1st Team peak in 2023-24, then regressed in 2024-25 (slipped to 26th in opp FG%, Heat from 5th → 9th DRtg). 2025-26 partial recovery alongside Ware.
- **Offense:** 2024-25 first half career-worst FG% (45.4%) → second half career-best stretch (51.3/43.2/81.1). 2025-26 closing-22.8 PPG / 31.8 3P% / 41.8 3P% post-Jan 25.
- **3PT extension:** clear, multi-year, sustained project. 4.1% → 19.4% 3P rate in one season, then maintained.
- **Age-28 read:** plateau on traditional defense, expansion on offense. Net trajectory: lateral, with offensive-skill ascendance offsetting defensive regression.

---

## PLAYOFF / BIG-GAME TRACK RECORD

**R13 sample minimum: MET** — 7 playoff seasons, 78 games. Recency status: **active** (last playoff 2024-25, gap 1 year; current 2025-26 ended in play-in loss with active back injury — see Injury section).

### Statistical (career playoff vs regular season, matched-season basis)

| Metric | Playoffs | Regular Season | Delta |
|---|---|---|---|
| TS% | 56.7% (78 GP, 7 seasons) | 59.0% (485 GP, 7 seasons) | **−2.3** |
| PPG | 16.4 | 16.9 | −0.5 |
| FGA/G | 12.5 | 12.2 | +0.3 |

### Last 3 playoff runs (most recent first)

| Season | GP | Playoff TS% | RS TS% | Delta | PPG |
|---|---|---|---|---|---|
| 2024-25 | 4 | 50.8% | 56.1% | **−5.3** | 17.5 |
| 2023-24 | 5 | 53.2% | 57.6% | **−4.4** | 22.6 |
| 2022-23 | 23 | 53.0% | 59.2% | **−6.2** | 17.9 |

### Qualitative

- **2023 Finals (#8 seed run, lost 4-1):** 21.8 PPG, 12.4 RPG, 3.2 APG (5 GP); Game 1: 26/13/5; Game 2: 21/9/4 (Heat won to tie 1-1). Duncan Robinson: "Bam is the heart and soul of what we're doing on both ends… sets the tone for us defensively with his versatility… usually on the team's best player." Spoelstra: "Arguably the toughest cover in the league [Jokic] and then he has to shoulder a big offensive role for us as well."
- **2020 Bubble Finals (lost 4-2):** Shoulder/neck strain in Game 1; missed Game 2; played limited rest of series. "[The Finals loss was] a gut punch." — Adebayo.
- **2025-26 play-in (Charlotte loss):** LaMelo Ball flagrant trip in 2Q; Adebayo limped off, ruled out. NBA fined Ball $35K (uncalled flagrant) + $25K (profanity) — $60K total. Spoelstra: "Stupid." 2025-26 ended with active back injury, R13 dormancy flag does **not** apply to next cycle (no documented multi-month ruling).
- **Big-game scoring rises:** 2023 Finals PPG 21.8 vs RS 20.4 — actual rise. 2023-24 PPG 22.6 vs RS 19.3 — also rise. Statistical TS drag without points drag suggests playoff defenses tighten his efficiency but he absorbs more usage.

### Classification (R13 Stage 1 — manual)
- Career matched TS% delta: **−2.3 (neutral)** — normal playoff drag.
- Recency: **active**.
- Per R13: "strong" requires statistical AND qualitative; "moderate" requires either.
- **Statistical:** neutral on career; mild shrink on each of last 3 individual runs (−4.4 to −6.2 TS%).
- **Qualitative:** rise language is dominant ("heart and soul," "Mr. Resilience") — but mostly framed around defense/passing, not scoring.
- **Working classification:** neutral-to-mild shrink on efficiency; **moderate rise on impact (scoring volume + defensive anchor) under big-game pressure**, qualitatively. Final R13 classification deferred to Skill 4.

---

## INJURY HISTORY

| Date / Window | Injury | Status / Recovery |
|---|---|---|
| 2020 ECF Game 4 (vs BOS) | Shoulder | Played through |
| 2020 NBA Finals Game 1 (vs LAL) | Shoulder/neck strain (driving collision with D. Howard) | Missed Game 2; limited rest of series |
| 2024-25 regular season | None significant | 78/82 GP — healthy |
| Early 2025-26 (Nov 2025) | Left big toe sprain | Missed 6 games starting Nov 5; minutes monitored on return |
| 2025-26 play-in (April 2026) | Lower back (LaMelo Ball trip — uncalled flagrant) | Ruled out for remainder of game; season-ending |

**R12 evaluation:** Eval window script auto-detected both seasons as healthy (2024-25 78 GP / 34.3 MPG; 2025-26 73 GP / 32.4 MPG). **No R12 trigger.** Both seasons countable; default 60/40 weighting applies.

**R12 secondary check (qualitative):** 2025-26 had two injury bookends (early toe, late back). Net regular-season GP 73 — full counting season. The back injury is end-of-season; does not re-frame the eval window.

---

## DATA GAP INVENTORY

### Sub-domains with strong statistical + qualitative support (3+ converging sources)
- #1 At-basket finishing
- #2 Contact finishing / foul draw (FTR + qualitative + 83-point game)
- #4 CAS 3PT
- #6 Mid-range (qualitative — script bug; mid-range freq 96th+ percentile multi-source)
- #7 Free throw
- #8 Handling / creation
- #10 Ball security
- #11 Court vision
- #12 Decision-making
- #13 Passing execution
- #15 On-ball pressure / switch defense
- #16 Help defense
- #19 Offensive rebounding
- #20 Defensive rebounding
- #21 Burst / explosion
- #22 Lateral quickness
- #23 Strength
- #24 Shot selection
- #26 Competitive character

### Sub-domains with moderate support (2 sources or partial script)
- #3 Post offense (no Synergy script; qualitative confirms post moves are present but no PPP/percentile data)
- #5 Off-dribble shooting (script ISO PPP + qualitative — Adebayo is not primary off-dribble engine)
- #9 Touch / feel (script floater bug; FT% + qualitative)
- #14 Off-ball movement (Cut + OffScreen Synergy, but he is hub-not-cutter; partial speed/distance)
- #17 Rim protection (script at-rim FG% N/A; qualitative 70.6% — multi-source)
- #18 Post defense (very low Synergy sample 0.8 poss; qualitative supports)
- #25 Effort / motor (multi-source qualitative; partial 2024-25 hustle data)

### Sub-domains with weak support (1 source or major gap)
- None below "moderate" — qualitative + cross-domain script triangulation covers all 26.

### Conflicting signals between sources
- **Domain 2 script outputs vs reality:** Script TS% 22.4% / eFG% 20.8% / Mid-Range FGA 0 are clearly bugged outputs; scoring must use cross-domain (Domain 1 FT% 77.4%, Domain 3 ISO data, qualitative shooting splits). Per S105-F01 learning: when web sources cite season-rate efficiency, prefer script aggregate — but when **script is bugged**, qualitative anchored against Basketball-Reference / StatMuse cross-checks is the fallback. Flag for SCRIPT-MAINTENANCE-BACKLOG.
- **3PT% range:** Qualitative cites multiple windows: 2023-24 35.7%, 2024-25 second-half 39.7-43.5%, 2025-26 final 42 games 31.8% / post-Jan 25 41.8%. Script weighted CAS 31.4% reflects full-window aggregate including cold first halves. Both true at different time scales — full-window is the scoring anchor; the late-window momentum is a trajectory note.
- **Rim protection:** Script unable to produce at-rim FG%; qualitative consistent at 70.6% (worst among qualifying centers, 2024-25). This is the most material data point lost to script and recovered qualitatively.
- **All-Defensive trajectory:** 1st Team in 2023-24, missed entirely in 2024-25 — represents a one-year regression, not a baseline. Whether 2024-25 or 2025-26-with-Ware is the truer reading is a Skill 2/3 judgment.

### Script-maintenance backlog candidates surfaced this run
- Domain 2 mid-range allocation (FG% 0.0%, FGA 0) — appears to map mid-range to wrong shot zone definition.
- Domain 2 TS%/eFG% calculation (22.4% / 20.8% — implausible; perhaps division by raw FGA instead of TSA, or units error).
- Domain 2 prior-season CAS/PullUp split shows N/A for prior — extraction not falling back correctly.
- Domain 3 Floater FGA = 0 — same shot-zone allocation issue likely.
- Domain 4 partial-endpoint timeout cascade caused null divide (TypeError on tov_p / pot_ast_p).
- Domain 5 at-rim DFGPOE endpoint (B# in backlog — reconfirmed).
- Domain 5 LeagueDashPtDefend `<6Ft` and `>15Ft` configured but timed out individually on first run; recovered on retry — backlog should add retry/backoff.
- Playoff_Track_Record.py first-call PlayerCareerStats endpoint highly sensitive to API congestion — needs retry wrapper.
```
=== END RESEARCH PACKET ===
```
