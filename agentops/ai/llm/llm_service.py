"""
LLM Service

Provider-agnostic interface for all language models.
"""

from agentops.ai.llm.openai_provider import OpenAIProvider


class LLMService:
    """
    Unified interface for language models.
    """

    def __init__(self) -> None:
        self.provider = OpenAIProvider()

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Generate a response using the configured provider.
        """

        return self.provider.generate(prompt)