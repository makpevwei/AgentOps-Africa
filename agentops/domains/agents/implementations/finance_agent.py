"""
Finance Agent
"""

from __future__ import annotations

from agentops.domains.agents.base_agent import BaseAgent
from agentops.domains.agents.execution_context import ExecutionContext
from agentops.domains.agents.task import AgentTask
from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_service import FinanceService
from agentops.domains.finance.finance_snapshot import FinanceSnapshot


class FinanceAgent(BaseAgent):
    """
    Executes finance tasks.
    """

    def __init__(self) -> None:
        self.service = FinanceService()

    @property
    def service_name(self) -> str:
        return "finance"

    def execute(
        self,
        task: AgentTask,
        context: ExecutionContext,
    ) -> FinanceSnapshot:

        company = context.company

        if not isinstance(company, CompanyProfile):
            raise ValueError("CompanyProfile missing from execution context.")

        return self.service.get_snapshot(company)
