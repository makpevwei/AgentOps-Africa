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

        tasks = [
            (
                "company",
                "resolve",
                "Resolve company information",
            ),
            (
                "finance",
                "snapshot",
                "Retrieve financial snapshot",
            ),
            (
                "research",
                "company_profile",
                "Collect company profile",
            ),
            (
                "research",
                "news",
                "Collect recent company news",
            ),
            (
                "analysis",
                "business",
                "Run business analysis",
            ),
            (
                "analysis",
                "financial",
                "Run financial analysis",
            ),
            (
                "analysis",
                "executive_summary",
                "Generate executive summary",
            ),
        ]

        for index, task in enumerate(tasks, start=1):

            plan.add_task(
                AgentTask(
                    id=index,
                    service=task[0],
                    action=task[1],
                    description=task[2],
                )
            )

        return plan