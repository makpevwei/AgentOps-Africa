"""
AI Client

Centralized interface for interacting with chat models.
"""

from langchain_core.messages import BaseMessage

from agentops.providers.model_provider import ChatModelProvider


class AIClient:
    """
    Thin wrapper around the configured chat model.
    """

    def __init__(self):
        self._llm = ChatModelProvider.create()

    def invoke(
        self,
        messages: list[BaseMessage],
    ):
        """
        Invoke the configured chat model.
        """
        return self._llm.invoke(messages)