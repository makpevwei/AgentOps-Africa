from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agentops.api.v1.router import api_router
from agentops.core.handlers import register_exception_handlers
from agentops.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan."""

    logger.info("🚀 Starting AgentOps Enterprise API...")
    yield
    logger.info("🛑 Shutting down AgentOps Enterprise API...")


app = FastAPI(
    title="AgentOps Africa API",
    description=(
        "AI Workforce Platform for African Businesses. "
        "Research, Opportunity Management, Proposal Generation, "
        "Executive Assistants, Finance AI Employees and Enterprise Automation."
    ),
    version="0.1.0",
    lifespan=lifespan,
)

# Register global exception handlers
register_exception_handlers(app)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:3001",
        "http://127.0.0.1:3001",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# API Routes
app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    """Root endpoint."""

    return {
        "name": "AfriAgent Studio API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
    }
