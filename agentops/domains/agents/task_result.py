"""
Task Result Models.

Defines the standard result returned by all Agent Services.
"""

from __future__ import annotations

from datetime import UTC, datetime
from typing import Any

from pydantic import BaseModel, Field


class TaskResult(BaseModel):
    """
    Standard result returned by every Agent Service.

    This provides a consistent contract between Agent Services
    and the Executor regardless of the type of work performed.
    """

    #
    # Overall execution status
    #
    success: bool = True

    #
    # Primary output produced by the task.
    #
    output: Any = None

    #
    # Additional execution metadata.
    #
    metadata: dict[str, Any] = Field(default_factory=dict)

    #
    # Provider used (Finnhub, Tavily, OpenAI, etc.)
    #
    provider: str | None = None

    #
    # Non-fatal warnings.
    #
    warnings: list[str] = Field(default_factory=list)

    #
    # Error message when success=False.
    #
    error: str | None = None

    #
    # Execution duration.
    #
    duration_ms: float | None = None

    #
    # Timestamp.
    #
    created_at: datetime = Field(
        default_factory=lambda: datetime.now(UTC)
    )