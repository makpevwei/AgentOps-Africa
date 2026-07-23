"""
Research Executor

Executes research tasks.
"""

from agentops.core.logger import logger
from agentops.tools.research.tavily_tool import TavilyResearchTool


class ResearchExecutor:
    """
    Executes research tasks.

    Responsible for calling the appropriate
    research tool for each task.
    """

    def __init__(self):

        self.tavily = TavilyResearchTool()

    def execute(self, tasks):

        logger.info(
            "Executing %d research task(s)...",
            len(tasks),
        )

        findings = []

        for task in tasks:

            logger.info("Running task: %s", task.title)

            if task.tool == "tavily":

                findings.extend(
                    self.tavily.search(
                        task.query or task.description
                    )
                )

        logger.info(
            "Collected %d research finding(s).",
            len(findings),
        )

        return findings