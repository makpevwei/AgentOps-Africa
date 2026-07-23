from pathlib import Path

from agentops.builders.agent_builder import AgentBuilder
from agentops.domains.research.engine import ResearchEngine
from agentops.tools.research.langchain_tools import tavily_search

PROMPT = (
    Path(__file__).resolve().parent.parent / "prompts" / "research_system.txt"
).read_text()


class ResearchAgent:
    """
    Enterprise Research Agent.
    """

    def __init__(self):

        self.engine = ResearchEngine()

        self.tools = [
            tavily_search,
        ]

        self.agent = AgentBuilder.build_deep_agent(
            tools=self.tools,
            system_prompt=PROMPT,
            name="ResearchAgent",
        )

    async def ask(
        self,
        question: str,
    ):

        report = self.engine.research(question)

        research_context = "\n\n".join(
            f"""
Title:
{finding.title}

Summary:
{finding.summary}

URL:
{finding.url}
"""
            for finding in report.findings
        )

        content = f"""
Question:

{question}

Research Findings:

{research_context}
"""

        return await self.agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": content,
                    }
                ]
            }
        )