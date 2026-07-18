"""
Enterprise Finance Service

Coordinates all financial data retrieval.

The Finance Service is the single public entry point
for all finance operations within the application.
"""

from __future__ import annotations

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_orchestrator import FinanceOrchestrator
from agentops.domains.finance.finance_snapshot import FinanceSnapshot


class FinanceService:
    """
    Service responsible for retrieving financial data.

    Consumers should never communicate directly with
    finance providers. All requests flow through the
    Finance Orchestrator.
    """

    def __init__(self) -> None:
        self.orchestrator = FinanceOrchestrator()

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:
        """
        Retrieve the best available financial snapshot.
        """

        return self.orchestrator.get_snapshot(company)
