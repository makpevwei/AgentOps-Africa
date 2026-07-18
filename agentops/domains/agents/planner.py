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

        plan = ExecutionPlan(goal=goal)

        #
        # Temporary entity extraction.
        #
        company = goal.replace("Analyze", "").replace("analyse", "").strip()

        plan.add_task(
            AgentTask(
                id=1,
                service="company",
                action="resolve",
                description="Resolve company information",
                payload={
                    "company": company,
                },
            )
        )

        plan.add_task(
            AgentTask(
                id=2,
                service="finance",
                action="snapshot",
                description="Retrieve financial snapshot",
                payload={
                    "company": company,
                },
            )
        )

        plan.add_task(
            AgentTask(
                id=3,
                service="research",
                action="research",
                description="Collect company research",
                payload={
                    "company": company,
                },
            )
        )

        return plan
