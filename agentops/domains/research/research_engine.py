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

    def __init__(self) -> None:
        self.planner: Planner = Planner()
        self.executor: Executor = Executor()

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

        # Create an execution plan.
        plan = self.planner.create_plan(
            f"Analyze {company_name}",
        )

        # Execute the plan.
        agent_context = self.executor.execute(plan)

        # Build the research context returned to callers.
        context = ResearchContext(
            query=company_name,
            company=agent_context.company,
            finance=agent_context.finance,
            research=agent_context.research.result,
        )

        duration = perf_counter() - started

        logger.info(
            "Research completed for %s in %.2f seconds",
            company_name,
            duration,
        )

        return context