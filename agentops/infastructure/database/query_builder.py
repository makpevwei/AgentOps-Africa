"""
Reusable SQLAlchemy Query Builder.

Provides search, filtering, sorting and pagination for repositories.
"""

from __future__ import annotations

from sqlalchemy import Select, asc, desc


class QueryBuilder:
    """Utility methods for building SQLAlchemy queries."""

    @staticmethod
    def sort(
        statement: Select,
        model: type,
        *,
        sort_by: str | None,
        sort_order: str,
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
