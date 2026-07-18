"""
Execution Plan

Defines an ordered collection of agent tasks.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from agentops.domains.agents.task import AgentTask, TaskStatus
from agentops.domains.agents.task_result import TaskResult


class ExecutionPlan(BaseModel):
    """
    Collection of tasks representing an execution workflow.

    Tasks may declare dependencies on one another, allowing the plan
    to evolve into a Directed Acyclic Graph (DAG).
    """

    goal: str

    tasks: list[AgentTask] = Field(default_factory=list)

    def add_task(
        self,
        task: AgentTask,
    ) -> None:
        """
        Add a task to the execution plan.
        """
        self.tasks.append(task)

    def get_task(
        self,
        task_id: int,
    ) -> AgentTask | None:
        """
        Retrieve a task by its identifier.
        """
        return next(
            (task for task in self.tasks if task.id == task_id),
            None,
        )

    def dependencies_completed(
        self,
        task: AgentTask,
    ) -> bool:
        """
        Returns True only if all dependencies completed successfully.
        """

        for dependency_id in task.depends_on:
            dependency = self.get_task(dependency_id)

            if dependency is None:
                return False

            if dependency.status != TaskStatus.COMPLETED:
                return False

        return True

    def dependencies_failed(
        self,
        task: AgentTask,
    ) -> bool:
        """
        Returns True if any dependency has failed.
        """

        for dependency_id in task.depends_on:
            dependency = self.get_task(dependency_id)

            if dependency and dependency.status == TaskStatus.FAILED:
                return True

        return False

    def ready_tasks(
        self,
    ) -> list[AgentTask]:
        """
        Return all executable tasks.
        """

        return [
            task
            for task in self.tasks
            if (
                task.status == TaskStatus.PENDING
                and self.dependencies_completed(task)
            )
        ]

    def blocked_tasks(
        self,
    ) -> list[AgentTask]:
        """
        Return pending tasks that can never execute because one
        of their dependencies failed.
        """

        return [
            task
            for task in self.tasks
            if (
                task.status == TaskStatus.PENDING
                and self.dependencies_failed(task)
            )
        ]

    def next_pending_task(
        self,
    ) -> AgentTask | None:
        """
        Return the next executable task.
        """
        ready = self.ready_tasks()

        return ready[0] if ready else None

    def mark_running(
        self,
        task_id: int,
    ) -> None:
        """
        Mark a task as running.
        """
        if task := self.get_task(task_id):
            task.status = TaskStatus.RUNNING

    def mark_completed(
        self,
        task_id: int,
        result: TaskResult,
    ) -> None:
        """
        Mark a task as completed.
        """
        if task := self.get_task(task_id):
            task.status = TaskStatus.COMPLETED
            task.result = result

    def mark_failed(
        self,
        task_id: int,
        error: str,
    ) -> None:
        """
        Mark a task as failed.
        """
        if task := self.get_task(task_id):
            task.status = TaskStatus.FAILED
            task.error = error

    @property
    def total_tasks(self) -> int:
        """Total number of tasks."""
        return len(self.tasks)

    @property
    def completed_tasks(self) -> int:
        """Number of completed tasks."""
        return sum(
            task.status == TaskStatus.COMPLETED
            for task in self.tasks
        )

    @property
    def failed_tasks(self) -> int:
        """Number of failed tasks."""
        return sum(
            task.status == TaskStatus.FAILED
            for task in self.tasks
        )

    @property
    def running_tasks(self) -> int:
        """Number of running tasks."""
        return sum(
            task.status == TaskStatus.RUNNING
            for task in self.tasks
        )

    @property
    def pending_tasks(self) -> int:
        """Number of pending tasks."""
        return sum(
            task.status == TaskStatus.PENDING
            for task in self.tasks
        )

    @property
    def has_ready_tasks(self) -> bool:
        """
        Returns True if there are executable tasks.
        """
        return bool(self.ready_tasks())

    @property
    def successful(self) -> bool:
        """
        Returns True when every task completed successfully.
        """
        return (
            self.completed_tasks == self.total_tasks
            and self.failed_tasks == 0
        )

    @property
    def is_failed(self) -> bool:
        """
        Returns True if one or more tasks failed.
        """
        return self.failed_tasks > 0

    @property
    def is_complete(self) -> bool:
        """
        Workflow is complete when there are no runnable tasks left.
        """
        return not self.has_ready_tasks