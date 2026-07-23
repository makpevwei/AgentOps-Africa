"""
Research Executor

Executes research tasks.
"""

from agentops.core.logger import logger


class ResearchExecutor:
    """
    Executes research tasks.

    This class is intentionally lightweight.

    Future versions will:

    - Execute Tavily
    - Execute Wikipedia
    - Execute SEC
    - Execute Finnhub
    - Execute MCP tools

    and merge the results.
    """

    def execute(self, tasks):
        logger.info(
            "Executing %d research task(s)...",
            len(tasks),
        )

        return tasks