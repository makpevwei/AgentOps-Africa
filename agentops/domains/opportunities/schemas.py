"""
Opportunity API Schemas

Request and response models for the Opportunity API.
"""

from datetime import datetime

from pydantic import BaseModel, ConfigDict, Field

from .models import (
    OpportunityPriority,
    OpportunitySource,
    OpportunityStatus,
)


class OpportunityCreate(BaseModel):
    """Request payload for creating a new opportunity."""

    title: str = Field(..., min_length=3, max_length=200)

    description: str = Field(..., min_length=10)

    company_name: str = Field(..., min_length=2)

    contact_name: str | None = None

    email: str | None = None

    phone: str | None = None

    source: OpportunitySource = OpportunitySource.MANUAL


class OpportunityUpdate(BaseModel):
    """Request payload for updating an opportunity."""

    title: str | None = Field(default=None, min_length=3, max_length=200)

    description: str | None = Field(default=None, min_length=10)

    contact_name: str | None = None

    email: str | None = None

    phone: str | None = None

    status: OpportunityStatus | None = None

    priority: OpportunityPriority | None = None


class OpportunityResponse(BaseModel):
    """Response returned to API clients."""

    model_config = ConfigDict(from_attributes=True)

    id: str

    organization_id: str

    title: str

    description: str

    company_id: str | None = None

    company_name: str

    contact_name: str | None = None

    email: str | None = None

    phone: str | None = None

    priority: OpportunityPriority | None = None

    source: OpportunitySource

    status: OpportunityStatus

    assigned_agent: str | None = None

    created_at: datetime

    updated_at: datetime


class OpportunitySummary(BaseModel):
    """Compact representation used in dashboards and lists."""

    id: str

    title: str

    company_name: str

    status: OpportunityStatus

    priority: OpportunityPriority | None = None
