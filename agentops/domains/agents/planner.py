"""
Workflow Planner

Coordinates AI planning and deterministic workflow creation.
"""

import logging

from agentops.ai.planning import (
    AIPlanner,
    WorkflowConverter,
)
from agentops.config import settings
from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.intent_router import IntentRouter
from agentops.domains.agents.task import AgentTask
from agentops.domains.agents.workflow_factory import WorkflowFactory

logger = logging.getLogger(__name__)


class Planner:

    def __init__(self):

        self.router = IntentRouter()

        self.factory = WorkflowFactory()

        self.ai = AIPlanner()

        self.converter = WorkflowConverter()

    def create_workflow(
        self,
        message: str,
    ):

        if settings.USE_AI_PLANNER:

            try:

                workflow_plan = self.ai.plan(message)

                return self.converter.convert(workflow_plan)

            except Exception as exc:

                logger.exception(
                    "AI planner failed. Falling back to WorkflowFactory.",
                    exc_info=exc,
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