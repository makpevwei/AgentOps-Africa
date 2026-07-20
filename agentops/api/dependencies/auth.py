from __future__ import annotations

from uuid import UUID

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from agentops.api.dependencies.database import get_db
from agentops.core.jwt import decode_token
from agentops.db.models.user import User, UserRole
from agentops.repositories.user_repository import UserRepository

bearer_scheme = HTTPBearer(
    auto_error=True,
)


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme),
    db: AsyncSession = Depends(get_db),
) -> User:
    """
    Return the authenticated user represented by the JWT.
    """

    try:
        payload = decode_token(credentials.credentials)

        subject = payload.get("sub")

        if subject is None:
            raise ValueError("Missing subject claim.")

        user_id = UUID(subject)

    except (JWTError, ValueError) as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired authentication token.",
        ) from exc

    repository = UserRepository(db)

    user = await repository.get_by_id(user_id)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found.",
        )

    return user


async def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    """
    Return the authenticated active user.
    """

    if not current_user.is_active:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="User account is inactive.",
        )

    return current_user


async def require_staff(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """
    Require STAFF or ADMIN privileges.
    """

    if current_user.role not in {
        UserRole.ADMIN,
        UserRole.STAFF,
    }:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Staff access required.",
        )

    return current_user


async def require_admin(
    current_user: User = Depends(get_current_active_user),
) -> User:
    """
    Require ADMIN privileges.
    """

    if current_user.role != UserRole.ADMIN:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Administrator access required.",
        )

    return current_user
