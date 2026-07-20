"""
Opportunity Domain Models

Core business entities for Opportunity Management.
"""

from datetime import datetime
from enum import StrEnum

from pydantic import BaseModel, Field


class OpportunityStatus(StrEnum):
    """Lifecycle of a business opportunity."""

    NEW = "new"
    RESEARCHING = "researching"
    PROPOSAL_DRAFTED = "proposal_drafted"
    QUOTATION_READY = "quotation_ready"
    AWAITING_APPROVAL = "awaiting_approval"
    SENT = "sent"
    NEGOTIATION = "negotiation"
    WON = "won"
    LOST = "lost"


class OpportunitySource(StrEnum):
    """Where the opportunity originated."""

    EMAIL = "email"
    TELEGRAM = "telegram"
    WHATSAPP = "whatsapp"
    WEBSITE = "website"
    LINKEDIN = "linkedin"
    MANUAL = "manual"
    API = "api"


class OpportunityPriority(StrEnum):
    """Business priority."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    URGENT = "urgent"


class Opportunity(BaseModel):
    """Canonical representation of a business opportunity."""

    id: str
    organization_id: str

    title: str
    description: str

    company_id: str | None = None
    company_name: str

    contact_name: str | None = None
    email: str | None = None
    phone: str | None = None

    priority: OpportunityPriority = OpportunityPriority.MEDIUM

    source: OpportunitySource = OpportunitySource.MANUAL
    status: OpportunityStatus = OpportunityStatus.NEW

    assigned_agent: str | None = None

    research_report_id: str | None = None
    proposal_id: str | None = None
    quotation_id: str | None = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
