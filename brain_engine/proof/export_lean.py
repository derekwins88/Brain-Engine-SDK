from __future__ import annotations

from typing import Any


def lean_from_capsule(cap: dict[str, Any]) -> str:
    """
    Emit a tiny Lean4 sketch capturing verdict shape.
    Not a proof—just a scaffold you can extend with mathlib later.
    """
    cid = cap.get("capsule_id", "CAP-UNKNOWN")
    claim = cap.get("claim", "OPEN")
    _delta = cap.get("delta_phi_series", [])  # retained for future refinements
    motifs = cap.get("motifs", [])
    meta = cap.get("metadata", {})

    return f"""-- Auto-generated sketch from capsule {cid}
-- claim: {claim}
-- motifs: {motifs}
-- pde_strength: {meta.get('pde_strength', 'n/a')}

import Mathlib

/--
Entropy collapse shape scaffold:
- monotone-ish or spike-and-hold indicates SAT or NP wall behavior
- Replace 'admit' with proper lemmas once data constraints are formalized.
--/
theorem entropy_wall_or_sat_shape : Prop := by
  -- outline: examine ∆Φ structure and motif votes (external CSV / JSON)
  admit
"""
