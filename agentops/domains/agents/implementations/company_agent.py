"""
Company Agent

Adapter between the Executor and CompanyService.
"""

from __future__ import annotations

from agentops.domains.agents.base_agent import BaseAgent
from agentops.domains.agents.execution_context import ExecutionContext
from agentops.domains.agents.task import AgentTask
from agentops.domains.companies.company_service import CompanyService
from agentops.domains.companies.models import CompanyProfile


class CompanyAgent(BaseAgent):
    """
    Executes company resolution tasks.
    """

    def __init__(self) -> None:
        self.service = CompanyService()

    @property
    def service_name(self) -> str:
        return "company"

    def execute(
        self,
        task: AgentTask,
        context: ExecutionContext,
    ) -> CompanyProfile:
        return self.service.resolve(
            task.payload["company"],
        )
