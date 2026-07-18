"""
Research Orchestrator.

Coordinates research across one or more research providers.
"""

from __future__ import annotations

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.research.provider_registry import (
    ResearchProviderRegistry,
)
from agentops.domains.research.research_models import (
    ResearchResult,
)


class ResearchOrchestrator:
    """
    Executes research using all supported providers and
    merges the results into a single ResearchResult.
    """

    def __init__(
        self,
        registry: ResearchProviderRegistry | None = None,
    ) -> None:
        self.registry = registry or ResearchProviderRegistry()

    def research(
        self,
        company: CompanyProfile,
    ) -> ResearchResult:
        """
        Execute research using every supporting provider.
        """

        providers = self.registry.get_providers(company)

        result = ResearchResult()

        for provider in providers:
            provider_result = provider.research(company)

            if provider_result.profile.company_name:
                result.profile = provider_result.profile

            result.news.extend(provider_result.news)
            result.sources.extend(provider_result.sources)

        return result
