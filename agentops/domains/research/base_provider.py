"""
Base interface for all Research Providers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.research.research_models import ResearchResult


class BaseResearchProvider(ABC):
    """
    Contract implemented by every Research Provider.
    """

    name: str

    @abstractmethod
    def supports(
        self,
        company: CompanyProfile,
    ) -> bool:
        """
        Return True if this provider can research the company.
        """
        raise NotImplementedError

    @abstractmethod
    def research(
        self,
        company: CompanyProfile,
    ) -> ResearchResult:
        """
        Perform research and return structured results.
        """
        raise NotImplementedError
