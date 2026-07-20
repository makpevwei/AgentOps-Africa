from __future__ import annotations

from datetime import UTC, datetime
from uuid import UUID

from jose import JWTError
from sqlalchemy.ext.asyncio import AsyncSession

from agentops.api.schemas.auth import (
    LoginRequest,
    RefreshTokenRequest,
    RegisterRequest,
    TokenResponse,
)
from agentops.core.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token,
    verify_token_type,
)
from agentops.core.security import (
    hash_password,
    verify_password,
)
from agentops.db.models.user import User
from agentops.repositories.user_repository import UserRepository


class AuthenticationError(Exception):
    """Raised when authentication fails."""


class UserAlreadyExistsError(Exception):
    """Raised when an email is already registered."""


class AuthService:
    """Business logic for authentication."""

    def __init__(self, session: AsyncSession):
        self.repository = UserRepository(session)

    def _create_token_response(
        self,
        user: User,
    ) -> TokenResponse:
        """
        Generate authentication tokens.
        """

        claims = {
            "email": user.email,
            "role": user.role.value,
        }

        access_token = create_access_token(
            subject=str(user.id),
            additional_claims=claims,
        )

        refresh_token = create_refresh_token(
            subject=str(user.id),
        )

        return TokenResponse(
            access_token=access_token,
            refresh_token=refresh_token,
        )

    async def register(
        self,
        data: RegisterRequest,
    ) -> TokenResponse:

        if await self.repository.exists_by_email(data.email):
            raise UserAlreadyExistsError("An account already exists with this email.")

        user = User(
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            password_hash=hash_password(data.password),
        )

        user = await self.repository.create(user)

        return self._create_token_response(user)

    async def login(
        self,
        data: LoginRequest,
    ) -> TokenResponse:

        user = await self.repository.get_by_email(data.email)

        if user is None:
            raise AuthenticationError("Invalid email or password.")

        if not verify_password(
            data.password,
            user.password_hash,
        ):
            raise AuthenticationError("Invalid email or password.")

        if not user.is_active:
            raise AuthenticationError("This account has been disabled.")

        user.last_login = datetime.now(UTC)

        await self.repository.update(user)

        return self._create_token_response(user)

    async def refresh(
        self,
        data: RefreshTokenRequest,
    ) -> TokenResponse:
        """
        Refresh authentication tokens.
        """

        try:
            payload = decode_token(data.refresh_token)

            verify_token_type(
                payload,
                "refresh",
            )

            subject = payload.get("sub")

            if subject is None:
                raise AuthenticationError("Invalid refresh token.")

            user = await self.repository.get_by_id(
                UUID(subject),
            )

        except (JWTError, ValueError) as exc:
            raise AuthenticationError("Invalid refresh token.") from exc

        if user is None:
            raise AuthenticationError("User not found.")

        if not user.is_active:
            raise AuthenticationError("User account is inactive.")

        return self._create_token_response(user)
