"""
Enterprise Company Resolver

Resolves company names, aliases and stock tickers
into a normalized CompanyProfile object.
"""

from rapidfuzz import fuzz, process

from agentops.domains.research.models import CompanyProfile


class CompanyResolver:
    """
    Resolves company names into normalized CompanyProfile objects.
    """

    def __init__(self):

        # ==========================================================
        # Local Company Cache
        # ==========================================================

        self._companies = {
            "gtco": CompanyProfile(
                company_name="GTCO Plc",
                aliases=[
                    "gtb",
                    "guaranty trust",
                    "guaranty trust bank",
                ],
                ticker="GTCO",
                exchange="NGX",
                country="Nigeria",
                industry="Banking",
            ),

            "zenith": CompanyProfile(
                company_name="Zenith Bank Plc",
                aliases=[
                    "zenith",
                    "zenith bank",
                ],
                ticker="ZENITHBANK",
                exchange="NGX",
                country="Nigeria",
                industry="Banking",
            ),

            "access": CompanyProfile(
                company_name="Access Holdings Plc",
                aliases=[
                    "access",
                    "access bank",
                ],
                ticker="ACCESSCORP",
                exchange="NGX",
                country="Nigeria",
                industry="Banking",
            ),

            "uba": CompanyProfile(
                company_name="United Bank for Africa Plc",
                aliases=[
                    "uba",
                    "united bank for africa",
                ],
                ticker="UBA",
                exchange="NGX",
                country="Nigeria",
                industry="Banking",
            ),

            "mtn": CompanyProfile(
                company_name="MTN Nigeria",
                aliases=[
                    "mtn",
                ],
                ticker="MTNN",
                exchange="NGX",
                country="Nigeria",
                industry="Telecommunications",
            ),

            "dangote": CompanyProfile(
                company_name="Dangote Cement Plc",
                aliases=[
                    "dangote",
                    "dangote cement",
                ],
                ticker="DANGCEM",
                exchange="NGX",
                country="Nigeria",
                industry="Manufacturing",
            ),

            "apple": CompanyProfile(
                company_name="Apple Inc.",
                aliases=[
                    "apple",
                ],
                ticker="AAPL",
                exchange="NASDAQ",
                country="USA",
                industry="Technology",
            ),

            "microsoft": CompanyProfile(
                company_name="Microsoft Corporation",
                aliases=[
                    "microsoft",
                    "msft",
                ],
                ticker="MSFT",
                exchange="NASDAQ",
                country="USA",
                industry="Technology",
            ),

            "tesla": CompanyProfile(
                company_name="Tesla Inc.",
                aliases=[
                    "tesla",
                ],
                ticker="TSLA",
                exchange="NASDAQ",
                country="USA",
                industry="Automotive",
            ),
        }

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