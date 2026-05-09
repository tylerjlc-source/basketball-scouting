# S100-F01 — Script output bugs surface during batch evaluations (eval_window GP aggregation + fragment mislabel; Playoff_Track_Record classification hint; NBA_Comp_Stats BLK% endpoint; Domain_1 rim-zone partial-season)

**Status:** Superseded (promoted to docs/SCRIPT-MAINTENANCE-BACKLOG.md as B1–B5, Session 114 2026-04-28)

**Original Date:** 2026-04-23 (original); extended 2026-04-24 (S102 — NBA_Comp_Stats.py BLK% bug added); extended 2026-04-24 (S104 — eval_window fragment-mislabel variant added); extended 2026-04-26 (S110 — Domain_1_Finishing rim-zone partial-season variant added)
**Severity:** Low (cosmetic — none affect composite or domain scoring when overridden at appropriate skill; all mislead if followed mechanically)
**Source file:** `docs/learnings/scout-research-learnings.md`
**Applications before promotion:** 24+ across 5 bug variants (BLK%/STL% endpoint alone hit 24+ individual cases — full breakdown in Applications section below)

---

**Context:** S100 batch-1 wing-scale validation sweep surfaced two distinct script bugs; S102 surfaced a third; S104 surfaced a fourth variant; S110 surfaced a fifth.

(1) **`eval_window.py` GP aggregation bug (TOT-row double-count):** reports GP counts that double-count traded-player rows. Confirmed pattern: Bogdanović showed 108 GP prior-season, Anderson showed 86/122 current/prior across three-team 2025-26 journey; Hauser as single-team showed correct 78/71; **Vučević S104 showed 128 GP for 2025-26 (actual 64) due to Feb 2026 Bulls→Celtics trade triggering TOT+team aggregation** — confirms the bug fires specifically when player was traded mid-season-in-eval-window. Matches S95-F07 PlayerCareerStats TOT-row pattern.

(2) **`eval_window.py` fragment-mislabel variant (S104 new):** Naz Reid S104 had 2024-25 80 GP labeled as "fragment" despite GP clearly ≥58 healthy-threshold per R12 eligibility floor. Different bug from GP aggregation — this is incorrect classification of sample size, not incorrect counting. Likely the R12 fragment-logic check misfires on full-healthy-season samples under some condition (possibly MPG below a threshold — Reid was 27.5 MPG in 2024-25; fragment threshold may be mis-set). **Watch pattern:** does this misfire on 70+ GP seasons with <28 MPG?

(3) **`Playoff_Track_Record.py` classification-hint logic mislabels negative deltas** — Anderson's −0.8 TS% career delta was labeled "moderate statistical rise" (wrong direction AND wrong magnitude; should be Neutral). Reconfirmed S102 on Mobley (+0.5 TS% career delta labeled "moderate statistical rise" despite thin magnitude that should map to Neutral). Naz Reid S104 +1.0 delta labeled "strong statistical rise" — at boundary but script hint is too assertive without AND-qualitative check.

(4) **`NBA_Comp_Stats.py` BLK%/STL% endpoint returns `None`** — S102 pattern confirmed, S104 reconfirms (all 4 Vucevic comp runs + all 4 Naz Reid comp runs returned BLK% None; 8 additional individual cases). Pattern is endpoint-wide, not player-specific. Likely an advanced-stats endpoint returning None for certain percentile columns when full season data hasn't aggregated or when the column isn't populated at the query level.

(5) **`Domain_1_Finishing__Stats.py` rim-zone returns 0 on `--season-override` for partial-season data (S110 new):** Embiid 2025-26 single-season run returned Rim FG% 0.0%, Rim FGA 0, Dunk Rate 0%, % Shots at Rim 0% — clearly impossible for an active high-volume center with 38 GP. Domain 3 captured Non-Dunk Rim FG% 67.5% from the same dataset, confirming the player has rim attempts; the bug is specific to Domain 1's ShotChartDetail rim-zone extraction logic on partial-season data via `--season-override`. **Tell:** Rim FGA == 0 for an active high-volume player. **Workaround:** substitute Non-Dunk Rim FG% from Domain 3's Touch/Feel block as the rim signal, document the substitution in Data Gap Inventory.

**Learning:** All four bug variants are confined to script output framing rather than scoring mechanics. For Skill 1 research packet assembly and Skill 5 comp assessment:
- When eval_window GP count exceeds a plausible season total (~82 GP per team stint), trust domain-script GP values over eval_window summary
- **When eval_window labels a 70+ GP season "fragment," verify against domain-script GP and R12 eligibility floor (≥58 GP = healthy); override label and treat as healthy anchor if GP clearly qualifies**
- When Playoff_Track_Record classification hint conflicts with stat sign, magnitude, OR the R13 strong-vs-moderate AND-qualitative requirement, apply R13 classification manually per SCORING-RULES.md R13
- When NBA_Comp_Stats.py BLK% (or STL%) returns None for Big or Wing comp candidates, proceed with primary TS% + available secondaries (USG%, REB%) for tier determination — do NOT fail the comp to 🔴 Rubric-only on endpoint quirk alone. Document the endpoint gap transparently in the comp flags.
- When Domain_1_Finishing rim metrics return 0 on a `--season-override` partial-season run, substitute Non-Dunk Rim FG% from Domain 3 Touch/Feel block as the rim signal; document substitution in Data Gap Inventory under "Conflicting signals" or "Script bugs."
- Flag all five in research packet / comp output transparently — downstream skills should override the hints, not the corrected values

**Applies to:** Skill 1 research packet assembly when using eval_window.py, Playoff_Track_Record.py, and Domain_1 outputs; Skill 5 comp assessment when using NBA_Comp_Stats.py outputs. All scripts should be fixed in a future maintenance session; none are blocking for evaluation work.

**Applications (final count at promotion):** 24+ individual cases across 5 variants:
- eval_window GP-aggregation: 3 (Bogdanović S100, Anderson S100, Vučević S104)
- eval_window fragment-mislabel: 1 (Naz Reid S104)
- Playoff_Track_Record classification: 6 (Anderson S100, Mobley S102, Naz Reid S104, Turner S107, Tatum S108, Embiid S110)
- NBA_Comp_Stats BLK%: 24+ (S102 Mobley/Sabonis/Bridges + S104 Vučević 4 runs + Naz Reid 4 runs + S107 Turner 4 runs + S108 Tatum 4 runs + S110 Embiid 2 runs + S112 Cade 3 runs + S113 Wemby 3 runs)
- Domain_1 rim-zone: 1 (Embiid S110 2025-26 override)

---

**Promotion record:** S100-F01 was logged as a script-bug catalog entry from S100 batch-1 wing-scale validation sweep, then progressively extended across S102, S104, and S110 as new bug variants surfaced. Workstream 2 spike (S110–S113) reconfirmed all five variants and added two more (Domain 5 #17 Rim D_FGA endpoint N/A from Wemby S113; Domain 5/6/8 partial endpoint timeouts from Wemby S113). Promotion threshold (≥3 applications) far exceeded — 24+ on BLK%/STL% endpoint alone.

Promoted to a new dedicated tracker doc rather than to a rule document because the catalog has lifecycle properties (entries get added, fixed, retired) that don't fit the rule-doc structure. Routing decision: SELF-LEARNING-PROTOCOL.md routing table has no "maintenance backlog" destination — closest entry is "Operational / process" but neither PRODUCT_DESIGN_DECISIONS (decision log) nor PROJECT_ROADMAP (project planning) fit the active-bug-tracker concern. New file `docs/SCRIPT-MAINTENANCE-BACKLOG.md` created as third tracker type, loaded on-demand only.

The backlog inherits 5 entries from S100-F01 (B1, B2, B3, B4, B5 in the new doc) and adds 2 from the W2 retrospective (B6 Domain 5 #17 endpoint N/A; B7 Domain 5/6/8 timeouts). Bugs ordered by fix priority — B4 (BLK%/STL% endpoint, 24+ apps, High) leads.

S95-F07 (PlayerCareerStats endpoint quirks — frame ordering + TOT rows) is structurally adjacent but already coded into PlayerCareerStats consumers; no open work, not added to the backlog. Remains in scout-research-learnings.md as an active learning.
