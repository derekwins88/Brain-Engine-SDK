from __future__ import annotations

import argparse
import json
from pathlib import Path

from brain_engine.bridges.clause_logic import to_cnf
from brain_engine.capsule import Capsule
from brain_engine.proof import (
    dimacs_from_cnf,
    have_minisat,
    lean_from_capsule,
    minisat_run_stub,
    run_minisat_dimacs,
    tex_from_capsule,
)
from brain_engine.quantum import qubo_from_capsule
from brain_engine.report import build_report
from brain_engine.resonance import render_resonance_wave, write_states_csv


def _series() -> list[float]:
    return [0.02, 0.04, 0.48, 0.62, 0.41, 0.37, 0.90]


def _motifs() -> list[str]:
    return ["reversal::clean", "volatility_surge::texture", "stabilization::drone"]


def build_all(out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)
    caps_dir = Path("capsules")
    caps_dir.mkdir(exist_ok=True)

    delta = _series()
    motifs = _motifs()
    cap = Capsule.new(motifs=motifs, delta_phi_series=delta, meta={"pde_strength": 0.44})
    cap_path = caps_dir / "day5_capsule.json"
    cap_path.write_text(cap.to_json(), encoding="utf-8")

    # Resonance
    render_resonance_wave(delta, out_dir / "resonance_wave.png")
    write_states_csv(delta, out_dir / "resonance_states.csv")

    # Proof (CNF + stub + Lean + TeX)
    n, cnf = to_cnf(motifs)
    dimacs = dimacs_from_cnf(n, cnf)
    (out_dir / "proof.cnf").write_text(dimacs, encoding="utf-8")

    sat_stub, prov_stub = minisat_run_stub(n, cnf)
    cap.metadata.update({"sat_stub": sat_stub, "sat_provenance": prov_stub})

    lean = lean_from_capsule(json.loads(cap.to_json()))
    tex = tex_from_capsule(json.loads(cap.to_json()))
    (out_dir / "proof_lean_sketch.lean").write_text(lean, encoding="utf-8")
    (out_dir / "proof_draft.tex").write_text(tex, encoding="utf-8")

    # Minisat (optional)
    minisat_sat = "unavailable"
    if have_minisat():
        sat, _ = run_minisat_dimacs(dimacs)
        minisat_sat = "SAT" if sat else "UNSAT"

    # Quantum toy
    Q, var = qubo_from_capsule(json.loads(cap.to_json()))
    (out_dir / "qubo.json").write_text(
        json.dumps({"Q": {f"{i},{j}": w for (i, j), w in Q.items()}, "var": var}, indent=2),
        encoding="utf-8",
    )

    # HTML + JSON report
    build_report(out_dir, json.loads(cap.to_json()), have_minisat(), minisat_sat)
    (out_dir / "report.json").write_text(
        json.dumps(
            {
                "capsule": json.loads(cap.to_json()),
                "minisat_available": have_minisat(),
                "minisat_sat": minisat_sat,
            },
            indent=2,
        ),
        encoding="utf-8",
    )


def main() -> None:
    ap = argparse.ArgumentParser(prog="be", description="Brain-Engine CLI")
    sp = ap.add_subparsers(dest="cmd")

    b = sp.add_parser("build", help="Build artifacts")
    b.add_argument("target", choices=["all"], help="What to build")
    b.add_argument("--out", default="docs")

    args = ap.parse_args()
    if args.cmd == "build":
        out = Path(args.out)
        if args.target == "all":
            build_all(out)
            print(f"[OK] artifacts in {out}/")
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
