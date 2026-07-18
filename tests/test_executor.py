from rich import print

from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.executor import Executor
from agentops.domains.agents.task import AgentTask


def main():

    plan = ExecutionPlan(
        goal="Analyze Apple",
    )

    plan.add_task(
        AgentTask(
            id=1,
            service="company",
            action="resolve",
            description="Resolve company",
            payload={
                "company": "Apple",
            },
        )
    )

    plan.add_task(
        AgentTask(
            id=2,
            service="finance",
            action="snapshot",
            description="Retrieve finance snapshot",
        )
    )

    executor = Executor()

    context = executor.execute(plan)

    print()
    print("=" * 60)
    print("Execution Plan")
    print("=" * 60)
    print(plan.model_dump())

    print()
    print("=" * 60)
    print("Agent Context")
    print("=" * 60)
    print(context.model_dump())


if __name__ == "__main__":
    main()
