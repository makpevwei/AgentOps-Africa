"""
Agent Execution Engine

Coordinates execution of an ExecutionPlan by dispatching
tasks to registered Agent Services.
"""

from __future__ import annotations

from rich import print

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.service_registry import ServiceRegistry


class Executor:
    """
    Executes an ExecutionPlan using registered Agent Services.
    """

    def __init__(self) -> None:
        self.registry = ServiceRegistry()

    def execute(
        self,
        plan: ExecutionPlan,
    ) -> AgentContext:
        """
        Execute all runnable tasks.
        """

        context = AgentContext()

        while plan.has_ready_tasks:
            task = plan.next_pending_task()

            if task is None:
                break

            print(f"\n▶ Running {task.service}:{task.action}")

            plan.mark_running(task.id)

            try:
                service = self.registry.get(task.service)

                if service is None:
                    raise ValueError(f"No service registered for '{task.service}'.")

                result = service.execute(
                    task,
                    context,
                )

                plan.mark_completed(
                    task.id,
                    result,
                )

                print(f"✅ Completed {task.service}:{task.action}")

            except Exception as ex:
                plan.mark_failed(
                    task.id,
                    str(ex),
                )

                print(f"❌ Failed {task.service}:{task.action}")
                print(ex)

        #
        # Report blocked tasks.
        #
        blocked = plan.blocked_tasks()

        if blocked:
            print("\n⚠ Blocked Tasks")

            for task in blocked:
                print(f"   • {task.service}:{task.action} (dependency failed)")

        #
        # Summary
        #
        print("\nExecution Summary")

        print(f"   Total     : {plan.total_tasks}")
        print(f"   Completed : {plan.completed_tasks}")
        print(f"   Failed    : {plan.failed_tasks}")
        print(f"   Pending   : {plan.pending_tasks}")

        return context
