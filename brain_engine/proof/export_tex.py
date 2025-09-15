from __future__ import annotations

from html import escape
from typing import Any, cast


def tex_from_capsule(cap: dict[str, Any]) -> str:
    cid = escape(str(cap.get("capsule_id", "CAP-UNKNOWN")))
    claim = escape(str(cap.get("claim", "OPEN")))
    motifs = ", ".join(cast(list[str], cap.get("motifs", [])))
    pde = cap.get("metadata", {}).get("pde_strength", "n/a")

    return r"""\documentclass{article}
\usepackage[margin=1in]{geometry}
\begin{document}
\section*{Entropy Collapse Capsule}
\textbf{Capsule ID}: """ + cid + r"""\\
\textbf{Claim}: """ + claim + r"""\\
\textbf{Motifs}: """ + motifs + r"""\\
\textbf{PDE Strength}: """ + str(pde) + r"""\\

\subsection*{Notes}
This is an auto-generated draft from the Brain-Engine SDK.
Replace with formal analysis once the data constraints are fixed.

\end{document}
"""
