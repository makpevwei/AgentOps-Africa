import asyncio

from agentops.agents.research_agent import ResearchAgent


async def main():

    agent = ResearchAgent()

    result = await agent.ask(
        "What is Agentic AI?"
    )

    print()

    print("=" * 60)

    print()

    print(result["messages"][-1].content)


if __name__ == "__main__":

    asyncio.run(main())