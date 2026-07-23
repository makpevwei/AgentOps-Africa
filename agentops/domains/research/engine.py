"""
Research Engine

Coordinates the end-to-end research workflow.
"""

import time

from agentops.core.logger import logger
from agentops.domains.research.executor import ResearchExecutor
from agentops.domains.research.models import (
    ResearchFinding,
    ResearchReport,
    ResearchSource,
)
from agentops.domains.research.planner import ResearchPlanner


class ResearchEngine:
    """
    Orchestrates research execution.
    """

    def __init__(self):

        self.planner = ResearchPlanner()

        self.executor = ResearchExecutor()

    def research(
        self,
        query: str,
    ) -> ResearchReport:

        logger.info("Starting research...")

        started = time.perf_counter()

        tasks = self.planner.create_plan(query)

        results = self.executor.execute(tasks)

        findings = [
            ResearchFinding(
                title=result.title,
                summary=result.summary,
                url=result.url,
                confidence=result.confidence,
            )
            for result in results
        ]

        sources = [
            ResearchSource(
                title=result.title,
                url=result.url,
                provider="tavily",
            )
            for result in results
        ]

        elapsed = int(
            (time.perf_counter() - started) * 1000
        )

        logger.info(
            "Research completed with %d findings.",
            len(findings),
        )

        return ResearchReport(
            query=query,
            findings=findings,
            sources=sources,
            summary=f"Collected {len(findings)} research findings.",
            execution_time_ms=elapsed,
        )