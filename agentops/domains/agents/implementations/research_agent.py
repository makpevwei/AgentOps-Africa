"""
Research Agent
"""

from __future__ import annotations

from agentops.domains.agents.base_agent import BaseAgent
from agentops.domains.agents.execution_context import ExecutionContext
from agentops.domains.agents.task import AgentTask
from agentops.domains.companies.models import CompanyProfile
from agentops.domains.research.research_models import ResearchResult
from agentops.domains.research.service import ResearchService


class ResearchAgent(BaseAgent):
    """
    Executes research tasks.
    """

    def __init__(self) -> None:
        self.service = ResearchService()

    @property
    def service_name(self) -> str:
        return "research"

    def execute(
        self,
        task: AgentTask,
        context: ExecutionContext,
    ) -> ResearchResult:

        company = context.company

        if not isinstance(company, CompanyProfile):
            raise ValueError("CompanyProfile missing from execution context.")

        return self.service.research(company)
