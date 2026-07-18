"""
Company Agent Service
"""

from __future__ import annotations

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.task import AgentTask
from agentops.domains.agents.task_result import TaskResult
from agentops.domains.companies.company_service import CompanyService


class CompanyAgentService(BaseAgentService):
    """
    Resolves company information.
    """

    name = "company"

    def __init__(self) -> None:
        self.company_service = CompanyService()

    def execute(
        self,
        task: AgentTask,
        context: AgentContext,
    ) -> TaskResult:
        """
        Resolve the company and store it in the shared context.
        """

        company_name = task.payload.get("company")

        if not company_name:
            raise ValueError("Task payload missing 'company'.")

        company = self.company_service.resolve(company_name)

        context.company = company

        return TaskResult(
            success=True,
            provider="CompanyService",
            output=company,
            metadata={
                "company": company.company_name,
                "ticker": company.ticker,
            },
        )
