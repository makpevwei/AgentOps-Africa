"""
Research Executor

Executes research tasks.
"""

from agentops.core.logger import logger
from agentops.domains.research.tool_registry import (
    ResearchToolRegistry,
)


class ResearchExecutor:
    """
    Executes research tasks.
    """

    def __init__(self):

        self.registry = ResearchToolRegistry()

    def execute(
        self,
        tasks,
    ):

        logger.info(
            "Executing %d research task(s)...",
            len(tasks),
        )

        findings = []

        for task in tasks:

            logger.info("Running task: %s", task.title)

            if not task.tool:
                continue

            tool = self.registry.get(task.tool)

            if tool is None:

                logger.warning(
                    "No registered tool for '%s'",
                    task.tool,
                )

                continue

            results = tool.search(
                task.query or task.description
            )

            findings.extend(results)

        logger.info(
            "Collected %d research finding(s).",
            len(findings),
        )

        return findings