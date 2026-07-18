from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.task import AgentTask

plan = ExecutionPlan(goal="Analyze Apple")

plan.add_task(
    AgentTask(
        id=1,
        service="company",
        action="resolve",
        description="Resolve company",
    )
)

plan.add_task(
    AgentTask(
        id=2,
        service="finance",
        action="snapshot",
        description="Get financial snapshot",
    )
)

print("Initial")
print(plan.model_dump())

plan.mark_running(1)

print("\nRunning Task 1")
print(plan.model_dump())

plan.mark_completed(
    1,
    {"company": "Apple Inc."},
)

print("\nCompleted Task 1")
print(plan.model_dump())

next_task = plan.next_pending_task()

print("\nNext Pending Task")
print(next_task)
