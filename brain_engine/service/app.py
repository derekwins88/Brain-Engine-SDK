from fastapi import FastAPI
from prometheus_client import CONTENT_TYPE_LATEST, Counter, generate_latest
from starlette.responses import Response

app = FastAPI(title="Brain-Engine Service", version="0.1.0")

CAPSULES_EMITTED = Counter("capsules_emitted_total", "Number of capsules emitted")


@app.get("/healthz")
def healthz() -> dict[str, bool]:
    return {"ok": True}


@app.get("/metrics")
def metrics() -> Response:
    data = generate_latest()
    return Response(content=data, media_type=CONTENT_TYPE_LATEST)


@app.post("/emit")
def emit_capsule() -> dict[str, str]:
    CAPSULES_EMITTED.inc()
    return {"status": "ok"}
