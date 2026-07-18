"""
Agent Task Models

Defines the basic unit of work executed by agents.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field

from agentops.domains.agents.task_result import TaskResult


class TaskStatus(str, Enum):
    """Execution status of an AgentTask."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentTask(BaseModel):
    """
    Represents a single executable unit of work.
    """

    id: int

    name: str | None = None

    service: str

    action: str

    description: str

    payload: dict = Field(default_factory=dict)

    depends_on: list[int] = Field(default_factory=list)

    status: TaskStatus = TaskStatus.PENDING

    result: TaskResult | None = None

    error: str | None = None

    @property
    def is_complete(self) -> bool:
        return self.status == TaskStatus.COMPLETED

    @property
    def is_failed(self) -> bool:
        return self.status == TaskStatus.FAILED

    @property
    def is_pending(self) -> bool:
        return self.status == TaskStatus.PENDING
