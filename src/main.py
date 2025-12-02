import os
from contextlib import asynccontextmanager
from logging import getLogger

from fastapi import FastAPI, Request
from fastapi.responses import StreamingResponse
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor


logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Server running on port {os.getenv('PORT', 80)}")
    yield
    logger.info("Server shutting down")


app = FastAPI(lifespan=lifespan)

@app.middleware("http")
async def log_request(request: Request, call_next):
    logger.info(f"{request.method} {request.url}")
    response = await call_next(request)
    return response

@app.post("/")
async def handle_request():
    return StreamingResponse("Hello World", media_type="text/event-stream")

FastAPIInstrumentor.instrument_app(app, exclude_spans=["receive", "send"])
