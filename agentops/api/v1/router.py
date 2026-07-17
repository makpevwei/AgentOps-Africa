from fastapi import APIRouter

from agentops.api.v1.endpoints.health import router as health_router
from agentops.api.v1.endpoints.research import router as research_router
from agentops.api.v1.endpoints.chat import router as chat_router

api_router = APIRouter()

api_router.include_router(
    health_router,
    tags=["Health"],
)

api_router.include_router(
    research_router,
    tags=["Research"],
)

api_router.include_router(
    chat_router,
    tags=["Chat"],
)