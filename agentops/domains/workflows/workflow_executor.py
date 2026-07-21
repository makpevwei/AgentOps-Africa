"""
Workflow Executor.

Coordinates workflow execution by converting workflows into
execution plans and delegating execution to the runtime executor.
"""

from __future__ import annotations

from agentops.domains.agents.execution_context import ExecutionContext
from agentops.domains.agents.executor import Executor
from agentops.domains.workflows.workflow import Workflow
from agentops.domains.workflows.workflow_engine import WorkflowEngine


class WorkflowExecutor:
    """
    Executes business workflows.
    """

    def __init__(
        self,
        workflow_engine: WorkflowEngine | None = None,
        executor: Executor | None = None,
    ) -> None:
        self.workflow_engine = workflow_engine or WorkflowEngine()
        self.executor = executor or Executor()

    def execute(
        self,
        workflow: Workflow,
        goal: str,
    ) -> ExecutionContext:
        """
        Build an execution plan from the workflow and execute it.
        """

        plan = self.workflow_engine.build_execution_plan(
            workflow=workflow,
            goal=goal,
        )

        return self.executor.execute(plan)
