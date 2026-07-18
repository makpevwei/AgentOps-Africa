"""
Analysis Provider Factory.
"""

from __future__ import annotations

from agentops.domains.analysis.providers.openai_provider import (
    OpenAIAnalysisProvider,
)
from agentops.domains.analysis.providers.registry import (
    AnalysisProviderRegistry,
)


class AnalysisProviderFactory:
    """
    Creates and manages Analysis Providers.
    """

    def __init__(self) -> None:
        self.registry = AnalysisProviderRegistry()

        self.registry.register(OpenAIAnalysisProvider())

    def get(
        self,
        provider: str = "openai",
    ):
        """
        Return the requested provider.
        """
        return self.registry.get(provider)
