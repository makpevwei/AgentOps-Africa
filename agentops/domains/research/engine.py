"""
Research Engine

Coordinates the end-to-end research workflow.
"""

from agentops.core.logger import logger
from agentops.domains.research.planner import ResearchPlanner


class ResearchEngine:
    """
    Orchestrates research execution.

    Responsibilities:

    - Build a research plan
    - Log execution
    - Return executable tasks

    Future versions will also:

    - Execute tools
    - Rank results
    - Deduplicate findings
    - Build reports
    """

    def __init__(self):
        self.planner = ResearchPlanner()

    def create_plan(self, query: str):
        """
        Create a research plan.
        """

        logger.info("Creating research plan...")

        tasks = self.planner.create_plan(query)

        logger.info("Research plan created with %d task(s).", len(tasks))

        return tasks