"""
Enterprise Company Resolver

Resolves company names, aliases and stock tickers
into a normalized CompanyProfile object.
"""

from rapidfuzz import fuzz, process

from agentops.domains.research.company_data import COMPANIES
from agentops.domains.research.models import CompanyProfile


class CompanyResolver:
    """
    Resolves company names into normalized CompanyProfile objects.
    """

    def __init__(self):

        # ==========================================================
        # Local Company Cache
        # ==========================================================

        self._companies = COMPANIES

        # ==========================================================
        # Build Lookup Dictionary
        # ==========================================================

        self._lookup = {}

        for company in self._companies.values():

            # Company name
            self._lookup[company.company_name.lower()] = company

            # Ticker
            if company.ticker:
                self._lookup[company.ticker.lower()] = company

            # Aliases
            for alias in company.aliases:
                self._lookup[alias.lower()] = company

    # ==============================================================
    # Resolve Company
    # ==============================================================

    def resolve(self, query: str) -> CompanyProfile | None:
        """
        Resolve a company from user input.

        Resolution order:

        1. Exact Match
        2. Fuzzy Match
        """

        query = query.lower().strip()

        # ----------------------------------------------------------
        # Exact Match
        # ----------------------------------------------------------

        if query in self._lookup:
            return self._lookup[query]

        # ----------------------------------------------------------
        # Fuzzy Match
        # ----------------------------------------------------------

        match = process.extractOne(
            query,
            self._lookup.keys(),
            scorer=fuzz.WRatio,
        )

        if match:

            best_match, score, _ = match

            if score >= 80:
                return self._lookup[best_match]

        # ----------------------------------------------------------
        # Nothing Found
        # ----------------------------------------------------------

        return None