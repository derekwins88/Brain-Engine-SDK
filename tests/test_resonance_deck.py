from pathlib import Path

from brain_engine.resonance import render_resonance_wave, write_states_csv


def test_resonance_outputs(tmp_path: Path) -> None:
    series = [0.01, 0.5, 0.9]
    png = render_resonance_wave(series, tmp_path / "wave.png")
    csv = write_states_csv(series, tmp_path / "states.csv")
    assert png.exists()
    assert csv.exists()
    assert csv.read_text(encoding="utf-8").count("\n") >= 3  # header + 3 rows
