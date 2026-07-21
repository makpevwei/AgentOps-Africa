"""
Agent Context

Shared execution context passed to every AI agent.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass(slots=True)
class AgentContext:
    """Execution context for an AI agent."""

    user_id: str

    organization_id: str

    session_id: str

    goal: str

    inputs: dict[str, Any] = field(default_factory=dict)

    metadata: dict[str, Any] = field(default_factory=dict)