"""
Generic Query Specification.

Encapsulates pagination, filtering, searching and sorting.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class QuerySpecification:
    """Generic query specification."""

    page: int = 1

    page_size: int = 20

    search: str | None = None

    sort_by: str | None = None

    sort_order: str = "desc"

    filters: dict[str, object] = field(default_factory=dict)
