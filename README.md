# Brain-Engine SDK (Day-1)

A minimal, reproducible core for your IMM stack:
- **Glyphs & Motifs**: canonical enums / structs
- **Capsules**: JSON/NDJSON schema for logging runs
- **Translator Bridges**: Clause⇌Logic (CNF) + Entropy⇌Complexity (ΔΦ gates)
- **Service**: FastAPI app with `/healthz` and Prometheus `/metrics`
- **CI**: ruff + mypy + pytest + artifact upload (sample capsules)

## Quickstart

```bash
uv venv && source .venv/bin/activate  # or python -m venv
pip install -e .[dev]
pre-commit install
python demo.py
uvicorn brain_engine.service.app:app --reload

Open metrics at: http://127.0.0.1:8000/metrics

What’s here
•brain_engine/glyphs.py — glyph & motif primitives
•brain_engine/capsule.py — dataclasses + validators
•brain_engine/emit.py — JSON/NDJSON emit helpers
•brain_engine/bridges/ — Clause⇌Logic mapper + ΔΦ classifiers
•brain_engine/service/app.py — FastAPI + Prometheus counters
•demo.py — emits a capsule and prints it

Next (Week-2 hints)
•add --export-lean & --export-tex in a proof/ module
•add resonance_deck.py PNG wave + CSV states
•add quantum/qubo_exporter.py stub + adapter interface

## Day-2: Proof exporters + Resonance Deck

### Proof exporters
- `brain_engine/proof/export_lean.py` emits a minimal Lean4 skeleton from a Capsule.
- `brain_engine/proof/export_tex.py` emits a LaTeX draft page.
- `brain_engine/proof/entropy_collapse_bridge.py` converts motif votes → SAT-ish shape and ∆Φ gates.

Run:
```bash
python demo_day2.py --proof
```

Artifacts: docs/proof_lean_sketch.lean, docs/proof_draft.tex

### Resonance Deck
- `brain_engine/resonance/resonance_deck.py` plots ∆Φ waveform and writes a CSV of entropy states.

Run:
```bash
python demo_day2.py --resonance
```

Artifacts: docs/resonance_wave.png, docs/resonance_states.csv

CI uploads the PNG/CSV/Lean/TeX as artifacts on every push.

## Day-4: Minisat + HTML Report
- CI installs minisat on Linux; runner gracefully falls back if not present.
- `demo_day4.py` writes `docs/report.html` (embeds PNG + links CNF/TeX/Lean/CSV).
- Artifacts uploaded separately for each Python version so uploads never clash.

## Day-5: Unified Builder + Report JSON + Lean seed
- `be build all --out docs` writes all artifacts (PNG/CSV/CNF/Lean/TeX/QUBO/HTML/JSON).
- CI runs the unified builder and uploads artifacts with unique names per Py version.
- Lean project seed added under `lean/` for local math work (CI does not compile Lean yet).
