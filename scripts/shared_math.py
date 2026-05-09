"""
Shared math + safe-coercion helpers for the domain stat-pipeline scripts.

Single source of truth for the weighting math used across Domain_1 through
Domain_8 stat scripts. Before this module existed, each script defined its
own copies of these helpers with subtly different names (`vol_wt_pct` vs
`vol_wt` vs `volume_weighted_pct`) and constants (`W_CUR` vs `W_CURRENT`).

The sentinel check `_is_missing(prior)` recognises None, the string "N/A",
and numeric 0 as "no prior season data" — the union of every sentinel any
of the previous local copies used. Math is otherwise identical to the
established Domain_1 implementation.

Defaults match the 60/40 recency weighting from S83 (current season 0.60,
prior season 0.40). Callers that derive weights at runtime from
`eval_window` (e.g. Domain_4_Playmaking) should pass `w_cur=` and `w_pri=`
explicitly.
"""

# ──────────────────────────────────────────────────────────────────────
# Default weights (S83: 60/40 current/prior)
# ──────────────────────────────────────────────────────────────────────

W_CURRENT_DEFAULT = 0.60
W_PRIOR_DEFAULT = 0.40


# ──────────────────────────────────────────────────────────────────────
# Internal sentinel detection
# ──────────────────────────────────────────────────────────────────────

def _is_missing(value):
    """True if `value` represents 'no prior-season data' for weighting purposes."""
    return value is None or value == "N/A" or value == 0


# ──────────────────────────────────────────────────────────────────────
# Weighting math
# ──────────────────────────────────────────────────────────────────────

def volume_weighted_pct(cur_made, cur_att, pri_made, pri_att,
                        w_cur=W_CURRENT_DEFAULT, w_pri=W_PRIOR_DEFAULT):
    """
    Volume-weighted percentage for shooting stats (S83 rule 5).
    Weights both numerator and denominator by attempts × season weight,
    then divides. Falls back to single-season percentage when prior is missing.
    """
    if _is_missing(pri_att):
        return round(cur_made / cur_att, 3) if cur_att and cur_att > 0 else 0
    w_made = cur_made * w_cur + pri_made * w_pri
    w_att = cur_att * w_cur + pri_att * w_pri
    return round(w_made / w_att, 3) if w_att > 0 else 0


def simple_weighted(cur_val, pri_val,
                    w_cur=W_CURRENT_DEFAULT, w_pri=W_PRIOR_DEFAULT):
    """
    Simple weighted average for rate stats (S83 rule 6).
    Falls back to current-season-only when prior is missing.
    """
    if _is_missing(pri_val):
        return cur_val
    return round(cur_val * w_cur + pri_val * w_pri, 3)


def stat_block(cur_val, pri_val, cur_vol=None, pri_vol=None, is_rate=False,
               w_cur=W_CURRENT_DEFAULT, w_pri=W_PRIOR_DEFAULT):
    """
    Build a 3-value stat block: current, prior, weighted.
    When `is_rate` is True, prior is weighted via simple_weighted.
    Otherwise, if cur_vol/pri_vol supplied, weighted via volume_weighted_pct.
    """
    if _is_missing(pri_val):
        if cur_vol is not None:
            return {
                "current": cur_val, "prior": "N/A", "weighted": cur_val,
                "current_volume": cur_vol, "prior_volume": "N/A",
                "total_volume": cur_vol,
            }
        return {"current": cur_val, "prior": "N/A", "weighted": cur_val}

    if is_rate:
        weighted = simple_weighted(cur_val, pri_val, w_cur=w_cur, w_pri=w_pri)
    elif cur_vol is not None and pri_vol is not None:
        weighted = volume_weighted_pct(cur_val, cur_vol, pri_val, pri_vol,
                                       w_cur=w_cur, w_pri=w_pri)
    else:
        weighted = simple_weighted(cur_val, pri_val, w_cur=w_cur, w_pri=w_pri)

    block = {"current": cur_val, "prior": pri_val, "weighted": weighted}
    if cur_vol is not None and pri_vol is not None:
        block.update({
            "current_volume": cur_vol,
            "prior_volume": pri_vol,
            "total_volume": cur_vol + pri_vol,
        })
    return block


# ──────────────────────────────────────────────────────────────────────
# Safe coercion helpers (NaN-safe int/float/round)
# ──────────────────────────────────────────────────────────────────────

def safe_int(v):
    """Coerce to int, treating None and NaN as 0."""
    try:
        if v is None or v != v:
            return 0
        return int(v)
    except (ValueError, TypeError):
        return 0


def safe_float(v):
    """Coerce to float, treating None and NaN as 0.0."""
    try:
        if v is None or v != v:
            return 0.0
        return float(v)
    except (ValueError, TypeError):
        return 0.0


def safe_round(v, d=3):
    """Coerce to float and round, treating None and NaN as 0."""
    try:
        if v is None or v != v:
            return 0
        return round(float(v), d)
    except (ValueError, TypeError):
        return 0


def safe_div(num, den, default=0.0):
    """Divide safely; return default on zero / None denominator."""
    if not den or den == 0:
        return default
    try:
        return num / den
    except (TypeError, ZeroDivisionError):
        return default


def safe_get(row, key, default=None):
    """Safely get a value from a row dict / pandas Series."""
    if row is None:
        return default
    try:
        val = row.get(key, default) if hasattr(row, "get") else row[key]
    except (KeyError, IndexError, AttributeError):
        return default
    if val is None:
        return default
    return val


# ──────────────────────────────────────────────────────────────────────
# Short aliases preserved from existing local helpers
# ──────────────────────────────────────────────────────────────────────
# Kept so that scripts using the short forms can import them directly
# without renaming every call site in one pass.

_si = safe_int
_sf = safe_float
_sr = safe_round
