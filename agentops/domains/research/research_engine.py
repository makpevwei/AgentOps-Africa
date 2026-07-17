"""
Enterprise Research Engine

Builds a complete research context for a company.
"""

import logging
import time

from agentops.domains.companies.company_service import CompanyService
from agentops.domains.finance.finance_service import FinanceService
from agentops.domains.research.research_context import ResearchContext

logger = logging.getLogger(__name__)


class ResearchEngine:
    """
    High-level orchestration for company research.
    """

    def __init__(
        self,
        company_service: CompanyService | None = None,
        finance_service: FinanceService | None = None,
    ):
        """
        Initialize the research engine.

        Dependencies can be injected for testing,
        otherwise the default implementations are used.
        """
        self.company_service = company_service or CompanyService()
        self.finance_service = finance_service or FinanceService()

    def build_context(
        self,
        company_name: str,
    ) -> ResearchContext:
        """
        Build a complete research context for a company.
        """

        start = time.perf_counter()

        logger.info("Resolving company: %s", company_name)

        company = self.company_service.resolve(company_name)

        logger.info(
            "Fetching finance snapshot for %s",
            company.company_name,
        )

        finance_snapshot = self.finance_service.get_snapshot(company)
        
        logger.info(
            "Finance Snapshot: %s",
            finance_snapshot.model_dump(),
        )

        context = ResearchContext(
            query=company_name,
            company=company,
            finance=finance_snapshot,
        )

        logger.info("Research context built successfully")

        logger.info(
            "Research completed in %.2f seconds",
            time.perf_counter() - start,
        )

        return context
