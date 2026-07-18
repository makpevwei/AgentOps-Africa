"""
Research Data Model.

Holds all information collected by the Research Agent.
"""

from __future__ import annotations

from pydantic import BaseModel, Field


class ResearchData(BaseModel):
    """
    Structured research collected from external sources.
    """

    company_profile: dict = Field(default_factory=dict)

    news: list[dict] = Field(default_factory=list)

    wikipedia: dict = Field(default_factory=dict)

    web: dict = Field(default_factory=dict)
