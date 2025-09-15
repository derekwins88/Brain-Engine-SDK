from __future__ import annotations

from .entropy_collapse_bridge import gates_from_delta_phi, sat_shape_from_motifs
from .export_lean import lean_from_capsule
from .export_tex import tex_from_capsule


def dimacs_from_cnf(n: int, cnf: list[list[int]]) -> str:
    lines = [f"p cnf {n} {len(cnf)}"]
    for clause in cnf:
        lines.append(" ".join(str(lit) for lit in clause) + " 0")
    return "\n".join(lines) + "\n"


def minisat_run_stub(n: int, cnf: list[list[int]]) -> tuple[bool, str]:
    # Treat presence of an empty clause as unsatisfiable; otherwise SAT.
    unsat = any(len(clause) == 0 for clause in cnf)
    return (not unsat), "stub"

__all__ = [
    "gates_from_delta_phi",
    "sat_shape_from_motifs",
    "lean_from_capsule",
    "tex_from_capsule",
    "dimacs_from_cnf",
    "minisat_run_stub",
]
