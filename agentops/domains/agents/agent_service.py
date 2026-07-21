"""
Agent Service

Coordinates AI interactions using the Workflow Runtime.
"""

from agentops.core.logger import logger
from agentops.domains.agents.agent_result import AgentResult
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
    ) -> AgentResult:

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

        #
        # Temporary compatibility adapter
        #
        return AgentResult(
            agent="workflow",
            message="Workflow completed successfully.",
            data=context,
        )
