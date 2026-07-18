"""
Agent Executor

Executes tasks in an execution plan.
"""

from __future__ import annotations

from rich.console import Console

from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.task import TaskStatus

console = Console()


class Executor:

    def execute(
        self,
        plan: ExecutionPlan,
    ) -> ExecutionPlan:

        while True:

            task = plan.next_pending_task()

            if task is None:
                break

            console.log(
                f"Executing Task {task.id}: "
                f"{task.service}.{task.action}"
            )

            plan.mark_running(task.id)

            try:

                # Placeholder implementation
                result = {
                    "service": task.service,
                    "action": task.action,
                    "status": "success",
                }

                plan.mark_completed(
                    task.id,
                    result,
                )

            except Exception as ex:

                plan.mark_failed(
                    task.id,
                    str(ex),
                )

        return plan