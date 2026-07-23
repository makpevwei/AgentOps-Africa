"""
Research Planner

Converts a user request into executable research tasks.
"""

from dataclasses import dataclass


@dataclass
class ResearchTask:
    """
    Represents one research task.
    """

    id: int
    title: str
    description: str
    query: str | None = None
    tool: str | None = None
    completed: bool = False


class ResearchPlanner:
    """
    Creates a research plan from a user query.
    """

    def create_plan(self, query: str) -> list[ResearchTask]:

        query_lower = query.lower()

        tasks: list[ResearchTask] = []

        # Company / Investment research

        if any(
            keyword in query_lower
            for keyword in [
                "invest",
                "stock",
                "share",
                "company",
                "bank",
            ]
        ):
            tasks.extend(
                [
                    ResearchTask(
                        id=1,
                        title="Resolve Company",
                        description="Determine the correct company identity.",
                        query=query,
                        tool="company_resolver",
                    ),
                    ResearchTask(
                        id=2,
                        title="Search Latest News",
                        description="Collect recent news articles.",
                        query=query,
                        tool="tavily",
                    ),
                    ResearchTask(
                        id=3,
                        title="Search Background Information",
                        description="Collect background information.",
                        query=query,
                        tool="wikipedia",
                    ),
                    ResearchTask(
                        id=4,
                        title="Generate Investment Report",
                        description="Summarize all findings.",
                    ),
                ]
            )

            return tasks

        # Generic research

        tasks.extend(
            [
                ResearchTask(
                    id=1,
                    title="Search the Web",
                    description="Search recent information.",
                    query=query,
                    tool="tavily",
                ),
                ResearchTask(
                    id=2,
                    title="Search Background Knowledge",
                    description="Gather encyclopedia information.",
                    query=query,
                    tool="wikipedia",
                ),
                ResearchTask(
                    id=3,
                    title="Generate Report",
                    description="Create a structured report.",
                ),
            ]
        )

        return tasks