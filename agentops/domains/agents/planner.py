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
        full_plan: bool = True,
    ) -> ExecutionPlan:

        plan = ExecutionPlan(goal=goal)

        # Temporary extraction.
        # Later this will come from an LLM planner / entity extractor.
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

        #
        # Temporary migration mode.
        #
        # Until the ResearchAgentService and AnalysisAgentService
        # are implemented, stop after the finance task.
        #
        if not full_plan:
            return plan

        plan.add_task(
            AgentTask(
                id=3,
                service="research",
                action="company_profile",
                description="Collect company profile",
                payload={
                    "company": company,
                },
            )
        )

        plan.add_task(
            AgentTask(
                id=4,
                service="research",
                action="news",
                description="Collect recent company news",
                payload={
                    "company": company,
                },
            )
        )

        plan.add_task(
            AgentTask(
                id=5,
                service="analysis",
                action="business",
                description="Run business analysis",
            )
        )

        plan.add_task(
            AgentTask(
                id=6,
                service="analysis",
                action="financial",
                description="Run financial analysis",
            )
        )

        plan.add_task(
            AgentTask(
                id=7,
                service="analysis",
                action="executive_summary",
                description="Generate executive summary",
            )
        )

        return plan
