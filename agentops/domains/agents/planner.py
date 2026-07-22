"""
Workflow Planner

Coordinates intent detection and workflow creation.
"""

from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.intent_router import IntentRouter
from agentops.domains.agents.task import AgentTask
from agentops.domains.agents.workflow_factory import WorkflowFactory


class Planner:
    """
    High-level workflow planner.

    Responsible for orchestrating the planning process,
    not implementing planning logic.
    """

    def __init__(self):

        self.router = IntentRouter()
        self.factory = WorkflowFactory()

    def create_workflow(
        self,
        message: str,
    ):

        intent = self.router.decide(message)

        return self.factory.create(
            intent,
            message,
        )

    def create_plan(
        self,
        message: str,
    ) -> ExecutionPlan:
        """
        Backward compatibility for legacy callers.
        """

        workflow = self.create_workflow(message)

        plan = ExecutionPlan(goal=message)

        for step in workflow.steps:
            plan.add_task(
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

        return plan