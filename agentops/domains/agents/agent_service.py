"""
Agent Service

Coordinates AI interactions using the Workflow Runtime.
"""

from uuid import uuid4

from agentops.config import settings
from agentops.core.logger import logger
from agentops.domains.agents.agent_execution_result import (
    AgentExecutionResult,
)
from agentops.domains.agents.planner import Planner
from agentops.domains.workflows.workflow_executor import WorkflowExecutor


class AgentService:
    """
    Coordinates AI requests using the Workflow Runtime.
    """

    def __init__(
        self,
        planner: Planner | None = None,
        workflow_executor: WorkflowExecutor | None = None,
    ) -> None:
        self.planner = planner or Planner()
        self.workflow_executor = workflow_executor or WorkflowExecutor()

    def chat(
        self,
        message: str,
    ) -> AgentExecutionResult:

        logger.info("Processing chat request: %s", message)

        workflow = self.planner.create_workflow(message)

        logger.info(
            "Planner created workflow: %s",
            workflow.name,
        )

        context = self.workflow_executor.execute(
            workflow=workflow,
            goal=message,
        )

        logger.info("Workflow completed successfully.")

        return AgentExecutionResult(
            workflow_id=f"wf_{uuid4().hex[:8]}",
            workflow_name=workflow.name,
            planner=(
                "ai"
                if settings.USE_AI_PLANNER
                else "deterministic"
            ),
            status="completed",
            message="Workflow completed successfully.",
            data=context,
        )