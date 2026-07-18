"""
Company Agent Service
"""

from __future__ import annotations

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.task import AgentTask
from agentops.domains.companies.company_service import CompanyService


class CompanyAgentService(BaseAgentService):
    name = "company"

    def __init__(self):

        self.company_service = CompanyService()

    def execute(
        self,
        task: AgentTask,
        context: AgentContext,
    ) -> dict:

        company_name = task.payload.get("company")

        if not company_name:
            raise ValueError("Task payload missing 'company'.")

        company = self.company_service.resolve(
            company_name,
        )

        context.company = company

        return company.model_dump()
