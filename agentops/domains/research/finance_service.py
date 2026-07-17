"""
Enterprise Finance Service

Coordinates all financial data retrieval.

The Finance Service selects the appropriate
provider and returns a complete FinanceSnapshot.
"""

from agentops.domains.research.finance_snapshot import FinanceSnapshot
from agentops.domains.companies.models import CompanyProfile
from agentops.providers.finance.provider_factory import FinanceProviderFactory


class FinanceService:
    """
    Service responsible for retrieving financial data.
    """

    def __init__(self):

        self.factory = FinanceProviderFactory()

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:

        provider = self.factory.create(company)

        return provider.get_snapshot(company)