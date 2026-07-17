"""
NGX Finance Provider

Provider for companies listed on the Nigerian Exchange (NGX).

This is currently a placeholder implementation.
Future versions will retrieve live market data from
an NGX-compatible data source.
"""

from agentops.domains.research.finance_snapshot import FinanceSnapshot
from agentops.domains.research.models import CompanyProfile
from agentops.providers.finance.base_provider import BaseFinanceProvider


class NgxFinanceProvider(BaseFinanceProvider):
    """
    Provider for Nigerian Exchange listed companies.
    """

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:

        # Placeholder until NGX integration is implemented.
        return FinanceSnapshot()