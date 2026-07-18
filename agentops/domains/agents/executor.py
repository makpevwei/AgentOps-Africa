"""
Agent Execution Engine

Coordinates the execution of an ExecutionPlan by dispatching
tasks to the appropriate Agent Services and maintaining a
shared AgentContext.
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
        Execute all tasks in the supplied execution plan.

        Returns
        -------
        AgentContext
            The shared execution context containing all outputs
            produced by the executed services.
        """

        context = AgentContext()

        while True:
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
                print(f"❌ Failed {task.service}:{task.action}")
                print(ex)

                plan.mark_failed(
                    task.id,
                    str(ex),
                )

                # Stop execution on the first failure.
                break

        return context
