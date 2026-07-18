"""
Chat Endpoint
"""

from fastapi import APIRouter

from agentops.api.schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from agentops.domains.agents.agent_service import AgentService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

service = AgentService()


@router.post(
    "",
    response_model=ChatResponse,
)
async def chat(
    request: ChatRequest,
) -> ChatResponse:
    """
    Analyze a company and return a structured AI response.
    """

    analysis = service.chat(request.message)

    return ChatResponse(
        response=analysis,
    )
