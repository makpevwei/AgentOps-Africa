"""
Reusable Pagination Models

Shared pagination models used across the AgentOps platform.
"""

from __future__ import annotations

from collections.abc import Sequence
from math import ceil
from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class Pagination(BaseModel):
    """Pagination request parameters."""

    page: int = Field(
        default=1,
        ge=1,
        description="Current page number.",
    )

    page_size: int = Field(
        default=20,
        ge=1,
        le=100,
        description="Number of records per page.",
    )


class Page(BaseModel, Generic[T]):
    """Generic paginated response."""

    items: list[T]

    total: int

    page: int

    page_size: int

    total_pages: int

    has_next: bool

    has_previous: bool

    @classmethod
    def create(
        cls,
        *,
        items: Sequence[T],
        total: int,
        page: int,
        page_size: int,
    ) -> Page[T]:
        """Create a paginated response."""

        total_pages = max(
            1,
            ceil(total / page_size),
        )

        return cls(
            items=list(items),
            total=total,
            page=page,
            page_size=page_size,
            total_pages=total_pages,
            has_next=page < total_pages,
            has_previous=page > 1,
        )
