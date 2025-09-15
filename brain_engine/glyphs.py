from enum import Enum


class Glyph(str, Enum):
    PHASE = "ψ"
    RECURSE = "⥁"
    MIRROR = "🪞"
    ANCHOR = "⧫"
    VOL = "🜃"
    LIQ = "🜄"


class Motif(str, Enum):
    COLLAPSE_WARNING_DISTORT = "collapse_warning::distort"
    REVERSAL_CLEAN = "reversal::clean"
    VOLATILITY_SURGE_TEXTURE = "volatility_surge::texture"
    STABILIZATION_DRONE = "stabilization::drone"
