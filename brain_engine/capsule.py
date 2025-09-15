from __future__ import annotations

import json
import uuid
from dataclasses import asdict, dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class Capsule:
    capsule_id: str
    schema_version: str
    claim: str
    delta_phi_series: list[float]
    motifs: list[str]
    metadata: dict[str, Any] = field(default_factory=dict)
    created_at: str = field(
        default_factory=lambda: datetime.utcnow().isoformat(timespec="seconds") + "Z"
    )

    @staticmethod
    def new(
        motifs: list[str],
        delta_phi_series: list[float],
        claim: str = "OPEN",
        schema_version: str = "capsule-1.0.0",
        meta: dict[str, Any] | None = None,
    ) -> Capsule:
        cid = f"CAP-{uuid.uuid4().hex[:12]}"
        return Capsule(
            capsule_id=cid,
            schema_version=schema_version,
            claim=claim,
            delta_phi_series=delta_phi_series,
            motifs=motifs,
            metadata=meta or {},
        )

    def to_json(self) -> str:
        return json.dumps(asdict(self), ensure_ascii=False)

    def to_ndjson_line(self) -> str:
        return self.to_json()

    def pde_strength(self) -> float:
        # toy PDE metric: Σ|clause| × 0.044 analogous stub
        return round(sum(abs(x) for x in self.delta_phi_series) * 0.044, 6)
