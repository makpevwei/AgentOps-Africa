"""
Research Planner

Converts a user request into executable research tasks.
"""

from dataclasses import dataclass, field


@dataclass
class ResearchTask:
    """
    Represents one research task.
    """

    id: int

    title: str

    description: str

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
                        1,
                        "Resolve Company",
                        "Determine the correct company identity.",
                        "company_resolver",
                    ),
                    ResearchTask(
                        2,
                        "Search Latest News",
                        "Collect recent news articles.",
                        "tavily",
                    ),
                    ResearchTask(
                        3,
                        "Search Background Information",
                        "Collect background information.",
                        "wikipedia",
                    ),
                    ResearchTask(
                        4,
                        "Generate Investment Report",
                        "Summarize all findings.",
                    ),
                ]
            )

            return tasks

        # Generic research

        tasks.extend(
            [
                ResearchTask(
                    1,
                    "Search the Web",
                    "Search recent information.",
                    "tavily",
                ),
                ResearchTask(
                    2,
                    "Search Background Knowledge",
                    "Gather encyclopedia information.",
                    "wikipedia",
                ),
                ResearchTask(
                    3,
                    "Generate Report",
                    "Create a structured report.",
                ),
            ]
        )

        return tasks