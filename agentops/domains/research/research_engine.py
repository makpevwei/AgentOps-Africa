"""
Enterprise Research Engine

Coordinates research using the Agent Runtime.
"""

from __future__ import annotations

import logging
import time

from agentops.domains.agents.executor import Executor
from agentops.domains.agents.planner import Planner
from agentops.domains.research.research_context import ResearchContext

logger = logging.getLogger(__name__)


class ResearchEngine:
    """
    High-level orchestration for company research.
    """

    def __init__(self) -> None:

        self.planner = Planner()

        self.executor = Executor()

    def build_context(
        self,
        company_name: str,
    ) -> ResearchContext:
        """
        Build a research context using the Agent Runtime.
        """

        start = time.perf_counter()

        logger.info(
            "Building research context for %s",
            company_name,
        )

        #
        # Temporary migration mode.
        #
        # Build only the tasks currently supported by
        # the Agent Runtime.
        #
        plan = self.planner.create_plan(
            f"Analyze {company_name}",
            full_plan=False,
        )

        agent_context = self.executor.execute(
            plan,
        )

        context = ResearchContext(
            query=company_name,
            company=agent_context.company,
            finance=agent_context.finance,
        )

        logger.info(
            "Research completed in %.2f seconds",
            time.perf_counter() - start,
        )

        return context
