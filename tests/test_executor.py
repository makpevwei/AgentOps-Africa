from agentops.domains.research.executor import ResearchExecutor
from agentops.domains.research.planner import ResearchPlanner


class FakeTool:

    def search(self, query):

        return []


def main():

    planner = ResearchPlanner()

    tasks = planner.create_plan(
        "Should I invest in Zenith Bank?"
    )

    executor = ResearchExecutor()

    executor.register_tool(
        "tavily",
        FakeTool(),
    )

    executor.register_tool(
        "wikipedia",
        FakeTool(),
    )

    executor.register_tool(
        "company_resolver",
        FakeTool(),
    )

    executor.execute(tasks)


if __name__ == "__main__":
    main()