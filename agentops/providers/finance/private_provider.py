"""
Private Company Finance Provider

Used for companies that are not publicly listed.

Examples:
- Flutterwave
- Moniepoint
- Interswitch
- Andela
- Paystack
"""

from agentops.domains.finance.finance_snapshot import FinanceSnapshot
from agentops.domains.companies.models import CompanyProfile
from agentops.providers.finance.base_provider import BaseFinanceProvider


class PrivateCompanyProvider(BaseFinanceProvider):
    """
    Provider for private companies.

    Since private companies have no public market data,
    we return an empty FinanceSnapshot for now.
    """

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:

        return FinanceSnapshot()