"""
Agent Planner

Creates an execution plan for a user request.
"""

from __future__ import annotations

from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.task import AgentTask


class Planner:
    """
    Creates an execution plan from a user goal.
    """

    def create_plan(
        self,
        goal: str,
    ) -> ExecutionPlan:
        """
        Build an execution plan for the supplied goal.
        """

        plan = ExecutionPlan(goal=goal)

        # Temporary entity extraction.
        company = (
            goal.replace("Analyze", "")
            .replace("analyse", "")
            .strip()
        )

        # Resolve company.
        plan.add_task(
            AgentTask(
                id=1,
                name="resolve_company",
                service="company",
                action="resolve",
                description="Resolve company information",
                payload={
                    "company": company,
                },
            )
        )

        # Retrieve financial data.
        plan.add_task(
            AgentTask(
                id=2,
                name="fetch_finance",
                service="finance",
                action="snapshot",
                description="Retrieve financial snapshot",
                depends_on=[1],
                payload={
                    "company": company,
                },
            )
        )

        # Collect company research.
        plan.add_task(
            AgentTask(
                id=3,
                name="collect_research",
                service="research",
                action="research",
                description="Collect company research",
                depends_on=[1],
                payload={
                    "company": company,
                },
            )
        )

        return plan