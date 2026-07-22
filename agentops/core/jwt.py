from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any

from jose import JWTError, jwt

from agentops.config import settings


def _create_token(
    *,
    subject: str,
    token_type: str,
    expires_delta: timedelta,
    additional_claims: dict[str, Any] | None = None,
) -> str:
    """
    Create a signed JWT.
    """

    expire = datetime.now(UTC) + expires_delta

    payload: dict[str, Any] = {
        "sub": subject,
        "type": token_type,
        "exp": expire,
    }

    if additional_claims:
        payload.update(additional_claims)

    return jwt.encode(
        payload,
        settings.JWT_SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def create_access_token(
    subject: str,
    additional_claims: dict[str, Any] | None = None,
) -> str:
    """
    Create an access token.
    """

    return _create_token(
        subject=subject,
        token_type="access",
        expires_delta=timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES,
        ),
        additional_claims=additional_claims,
    )


def create_refresh_token(
    subject: str,
    additional_claims: dict[str, Any] | None = None,
) -> str:
    """
    Create a refresh token.
    """

    return _create_token(
        subject=subject,
        token_type="refresh",
        expires_delta=timedelta(
            days=settings.REFRESH_TOKEN_EXPIRE_DAYS,
        ),
        additional_claims=additional_claims,
    )


def decode_token(
    token: str,
) -> dict[str, Any]:
    """
    Decode and validate a JWT.
    """

    return jwt.decode(
        token,
        settings.JWT_SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM],
    )


def verify_token_type(
    payload: dict[str, Any],
    expected_type: str,
) -> None:
    """
    Ensure the JWT is of the expected type.
    """

    token_type = payload.get("type")

    if token_type != expected_type:
        raise JWTError("Invalid token type.")
