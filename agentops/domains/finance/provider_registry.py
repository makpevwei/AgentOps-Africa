"""
Finance Provider Registry

Responsible for registering and exposing finance providers
to the Finance Orchestrator.

The orchestrator never knows about individual providers.
"""

from __future__ import annotations

from agentops.providers.finance.base_provider import BaseFinanceProvider
from agentops.providers.finance.finnhub_provider import FinnhubProvider


class ProviderRegistry:
    """
    Registers all finance providers.

    Later this registry will also support:

    - Provider priorities
    - Provider health
    - Feature flags
    - Environment configuration
    """

    def __init__(self) -> None:

        self._providers: list[BaseFinanceProvider] = [
            FinnhubProvider(),
        ]

    def providers(self) -> list[BaseFinanceProvider]:
        """
        Returns providers in execution order.
        """

        return self._providers

    def register(
        self,
        provider: BaseFinanceProvider,
    ) -> None:
        """
        Register a new provider.
        """

        self._providers.append(provider)
