"""
Base Finance Provider

Defines the contract that every finance provider
(Yahoo, Finnhub, Alpha Vantage, NGX, etc.)
must implement.
"""

from abc import ABC, abstractmethod
from agentops.domains.finance.finance_snapshot import FinanceSnapshot
from agentops.domains.companies.models import CompanyProfile


class BaseFinanceProvider(ABC):
    """
    Abstract base class for all finance providers.
    """

    @abstractmethod
    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:
        """
        Retrieve a complete financial snapshot for a company.

        The implementation should gather everything it can
        from a single provider session and return it as a
        FinanceSnapshot.
        """
        raise NotImplementedError