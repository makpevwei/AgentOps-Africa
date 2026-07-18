from agentops.domains.agents.task import AgentTask

task = AgentTask(
    id=1,
    service="finance",
    action="get_snapshot",
    description="Retrieve financial snapshot for Apple",
    payload={"company": "Apple"},
)

print(task.model_dump())
