# SCRIPT MAINTENANCE BACKLOG

Active bug tracker for the Python statistical pipeline. Each entry covers one observed bug, its workaround, application count (frequency signal), and fix priority.

**Loaded on-demand:**
- When a script run produces unexpected output (lookup workaround)
- When opening a maintenance session (lookup priority queue)

Not loaded at Skill 1 runtime by default — most evaluations don't hit a script bug. The relevant scout-research-learnings.md pointer signals when to consult this file.

**Bug ordering: by fix priority, then by application count.**

---

## OPEN BUGS

### B1 — `eval_window.py` GP aggregation TOT-row double-count
**Script:** `scripts/eval_window.py`
**Symptom:** Reports inflated GP counts (e.g., 108, 122, 128) for traded-player rows, due to TOT row + individual team rows both summed.
**Trigger:** Player was traded mid-season-in-eval-window; nba_api PlayerCareerStats returns multiple rows per season.
**Workaround:** When eval_window GP exceeds plausible season total (~82 GP), trust domain-script GP values over eval_window summary.
**Applications:** 4 (Bogdanović S100, Anderson S100 — three-team 86/122 split, Vučević S104 — 128 GP for 2025-26 due to Feb 2026 Bulls→Celtics trade, Doncic S124 — 100 GP for 2024-25 due to Feb 2025 Mavs→Lakers trade).
**Root cause family:** Same family as S95-F07 — TOT-row aggregation mismatch in PlayerCareerStats consumers. S95-F07 was coded into Playoff_Track_Record.py; eval_window.py needs the same treatment.
**Fix priority:** Medium (cosmetic; workaround reliable; affects display logic only).
**Status:** Open.

---

### B3 — `Playoff_Track_Record.py` classification-hint mislabeling
**Script:** `scripts/Playoff_Track_Record.py`
**Symptom:** Classification hints for TS% delta produce wrong direction (Anderson −0.8 labeled "moderate statistical rise") or wrong magnitude without the R13 strong-vs-moderate AND-qualitative requirement (Mobley +0.5 labeled "moderate statistical rise" despite thin magnitude that should map to Neutral).
**Trigger:** Script generates strong/moderate/rise/shrink/neutral hints from stat sign + magnitude alone, missing R13's qualitative AND-rule and convergence-gate logic.
**Workaround:** When classification hint conflicts with stat sign, magnitude, or R13 AND-qualitative requirement, apply R13 classification manually per SCORING-RULES.md R13.
**Applications:** 6 (Anderson S100 wrong direction; Mobley S102 thin magnitude assertive; Naz Reid S104 boundary too assertive; Turner S107; Tatum S108; Embiid S110 career delta −3.6 labeled "moderate statistical shrink").
**Fix priority:** Medium (consistent mislabeling; fix would require encoding R13 AND-rule + convergence-gate logic in script — non-trivial; convergence-gate now explicit in SCORING-RULES.md R13 per S114 promotion).
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

### B10 — Domain 1 #3 Post Offense unimplemented despite SCRIPT-REGISTRY and SUB-DOMAIN-SOURCE-MAP coverage claims
**Script:** `scripts/Domain_1_Finishing__Stats.py`
**Symptom:** Domain 1 script never queries SynergyPlayTypes; output JSON contains only `subdomain_1_at_basket_finishing` and `subdomain_2_contact_finishing`; `print_comparison` renders #1 and #2 only. Two reference docs originally claimed automated coverage:
- SCRIPT-REGISTRY.md Domain 1 row listed "#3 Post offense" with "post-up PPP (SynergyPlayTypes)" as a key endpoint (corrected S117 — row trimmed to #1 + #2; web-search-only note added under domain script table).
- SUB-DOMAIN-SOURCE-MAP_v1.md #3 Block A line 199 listed NBA post-up PPP "🟢 Automated" via nba_api; Block B Priority 1 line 212 listed post touch frequency "🟢 NBA" via nba_api Player Tracking; Block E line 246 confidence ladder listed "Post-up PPP from nba_api" as a High-tier requirement (corrected S117 — line 199 → manual public-web lookup; line 212 → manual public-web lookup; line 246 kept aspirational with parenthetical pointer to this entry).
**Trigger:** Persistent — affected every Domain 1 run since the script existed.
**Tell:** grep `Domain_1_Finishing__Stats.py` for "SynergyPlayTypes" or "post" — no matches. Output JSON missing `subdomain_3_post_offense` key.
**Workaround:** #3 sourced via web search at all competition levels (NBA included — NBA.com Play Type pages, Synergy data cited in scouting reports, EvanMiya role/assist signals at college). Same workflow path as Domain 7 athleticism.
**Applications:** Persistent across all NBA evaluations since the Domain 1 script existed. No realized scoring friction observed (qualitative web search has covered the gap), but documentation drift gave scorers a false sense of automated coverage across two reference docs.
**Residual drift retained S117:** SUB-DOMAIN-SOURCE-MAP_v1.md line 213 ("Assist rate in half-court settings | EvanMiya assist rate + role metric (college) / nba_api (NBA) | 🟢 NBA / 🟡 College manual") was retained as defensible — NBA assist rate IS captured by Domain 4, though the "half-court settings" qualifier is not script-scoped. Logged here for future review when this entry is revisited.
**Fix priority:** Medium (S117 promotion — doc-fidelity drift propagated across two reference docs constitutes a P3-flavored architectural concern; runtime impact remains low because qualitative workaround is reliable).
**Remediation paths:**
- **Option A — Documentation patches (applied S117):** SCRIPT-REGISTRY + SUB-DOMAIN-SOURCE-MAP corrected. Doc-vs-implementation alignment restored.
- **Option B — Script implementation (deferred):** Add SynergyPlayTypes post-up PPP query as third sub-domain block in `Domain_1_Finishing__Stats.py`. Pattern established (Domain 3 already uses SynergyPlayTypes for ISO PPP). Effort: medium.
**Status:** Open (Option A complete S117; Option B pending).

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

- **2026-05-09** — B9 resolved. `Domain_8_IQ_Motor__Stats.py weighted_avg` now falls back to current-only when prior is empty/missing, matching Domain 1's `stat_block` behavior. Eliminates silent ~60%-of-truth miscalibration on prior-season endpoint timeouts. Verified via 6-case synthetic-input test.
- **2026-05-09** — B4 resolved. `NBA_Comp_Stats.py` switched STL/BLK source from missing Advanced columns to `Base/Per100Possessions`; switched TOV source to `E_TOV_PCT` (also missing as `TOV_PCT`). Output fields renamed `stl_pct`/`blk_pct` → `stl_per_100`/`blk_per_100`. `NBA-COMP-METHODOLOGY.md` §A.2 tolerance-band table updated to match (±0.5 STL/100, ±1.0 BLK/100; per-100 and STL%/BLK% are >0.9 correlated, so the substitution is cosmetic). Live-verified on Wemby 2024-25.
- **S124 (2026-04-30)** — B1 Applications count incremented 3 → 4 with Doncic case (100 GP for 2024-25 due to Feb 2025 Mavs→Lakers trade). Same TOT-row aggregation pattern as Bogdanović / Anderson / Vučević precedents; no new bug variant.
- **S117 (2026-04-29)** — Added B8 (Domain 1 ShotChartDetail rim-zone N/A on default-window prior season; B5 sibling), B9 (Domain 8 `weighted_avg` silently treats missing prior as zero; produces ~60%-of-true display), B10 (Domain 1 #3 Post Offense unimplemented despite SCRIPT-REGISTRY and SUB-DOMAIN-SOURCE-MAP coverage claims — promoted to Medium for doc-fidelity / P3 concern). All three from S116 Giannis Skill 1 observations. B10 Option A documentation patches applied same session: SCRIPT-REGISTRY.md Domain 1 row trimmed + web-search-only note added; SUB-DOMAIN-SOURCE-MAP_v1.md #3 Block A line 199 + Block B line 212 changed to manual public-web lookup; Block E line 246 confidence ladder kept aspirational with backlog pointer; line 213 retained as defensible (logged for future review).
- **S114 (2026-04-28)** — Backlog promoted from scout-research-learnings.md S100-F01 family per Workstream 2 retrospective recommendation. Initial entries B1–B7 cover 5 variants from S100-F01 (eval_window GP aggregation + fragment mislabel; Playoff_Track_Record classification hint; NBA_Comp_Stats BLK%/STL%; Domain 1 rim-zone partial-season) plus 2 from W2 retrospective (Domain 5 #17 endpoint N/A; Domain 5/6/8 partial endpoint timeouts). 24+ total applications across the family. S95-F07 (PlayerCareerStats frame ordering + TOT rows) already coded into PlayerCareerStats consumers — not added (no open work).

---

*Created Session 114. Promoted from S100-F01 scout-research learning per Workstream 2 retrospective. Loaded on-demand during maintenance sessions or when a script run produces unexpected output. Append-only structure: bugs move to "Resolved" when fixed; never deleted (frequency record preserves the prioritization signal).*
