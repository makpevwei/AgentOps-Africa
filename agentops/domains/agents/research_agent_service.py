"""
Research Agent Service.
"""

from __future__ import annotations

from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.execution_context import ExecutionContext
from agentops.domains.agents.task import AgentTask
from agentops.domains.agents.task_result import TaskResult
from agentops.domains.research.service import ResearchService


class ResearchAgentService(BaseAgentService):
    """
    Executes company research and stores the results
    in the shared AgentContext.
    """

    name = "research"

    def __init__(
        self,
        service: ResearchService | None = None,
    ) -> None:
        self.service = service or ResearchService()

    def execute(
        self,
        task: AgentTask,
        context: ExecutionContext,
    ) -> TaskResult:
        """
        Execute the research task.
        """

        if context.company is None:
            raise ValueError(
                "Company information must be resolved before research can execute."
            )

        result = self.service.research(
            context.company,
        )

        context.research.result = result

        return TaskResult(
            success=True,
            provider="ResearchService",
            output=result,
            metadata={
                "provider_count": len(result.sources),
                "news_count": len(result.news),
            },
        )
