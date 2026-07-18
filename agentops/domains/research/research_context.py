"""
Research Context

Represents everything collected during a research session.

A ResearchContext is the central object exchanged
between the Research Engine, AI Agents, and
Report Builders.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_snapshot import FinanceSnapshot
from agentops.domains.research.research_models import (
    ResearchResult,
)


class ResearchContext(BaseModel):
    """
    Complete research context for a company.
    """

    # Original user query
    query: str

    # Resolved company profile
    company: CompanyProfile

    # Financial information
    finance: FinanceSnapshot | None = None

    # Research gathered from providers
    research: ResearchResult = Field(
        default_factory=ResearchResult,
    )

    # Additional metadata
    metadata: dict[str, object] = Field(
        default_factory=dict,
    )
