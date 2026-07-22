"""
Workflow Planner

Coordinates AI planning and deterministic workflow creation.
"""

import logging

from agentops.ai.planning import PlanningPipeline
from agentops.config import settings
from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.intent_router import IntentRouter
from agentops.domains.agents.task import AgentTask
from agentops.domains.agents.workflow_factory import WorkflowFactory

logger = logging.getLogger(__name__)


class Planner:
    """
    Coordinates workflow planning.

    Uses the AI planning pipeline when enabled and falls back to the
    deterministic workflow factory if AI planning fails.
    """

    def __init__(self) -> None:
        self.router = IntentRouter()
        self.factory = WorkflowFactory()
        self.pipeline = PlanningPipeline()

    def create_workflow(self, message: str):
        """
        Create a workflow for the given user request.
        """

        if settings.USE_AI_PLANNER:
            try:
                return self.pipeline.plan(message)

            except Exception:
                logger.exception(
                    "AI planning failed. Falling back to deterministic planner."
                )

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
        Convert a workflow into an executable plan.
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