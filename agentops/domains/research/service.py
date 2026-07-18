"""
Research Service.

Business service responsible for executing company research.
"""

from __future__ import annotations

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.research.orchestrator import (
    ResearchOrchestrator,
)
from agentops.domains.research.research_models import (
    ResearchResult,
)


class ResearchService:
    """
    High-level service for executing company research.
    """

    def __init__(
        self,
        orchestrator: ResearchOrchestrator | None = None,
    ) -> None:
        self.orchestrator = orchestrator or ResearchOrchestrator()

    def research(
        self,
        company: CompanyProfile,
    ) -> ResearchResult:
        """
        Execute research for a company.
        """

        return self.orchestrator.research(company)
