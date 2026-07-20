"""
Execution Plan

Defines an ordered collection of agent tasks and their execution state.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from agentops.domains.agents.task import AgentTask, TaskStatus
from agentops.domains.agents.task_result import TaskResult


class ExecutionPlan(BaseModel):
    """
    Represents a workflow of dependent tasks.
    """

    goal: str

    tasks: list[AgentTask] = Field(default_factory=list)

    def add_task(
        self,
        task: AgentTask,
    ) -> None:
        """Add a task to the execution plan."""
        self.tasks.append(task)

    def get_task(
        self,
        task_id: int,
    ) -> AgentTask | None:
        """Retrieve a task by ID."""
        return next(
            (task for task in self.tasks if task.id == task_id),
            None,
        )

    def dependencies_completed(
        self,
        task: AgentTask,
    ) -> bool:
        """Return True if all dependencies completed successfully."""

        return all(
            (dependency := self.get_task(dependency_id)) is not None
            and dependency.status == TaskStatus.COMPLETED
            for dependency_id in task.depends_on
        )

    def dependencies_failed(
        self,
        task: AgentTask,
    ) -> bool:
        """Return True if any dependency failed."""

        return any(
            (dependency := self.get_task(dependency_id)) is not None
            and dependency.status == TaskStatus.FAILED
            for dependency_id in task.depends_on
        )

    def ready_tasks(self) -> list[AgentTask]:
        """
        Return every task that is ready to execute.
        """

        return [
            task
            for task in self.tasks
            if task.status == TaskStatus.PENDING and self.dependencies_completed(task)
        ]

    def next_task(self) -> AgentTask | None:
        """
        Return the next executable task.
        """

        ready = self.ready_tasks()

        return ready[0] if ready else None

    def mark_running(
        self,
        task_id: int,
    ) -> None:
        """Mark a task as running."""

        task = self.get_task(task_id)

        if task:
            task.status = TaskStatus.RUNNING

    def mark_completed(
        self,
        task_id: int,
        result: TaskResult,
    ) -> None:
        """Mark a task as completed."""

        task = self.get_task(task_id)

        if task:
            task.status = TaskStatus.COMPLETED
            task.result = result

    def mark_failed(
        self,
        task_id: int,
        error: str,
    ) -> None:
        """Mark a task as failed."""

        task = self.get_task(task_id)

        if task:
            task.status = TaskStatus.FAILED
            task.error = error

    @property
    def total_tasks(self) -> int:
        return len(self.tasks)

    @property
    def completed_tasks(self) -> int:
        return sum(task.status == TaskStatus.COMPLETED for task in self.tasks)

    @property
    def failed_tasks(self) -> int:
        return sum(task.status == TaskStatus.FAILED for task in self.tasks)

    @property
    def pending_tasks(self) -> int:
        return sum(task.status == TaskStatus.PENDING for task in self.tasks)

    @property
    def running_tasks(self) -> int:
        return sum(task.status == TaskStatus.RUNNING for task in self.tasks)

    @property
    def is_complete(self) -> bool:
        """
        The workflow is complete when every task has either
        completed successfully or failed.
        """

        return (self.completed_tasks + self.failed_tasks) == self.total_tasks

    @property
    def successful(self) -> bool:
        """Return True when every task completed successfully."""

        return self.completed_tasks == self.total_tasks and self.failed_tasks == 0
