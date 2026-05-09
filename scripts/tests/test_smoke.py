r"""
test_smoke.py — Phase 5 regression guard for the data pipeline.

What this catches:
  * a refactor breaking JSON output shape (missing keys, renamed fields)
  * a script silently writing an empty / malformed file
  * a key numerical signal disappearing (None where a number was expected)
  * meaningful drift from a saved baseline (default tolerance ±10% to absorb
    NBA stat drift across days as more games are played)

What this DOES NOT do:
  * run the domain scripts itself — separate concern, use run_eval.ps1 first
  * assert exact values — those move when the underlying NBA data updates

Workflow:
  1. From a clean state, run:        .\scripts\run_eval.ps1 "Myles Turner"
  2. Capture the baseline:           python scripts/tests/test_smoke.py --snapshot
  3. After any refactor, re-run:     .\scripts\run_eval.ps1 "Myles Turner"
                                     python scripts/tests/test_smoke.py
     If shape or key numbers drifted unexpectedly the test fails loudly.

Default fixture player is Myles Turner. Override via env var BBSCOUT_SMOKE_PLAYER
or CLI flag --player.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path

# Allow `python scripts/tests/test_smoke.py` to import config.py from scripts/.
HERE = Path(__file__).resolve().parent
SCRIPTS_DIR = HERE.parent
sys.path.insert(0, str(SCRIPTS_DIR))

from config import SCRIPTS_DIR as CONFIG_SCRIPTS_DIR  # noqa: E402

SNAPSHOT_PATH = HERE / "smoke_snapshot.json"
DEFAULT_PLAYER = os.environ.get("BBSCOUT_SMOKE_PLAYER", "Myles Turner")
DEFAULT_TOLERANCE = 0.10  # ±10% on baseline values

# Per-output expected shape and key numerical fingerprints we want to lock in.
# `path` describes how to drill into the JSON to reach a numeric value:
# a list of either str (dict key) or int (list index).
# Most domain scripts emit a list of profile dicts → first profile is at [0].
# Domain 8 emits a dict keyed by player name → drilled in via [PLAYER_NAME].
CHECKS = [
    {
        "label": "Domain 1 — Finishing",
        "file": "finishing_output.json",
        "kind": "list",
        "required_top_keys": [
            "player", "evaluation_window",
            "subdomain_1_at_basket_finishing",
            "subdomain_2_contact_finishing",
            "subdomain_3_post_offense",
        ],
        "fingerprints": [
            ["subdomain_1_at_basket_finishing", "rim_fg_pct"],
            ["subdomain_2_contact_finishing", "ftr"],
            ["subdomain_3_post_offense", "post_ppp"],
        ],
    },
    {
        "label": "Domain 2 — Shooting",
        "file": "shooting_output.json",
        "kind": "list",
        "required_top_keys": [
            "player", "evaluation_window",
            "subdomain_4_cas_3pt", "subdomain_5_off_dribble",
            "subdomain_6_midrange", "subdomain_7_ft",
        ],
        "fingerprints": [
            ["subdomain_4_cas_3pt"],
            ["subdomain_7_ft"],
        ],
    },
    {
        "label": "Domain 3 — Ball Skills",
        "file": "ball_skills_output.json",
        "kind": "list",
        "required_top_keys": [
            "player", "evaluation_window",
            "subdomain_8_handling_creation",
            "subdomain_9_touch_feel",
            "subdomain_10_ball_security",
        ],
        "fingerprints": [
            ["subdomain_8_handling_creation"],
        ],
    },
    {
        "label": "Domain 4 — Playmaking",
        "file": "playmaking_output.json",
        "kind": "list",
        "required_top_keys": [
            "player", "evaluation_window",
            "subdomain_11_court_vision",
            "subdomain_12_decision_making",
            "subdomain_13_passing_execution",
            "subdomain_14_off_ball_movement",
        ],
        "fingerprints": [
            ["subdomain_11_court_vision"],
            ["subdomain_12_decision_making"],
        ],
    },
    {
        "label": "Domain 5 — Defense",
        "file": "defense_output.json",
        "kind": "list",
        "required_top_keys": [
            "player", "evaluation_window",
            "subdomain_15_on_ball_pressure",
            "subdomain_16_help_defense",
            "subdomain_17_rim_protection",
            "subdomain_18_post_defense",
        ],
        "fingerprints": [
            ["subdomain_15_on_ball_pressure"],
            ["subdomain_17_rim_protection"],
        ],
    },
    {
        "label": "Domain 6 — Rebounding",
        "file": "rebounding_output.json",
        "kind": "list",
        "required_top_keys": [
            "player", "evaluation_window", "seasons", "weighted",
        ],
        "fingerprints": [
            ["weighted"],
        ],
    },
    {
        "label": "Domain 8 — IQ / Motor",
        "file": "iq_motor_output.json",
        "kind": "dict_by_player",
        "required_top_keys": [
            "player_name", "player_id", "evaluation_window",
        ],
        "fingerprints": [
            ["evaluation_window", "mode"],  # string sentinel — always present
        ],
    },
]


def _drill(obj, path):
    """Walk a dotted path into a nested JSON object, returning None if any
    step is missing rather than raising — callers decide what missing means."""
    cur = obj
    for step in path:
        if cur is None:
            return None
        try:
            cur = cur[step]
        except (KeyError, IndexError, TypeError):
            return None
    return cur


def _first_numeric(obj):
    """Return the first numeric leaf reached by a depth-first walk, else None.
    Used as a low-bar smell test for fingerprints that point at a sub-block
    rather than a single number."""
    if isinstance(obj, (int, float)) and not isinstance(obj, bool):
        return float(obj)
    if isinstance(obj, dict):
        for v in obj.values():
            r = _first_numeric(v)
            if r is not None:
                return r
    if isinstance(obj, list):
        for v in obj:
            r = _first_numeric(v)
            if r is not None:
                return r
    return None


def _select_profile(payload, kind, player):
    """Domain 1–6 emit a list of profiles → take the first whose `player`
    field matches (so a stale fixture from a different player is caught).
    Domain 8 emits a dict keyed by player name → look up by player."""
    if kind == "list":
        if not isinstance(payload, list) or not payload:
            return None
        for prof in payload:
            if isinstance(prof, dict) and prof.get("player") == player:
                return prof
        return None
    if kind == "dict_by_player":
        if not isinstance(payload, dict):
            return None
        return payload.get(player)
    raise ValueError(f"unknown kind: {kind}")


class CheckFailure(Exception):
    pass


def run_checks(player: str, tolerance: float, snapshot_data: dict | None):
    """Returns (failures: list[str], captured: dict).

    `captured` is the new snapshot payload — written to disk only when
    --snapshot was requested. Always built so we can show drift either way.
    """
    failures: list[str] = []
    captured: dict = {"player": player, "fingerprints": {}}

    for check in CHECKS:
        path = CONFIG_SCRIPTS_DIR / check["file"]
        label = check["label"]

        if not path.exists():
            failures.append(f"[{label}] missing output file: {check['file']}")
            continue

        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            failures.append(f"[{label}] JSON parse error in {check['file']}: {e}")
            continue

        profile = _select_profile(payload, check["kind"], player)
        if profile is None:
            failures.append(
                f"[{label}] could not locate profile in {check['file']} "
                f"(kind={check['kind']}, player={player!r}). "
                f"Did you run run_eval.ps1 against the same player?"
            )
            continue

        # Top-level key shape check.
        missing_keys = [k for k in check["required_top_keys"] if k not in profile]
        if missing_keys:
            failures.append(
                f"[{label}] missing top-level keys in profile: {missing_keys}"
            )

        # Fingerprint capture + comparison.
        for fp_path in check["fingerprints"]:
            value = _drill(profile, fp_path)
            numeric = value if isinstance(value, (int, float)) and not isinstance(value, bool) else _first_numeric(value)
            fp_key = f"{check['file']}::" + ".".join(str(p) for p in fp_path)
            captured["fingerprints"][fp_key] = numeric

            if value is None:
                failures.append(f"[{label}] fingerprint missing: {fp_key}")
                continue

            if numeric is None:
                # Non-numeric leaf (e.g. a string mode like 'TWO_SEASON') — only
                # check it's truthy so we don't lose the smoke value.
                if not value:
                    failures.append(f"[{label}] fingerprint empty: {fp_key}")
                continue

            if snapshot_data:
                baseline = snapshot_data.get("fingerprints", {}).get(fp_key)
                if baseline is None:
                    # Snapshot exists but doesn't have this key — likely a new
                    # fingerprint added after baseline. Surface as a soft note,
                    # not a failure.
                    print(f"  note: no baseline for {fp_key} (new since snapshot)")
                    continue
                if baseline == 0:
                    if abs(numeric) > tolerance:
                        failures.append(
                            f"[{label}] {fp_key}: baseline=0, current={numeric:.4f} "
                            f"(>±{tolerance})"
                        )
                    continue
                drift = abs(numeric - baseline) / abs(baseline)
                if drift > tolerance:
                    failures.append(
                        f"[{label}] {fp_key}: drift {drift*100:.1f}% "
                        f"(baseline={baseline}, current={numeric}, tol=±{tolerance*100:.0f}%)"
                    )

    return failures, captured


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--player", default=DEFAULT_PLAYER,
                        help=f"Fixture player (default: {DEFAULT_PLAYER!r}; "
                             f"override via env BBSCOUT_SMOKE_PLAYER)")
    parser.add_argument("--snapshot", action="store_true",
                        help="Capture current outputs as the new baseline snapshot.")
    parser.add_argument("--tolerance", type=float, default=DEFAULT_TOLERANCE,
                        help=f"Numeric drift tolerance vs snapshot (default {DEFAULT_TOLERANCE}).")
    args = parser.parse_args()

    print(f"smoke test — player={args.player!r}, scripts dir={CONFIG_SCRIPTS_DIR}")
    print(f"snapshot: {SNAPSHOT_PATH}")
    print()

    snapshot_data = None
    if SNAPSHOT_PATH.exists() and not args.snapshot:
        snapshot_data = json.loads(SNAPSHOT_PATH.read_text(encoding="utf-8"))
        if snapshot_data.get("player") != args.player:
            print(f"WARNING: snapshot was taken for {snapshot_data.get('player')!r} "
                  f"but you're testing {args.player!r}. Skipping numeric drift checks.")
            snapshot_data = None

    failures, captured = run_checks(args.player, args.tolerance, snapshot_data)

    if args.snapshot:
        SNAPSHOT_PATH.write_text(json.dumps(captured, indent=2), encoding="utf-8")
        print(f"snapshot written: {SNAPSHOT_PATH}")
        print(f"  {len(captured['fingerprints'])} fingerprint(s) recorded")
        if failures:
            print()
            print(f"Note: {len(failures)} shape/data issue(s) recorded alongside the snapshot:")
            for f in failures:
                print(f"  - {f}")
            sys.exit(1)
        sys.exit(0)

    if failures:
        print(f"FAIL — {len(failures)} issue(s):")
        for f in failures:
            print(f"  - {f}")
        sys.exit(1)

    fp_count = sum(1 for v in captured["fingerprints"].values() if v is not None)
    print(f"OK — {fp_count} fingerprint(s) checked, no drift beyond ±{args.tolerance*100:.0f}%.")
    sys.exit(0)


if __name__ == "__main__":
    main()
