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

        #
        # 1. Resolve Company
        #
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

        #
        # 2. Finance
        #
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

        #
        # 3. Research
        #
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

        #
        # Future
        #
        # plan.add_task(
        #     AgentTask(
        #         id=4,
        #         name="analyze_company",
        #         service="analysis",
        #         action="analyze",
        #         depends_on=[2, 3],
        #     )
        # )

        return plan
