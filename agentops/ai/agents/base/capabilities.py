"""
Shared capability constants for AI agents.
"""

from enum import StrEnum


class Capability(StrEnum):
    COMPANY_RESEARCH = "company_research"
    MARKET_ANALYSIS = "market_analysis"
    WEB_SEARCH = "web_search"

    PROPOSAL_GENERATION = "proposal_generation"
    QUOTATION_GENERATION = "quotation_generation"

    CRM = "crm"
    SALES = "sales"

    FINANCE = "finance"
    ACCOUNTING = "accounting"

    HR = "hr"
    RECRUITMENT = "recruitment"

    EMAIL = "email"
    CALENDAR = "calendar"

    DOCUMENT_ANALYSIS = "document_analysis"
    SUMMARIZATION = "summarization"