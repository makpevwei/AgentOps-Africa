"""
Enterprise Company Data

This file contains locally known companies.

No business logic should exist here.
Only company data.
"""

from agentops.domains.companies.models import CompanyProfile

COMPANIES = {
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
