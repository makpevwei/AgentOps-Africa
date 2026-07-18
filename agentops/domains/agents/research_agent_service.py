"""
Research Agent Service.
"""

from __future__ import annotations

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.task import AgentTask
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
        context: AgentContext,
    ) -> dict:
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

        return {
            "provider_count": len(result.sources),
            "news_count": len(result.news),
        }
