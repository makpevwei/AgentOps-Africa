from typing import Protocol

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_models import FinanceSnapshot


class FinanceProvider(Protocol):

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:
        ...