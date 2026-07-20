"""
Standard API Response Models

Reusable response models for the entire AgentOps platform.
"""

from __future__ import annotations

from typing import Generic, TypeVar

from pydantic import BaseModel, Field

T = TypeVar("T")


class APIResponse(BaseModel, Generic[T]):
    """
    Standard successful API response.
    """

    success: bool = True

    message: str = "Request completed successfully."

    data: T | None = None


class ErrorResponse(BaseModel):
    """
    Standard error response.
    """

    success: bool = False

    message: str

    errors: list[str] = Field(default_factory=list)