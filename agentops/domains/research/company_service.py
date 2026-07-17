"""
Enterprise Company Service

Coordinates company resolution across:

1. Local company dataset
2. Learned company registry
3. Company discovery
4. LLM normalization

This is the ONLY class the rest of the application
should use for resolving companies.
"""

from agentops.domains.research.company_discovery import CompanyDiscovery
from agentops.domains.research.company_normalizer import CompanyNormalizer
from agentops.domains.research.company_registry import CompanyRegistry
from agentops.domains.research.company_resolver import CompanyResolver
from agentops.domains.research.models import CompanyProfile


class CompanyService:

    def __init__(self):

        self.resolver = CompanyResolver()

        self.discovery = CompanyDiscovery()

        self.normalizer = CompanyNormalizer()

        self.registry = CompanyRegistry()

    def resolve(
        self,
        query: str,
    ) -> CompanyProfile:

        # -----------------------------------
        # 1. Try Local Resolver
        # -----------------------------------

        company = self.resolver.resolve(query)

        if company:

            return company

        # -----------------------------------
        # 2. Discover Company
        # -----------------------------------

        findings = self.discovery.search(query)

        # -----------------------------------
        # 3. Normalize
        # -----------------------------------

        company = self.normalizer.normalize(
            query=query,
            findings=findings,
        )

        # -----------------------------------
        # 4. Save
        # -----------------------------------

        self.registry.save(company)

        # -----------------------------------
        # 5. Reload Resolver
        # -----------------------------------

        self.resolver = CompanyResolver()

        return company