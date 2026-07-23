"""
Research Engine

Coordinates the end-to-end research workflow.
"""

from agentops.core.logger import logger
from agentops.domains.research.executor import ResearchExecutor
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
    ):

        logger.info("Starting research...")

        tasks = self.planner.create_plan(query)

        findings = self.executor.execute(tasks)

        logger.info(
            "Research completed with %d finding(s).",
            len(findings),
        )

        return findings