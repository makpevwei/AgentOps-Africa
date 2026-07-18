from agentops.domains.agents.planner import Planner

planner = Planner()

plan = planner.create_plan("Analyze Apple Inc.")

print()

print("=" * 60)

print(plan.goal)

print("=" * 60)


for task in plan.tasks:
    print(task.model_dump())
