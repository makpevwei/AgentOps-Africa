"""
Finance Agent Service
"""

from __future__ import annotations

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.task import AgentTask
from agentops.domains.finance.finance_service import FinanceService


class FinanceAgentService(BaseAgentService):
    name = "finance"

    def __init__(self):

        self.finance_service = FinanceService()

    def execute(
        self,
        task: AgentTask,
        context: AgentContext,
    ) -> dict:

        if context.company is None:
            raise ValueError("Company has not been resolved.")

        snapshot = self.finance_service.get_snapshot(
            context.company,
        )

        context.finance = snapshot

        return snapshot.model_dump()
