"""
Research Task Executor

Executes a research plan using the available tools.
"""

from agentops.domains.research.planner import ResearchTask


class ResearchExecutor:

    def __init__(self):

        self.tools = {}

    def register_tool(
        self,
        name,
        tool,
    ):

        self.tools[name] = tool

    def execute(self, tasks):

        for task in tasks:

            print()

            print(f"Executing: {task.title}")

            if task.tool is None:

                task.completed = True

                continue

            if task.tool not in self.tools:

                print(
                    f"No tool registered for {task.tool}"
                )

                continue

            print(
                f"Using tool -> {task.tool}"
            )

            task.completed = True

        return tasks