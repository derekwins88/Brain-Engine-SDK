import argparse
import json
from pathlib import Path

from brain_engine.capsule import Capsule
from brain_engine.proof import (
    gates_from_delta_phi,
    lean_from_capsule,
    sat_shape_from_motifs,
    tex_from_capsule,
)
from brain_engine.resonance import render_resonance_wave, write_states_csv


def sample_series() -> list[float]:
    # toy series with a recursive rise; tweak to test collapse branch
    return [0.02, 0.03, 0.05, 0.12, 0.36, 0.52, 0.61, 0.44, 0.40]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--proof", action="store_true")
    ap.add_argument("--resonance", action="store_true")
    args = ap.parse_args()

    delta = sample_series()
    motifs = ["reversal::clean", "volatility_surge::texture"]

    cap = Capsule.new(motifs=motifs, delta_phi_series=delta, meta={"pde_strength": 0.44})

    Path("docs").mkdir(exist_ok=True)
    Path("capsules").mkdir(exist_ok=True)
    (Path("capsules") / "day2_capsule.json").write_text(cap.to_json(), encoding="utf-8")

    if args.proof:
        np_wall, no_recovery = gates_from_delta_phi(delta, thr=0.045, recov_window=5)
        sat_like = sat_shape_from_motifs(motifs)

        cap.metadata.update({
            "np_wall": np_wall,
            "no_recovery": no_recovery,
            "sat_shape": sat_like,
        })

        lean = lean_from_capsule(json.loads(cap.to_json()))
        tex = tex_from_capsule(json.loads(cap.to_json()))
        Path("docs/proof_lean_sketch.lean").write_text(lean, encoding="utf-8")
        Path("docs/proof_draft.tex").write_text(tex, encoding="utf-8")
        print("Wrote Lean/TeX exporters → docs/")

    if args.resonance:
        render_resonance_wave(delta, "docs/resonance_wave.png")
        write_states_csv(delta, "docs/resonance_states.csv")
        print("Wrote Resonance Deck → docs/")


if __name__ == "__main__":
    main()
