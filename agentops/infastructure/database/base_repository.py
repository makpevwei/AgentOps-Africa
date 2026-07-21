"""
Generic SQLAlchemy Repository

Reusable CRUD repository used by all domains.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from sqlalchemy import delete, select
from sqlalchemy.ext.asyncio import AsyncSession

ModelType = TypeVar("ModelType")


class BaseRepository(Generic[ModelType]):
    """Generic SQLAlchemy repository."""

    def __init__(
        self,
        session: AsyncSession,
        model: type[ModelType],
    ) -> None:
        self.session = session
        self.model = model

    async def create(
        self,
        entity: ModelType,
    ) -> ModelType:
        self.session.add(entity)
        await self.session.commit()
        await self.session.refresh(entity)
        return entity

    async def get(
        self,
        entity_id: str,
    ) -> ModelType | None:
        statement = select(self.model).where(
            self.model.id == entity_id,
        )

        result = await self.session.execute(statement)

        return result.scalar_one_or_none()

    async def delete(
        self,
        entity_id: str,
    ) -> None:
        statement = delete(self.model).where(
            self.model.id == entity_id,
        )

        await self.session.execute(statement)
        await self.session.commit()

    async def list(
        self,
    ) -> list[ModelType]:
        statement = select(self.model)

        result = await self.session.execute(statement)

        return list(result.scalars().all())

    async def update(
        self,
        entity: ModelType,
    ) -> ModelType:
        await self.session.commit()
        await self.session.refresh(entity)
        return entity
