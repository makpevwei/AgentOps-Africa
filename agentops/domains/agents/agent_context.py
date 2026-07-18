"""
Agent Runtime Context.

Shared context passed between Agent Services during execution.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from agentops.domains.agents.models.analysis_data import AnalysisData
from agentops.domains.agents.models.research_data import ResearchData
from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_models import FinanceSnapshot


class AgentContext(BaseModel):
    """
    Shared execution context for the Agent Runtime.

    Every Agent Service receives the same context instance and may
    enrich it with additional information for downstream services.
    """

    company: CompanyProfile | None = None

    finance: FinanceSnapshot | None = None

    research: ResearchData = Field(
        default_factory=ResearchData,
    )

    analysis: AnalysisData = Field(
        default_factory=AnalysisData,
    )

    summary: str | None = None
