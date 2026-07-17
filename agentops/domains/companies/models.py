"""
Companies Domain Models

Core business models for company identity and metadata.
"""

from pydantic import BaseModel, Field


class CompanyProfile(BaseModel):
    """
    Canonical representation of a company.
    """

    company_name: str

    aliases: list[str] = Field(default_factory=list)

    # Canonical ticker used internally
    ticker: str | None = None

    # Provider-specific finance symbol
    finance_symbol: str | None = None

    exchange: str | None = None

    country: str | None = None

    industry: str | None = None

    sector: str | None = None

    website: str | None = None