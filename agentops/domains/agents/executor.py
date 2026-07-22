"""
Agent Executor

Executes an execution plan using the registered agents.
"""

from __future__ import annotations

from agentops.core.logger import logger
from agentops.domains.agents.execution_context import ExecutionContext
from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.service_registry import ServiceRegistry


class Executor:
    """
    Executes an execution plan.
    """

    def __init__(self) -> None:
        self.registry = ServiceRegistry()

    def execute(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionContext:

        context = ExecutionContext()

        logger.info(
            "Starting execution: %s",
            plan.goal,
        )

        while not plan.is_complete:
            task = plan.next_task()

            if task is None:
                break

            logger.info(
                "Executing task %s (%s)",
                task.id,
                task.name,
            )

            plan.mark_running(task.id)

            try:
                agent = self.registry.get(task.service)

                result = agent.execute(
                    task,
                    context,
                )

                context.set_result(
                    task.service,
                    result,
                )

                context.mark_completed(task.id)

                plan.mark_completed(
                    task.id,
                    result,
                )

            except Exception:
                logger.exception(
                    "Task %s failed",
                    task.id,
                )

                context.add_error(f"Task {task.id} failed.")

                plan.mark_failed(
                    task.id,
                    f"Task {task.id} failed.",
                )

        logger.info(
            "Execution completed (%s/%s tasks)",
            plan.completed_tasks,
            plan.total_tasks,
        )

        return context
