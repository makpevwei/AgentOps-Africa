"""
Enterprise Research Engine

Builds a complete research context for a company.
"""

from agentops.domains.companies.company_service import CompanyService
from agentops.domains.finance.finance_service import FinanceService
from agentops.domains.research.research_context import ResearchContext


class ResearchEngine:
    """
    High-level orchestration for company research.
    """

    def __init__(self):

        self.company_service = CompanyService()
        self.finance_service = FinanceService()

    def build_context(
        self,
        company_name: str,
    ) -> ResearchContext:
        """
        Build a complete research context for a company.
        """

        # -------------------------------------------------
        # Resolve Company
        # -------------------------------------------------

        company = self.company_service.resolve(company_name)

        # -------------------------------------------------
        # Retrieve Financial Snapshot
        # -------------------------------------------------

        finance_snapshot = self.finance_service.get_snapshot(company)

        # -------------------------------------------------
        # Build Context
        # -------------------------------------------------

        return ResearchContext(
            query=company_name,
            company=company,
            finance=finance_snapshot,
        )