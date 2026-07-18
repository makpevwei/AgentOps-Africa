from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.task import AgentTask


class DemoService(BaseAgentService):
    name = "demo"

    def execute(
        self,
        task: AgentTask,
    ) -> dict:

        return {"message": "Hello Agent Runtime"}


service = DemoService()

result = service.execute(
    AgentTask(
        id=1,
        service="demo",
        action="hello",
        description="Demo",
    )
)

print(result)
