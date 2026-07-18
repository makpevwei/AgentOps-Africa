"""
Agent Task Models

Defines the basic unit of work executed by agents.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class TaskStatus(str, Enum):
    """Execution status of an AgentTask."""

    PENDING = "pending"
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"


class AgentTask(BaseModel):
    """
    Represents a single executable unit of work.

    Tasks may declare dependencies on other tasks, allowing the
    execution plan to evolve from a simple sequential pipeline into
    a directed acyclic graph (DAG) suitable for parallel execution.
    """

    # Unique task identifier
    id: int

    # Optional human-readable name
    name: str | None = None

    # Service responsible for execution
    service: str

    # Action to perform
    action: str

    # Human-readable description
    description: str

    # Task-specific input
    payload: dict = Field(default_factory=dict)

    # IDs of prerequisite tasks
    depends_on: list[int] = Field(default_factory=list)

    # Runtime state
    status: TaskStatus = TaskStatus.PENDING

    # Task output
    result: dict | None = None

    # Failure reason
    error: str | None = None

    @property
    def is_complete(self) -> bool:
        """Return True if the task completed successfully."""
        return self.status == TaskStatus.COMPLETED

    @property
    def is_failed(self) -> bool:
        """Return True if the task failed."""
        return self.status == TaskStatus.FAILED

    @property
    def is_pending(self) -> bool:
        """Return True if the task has not started."""
        return self.status == TaskStatus.PENDING
