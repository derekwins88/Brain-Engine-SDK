from pathlib import Path

from brain_engine.bridges.clause_logic import to_cnf
from brain_engine.bridges.entropy_classifiers import classify_delta_phi
from brain_engine.capsule import Capsule
from brain_engine.emit import append_ndjson, write_json

delta = [0.02, 0.04, 0.51, 0.72, 0.83]  # toy ∆Φ series
motifs = ["reversal::clean", "volatility_surge::texture"]

cap = Capsule.new(motifs=motifs, delta_phi_series=delta, meta={"source": "demo"})
print("Capsule:", cap.to_json())
print("PDE strength:", cap.pde_strength())
vars_n, cnf = to_cnf(motifs)
print("CNF:", vars_n, cnf)
print("Entropy state:", classify_delta_phi(delta))

Path("capsules").mkdir(exist_ok=True)
write_json("capsules/demo_capsule.json", cap)
append_ndjson("capsules/demo_capsules.ndjson", [cap])
print("Wrote capsules to ./capsules/")
