import json

from brain_engine.capsule import Capsule
from brain_engine.proof import (
    gates_from_delta_phi,
    lean_from_capsule,
    sat_shape_from_motifs,
    tex_from_capsule,
)


def test_proof_exports_basic() -> None:
    delta = [0.01, 0.02, 0.5]
    motifs = ["reversal::clean"]
    cap = Capsule.new(motifs=motifs, delta_phi_series=delta, meta={"pde_strength": 0.44})
    np_wall, no_rec = gates_from_delta_phi(delta, thr=0.045, recov_window=2)
    assert np_wall is True
    assert no_rec in (True, False)

    sat_like = sat_shape_from_motifs(motifs)
    assert isinstance(sat_like, bool)

    lean = lean_from_capsule(json.loads(cap.to_json()))
    tex = tex_from_capsule(json.loads(cap.to_json()))
    assert "theorem entropy_wall_or_sat_shape" in lean
    assert r"\section*{Entropy Collapse Capsule}" in tex
