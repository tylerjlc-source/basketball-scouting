# SCRIPT MAINTENANCE BACKLOG

Active bug tracker for the Python statistical pipeline. Each entry covers one observed bug, its workaround, application count (frequency signal), and fix priority.

**Loaded on-demand:**
- When a script run produces unexpected output (lookup workaround)
- When opening a maintenance session (lookup priority queue)

Not loaded at Skill 1 runtime by default — most evaluations don't hit a script bug. The relevant scout-research-learnings.md pointer signals when to consult this file.

**Bug ordering: by fix priority, then by application count.**

---

## OPEN BUGS

### B11 — `Public_Narrative_Stats.py` shared-output race condition on parallel runs
**Script:** `scripts/Public_Narrative_Stats.py`
**Symptom:** Concurrent invocations on different players race-condition on the shared payload file `scripts/public_narrative_stats_output.json`. The last writer wins; the markdown rendering at end of each run reads from the shared file, so multiple parallel runs report identical data (whichever player happened to write last). Tatum (solo) ran clean; subsequent parallel Mitchell + Brown + Kawhi all reported identical CAS / pull-up / isolation values.
**Trigger:** Two or more `python scripts/Public_Narrative_Stats.py "<player>"` invocations running concurrently against the same working directory.
**Tell:** Distinct players returning byte-identical per-season splits in their respective output files.
**Workaround:** Run serially (one player at a time) until fix lands.
**Fix direction:** Per-player payload filename (e.g., `public_narrative_stats__<player_slug>.json`) or run-scoped temp file with player-keyed output.
**Applications:** 1 multi-player case (Wave-2 backfill QC7 retrofit sweep — Mitchell / Brown / Kawhi 2026-05-09).
**Fix priority:** Medium (Wave-2 backfill needs the script; serial workaround is functional but slows the sweep 4×).
**Status:** Open.

### B12 — `Domain_4_Playmaking__Stats.py` TypeError on missing `pot_ast_p`
**Script:** `scripts/Domain_4_Playmaking__Stats.py`
**Symptom:** Crashes with `TypeError: unsupported operand type(s) for /: 'NoneType' and 'float'` at `tov_pot_p = round(tov_p / pot_ast_p, 2) if pot_ast_p and pot_ast_p > 0 else None`. The guard short-circuits on `pot_ast_p` being falsy, but `tov_p` (numerator) being None still reaches the divide.
**Trigger:** Script run when `tov_p` returns None from upstream lookup.
**Tell:** Script failure at the `tov_pot_p` line specifically; D4 returns no payload.
**Workaround:** None at runtime; playmaking domain returns empty until script is patched.
**Fix direction:** Reorder the guard to also check `tov_p is not None`.
**Applications:** 3 (Tatum 2026-05-09, Mitchell 2026-05-09, Brown 2026-05-09 — all during QC7 retrofit sweep).
**Fix priority:** Medium (D4 systematically fails; worth the small fix to unblock playmaking-anchor narrative pulls).
**Status:** Open.

---

### B7 — Domain 5/6/8 partial endpoint timeouts on 2025-26 single-season runs
**Scripts:** `scripts/Domain_5_Defense__Stats.py`, `scripts/Domain_6_Rebounding__Stats.py`, `scripts/Domain_8_IQ_Motor__Stats.py`
**Symptom:** Various endpoints return partial data or timeout on 2025-26 single-season runs (D5 LeagueDashPtDefend partial; D6 Tracking Rebounding 2025-26; D8 distance bands + shot clock 2025-26).
**Trigger:** Likely partial-season data availability issue; endpoint behavior varies by season.
**Workaround:** 2024-25 fallback or qualitative substitution.
**Applications:** 1 multi-endpoint case (Wemby S113 — D5/D6/D8 simultaneous on 2025-26).
**Fix priority:** Medium (multiple endpoints affected; suggests systemic 2025-26 partial-season data issue; investigate root cause before patching individually).
**Status:** Open. Watchpoint: does this fire again on next 2025-26 single-season run?

---

### B2 — `eval_window.py` fragment-mislabel variant
**Script:** `scripts/eval_window.py`
**Symptom:** Healthy 70+ GP seasons labeled "fragment" despite clearly meeting R12 ≥58-GP eligibility floor.
**Trigger:** Likely MPG below a threshold; surfaces on full-healthy-season samples with low-volume players. Possibly the R12 fragment-logic check misfires on full-healthy-season samples under some MPG-threshold condition.
**Workaround:** When eval_window labels a 70+ GP season as fragment, verify against domain-script GP and override label per R12 eligibility floor.
**Applications:** 1 (Naz Reid S104 — 80 GP at 27.5 MPG mislabeled fragment).
**Fix priority:** Low (single occurrence; watchpoint pending more data).
**Watchpoint:** Does this misfire on 70+ GP seasons with <28 MPG?
**Status:** Open.

---

### B5 — `Domain_1_Finishing__Stats.py` rim-zone returns 0 on `--season-override` partial-season
**Script:** `scripts/Domain_1_Finishing__Stats.py`
**Symptom:** Rim FG%, Rim FGA, Dunk Rate, % Shots at Rim all return 0 for active high-volume players when running `--season-override` on partial-season data. Domain 3 captures Non-Dunk Rim FG% from same dataset, confirming the player has rim attempts — bug is specific to Domain 1's ShotChartDetail rim-zone extraction logic on partial-season data.
**Trigger:** ShotChartDetail rim-zone extraction logic fails on partial-season data via `--season-override`.
**Tell:** Rim FGA == 0 for an active high-volume player.
**Workaround:** Substitute Non-Dunk Rim FG% from Domain 3 Touch/Feel block as rim signal. Document substitution in Data Gap Inventory under "Conflicting signals" or "Script bugs."
**Applications:** 1 (Embiid S110 2025-26 single-season).
**Fix priority:** Low (partial-season override is used rarely; workaround clean).
**Status:** Open.

---

### B6 — `Domain_5_Defense__Stats.py` #17 Rim D_FGA endpoint N/A
**Script:** `scripts/Domain_5_Defense__Stats.py`
**Symptom:** Rim D_FGA endpoint returns N/A; rim-protection direct measurement unavailable from primary endpoint.
**Trigger:** Endpoint-specific (LeagueDashPtDefend rim-zone defender data) returns N/A in some contexts.
**Workaround:** Proxy via BLK + Contested + on/off + qualitative.
**Applications:** 1 (Wemby S113).
**Fix priority:** Low (single occurrence; proxy reliable).
**Status:** Open.

---

### B8 — `Domain_1_Finishing__Stats.py` rim-zone N/A on default 2-season window prior-season pull
**Script:** `scripts/Domain_1_Finishing__Stats.py`
**Symptom:** Rim FG% prior-season displays N/A on default 2-season-window run for active high-volume players with confirmed healthy prior-season rim attempts. Current-season rim data populates correctly; weighted output falls back to current-only via `stat_block` N/A path.
**Trigger:** ShotChartDetail prior-season pull fails or returns empty on default 2-season window. Distinct from B5 (`--season-override` partial-season trigger).
**Tell:** Rim FGA prior column == "N/A" while Domain 3 non-dunk rim FG% prior captures cleanly from same ShotChartDetail dataset.
**Workaround:** Substitute Domain 3 non-dunk rim FG% as rim signal for the prior season (same as B5). Document substitution in Data Gap Inventory.
**Applications:** 1 (Giannis S116 — 2025-26 + 2024-25 default window; 2024-25 prior-season ShotChartDetail returned N/A while D3 captured same dataset cleanly).
**Root cause family:** B5 sibling — both are ShotChartDetail rim-zone extraction failures; B5 on `--season-override` partial-season, B8 on default-window prior-season. Combined evidence suggests `get_shot_chart_data` has season-parameter handling fragility meriting a unified fix.
**Fix priority:** Low (single occurrence; workaround clean; pair with B5 if patched).
**Status:** Open.

---

## RESOLVED

### B3 — `Playoff_Track_Record.py` classification-hint mislabeling (resolved 2026-05-09)
**Script:** `scripts/Playoff_Track_Record.py`
**Original symptom:** `classify_delta` returned a single label asserted from stat sign + magnitude alone, missing R13's AND/OR-qualitative rules and the Stage 2 convergence-gate. Anderson −0.8 was labeled "moderate statistical rise" (wrong direction); Mobley +0.5 was labeled "moderate rise" despite a magnitude too thin for any Stage 2 modifier; Embiid career −3.6 was labeled "moderate shrink" without flagging the AND-rule.
**Fix:** Rewrote `classify_delta` to return a `(label, modifier_eligibility)` tuple. Label now spells out direction (rise / shrink / neutral) + magnitude (near-baseline / moderate / strong) + the Stage 2 modifier the stat side could *enable* with qualitative convergence (e.g. moderate shrink −0.20 with qual OR-rule, strong shrink −0.40 with qual AND-rule). Near-baseline range (delta in (−1, +1)) explicitly flagged as "convergence-gate likely fails." Script never asserts a final R13 classification — that requires qualitative-side review the script can't see. New `stage2_modifier_eligibility` field added to JSON output.
**Verification:** 11-case synthetic test covering all R13 thresholds plus the three documented backlog reproductions:
  - Anderson −0.8 → "near-baseline shrink, magnitude too thin for Stage 2 modifier" (was: "moderate statistical rise")
  - Mobley +0.5 → "near-baseline rise, magnitude too thin for Stage 2 modifier" (was: "moderate statistical rise")
  - Embiid career delta → live run on Embiid produces "shrink (delta −4.1) — eligible for moderate shrink (−0.20) with qualitative convergence; strong shrink (−0.40) requires qualitative AND-rule"
**Original applications count:** 6 (Anderson S100, Mobley S102, Naz Reid S104, Turner S107, Tatum S108, Embiid S110).

### B10 — Domain 1 #3 Post Offense unimplemented (resolved 2026-05-09)
**Script:** `scripts/Domain_1_Finishing__Stats.py`
**Original symptom:** Domain 1 had only sub-domains #1 and #2; no SynergyPlayTypes Postup query existed. Two reference docs had originally claimed automated coverage; S117 walked the docs back to web-search-only as Option A. Option B (script implementation) was deferred.
**Fix (Option B):** Added `get_league_postup(season)` (SynergyPlayTypes Postup, offensive, 3-retry backoff mirroring Domain 3) and `extract_postup(result, pid)` extractor. Wired both into `pull_finishing_profile_2season` and the `__main__` orchestration. Profile dict now includes `subdomain_3_post_offense` with weighted post-up PPP, possessions, FG%, and percentile. `print_comparison` renders the new sub-domain. `synergyplaytypes` added to imports.
**Doc updates:**
- `SCRIPT-REGISTRY.md` Domain 1 row now lists #3; the "Note on Sub-Domain #3" reverted from web-search-only to "NBA automated; college / HS still manual."
- `SUB-DOMAIN-SOURCE-MAP_v1.md` §3 Block A line 199 (NBA PPP) and Block B Priority 1 (post touch freq) flipped to 🟢 Automated; Block E High-confidence row dropped the "aspirational" parenthetical.
**Verification:** Live run on Jokić 2024-25 produced post-up PPP weighted = 1.108 — matches the documented 1.09 anchor in `SUB-DOMAIN-SOURCE-MAP_v1.md` line 257 (Jokić, "1.09 PPP on post-ups"). Possessions = 436 weighted, FG% = 59.1%, percentile = 77.7%.

### B1 — `eval_window.py` GP aggregation TOT-row double-count (resolved 2026-05-09)
**Script:** `scripts/eval_window.py`
**Original symptom:** Reported inflated GP counts (108, 122, 128, 100) for traded-player seasons due to summing per-team rows AND the season-aggregate TOT row.
**Root cause:** `fetch_career_seasons` iterated every row of `PlayerCareerStats.SeasonTotalsRegularSeason`. The NBA API emits one row per team plus a TOT row (`TEAM_ABBREVIATION="TOT"`) for traded players, so the season was effectively counted twice.
**Fix:** Refactored `fetch_career_seasons` to prefer the TOT row when present, falling back to the single team row otherwise — same trade-aware pattern as Playoff_Track_Record.py's S95-F07 fix. Removed unused `defaultdict` import.
**Verification:** All 5 existing R12 validation cases still pass (`python scripts/eval_window.py --validate`). Live B1 reproduction on Doncic 2024-25 now correctly reports 50 GP (was 100 GP — 50 actual × 2 from TOT double-count).
**Original applications count:** 4 (Bogdanović S100, Anderson S100, Vučević S104, Doncic S124).

### B9 — `Domain_8_IQ_Motor__Stats.py` `weighted_avg` silently treats missing prior season as zero (resolved 2026-05-09)
**Script:** `scripts/Domain_8_IQ_Motor__Stats.py`
**Original symptom:** Speed/distance and clutch summary tables displayed values at ~60% of true magnitude when prior-season pull timed out or returned an empty dict — silent miscalibration with no N/A tell.
**Root cause:** `weighted_avg(c, p, key)` resolved a missing `prior[key]` to 0 (via `prior.get(key, 0) or 0`), then computed `c * 0.60 + 0 * 0.40` rather than falling back to current-only when prior was unavailable.
**Fix:** Rewrote `weighted_avg` to detect missing prior (`p_val is None` or empty dict) and return current-only `round(c_val, 3)` in that case. Mirrors Domain 1's `stat_block` fallback. Also handles missing-current and both-missing cases.
**Verification:** Synthetic-input test suite (6 cases including the Giannis-style reproduction): empty prior with current=4.2 now returns 4.2 (was 2.52); other cases unchanged.
**Original applications count:** 1 (Giannis S116). Fix is preventive — silent miscalibration that produced no visible tell, so true frequency may have been higher than catalogued.

### B4 — `NBA_Comp_Stats.py` BLK%/STL% endpoint returns `None` (resolved 2026-05-09)
**Script:** `scripts/NBA_Comp_Stats.py`
**Original symptom:** BLK% and STL% (and silently TOV%) advanced-stat columns returned `None` for every comp candidate across all groups.
**Root cause:** The NBA Stats `LeagueDashPlayerStats(measure_type="Advanced")` response does not include `STL_PCT`, `BLK_PCT`, or `TOV_PCT` keys at all — `dict.get()` returned `None` because those keys never existed. (TOV% had been silently broken too; not previously catalogued.)
**Fix:** Added `pull_per100_stats()` for `Base/Per100Possessions` to source `STL/100` and `BLK/100`. Switched TOV source from missing `TOV_PCT` to `E_TOV_PCT` (Advanced — already in percent). Replaced `stl_pct`/`blk_pct` output keys with `stl_per_100`/`blk_per_100`; updated tolerance bands to per-100 units (±0.5 / ±1.0). Updated `NBA-COMP-METHODOLOGY.md` §A.2 stat table + tolerance bands to match.
**Verification:** Live run on Wemby 2024-25 returned TOV%=11.9, STL/100=1.6, BLK/100=5.5 — all previously `None`.
**Original applications count:** 24+ across 10+ players (Mobley/Sabonis/Bridges S102; Vučević/Naz Reid S104 4 runs each; Turner S107; Tatum S108; Embiid S110 2 runs; Cade S112 3 runs; Wemby S113 3 runs).

---

## CHANGE LOG

- **2026-05-09** — B3 resolved. `Playoff_Track_Record.classify_delta` rewritten to return `(label, stage2_modifier_eligibility)` tuple. Eliminates the wrong-direction labels (e.g. Anderson −0.8 "moderate rise") and the asserted-strong-without-qualitative labels (e.g. Mobley +0.5 "moderate rise"). Near-baseline range explicitly flagged for likely convergence-gate fail. Output JSON gains `stage2_modifier_eligibility` field. Script never asserts a final R13 classification — qualitative-side review required per R13 Stage 2 AND/OR rules. 11-case synthetic test plus live run on Embiid (delta −4.1, "shrink, eligible for moderate shrink with qual OR-rule") verify the fix.
- **2026-05-09** — B10 Option B resolved. Domain 1 now pulls SynergyPlayTypes Postup (offensive) league-wide per season and renders sub-domain #3 (post-up PPP / poss / FG% / percentile) in both the JSON profile and the print_comparison summary. SCRIPT-REGISTRY.md and SUB-DOMAIN-SOURCE-MAP_v1.md flipped from manual / aspirational to automated for NBA-level coverage. College/HS coverage stays web-search-only. Live-verified on Jokić 2024-25 (post-up PPP weighted 1.108, matching the documented 1.09 career anchor).
- **2026-05-09** — B1 resolved. `eval_window.py fetch_career_seasons` now prefers the TOT row (when traded mid-season) and falls back to the single team row otherwise — same pattern as Playoff_Track_Record's S95-F07 fix. Eliminates the per-team + TOT double-count that produced 100/122/128 GP totals. All 5 R12 validation cases still pass; live-verified on Doncic 2024-25 (50 GP, was 100).
- **2026-05-09** — B9 resolved. `Domain_8_IQ_Motor__Stats.py weighted_avg` now falls back to current-only when prior is empty/missing, matching Domain 1's `stat_block` behavior. Eliminates silent ~60%-of-truth miscalibration on prior-season endpoint timeouts. Verified via 6-case synthetic-input test.
- **2026-05-09** — B4 resolved. `NBA_Comp_Stats.py` switched STL/BLK source from missing Advanced columns to `Base/Per100Possessions`; switched TOV source to `E_TOV_PCT` (also missing as `TOV_PCT`). Output fields renamed `stl_pct`/`blk_pct` → `stl_per_100`/`blk_per_100`. `NBA-COMP-METHODOLOGY.md` §A.2 tolerance-band table updated to match (±0.5 STL/100, ±1.0 BLK/100; per-100 and STL%/BLK% are >0.9 correlated, so the substitution is cosmetic). Live-verified on Wemby 2024-25.
- **S124 (2026-04-30)** — B1 Applications count incremented 3 → 4 with Doncic case (100 GP for 2024-25 due to Feb 2025 Mavs→Lakers trade). Same TOT-row aggregation pattern as Bogdanović / Anderson / Vučević precedents; no new bug variant.
- **S117 (2026-04-29)** — Added B8 (Domain 1 ShotChartDetail rim-zone N/A on default-window prior season; B5 sibling), B9 (Domain 8 `weighted_avg` silently treats missing prior as zero; produces ~60%-of-true display), B10 (Domain 1 #3 Post Offense unimplemented despite SCRIPT-REGISTRY and SUB-DOMAIN-SOURCE-MAP coverage claims — promoted to Medium for doc-fidelity / P3 concern). All three from S116 Giannis Skill 1 observations. B10 Option A documentation patches applied same session: SCRIPT-REGISTRY.md Domain 1 row trimmed + web-search-only note added; SUB-DOMAIN-SOURCE-MAP_v1.md #3 Block A line 199 + Block B line 212 changed to manual public-web lookup; Block E line 246 confidence ladder kept aspirational with backlog pointer; line 213 retained as defensible (logged for future review).
- **S114 (2026-04-28)** — Backlog promoted from scout-research-learnings.md S100-F01 family per Workstream 2 retrospective recommendation. Initial entries B1–B7 cover 5 variants from S100-F01 (eval_window GP aggregation + fragment mislabel; Playoff_Track_Record classification hint; NBA_Comp_Stats BLK%/STL%; Domain 1 rim-zone partial-season) plus 2 from W2 retrospective (Domain 5 #17 endpoint N/A; Domain 5/6/8 partial endpoint timeouts). 24+ total applications across the family. S95-F07 (PlayerCareerStats frame ordering + TOT rows) already coded into PlayerCareerStats consumers — not added (no open work).

---

*Created Session 114. Promoted from S100-F01 scout-research learning per Workstream 2 retrospective. Loaded on-demand during maintenance sessions or when a script run produces unexpected output. Append-only structure: bugs move to "Resolved" when fixed; never deleted (frequency record preserves the prioritization signal).*
