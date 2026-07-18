"""
Research Provider Registry.
"""

from __future__ import annotations

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.research.base_provider import BaseResearchProvider
from agentops.domains.research.static_provider import StaticResearchProvider


class ResearchProviderRegistry:
    """
    Registry of available Research Providers.
    """

    def __init__(self) -> None:

        self.providers: list[BaseResearchProvider] = [
            StaticResearchProvider(),
        ]

    def register(
        self,
        provider: BaseResearchProvider,
    ) -> None:
        """
        Register a new research provider.
        """

        self.providers.append(provider)

    def get_providers(
        self,
        company: CompanyProfile,
    ) -> list[BaseResearchProvider]:
        """
        Return all providers capable of researching the company.
        """

        return [provider for provider in self.providers if provider.supports(company)]
