from fastapi import FastAPI

from src.api.routers.incidents import (
    router as incidents_router,
)

app = FastAPI(
    title="AI Ops Copilot",
)

app.include_router(
    incidents_router,
)