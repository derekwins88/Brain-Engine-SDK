from __future__ import annotations

import shutil
import subprocess
import tempfile
from pathlib import Path
from typing import Any


def have_minisat() -> bool:
    return shutil.which("minisat") is not None


def run_minisat_dimacs(dimacs: str) -> tuple[bool, dict[str, Any]]:
    """
    Runs minisat if available. Returns (is_sat, provenance).
    Falls back to stub-like UNSAT/SAT parsing errors gracefully.
    """
    if not have_minisat():
        return (False, {"mode": "minisat", "binary": None, "error": "not installed"})

    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td)
        cnf = tmp / "input.cnf"
        out = tmp / "result.txt"
        cnf.write_text(dimacs, encoding="utf-8")
        try:
            proc = subprocess.run(
                ["minisat", str(cnf), str(out)],
                capture_output=True,
                text=True,
                timeout=20,
            )
            if out.exists():
                text = out.read_text(encoding="utf-8")
                is_sat = "SAT" in text.splitlines()[0]
            else:
                # some minisat versions write to stdout only
                is_sat = "SATISFIABLE" in proc.stdout
            return (is_sat, {"mode": "minisat", "code": proc.returncode})
        except Exception as e:
            return (False, {"mode": "minisat", "error": repr(e)})
