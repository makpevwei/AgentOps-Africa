"""
Finance Orchestrator

Coordinates multiple finance providers and returns the best
available FinanceSnapshot.
"""

from __future__ import annotations

from agentops.core.logger import logger
from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_snapshot import FinanceSnapshot
from agentops.providers.finance.base_provider import BaseFinanceProvider


class FinanceOrchestrator:
    """
    Executes finance providers in priority order.
    """

    def __init__(
        self,
        providers: list[BaseFinanceProvider],
    ):
        self.providers = providers

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:

        for provider in self.providers:

            logger.info(
                "Trying finance provider: %s",
                provider.name,
            )

            result = provider.get_snapshot(company)

            if result.success and not result.is_empty:

                logger.info(
                    "Finance provider succeeded: %s (%.2f ms)",
                    result.provider,
                    result.response_time_ms or 0,
                )

                return result.snapshot

            logger.warning(
                "Finance provider failed: %s (%s)",
                result.provider,
                ", ".join(result.errors),
            )

        logger.warning(
            "No finance provider returned data for %s",
            company.company_name,
        )

        return FinanceSnapshot()