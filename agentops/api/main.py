from fastapi import FastAPI

from agentops.api.routers.health import router as health_router

app = FastAPI(
    title="AgentOps Africa API",
    version="0.1.0",
    description="Enterprise Agentic AI Platform",
)

app.include_router(health_router)