from enum import Enum


class EntropyState(str, Enum):
    STABLE = "stable"
    RECURSIVE = "recursive"
    COLLAPSE = "collapse"


def classify_delta_phi(
    series: list[float], collapse_thr: float = 0.85, recursive_thr: float = 0.45
) -> EntropyState:
    if not series:
        return EntropyState.STABLE
    mx = max(series)
    if mx >= collapse_thr:
        return EntropyState.COLLAPSE
    if mx >= recursive_thr:
        return EntropyState.RECURSIVE
    return EntropyState.STABLE
