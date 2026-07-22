"""
Chat API Schemas
"""

from typing import Any

from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
    """
    Chat request payload.
    """

    message: str = Field(
        ...,
        description="User message or prompt.",
        examples=[
            "Analyze MTN Nigeria",
            "Tell me about Flutterwave",
            "Research Dangote Cement",
        ],
    )


class ChatResponse(BaseModel):
    """
    Standard response returned by the AgentOps runtime.
    """

    workflow_id: str = Field(
        ...,
        description="Unique workflow identifier.",
    )

    workflow_name: str = Field(
        ...,
        description="Workflow selected by the planner.",
    )

    planner: str = Field(
        ...,
        description="Planner used to generate the workflow.",
    )

    status: str = Field(
        ...,
        description="Workflow execution status.",
    )

    message: str = Field(
        ...,
        description="Human readable status message.",
    )

    result: Any = Field(
        ...,
        description="Workflow execution result.",
    )