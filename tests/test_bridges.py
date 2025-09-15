from brain_engine.bridges.clause_logic import to_cnf
from brain_engine.bridges.entropy_classifiers import EntropyState, classify_delta_phi


def test_entropy_classifier() -> None:
    assert classify_delta_phi([0.1]) == EntropyState.STABLE
    assert classify_delta_phi([0.5]) == EntropyState.RECURSIVE
    assert classify_delta_phi([0.9]) == EntropyState.COLLAPSE


def test_cnf_stub() -> None:
    vars_n, clauses = to_cnf(["reversal::clean"])
    assert vars_n == 3
    assert len(clauses) == 3
