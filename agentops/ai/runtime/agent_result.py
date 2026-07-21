"""
Agent Result
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AgentResult:
    """Standard result returned by every AI agent."""

    success: bool

    output: Any = None

    reasoning: str | None = None

    execution_time: float = 0.0

    metadata: dict[str, Any] = field(default_factory=dict)
