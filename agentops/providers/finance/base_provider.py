"""
Base Finance Provider

Every finance provider must implement this interface.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.provider_result import ProviderResult


class BaseFinanceProvider(ABC):
    """
    Abstract base class for all finance providers.
    """

    name: str = "Unknown"

    @abstractmethod
    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> ProviderResult:
        """
        Retrieve a financial snapshot for a company.
        """
        raise NotImplementedError
