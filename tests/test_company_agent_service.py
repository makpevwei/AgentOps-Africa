from rich import print

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.company_agent_service import CompanyAgentService
from agentops.domains.agents.task import AgentTask


def main():

    service = CompanyAgentService()

    context = AgentContext()

    task = AgentTask(
        id=1,
        service="company",
        action="resolve",
        description="Resolve Apple",
        payload={
            "company": "Apple",
        },
    )

    company = service.execute(
        task,
        context,
    )

    print("=" * 60)
    print("Company Result")
    print("=" * 60)
    print(company)

    print()
    print("=" * 60)
    print("Agent Context")
    print("=" * 60)
    print(context.model_dump())


if __name__ == "__main__":
    main()
