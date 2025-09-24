import os
from contextlib import asynccontextmanager
from logging import getLogger

from fastapi import FastAPI
from fastapi.responses import StreamingResponse
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

from .error import init_error_handlers
from .middleware import init_middleware

logger = getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info(f"Server running on port {os.getenv('BL_SERVER_PORT', 80)}")
    yield
    logger.info("Server shutting down")


app = FastAPI(lifespan=lifespan)

@app.post("/")
async def handle_request():
    return StreamingResponse("Hello World", media_type="text/event-stream")

init_error_handlers(app)
init_middleware(app)


FastAPIInstrumentor.instrument_app(app, exclude_spans=["receive", "send"])
