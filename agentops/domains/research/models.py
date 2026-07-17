"""
Research Domain Models

These models define the business objects used by the
Research Engine.

Nothing here depends on LangChain, DeepAgents,
OpenAI, Tavily, or any external API.
"""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field


class ResearchResult(BaseModel):
    """
    Represents ONE research finding from a source.
    """

    source: str

    title: str

    summary: str

    url: str | None = None

    confidence: float = Field(default=1.0, ge=0, le=1)

    metadata: dict[str, Any] = Field(default_factory=dict)


class ResearchReport(BaseModel):
    """
    Final research report produced by the engine.
    """

    query: str

    created_at: datetime = Field(default_factory=datetime.utcnow)

    summary: str = ""

    findings: list[ResearchResult] = Field(default_factory=list)

    recommendations: list[str] = Field(default_factory=list)

    confidence: float = 0.0