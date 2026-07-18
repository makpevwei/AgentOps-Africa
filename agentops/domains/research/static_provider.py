"""
Static Research Provider.

Returns mock research data for testing the Research pipeline.
"""

from __future__ import annotations

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.research.base_provider import BaseResearchProvider
from agentops.domains.research.research_models import (
    NewsArticle,
    ResearchProfile,
    ResearchResult,
    ResearchSource,
)


class StaticResearchProvider(BaseResearchProvider):
    """
    Mock provider used while building the Research pipeline.
    """

    name = "Static"

    def supports(
        self,
        company: CompanyProfile,
    ) -> bool:
        return True

    def research(
        self,
        company: CompanyProfile,
    ) -> ResearchResult:

        profile = ResearchProfile(
            company_name=company.company_name,
            description=(
                f"{company.company_name} is a sample company "
                "returned by the Static Research Provider."
            ),
            industry=company.industry,
            website=company.website,
        )

        article = NewsArticle(
            title=f"{company.company_name} launches new initiative",
            summary="This is placeholder research data.",
            source="Static Provider",
        )

        source = ResearchSource(
            provider=self.name,
            confidence=1.0,
        )

        return ResearchResult(
            profile=profile,
            news=[article],
            sources=[source],
        )
