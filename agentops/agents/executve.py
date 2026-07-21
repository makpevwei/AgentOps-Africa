from agentops.agents.base import BaseAgent
from agentops.providers.openai_provider import OpenAIProvider


class ExecutiveAgent(BaseAgent):
    def __init__(self):
        super().__init__("Executive Assistant")
        self.provider = OpenAIProvider()

    async def execute(self, prompt: str) -> str:
        return await self.provider.chat(prompt)
