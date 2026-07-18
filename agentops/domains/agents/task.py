"""
Agent Task Models

Defines the basic unit of work executed by agents.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentTask(BaseModel):
    """
    Represents a single unit of work.
    """

    id: int

    service: str

    action: str

    description: str

    payload: dict = Field(default_factory=dict)

    status: TaskStatus = TaskStatus.PENDING

    result: dict | None = None

    error: str | None = None