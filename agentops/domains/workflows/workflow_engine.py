"""
Workflow Engine

Converts workflows into executable plans.
"""

from __future__ import annotations

from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.task import AgentTask
from agentops.domains.workflows.workflow import Workflow


class WorkflowEngine:
    """
    Converts business workflows into execution plans.
    """

    def build_execution_plan(
        self,
        workflow: Workflow,
        goal: str,
    ) -> ExecutionPlan:
        """
        Build an execution plan from a workflow.
        """

        tasks: list[AgentTask] = []

        for step in workflow.steps:
            tasks.append(
                AgentTask(
                    id=step.id,
                    name=step.name,
                    service=step.service,
                    action=step.action,
                    description=step.description,
                    payload=step.payload,
                    depends_on=step.depends_on,
                )
            )

        return ExecutionPlan(
            goal=goal,
            tasks=tasks,
        )
