from rich import print

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.finance_agent_service import FinanceAgentService
from agentops.domains.agents.task import AgentTask
from agentops.domains.companies.company_service import CompanyService


def main():

    company_service = CompanyService()

    context = AgentContext()

    context.company = company_service.resolve(
        "Apple",
    )

    service = FinanceAgentService()

    task = AgentTask(
        id=1,
        service="finance",
        action="snapshot",
        description="Retrieve Apple financials",
    )

    result = service.execute(
        task,
        context,
    )

    print("=" * 60)
    print("Finance Result")
    print("=" * 60)
    print(result)

    print()
    print("=" * 60)
    print("Agent Context")
    print("=" * 60)
    print(context.model_dump())


if __name__ == "__main__":
    main()
