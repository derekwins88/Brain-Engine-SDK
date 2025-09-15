from __future__ import annotations

import argparse
from pathlib import Path

from brain_engine.bridges.clause_logic import to_cnf
from brain_engine.capsule import Capsule
from brain_engine.proof import dimacs_from_cnf, minisat_run_stub
from brain_engine.resonance import render_resonance_wave, write_states_csv


def main() -> None:
    ap = argparse.ArgumentParser(prog="be", description="Brain-Engine CLI")
    ap.add_argument(
        "--series",
        nargs="*",
        type=float,
        default=[0.02, 0.04, 0.48, 0.62, 0.41, 0.37, 0.9],
    )
    ap.add_argument(
        "--motifs",
        nargs="*",
        default=["reversal::clean", "volatility_surge::texture"],
    )
    ap.add_argument("--out", default="docs")
    args = ap.parse_args()

    delta = list(args.series)
    motifs = list(args.motifs)

    out = Path(args.out)
    out.mkdir(exist_ok=True, parents=True)

    # resonance
    render_resonance_wave(delta, out / "resonance_wave.png")
    write_states_csv(delta, out / "resonance_states.csv")

    # proof (DIMACS + stub)
    n, cnf = to_cnf(motifs)
    (out / "proof.cnf").write_text(dimacs_from_cnf(n, cnf), encoding="utf-8")
    sat, prov = minisat_run_stub(n, cnf)

    cap = Capsule.new(motifs, delta, meta={"sat_stub": sat, "sat_provenance": prov})
    Path("capsules").mkdir(exist_ok=True)
    (Path("capsules") / "cli_capsule.json").write_text(cap.to_json(), encoding="utf-8")

    print(f"[OK] artifacts in {out}/ and capsules/cli_capsule.json")
