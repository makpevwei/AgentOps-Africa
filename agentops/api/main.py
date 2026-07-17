from fastapi import FastAPI

from agentops.api.v1.router import api_router

app = FastAPI(
    title="AgentOps Enterprise API",
    description="Enterprise AI Platform by Agentic AI Africa",
    version="1.0.0",
)

app.include_router(
    api_router,
    prefix="/api/v1",
)