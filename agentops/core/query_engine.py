"""
Reusable SQLAlchemy Query Engine.

Provides reusable filtering, searching, sorting and pagination for
SQLAlchemy repositories.
"""

from __future__ import annotations

from typing import Any

from sqlalchemy import Select, asc, desc, func, or_
from sqlalchemy.orm.attributes import InstrumentedAttribute

from agentops.core.specification import QuerySpecification


class QueryEngine:
    """Reusable SQLAlchemy query builder."""

    @staticmethod
    def apply_filters(
        statement: Select,
        model: type,
        specification: QuerySpecification,
    ) -> Select:
        """Apply equality filters."""

        for field, value in specification.filters.items():
            if value is None:
                continue

            if hasattr(model, field):
                statement = statement.where(
                    getattr(model, field) == value
                )

        return statement

    @staticmethod
    def apply_search(
        statement: Select,
        model: type,
        specification: QuerySpecification,
        *,
        searchable_fields: list[str],
    ) -> Select:
        """Apply free-text search."""

        if not specification.search:
            return statement

        search_conditions = []

        for field in searchable_fields:
            if hasattr(model, field):
                column = getattr(model, field)
                search_conditions.append(column.ilike(f"%{specification.search}%"))

        if search_conditions:
            statement = statement.where(or_(*search_conditions))

        return statement

    @staticmethod
    def apply_sorting(
        statement: Select,
        *,
        allowed_fields: dict[str, InstrumentedAttribute[Any]],
        specification: QuerySpecification,
    ) -> Select:
        """Apply sorting."""

        if not specification.sort_by:
            return statement

        column = allowed_fields.get(specification.sort_by)

        if column is None:
            return statement

        if specification.sort_order.lower() == "desc":
            return statement.order_by(desc(column))

        return statement.order_by(asc(column))

    @staticmethod
    def apply_pagination(
        statement: Select,
        specification: QuerySpecification,
    ) -> Select:
        """Apply pagination."""

        offset = (specification.page - 1) * specification.page_size

        return (
            statement
            .offset(offset)
            .limit(specification.page_size)
        )

    @staticmethod
    def count_statement(
        statement: Select,
    ) -> Select:
        """Build count query."""

        return statement.with_only_columns(
            func.count(),
        ).order_by(None)