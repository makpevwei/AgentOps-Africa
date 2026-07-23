from pathlib import Path

from agentops.builders.agent_builder import AgentBuilder
from agentops.domains.research.engine import ResearchEngine
from agentops.tools.research.langchain_tools import tavily_search

PROMPT = (
    Path(__file__).resolve().parent.parent / "prompts" / "research_system.txt"
).read_text()


class ResearchAgent:

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

    async def ask(self, question: str):

        plan = self.engine.create_plan(question)

        return await self.agent.ainvoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question,
                    }
                ],
                "research_plan": [
                    task.__dict__
                    for task in plan
                ],
            }
        )