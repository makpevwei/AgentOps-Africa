"""
Finance Provider Factory

Selects the appropriate finance provider.
"""

from agentops.domains.companies.models import CompanyProfile
from agentops.providers.finance.base_provider import BaseFinanceProvider
from agentops.providers.finance.private_provider import PrivateCompanyProvider
from agentops.providers.finance.yahoo_provider import YahooFinanceProvider


class FinanceProviderFactory:
    """
    Factory responsible for selecting the appropriate
    finance provider.
    """

    @staticmethod
    def create(
        company: CompanyProfile,
    ) -> BaseFinanceProvider:
        """
        Select a finance provider.

        Current Strategy
        ----------------
        - Private companies -> PrivateCompanyProvider
        - All listed companies -> YahooFinanceProvider

        NGX-specific provider will be introduced later
        when live NGX integration is implemented.
        """

        if not company.ticker:
            return PrivateCompanyProvider()

        return YahooFinanceProvider()