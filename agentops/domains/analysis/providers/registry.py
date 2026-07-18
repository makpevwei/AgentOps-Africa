"""
Analysis Provider Registry.
"""

from __future__ import annotations

from agentops.domains.analysis.providers.base_provider import (
    BaseAnalysisProvider,
)


class AnalysisProviderRegistry:
    """
    Registry of available Analysis Providers.
    """

    def __init__(self) -> None:
        self._providers: dict[str, BaseAnalysisProvider] = {}

    def register(
        self,
        provider: BaseAnalysisProvider,
    ) -> None:
        """
        Register an analysis provider.
        """
        self._providers[provider.name] = provider

    def get(
        self,
        name: str,
    ) -> BaseAnalysisProvider:
        """
        Retrieve a registered provider.
        """
        try:
            return self._providers[name]
        except KeyError as exc:
            raise ValueError(f"Analysis provider '{name}' is not registered.") from exc

    def list(self) -> list[str]:
        """
        List registered provider names.
        """
        return sorted(self._providers.keys())
