def clause_truth_table(motif: str) -> dict[str, bool]:
    # Minimal illustrative mapping; extend as you formalize
    table = {
        "collapse_warning::distort": {"np_wall": True, "no_recovery": True, "sat_shape": False},
        "reversal::clean": {"np_wall": False, "no_recovery": False, "sat_shape": True},
        "volatility_surge::texture": {"np_wall": True, "no_recovery": False, "sat_shape": False},
        "stabilization::drone": {"np_wall": False, "no_recovery": True, "sat_shape": True},
    }
    return table.get(motif, {"np_wall": False, "no_recovery": False, "sat_shape": False})


def to_cnf(motifs: list[str]) -> tuple[int, list[list[int]]]:  # DIMACS-ish stub
    # Encode booleans as variables: 1=np_wall, 2=no_recovery, 3=sat_shape
    # Build CNF from motif votes (very simplified)
    votes = {"np_wall": 0, "no_recovery": 0, "sat_shape": 0}
    for m in motifs:
        tbl = clause_truth_table(m)
        for k, v in tbl.items():
            votes[k] += 1 if v else -1
    # Majority vote -> unit clauses
    clauses: list[list[int]] = []
    clauses.append([1 if votes["np_wall"] >= 0 else -1])
    clauses.append([2 if votes["no_recovery"] >= 0 else -2])
    clauses.append([3 if votes["sat_shape"] >= 0 else -3])
    return 3, clauses
