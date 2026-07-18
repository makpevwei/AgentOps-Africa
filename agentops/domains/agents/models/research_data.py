"""
Research Data Model.

Holds all information collected by the Research Agent.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from agentops.domains.research.research_models import ResearchResult


class ResearchData(BaseModel):
    """
    Structured research collected by the Research Domain.
    """

    result: ResearchResult = Field(
        default_factory=ResearchResult,
    )
