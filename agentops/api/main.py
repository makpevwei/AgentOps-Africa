from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from agentops.api.v1.router import api_router
from agentops.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("🚀 Starting AgentOps Enterprise API...")
    yield
    logger.info("🛑 Shutting down AgentOps Enterprise API...")


app = FastAPI(
    title="AfriAgent Studio API",
    description="Enterprise AI Workspace for Research, Business Analysis, Proposal Writing, and AI Assistants.",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
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
async def root():
    return {
        "name": "AfriAgent Studio API",
        "version": "1.0.0",
        "status": "running",
        "docs": "/docs",
    }
