"""
Execution Context

Holds the accumulated results produced while executing an execution plan.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field


class ExecutionContext(BaseModel):
    """
    Shared state produced during execution.

    Each agent writes its output into this context so later
    tasks can consume previous results.
    """

    company: Any | None = None

    finance: Any | None = None

    research: Any | None = None

    metadata: dict[str, Any] = Field(default_factory=dict)

    errors: list[str] = Field(default_factory=list)

    completed_tasks: list[int] = Field(default_factory=list)

    def set_result(
        self,
        service: str,
        result: Any,
    ) -> None:
        """
        Store the result for a service.
        """

        setattr(self, service, result)

    def get_result(
        self,
        service: str,
    ) -> Any:
        """
        Retrieve the result produced by a service.
        """

        return getattr(self, service, None)

    def add_error(
        self,
        error: str,
    ) -> None:
        """
        Record an execution error.
        """

        self.errors.append(error)

    def mark_completed(
        self,
        task_id: int,
    ) -> None:
        """
        Record a completed task.
        """

        self.completed_tasks.append(task_id)

    @property
    def successful(self) -> bool:
        """
        True when no execution errors occurred.
        """

        return not self.errors
