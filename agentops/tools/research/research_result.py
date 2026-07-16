from pydantic import BaseModel, Field
from typing import Optional


class ResearchResult(BaseModel):
    """
    Standard research object used across the entire AgentOps Africa platform.

    Every research tool should return this model so that
    DeepAgents can reason over a consistent structure.
    """

    source: str = Field(
        description="The origin of the information."
    )

    title: str = Field(
        description="Short descriptive title."
    )

    summary: str = Field(
        description="Concise summary of the findings."
    )

    url: Optional[str] = Field(
        default=None,
        description="Original source URL."
    )

    confidence: float = Field(
        default=1.0,
        ge=0.0,
        le=1.0,
        description="Confidence score between 0 and 1."
    )

    metadata: dict = Field(
        default_factory=dict,
        description="Additional structured information."
    )