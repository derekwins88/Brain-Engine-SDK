from __future__ import annotations

import csv
from pathlib import Path


# Important: Day-2 constraint → use matplotlib (single plot, no style/colors)
def _state(delta: float, collapse_thr: float = 0.85, recursive_thr: float = 0.45) -> str:
    if delta >= collapse_thr:
        return "collapse"
    if delta >= recursive_thr:
        return "recursive"
    return "stable"


def render_resonance_wave(delta_phi_series: list[float], out_png: str | Path) -> Path:
    """Render a simple waveform of ∆Φ over index."""
    import matplotlib.pyplot as plt  # local import, runtime only
    out = Path(out_png)
    out.parent.mkdir(parents=True, exist_ok=True)

    xs = list(range(len(delta_phi_series)))
    ys = delta_phi_series

    plt.figure()
    plt.plot(xs, ys)  # no explicit colors/styles per constraints
    plt.title("Resonance Wave (∆Φ)")
    plt.xlabel("Index")
    plt.ylabel("Delta Phi")
    plt.savefig(str(out), dpi=160, bbox_inches="tight")
    plt.close()
    return out


def write_states_csv(delta_phi_series: list[float], out_csv: str | Path) -> Path:
    """Write CSV of per-sample entropy states (stable/recursive/collapse)."""
    out = Path(out_csv)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["index", "delta_phi", "state"])
        for i, v in enumerate(delta_phi_series):
            w.writerow([i, f"{v:.6f}", _state(v)])
    return out
