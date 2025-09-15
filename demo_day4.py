from __future__ import annotations

import json
from pathlib import Path

from brain_engine.bridges.clause_logic import to_cnf
from brain_engine.capsule import Capsule
from brain_engine.proof import (
    dimacs_from_cnf,
    have_minisat,
    minisat_run_stub,
    run_minisat_dimacs,
)
from brain_engine.report import build_report
from brain_engine.resonance import render_resonance_wave, write_states_csv


def series() -> list[float]:
    return [0.02, 0.04, 0.48, 0.62, 0.41, 0.37, 0.9]


def main() -> None:
    docs = Path("docs")
    docs.mkdir(exist_ok=True)
    caps = Path("capsules")
    caps.mkdir(exist_ok=True)

    delta = series()
    motifs = ["reversal::clean", "volatility_surge::texture", "stabilization::drone"]
    cap = Capsule.new(motifs=motifs, delta_phi_series=delta, meta={"pde_strength": 0.44})

    # resonance
    render_resonance_wave(delta, docs / "resonance_wave.png")
    write_states_csv(delta, docs / "resonance_states.csv")

    # CNF & stub SAT
    n, cnf = to_cnf(motifs)
    dimacs = dimacs_from_cnf(n, cnf)
    (docs / "proof.cnf").write_text(dimacs, encoding="utf-8")
    sat_stub, prov_stub = minisat_run_stub(n, cnf)
    cap.metadata.update({"sat_stub": sat_stub, "sat_provenance": prov_stub})
    (caps / "day4_capsule.json").write_text(cap.to_json(), encoding="utf-8")

    # real minisat if available
    minisat_sat = "unavailable"
    if have_minisat():
        sat, _ = run_minisat_dimacs(dimacs)
        minisat_sat = "SAT" if sat else "UNSAT"
    build_report(docs, json.loads(cap.to_json()), have_minisat(), minisat_sat)
    print("Day-4 report → docs/report.html")


if __name__ == "__main__":
    main()
