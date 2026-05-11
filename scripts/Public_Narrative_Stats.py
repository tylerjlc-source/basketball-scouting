"""
Skill 7 — Public Narrative Stats puller.

Orchestrates the 7 Skill-1 domain stats scripts at publish time and re-emits
per-season + two-season-aggregate granular splits for public-narrative use
(no 60/40 weighted blends — see PUBLIC-LANGUAGE-GUIDE.md §5.3, §8 QC7).

Pipeline:
  1. Resolve eval window via eval_window.py (handles R12 modes).
  2. Run all 7 Domain_X_*.py scripts in parallel as subprocesses for the player.
     Each domain script writes its own per-player JSON to scripts/<name>_output.json.
  3. Read each JSON output. Walk every {current, prior, weighted, [volumes]} block
     produced by the domain scripts' shared `sb()` shape.
  4. For each block emit three views:
       current_season       raw value + raw count for the most-recent season
       prior_season         raw value + raw count for the prior season
       two_season_aggregate sum/sum across both seasons (NOT 60/40 weighted) +
                            combined raw count and 'since [year]' frame
     The 60/40 weighted field from the source JSON is dropped.
  5. Emit:
       stdout: markdown handoff block organized by sub-domain
       file:   scripts/public_narrative_stats_output.json structured payload

Eval-window mode handling:
  DEFAULT       60/40 two-season window — emit all three views.
  R12_ANCHOR    single healthy anchor season — emit current_season only;
                skip prior + aggregate (anchor IS the most-recent meaningful sample).
  R12_AGGREGATE two compromised seasons — emit both individually with GP context
                in the structured payload so narrative framing can cite each
                season's GP explicitly per PUBLIC-LANGUAGE-GUIDE §10.
  ROOKIE        rookie season only — emit current_season only.
  OVERRIDE      manual --season-override — emit single season at 100% weight.

Aggregate math (rounding caveat):
  The source JSON stores percentage (e.g., .407) and volume (e.g., 280 attempts)
  but NOT the raw makes count. We reverse-compute makes ≈ round(pct * volume),
  introducing ±1 make of rounding error per season. For the standard CAS 3PT
  use case (200-700 attempts), this is ±0.1-0.5% drift on the aggregate —
  well within R14 dial tolerance and visually equivalent to the true sum/sum
  for narrative purposes. Documented at
  PUBLIC-LANGUAGE-GUIDE.md §9.5.

Usage:
  python Public_Narrative_Stats.py "Player Name"
  python Public_Narrative_Stats.py "Player Name" --current-season 2024-25
  python Public_Narrative_Stats.py "Player Name" --season-override 2017-18
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Optional

sys.stdout.reconfigure(encoding="utf-8")

from eval_window import determine_evaluation_window, format_window  # noqa: E402
from config import SCRIPTS_DIR  # noqa: E402


# ──────────────────────────────────────────────────────────────────────
# Domain script registry
# ──────────────────────────────────────────────────────────────────────

DOMAIN_SCRIPTS = [
    ("Domain_1_Finishing__Stats.py",   "finishing_output.json",   "Finishing"),
    ("Domain_2_Shooting__Stats.py",    "shooting_output.json",    "Shooting"),
    ("Domain_3_Ball_Skills__Stats.py", "ball_skills_output.json", "Ball Skills"),
    ("Domain_4_Playmaking__Stats.py",  "playmaking_output.json",  "Playmaking"),
    ("Domain_5_Defense__Stats.py",     "defense_output.json",     "Defense"),
    ("Domain_6_Rebounding__Stats.py",  "rebounding_output.json",  "Rebounding"),
    ("Domain_8_IQ_Motor__Stats.py",    "iq_motor_output.json",    "IQ / Motor"),
]


# ──────────────────────────────────────────────────────────────────────
# Subprocess orchestration
# ──────────────────────────────────────────────────────────────────────

def run_domain(player: str, script: str, current_season: Optional[str],
               season_override: Optional[str]) -> tuple[str, int, str]:
    """Spawn a domain script for the player. Returns (script, returncode, stderr_tail)."""
    cmd = [sys.executable, os.path.join(SCRIPTS_DIR, script), player]
    if current_season:
        cmd += ["--current-season", current_season]
    if season_override:
        cmd += ["--season-override", season_override]
    try:
        result = subprocess.run(
            cmd, cwd=SCRIPTS_DIR, capture_output=True, text=True, timeout=600
        )
        tail = (result.stderr or "").strip().splitlines()[-3:]
        return (script, result.returncode, "\n".join(tail))
    except subprocess.TimeoutExpired:
        return (script, -1, "timeout (10 min)")
    except Exception as exc:
        return (script, -1, str(exc))


def run_all_domains(player: str, current_season: Optional[str],
                    season_override: Optional[str]) -> dict:
    """Run all 7 domain scripts in parallel. Returns {script: (returncode, stderr_tail)}."""
    print(f"Running {len(DOMAIN_SCRIPTS)} domain scripts in parallel...", file=sys.stderr)
    results: dict[str, tuple[int, str]] = {}
    with ThreadPoolExecutor(max_workers=len(DOMAIN_SCRIPTS)) as ex:
        futures = {
            ex.submit(run_domain, player, script, current_season, season_override): script
            for script, _, _ in DOMAIN_SCRIPTS
        }
        for fut in as_completed(futures):
            script, rc, tail = fut.result()
            results[script] = (rc, tail)
            status = "ok" if rc == 0 else f"FAIL (rc={rc})"
            print(f"  {script}: {status}", file=sys.stderr)
            if rc != 0 and tail:
                print(f"    {tail}", file=sys.stderr)
    return results


def load_domain_output(json_name: str) -> Optional[dict]:
    """Load the JSON written by a domain script. Returns the first profile or None."""
    path = os.path.join(SCRIPTS_DIR, json_name)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return None
    if isinstance(data, list):
        return data[0] if data else None
    if isinstance(data, dict):
        return data
    return None


# ──────────────────────────────────────────────────────────────────────
# Three-view transform
# ──────────────────────────────────────────────────────────────────────

def is_sb_block(d) -> bool:
    """True if the dict matches the sb() shape from domain scripts."""
    return (
        isinstance(d, dict)
        and "current" in d
        and "prior" in d
        and "weighted" in d
    )


def _to_float(v):
    if v is None or v == "N/A":
        return None
    try:
        f = float(v)
        if f != f:  # NaN
            return None
        return f
    except (ValueError, TypeError):
        return None


def transform_block(block: dict, current_season: str, prior_season: Optional[str]) -> dict:
    """Transform a {current, prior, weighted, [volumes]} block to the three-view payload.

    The 60/40 weighted field is dropped. Two-season aggregate is computed via
    sum/sum from the per-season volumes when available — see module docstring
    for the rounding caveat (±1 make per season from reverse-computing makes).
    """
    cur_val = _to_float(block.get("current"))
    pri_val = _to_float(block.get("prior"))
    cur_vol = _to_float(block.get("current_volume"))
    pri_vol = _to_float(block.get("prior_volume"))

    out: dict = {
        "current_season": {
            "season": current_season,
            "value": cur_val,
            "volume": int(cur_vol) if cur_vol is not None else None,
        },
    }

    if prior_season and pri_val is not None:
        out["prior_season"] = {
            "season": prior_season,
            "value": pri_val,
            "volume": int(pri_vol) if pri_vol is not None else None,
        }

        # Two-season aggregate: sum/sum from raw counts.
        # NOTE (Phase C, 2026-05-10): emitted shape slimmed to the four
        # consumer-facing fields. current_count, prior_count, and
        # rounding_caveat were never cited by scout-publish writer or by
        # fact-audit Subagent F; dropped to cut JSON-payload token cost.
        # The ±1-per-season rounding caveat is documented in this script's
        # module docstring + PUBLIC-LANGUAGE-GUIDE.md §9.5.
        if cur_vol is not None and pri_vol is not None and (cur_vol + pri_vol) > 0:
            cur_makes = round(cur_val * cur_vol) if cur_val is not None else 0
            pri_makes = round(pri_val * pri_vol)
            total_makes = cur_makes + pri_makes
            total_vol = cur_vol + pri_vol
            agg = round(total_makes / total_vol, 3) if total_vol > 0 else None
            out["two_season_aggregate"] = {
                "value": agg,
                "raw_count": int(total_vol),
                "since": prior_season,
            }

    return out


def walk_and_transform(node, current_season: str, prior_season: Optional[str], path=()):
    """Recursively walk a domain JSON, replacing sb() blocks with three-view payloads.

    Non-sb dicts are descended; non-sb leaves are passed through unchanged.
    Returns a new structure (does not mutate input).
    """
    if is_sb_block(node):
        return transform_block(node, current_season, prior_season)
    if isinstance(node, dict):
        return {
            k: walk_and_transform(v, current_season, prior_season, path + (k,))
            for k, v in node.items()
        }
    if isinstance(node, list):
        return [
            walk_and_transform(item, current_season, prior_season, path + (i,))
            for i, item in enumerate(node)
        ]
    return node


# ──────────────────────────────────────────────────────────────────────
# Markdown rendering
# ──────────────────────────────────────────────────────────────────────

def fmt_pct(v) -> str:
    if v is None:
        return "—"
    if isinstance(v, (int, float)) and 0 <= v <= 1:
        return f"{v * 100:.1f}%"
    return str(v)


def fmt_count(v) -> str:
    if v is None:
        return "—"
    return str(int(v))


def render_three_view(view: dict) -> str:
    """Render a transformed block as a one-line three-view summary."""
    parts = []
    if "current_season" in view:
        c = view["current_season"]
        parts.append(
            f"current ({c['season']}): {fmt_pct(c['value'])}"
            f"{f' on {fmt_count(c['volume'])}' if c['volume'] is not None else ''}"
        )
    if "prior_season" in view:
        p = view["prior_season"]
        parts.append(
            f"prior ({p['season']}): {fmt_pct(p['value'])}"
            f"{f' on {fmt_count(p['volume'])}' if p['volume'] is not None else ''}"
        )
    if "two_season_aggregate" in view:
        a = view["two_season_aggregate"]
        parts.append(
            f"2-season agg: {fmt_pct(a['value'])} "
            f"({fmt_count(a['raw_count'])} since {a['since']})"
        )
    return " | ".join(parts)


def is_three_view(d) -> bool:
    return (
        isinstance(d, dict)
        and "current_season" in d
        and isinstance(d["current_season"], dict)
        and "season" in d["current_season"]
    )


def render_subdomain(name: str, data) -> list[str]:
    """Render a sub-domain block. Walks one level of metrics, surfacing each."""
    lines = [f"### {name}"]
    if not isinstance(data, dict):
        lines.append(f"  (no data)")
        return lines

    rendered_any = False
    for metric_key, metric_val in data.items():
        if is_three_view(metric_val):
            lines.append(f"- **{metric_key}** — {render_three_view(metric_val)}")
            rendered_any = True
        elif isinstance(metric_val, dict):
            # One level deeper — defender-distance, area splits, etc.
            for sub_k, sub_v in metric_val.items():
                if is_three_view(sub_v):
                    lines.append(
                        f"- **{metric_key} / {sub_k}** — {render_three_view(sub_v)}"
                    )
                    rendered_any = True

    if not rendered_any:
        lines.append("  (no per-season splits captured)")
    return lines


def render_payload_markdown(payload: dict) -> str:
    """Render the full payload as the markdown handoff block for Skill 7 Step 3."""
    lines = [
        "## Public narrative stats — per-season + two-season-aggregate granular splits",
        "",
        f"**Player:** {payload.get('player', '—')}  ",
        f"**Eval window mode:** {payload.get('eval_window', {}).get('mode', '—')}  ",
        f"**Seasons used:** {payload.get('eval_window', {}).get('seasons_label', '—')}  ",
        "",
        "_Use single-season values for narrative anchoring; two-season aggregate "
        "available for context where current sample is thin or trend matters. "
        "Never cite the 60/40 weighted blend — that is the scoring substrate, "
        "not a publishable number (PUBLIC-LANGUAGE-GUIDE §5.3, §8 QC7)._",
        "",
    ]
    for domain_label, subdomains in payload.get("domains", {}).items():
        lines.append(f"## {domain_label}")
        lines.append("")
        if not subdomains:
            lines.append("_No data captured (script failed or returned empty)._")
            lines.append("")
            continue
        for sub_key, sub_val in subdomains.items():
            lines.extend(render_subdomain(sub_key, sub_val))
            lines.append("")
    return "\n".join(lines).rstrip() + "\n"


# ──────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.strip().splitlines()[0])
    parser.add_argument("player", help="Player full name")
    parser.add_argument("--current-season", help="Override current season (e.g. '2024-25')")
    parser.add_argument("--season-override", help="Force a specific season at 100%% weight")
    args = parser.parse_args()

    # Eval window
    try:
        window = determine_evaluation_window(
            player_name=args.player,
            season_override=args.season_override,
            current_season_override=args.current_season,
        )
    except Exception as exc:
        print(f"Error resolving eval window: {exc}", file=sys.stderr)
        return 1

    print(format_window(window), file=sys.stderr)
    print("", file=sys.stderr)

    if window.mode == "INSUFFICIENT_DATA":
        print(f"ERROR: {window.flag_template}", file=sys.stderr)
        return 1

    seasons_used = window.seasons_used
    if not seasons_used:
        print("ERROR: no seasons resolved", file=sys.stderr)
        return 1

    current_season = seasons_used[0][0]
    prior_season = seasons_used[1][0] if len(seasons_used) >= 2 else None
    seasons_label = ", ".join(f"{s} ({w:.2f})" for s, w in seasons_used)

    # Run domain scripts in parallel
    rc_map = run_all_domains(args.player, args.current_season, args.season_override)

    # Load JSONs and transform
    domains_payload: dict = {}
    for script, json_name, label in DOMAIN_SCRIPTS:
        rc, _tail = rc_map.get(script, (-1, ""))
        if rc != 0:
            domains_payload[label] = {}
            continue
        loaded = load_domain_output(json_name)
        if loaded is None:
            domains_payload[label] = {}
            continue
        # Each loaded profile contains subdomain_X_* keys (and metadata keys)
        sub_views: dict = {}
        for k, v in loaded.items():
            if not k.startswith("subdomain_"):
                continue
            sub_views[k] = walk_and_transform(v, current_season, prior_season)
        domains_payload[label] = sub_views

    # NOTE (Phase C, 2026-05-10): payload shape slimmed for token-cost
    # reduction. seasons_used drops the per-season scoring weight (the 60/40
    # blend is the scoring substrate, not a public surface value per
    # PUBLIC-LANGUAGE-GUIDE §5.3, §8 QC7). eval_window.flag_template was
    # never cited by scout-publish writer or by fact-audit's Subagent F.
    # seasons_label preserved because render_payload_markdown surfaces it
    # in the markdown handoff header.
    payload = {
        "player": args.player,
        "eval_window": {
            "mode": window.mode,
            "seasons_used": [{"season": s} for s, _ in seasons_used],
            "seasons_label": seasons_label,
        },
        "domains": domains_payload,
    }

    # ── stdout: markdown handoff block ──
    print(render_payload_markdown(payload))

    # ── file: structured JSON ──
    save_path = os.path.join(SCRIPTS_DIR, "public_narrative_stats_output.json")
    with open(save_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, default=str)
    print(f"\nStructured payload saved to {save_path}", file=sys.stderr)

    # Surface failures explicitly
    failed = [s for s, (rc, _) in rc_map.items() if rc != 0]
    if failed:
        print(
            f"\nWARNING: {len(failed)} domain script(s) failed; payload incomplete: "
            f"{', '.join(failed)}",
            file=sys.stderr,
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
