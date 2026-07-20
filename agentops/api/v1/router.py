from fastapi import APIRouter

from agentops.api.v1.endpoints.auth import router as auth_router
from agentops.api.v1.endpoints.chat import router as chat_router
from agentops.api.v1.endpoints.health import router as health_router
from agentops.api.v1.endpoints.opportunities import (
    router as opportunities_router,
)
from agentops.api.v1.endpoints.research import router as research_router

api_router = APIRouter()

# Health
api_router.include_router(
    health_router,
    tags=["Health"],
)

# AI Chat
api_router.include_router(
    chat_router,
    tags=["Chat"],
)

# Research
api_router.include_router(
    research_router,
    tags=["Research"],
)

# Authentication
api_router.include_router(
    auth_router,
    tags=["Authentication"],
)

# Opportunities
api_router.include_router(
    opportunities_router,
    tags=["Opportunities"],
)
