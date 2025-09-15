from __future__ import annotations


def _votes(motifs: list[str]) -> dict[str, int]:
    table: dict[str, dict[str, bool]] = {
        "collapse_warning::distort": {"np_wall": True,  "no_recovery": True,  "sat_shape": False},
        "reversal::clean":           {"np_wall": False, "no_recovery": False, "sat_shape": True},
        "volatility_surge::texture": {"np_wall": True,  "no_recovery": False, "sat_shape": False},
        "stabilization::drone":      {"np_wall": False, "no_recovery": True,  "sat_shape": True},
    }
    v = {"np_wall": 0, "no_recovery": 0, "sat_shape": 0}
    for m in motifs:
        row = table.get(m, {"np_wall": False, "no_recovery": False, "sat_shape": False})
        for k, b in row.items():
            v[k] += (1 if b else -1)
    return v


def sat_shape_from_motifs(motifs: list[str]) -> bool:
    """Return a crude SAT-ish shape by motif voting."""
    v = _votes(motifs)
    return v["sat_shape"] >= 0


def gates_from_delta_phi(
    delta: list[float],
    *,
    thr: float = 0.045,
    recov_window: int = 8,
) -> tuple[bool, bool]:
    """Return (np_wall, no_recovery)."""
    if not delta:
        return (False, False)
    np_wall = max(delta) > thr
    last_spike = max((i for i, x in enumerate(delta) if x > thr), default=-1)
    if last_spike < 0:
        return (np_wall, False)
    tail = delta[last_spike + 1 : last_spike + 1 + recov_window]
    no_recovery = bool(tail) and all(x > thr for x in tail)
    return (np_wall, no_recovery)
