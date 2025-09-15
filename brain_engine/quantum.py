from __future__ import annotations

from typing import Any


def qubo_from_capsule(
    capsule: dict[str, Any],
) -> tuple[dict[tuple[int, int], float], dict[str, int]]:
    """Build a toy QUBO from capsule data.

    The construction is intentionally simple yet deterministic so that the
    exported JSON remains stable for CI artifacts. Each ∆Φ sample maps to a
    binary variable and contributes a diagonal weight; neighbouring samples add a
    small coupling term. Motifs are recorded as named variables to mirror the
    classical pipeline.
    """

    delta = [float(x) for x in capsule.get("delta_phi_series", [])]
    motifs = list(capsule.get("motifs", []))

    Q: dict[tuple[int, int], float] = {}
    for idx, value in enumerate(delta):
        Q[(idx, idx)] = round(value, 6)
        if idx + 1 < len(delta):
            coupling = round(0.5 * value * float(delta[idx + 1]), 6)
            if coupling:
                Q[(idx, idx + 1)] = coupling
                Q[(idx + 1, idx)] = coupling

    var = {motif: i for i, motif in enumerate(motifs)}
    return Q, var
