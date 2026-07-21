"""
Reusable Query Models

Shared query parameters used across the AgentOps platform.
"""

from __future__ import annotations

from pydantic import Field

from agentops.core.pagination import Pagination


class Query(Pagination):
    """Base query model for list endpoints."""

    search: str | None = Field(
        default=None,
        description="Free-text search.",
    )

    sort_by: str | None = Field(
        default=None,
        description="Field to sort by.",
    )

    sort_order: str = Field(
        default="asc",
        pattern="^(asc|desc)$",
        description="Sort direction.",
    )
