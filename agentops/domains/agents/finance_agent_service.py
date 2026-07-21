"""
Finance Agent Service
"""

from __future__ import annotations

from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.execution_context import ExecutionContext
from agentops.domains.agents.task import AgentTask
from agentops.domains.agents.task_result import TaskResult
from agentops.domains.finance.finance_service import FinanceService


class FinanceAgentService(BaseAgentService):
    """
    Retrieves financial information for a company and stores it
    in the shared AgentContext.
    """

    name = "finance"

    def __init__(self) -> None:
        self.finance_service = FinanceService()

    def execute(
        self,
        task: AgentTask,
        context: ExecutionContext,
    ) -> TaskResult:
        """
        Retrieve the financial snapshot.

        The FinanceService always returns a FinanceSnapshot, but
        individual sections (quote, fundamentals, history, news)
        may be unavailable if no provider succeeds.
        """

        if context.company is None:
            raise ValueError("Company has not been resolved.")

        snapshot = self.finance_service.get_snapshot(
            context.company,
        )

        context.finance = snapshot

        metadata = {
            "has_quote": snapshot.quote is not None,
            "has_fundamentals": snapshot.fundamentals is not None,
            "history_count": len(snapshot.history),
            "news_count": len(snapshot.news),
        }

        if snapshot.quote is not None:
            metadata.update(
                {
                    "symbol": snapshot.quote.symbol,
                    "price": snapshot.quote.price,
                    "currency": snapshot.quote.currency,
                }
            )

        return TaskResult(
            success=True,
            provider="FinanceService",
            output=snapshot,
            metadata=metadata,
        )
