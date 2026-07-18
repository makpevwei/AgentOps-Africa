"""
Research domain models.

Strongly typed models shared across the Research Domain.
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field


class ResearchProfile(BaseModel):
    """
    Structured company profile information gathered from external
    research providers.
    """

    company_name: str | None = None

    description: str | None = None

    industry: str | None = None

    sector: str | None = None

    website: str | None = None

    headquarters: str | None = None

    founded: int | None = None

    employees: int | None = None

    ceo: str | None = None


class NewsArticle(BaseModel):
    """
    Represents a single news article.
    """

    title: str

    summary: str | None = None

    url: str | None = None

    source: str | None = None

    published_at: datetime | None = None

    sentiment: str | None = None


class ResearchSource(BaseModel):
    """
    Metadata describing where research data originated.
    """

    provider: str

    url: str | None = None

    confidence: float | None = None

    retrieved_at: datetime = Field(
        default_factory=datetime.utcnow,
    )


class ResearchResult(BaseModel):
    """
    Combined research returned by the Research Orchestrator.
    """

    profile: ResearchProfile = Field(
        default_factory=ResearchProfile,
    )

    news: list[NewsArticle] = Field(
        default_factory=list,
    )

    sources: list[ResearchSource] = Field(
        default_factory=list,
    )
