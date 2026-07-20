from uuid import UUID

from sqlalchemy import exists, select
from sqlalchemy.ext.asyncio import AsyncSession

from agentops.db.models.user import User


class UserRepository:
    """Repository for user database operations."""

    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, user: User) -> User:
        """
        Persist a new user to the database.
        """
        try:
            self.session.add(user)
            await self.session.commit()
            await self.session.refresh(user)
            return user
        except Exception:
            await self.session.rollback()
            raise

    async def get_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email address.
        """
        result = await self.session.execute(select(User).where(User.email == email))
        return result.scalar_one_or_none()

    async def exists_by_email(self, email: str) -> bool:
        """
        Check whether a user already exists with the given email.
        """
        result = await self.session.scalar(select(exists().where(User.email == email)))
        return bool(result)

    async def get_by_id(self, user_id: UUID) -> User | None:
        """
        Retrieve a user by ID.
        """
        result = await self.session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()

    async def update(self, user: User) -> User:
        """
        Persist changes made to a user.
        """
        try:
            await self.session.commit()
            await self.session.refresh(user)
            return user
        except Exception:
            await self.session.rollback()
            raise

    async def delete(self, user: User) -> None:
        """
        Delete a user from the database.
        """
        try:
            await self.session.delete(user)
            await self.session.commit()
        except Exception:
            await self.session.rollback()
            raise
