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
