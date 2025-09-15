from __future__ import annotations

from collections.abc import Iterable
from pathlib import Path

from .capsule import Capsule


def write_json(path: str | Path, capsule: Capsule) -> Path:
    p = Path(path)
    p.write_text(capsule.to_json(), encoding="utf-8")
    return p


def append_ndjson(path: str | Path, capsules: Iterable[Capsule]) -> Path:
    p = Path(path)
    p.parent.mkdir(parents=True, exist_ok=True)
    with p.open("a", encoding="utf-8") as f:
        for c in capsules:
            f.write(c.to_ndjson_line() + "\n")
    return p
