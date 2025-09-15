from brain_engine.capsule import Capsule


def test_capsule_roundtrip() -> None:
    cap = Capsule.new(["stabilization::drone"], [0.01, 0.02])
    js = cap.to_json()
    assert "CAP-" in js
    assert cap.pde_strength() >= 0.0
