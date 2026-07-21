"""
Common result model returned by every AI agent.
"""

from typing import Any

from pydantic import BaseModel, Field


class AgentResult(BaseModel):
    """
    Standard response from any AI worker.
    """

    success: bool = True
    agent: str
    message: str
    data: Any | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)