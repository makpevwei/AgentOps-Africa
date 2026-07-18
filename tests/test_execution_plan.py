from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.task import AgentTask

plan = ExecutionPlan(goal="Analyze Apple Inc.")

plan.add_task(
    AgentTask(id=1, service="company", action="resolve", description="Resolve company")
)

plan.add_task(
    AgentTask(
        id=2,
        service="finance",
        action="snapshot",
        description="Retrieve finance snapshot",
    )
)

print(plan.model_dump())

print()

print(f"Goal: {plan.goal}")
print(f"Tasks: {plan.total_tasks}")
print(f"Pending: {plan.pending_tasks}")
