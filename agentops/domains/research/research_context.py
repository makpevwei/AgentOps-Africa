"""
Research Context

Represents everything collected during a research session.

A ResearchContext is the central object exchanged
between the Research Engine, AI Agents, and
Report Builders.
"""

from pydantic import BaseModel, Field

from agentops.domains.research.finance_snapshot import FinanceSnapshot
from agentops.domains.companies.models import CompanyProfile


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

    # AI-generated analysis (to be added later)
    research: list = Field(default_factory=list)

    # Additional metadata
    metadata: dict = Field(default_factory=dict)