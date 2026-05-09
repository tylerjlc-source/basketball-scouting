# SCRIPT REGISTRY — NBA Statistical Pipeline
**Maps Python scripts to sub-domains and data sources. Governs scout-research automated data collection.**
**Scripts live in /mnt/project/ (read-only). Copy to /home/claude/ before execution.**
**Known issues and fix backlog:** [SCRIPT-MAINTENANCE-BACKLOG.md](SCRIPT-MAINTENANCE-BACKLOG.md) — consult when a script run produces unexpected output.

---

## EXECUTION PROTOCOL

1. Identify player name and competition level.
2. **NBA players only** — run all seven Domain scripts + comp script as needed. College/HS/international players skip to qualitative research.
3. Copy required scripts from `/mnt/project/` to `/home/claude/`.
4. Run each script with the player's name as the first argument: `python Domain_X_Stats.py 'Player Name'`
5. Collect structured output into the research packet.

**2-season evaluation window:** Auto-detected from current date. Current season weight 0.60, prior season weight 0.40. Both seasons queried independently. Weighted composite computed in Python. Exception: rookies or players who missed the entire prior season use current season only.

**R12 injury-window override:** When both recent seasons are compromised, eval_window.py overrides the default weighting and anchors on the most recent healthy season. Full rule: SCORING-RULES.md R12. Detection logic and output format: EVAL-WINDOW-AUTOMATION.md.

---

## SCRIPT TABLE — DOMAIN SCRIPTS

| Script | Path | Sub-domains fed | Key endpoints (nba_api) |
|---|---|---|---|
| Domain_1_Finishing_Stats | /mnt/project/Domain_1_Finishing__Stats.py | #1 At-basket finishing, #2 Contact finishing / foul draw | Restricted area FG% (nba_api), FTR, drive data (LeagueDashPtStats) |
| Domain_2_Shooting_Stats | /mnt/project/Domain_2_Shooting__Stats.py | #4 CAS 3PT, #5 Off-dribble shooting, #6 Mid-range, #7 Free throw | CAS 3PT% (LeagueDashPtStats CatchShoot), pull-up splits (LeagueDashPtStats PullUpShot), ShotChartDetail zone splits, mid-range FG% (LeagueDashPlayerShotLocations), FT% career + current (PlayerCareerStats) |
| Domain_3_Ball_Skills_Stats | /mnt/project/Domain_3_Ball_Skills__Stats.py | #8 Handling / creation, #9 Touch / feel, #10 Ball security | ISO PPP + PnR BH PPP (SynergyPlayTypes), drives/game (LeagueDashPtStats Drives), TOV/touch (LeagueDashPtStats Possessions), floater-range FG% (ShotChartDetail 4-14ft), non-dunk rim FG%, handoff PPP (SynergyPlayTypes) |
| Domain_4_Playmaking_Stats | /mnt/project/Domain_4_Playmaking__Stats.py | #11 Court vision, #12 Decision-making, #13 Passing execution, #14 Off-ball movement | Potential assists + secondary assists + FT assists (LeagueDashPtStats Passing), bad pass TOV + lost ball TOV (LeagueDashPlayerStats), transition PPP (SynergyPlayTypes), cut + off-screen PPP (SynergyPlayTypes), avg offensive speed (LeagueDashPtStats SpeedDistance) |
| Domain_5_Defense_Stats | /mnt/project/Domain_5_Defense__Stats.py | #15 On-ball pressure, #16 Help defense, #17 Rim protection, #18 Post defense | Opponent FG% as closest defender + DFGPOE (LeagueDashPtDefend), deflections + steals + charges + contested shots + box-outs + loose balls (LeagueHustleStatsPlayer), ISO defense PPP (SynergyPlayTypes), post-up defense PPP (SynergyPlayTypes), team DRtg on/off (LeagueDashPlayerStats Advanced) |
| Domain_6_Rebounding_Stats | /mnt/project/Domain_6_Rebounding__Stats.py | #19 Offensive rebounding, #20 Defensive rebounding | OREB% + DREB% (LeagueDashPlayerStats Advanced), contested/uncontested splits + chances + conversion % (LeagueDashPtStats Rebounding), box-outs off + def (LeagueHustleStatsPlayer) |
| Domain_8_IQ_Motor_Stats | /mnt/project/Domain_8_IQ_Motor__Stats.py | #24 Shot selection, #25 Effort / motor, #26 Competitive character | Defender distance distribution (LeagueDashPtShots), shot zone distribution (ShotChartDetail), clutch stats (LeagueDashPlayerClutch), hustle stats full suite (LeagueHustleStatsPlayer) |

**Note on Sub-Domain #3 Post Offense:** Not currently produced by any script. Sourced via web search at all competition levels (NBA.com Play Type pages, Synergy data cited in scouting reports, EvanMiya role/assist signals for college). Same workflow path as Domain 7 athleticism. Script implementation (a SynergyPlayTypes post-up PPP query in Domain 1) is tracked under [SCRIPT-MAINTENANCE-BACKLOG.md](SCRIPT-MAINTENANCE-BACKLOG.md) B10.

---

## SCRIPT TABLE — NBA COMP MATCHING

| Script | Path | Purpose | Key endpoints (nba_api) |
|---|---|---|---|
| NBA_Comp_Stats | /mnt/project/NBA_Comp_Stats.py | Pulls statistical similarity data for NBA Comp matching in Skill 5 | LeagueDashPlayerStats (Advanced): TS_PCT, USG_PCT, AST_PCT, TOV_PCT, REB_PCT, STL_PCT, BLK_PCT. LeagueDashPlayerStats (Base): PTS (PPG fallback). PlayerCareerStats: rookie season detection. |

**Usage:**
```
python NBA_Comp_Stats.py 'Player Name'              # rookie season (default)
python NBA_Comp_Stats.py 'Player Name' --current    # current season
python NBA_Comp_Stats.py 'Player Name' --season 2022-23  # specific season
```

**When to run:** Called by Skill 5 (scout-output) during NBA Comp assignment for prospect evaluations only (States 1–3). Run once per comp candidate — typically 2–3 candidates per evaluation. Not run for NBA vet evaluations (≥25 NBA games — per S119 lineage-comp split — see NBA-COMP-METHODOLOGY.md § B).

**Stats pulled per group:**

| Group | Primary | Secondary |
|---|---|---|
| Guards | TS% | Usage rate, Assist rate, Turnover rate |
| Wings | TS% | Usage rate, Rebound rate, Steal rate |
| Bigs | TS% | Usage rate, Rebound rate, Block rate |

---

## SCRIPT TABLE — R13 PLAYOFF TRACK RECORD

| Script | Path | Purpose | Key endpoints (nba_api) |
|---|---|---|---|
| Playoff_Track_Record | /mnt/project/Playoff_Track_Record.py | Pulls playoff-vs-regular-season delta summary across a player's qualifying playoff runs. Feeds R13 Stage 1 POT modifier (Skill 5) and Stage 2 composite modifier (Skill 4). | LeagueDashPlayerStats + SynergyPlayTypes with SeasonType='Playoffs' variants; PlayerCareerStats for playoff season detection |

**Usage:**
```
python Playoff_Track_Record.py 'Player Name'
```

**When to run:** Called by Skill 1 (scout-research) when the NBA player has ≥2 playoff series across different years (R13 sample minimum).

**Output:** Multi-run playoff vs. regular-season delta summary for scoring-relevant stats (TS%, usage-adjusted PPG, archetype-primary stats, DFGPOE). Includes recency flag — active (within last 2 playoff cycles) / historical-only / active-injury dormant — per R13 classification.

---

## SCRIPT TABLE — SKILL 7 (PUBLIC PROFILE APPENDIX)

| Script | Path | Purpose | Key endpoints (nba_api) |
|---|---|---|---|
| Public_Career_Stats | /mnt/project/Public_Career_Stats.py | Pulls full career per-game stats (Regular Season + Playoffs) for the `## Career stats` reference appendix on `_public.md`. NBA-only — college handled by Skill 1 sub-agent fallback per scout-publish.md Step 1.7. | PlayerCareerStats with `per_mode36='PerGame'` (frames: SeasonTotalsRegularSeason, CareerTotalsRegularSeason, SeasonTotalsPostSeason, CareerTotalsPostSeason — single API call covers all four). |

**Usage:**
```
python Public_Career_Stats.py 'Player Name'
```

**When to run:** Called by Skill 7 (scout-publish) Phase A Step 1.7 on every NBA-vet publish invocation. Parallelizes with the Phase A read batch — player name is the only input.

**Output:** Two artifacts in one call.
- stdout: two markdown tables (RS + Playoffs) with the career row bolded, ready to paste into the `## Career stats` section of `_public.md`. Per-game stats render to 1 decimal; percentages render in `.XXX` NBA.com form.
- file: `scripts/public_career_stats_output.json` — structured payload (`career_stats.regular_season[]`, `career_stats.playoffs[]`) for the export pipeline. Each row matches the `career_stats_row` schema.

**Trade handling:** PlayerCareerStats emits one row per (season, team) plus a `TOT` row for traded seasons. Script uses the TOT row for the per-game numbers and joins non-TOT team abbreviations with `/` for the team display.

**Display spec:** PUBLIC-LANGUAGE-GUIDE §9 (placement, format, numeric form, omission rules).

---

## DOMAIN 7 — ATHLETICISM (NO SCRIPT)

Sub-domains #21 (Burst/explosion), #22 (Lateral quickness), #23 (Strength) have no dedicated script — sourced via web-search biometrics (NBA Combine / Pro Day measurements) and cross-domain proxies already captured elsewhere (dunk rate from Domain 1, drive data from Domain 3, on-ball defense from Domain 5).

---

## COLLEGE / HS / INTERNATIONAL PLAYERS

Scripts are NBA-only (nba_api). For non-NBA players, scout-research gathers data through:
- **EvanMiya** (college D1): manual lookup for skill projections, DBPR, BPR, role metric, opponent-adjusted stats
- **Basketball-Reference** (college): scrapeable for base stats, FT%, TOV%, AST%
- **Hoop-Math** (college D1): scraper build required for rim FG%, shot distribution, % assisted
- **FIBA box scores** (international): manual per player via web search
- **Web search**: scouting reports, combine data, biometrics, character signals

Data source access and priority governed by SUB-DOMAIN-SOURCE-MAP_v1.md and SCORING-RULES.md R2 (Signal Hierarchy).

---

*Maps to SUB-DOMAIN-SOURCE-MAP_v1.md data architecture.*
