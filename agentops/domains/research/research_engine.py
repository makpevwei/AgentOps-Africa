"""
Enterprise Research Engine

Coordinates research using the Agent Runtime.
"""

from __future__ import annotations

from time import perf_counter

from agentops.core.logger import logger
from agentops.domains.agents.executor import Executor
from agentops.domains.agents.planner import Planner
from agentops.domains.research.research_context import ResearchContext


class ResearchEngine:
    """
    High-level orchestration layer responsible for coordinating
    company research using the Agent Runtime.
    """

    def __init__(
        self,
        company_service=None,
        finance_service=None,
    ) -> None:

        # Legacy compatibility
        self.company_service = company_service
        self.finance_service = finance_service

        # New runtime
        self.planner = Planner()
        self.executor = Executor()

    def build_context(
        self,
        company_name: str,
    ) -> ResearchContext:
        """
        Build a complete research context for a company.
        """

        started = perf_counter()

        logger.info(
            "Building research context for %s",
            company_name,
        )

        #
        # -----------------------------------------------------------------
        # Legacy compatibility path
        # -----------------------------------------------------------------
        #
        if self.company_service is not None and self.finance_service is not None:
            company = self.company_service.resolve(company_name)
            finance = self.finance_service.get_snapshot(company)

            return ResearchContext(
                query=company_name,
                company=company,
                finance=finance,
            )

        #
        # -----------------------------------------------------------------
        # New runtime
        # -----------------------------------------------------------------
        #

        plan = self.planner.create_plan(
            f"Analyze {company_name}",
        )

        agent_context = self.executor.execute(plan)

        context = ResearchContext(
            query=company_name,
            company=agent_context.company,
            finance=agent_context.finance,
            research=agent_context.research,
        )

        duration = perf_counter() - started

        logger.info(
            "Research completed for %s in %.2f seconds",
            company_name,
            duration,
        )

        return context
