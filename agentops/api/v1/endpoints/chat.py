"""
Chat Endpoint
"""

from fastapi import APIRouter, HTTPException

from agentops.api.schemas.chat import (
    ChatRequest,
    ChatResponse,
)
from agentops.core.logger import logger
from agentops.domains.agents.agent_service import AgentService

router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)

service = AgentService()


@router.post(
    "",
    response_model=ChatResponse,
    summary="Chat with the AI Assistant",
)
async def chat(
    request: ChatRequest,
) -> ChatResponse:
    """
    Process a user message using the AgentOps workflow runtime.
    """

    try:
        response = service.chat(request.message)

        return ChatResponse(
            workflow_id="temp",
            workflow_name="Workflow",
            planner="runtime",
            status="completed",
            message=response.message,
            result=response.data,
        )

    except Exception as ex:
        logger.exception("Chat endpoint failed")

        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        ) from ex