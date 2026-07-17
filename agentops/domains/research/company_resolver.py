"""
Enterprise Company Resolver

Responsible ONLY for resolving known companies.

Responsibilities
----------------
1. Load built-in company dataset
2. Load learned company registry
3. Exact matching
4. Fuzzy matching

It NEVER:
- discovers companies
- calls an LLM
- searches Tavily
- saves companies
"""

from rapidfuzz import fuzz, process

from agentops.domains.research.company_data import COMPANIES
from agentops.domains.research.company_registry import CompanyRegistry
from agentops.domains.research.models import CompanyProfile


class CompanyResolver:
    """
    Resolves already-known companies.

    Unknown companies should be handled
    by CompanyService.
    """

    def __init__(self):

        self.registry = CompanyRegistry()

        self.lookup = {}

        # =====================================================
        # Built-in Companies
        # =====================================================

        for company in COMPANIES.values():

            names = [
                company.company_name,
                *company.aliases,
            ]

            for name in names:

                self.lookup[name.lower()] = company

        # =====================================================
        # Learned Companies
        # =====================================================

        for company in self.registry.load():

            names = [
                company.company_name,
                *company.aliases,
            ]

            for name in names:

                self.lookup[name.lower()] = company

    def resolve(
        self,
        query: str,
    ) -> CompanyProfile | None:

        query = query.strip().lower()

        # =====================================================
        # Exact Match
        # =====================================================

        if query in self.lookup:

            return self.lookup[query]

        # =====================================================
        # Fuzzy Match
        # =====================================================

        match = process.extractOne(
            query,
            self.lookup.keys(),
            scorer=fuzz.WRatio,
        )

        if match:

            best_match, score, _ = match

            if score >= 85:

                return self.lookup[best_match]

        # =====================================================
        # Unknown Company
        # =====================================================

        return None