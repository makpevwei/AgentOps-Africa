"""
Opportunity Query Models.
"""

from __future__ import annotations

from pydantic import Field

from agentops.core.query import Query
from agentops.domains.opportunities.models import (
    OpportunityPriority,
    OpportunityStatus,
)


class OpportunityQuery(Query):
    """Query parameters for listing opportunities."""

    status: OpportunityStatus | None = Field(
        default=None,
        description="Filter by opportunity status.",
    )

    priority: OpportunityPriority | None = Field(
        default=None,
        description="Filter by opportunity priority.",
    )

    company_name: str | None = Field(
        default=None,
        description="Filter by company name.",
    )

    sort_by: str | None = Field(
        default="created_at",
        description="Field used for sorting.",
    )

    sort_order: str = Field(
        default="desc",
        pattern="^(asc|desc)$",
        description="Sort direction.",
    )