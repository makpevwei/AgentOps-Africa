"""
Reusable SQLAlchemy Repository Utilities.
"""

from __future__ import annotations

from sqlalchemy import Select, asc, desc


class RepositoryUtils:
    """Reusable helpers for SQLAlchemy repositories."""

    @staticmethod
    def apply_sorting(
        statement: Select,
        *,
        model: type,
        sort_by: str | None,
        sort_order: str = "asc",
    ) -> Select:
        """Apply sorting to a SQLAlchemy statement."""

        if not sort_by:
            return statement

        if not hasattr(model, sort_by):
            return statement

        column = getattr(model, sort_by)

        if sort_order.lower() == "desc":
            return statement.order_by(desc(column))

        return statement.order_by(asc(column))