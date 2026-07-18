"""
Execution Plan

Defines an ordered collection of agent tasks.
"""

from __future__ import annotations

from pydantic import BaseModel, Field

from agentops.domains.agents.task import AgentTask, TaskStatus


class ExecutionPlan(BaseModel):
    """
    Ordered collection of tasks to execute.
    """

    goal: str

    tasks: list[AgentTask] = Field(default_factory=list)

    def add_task(
        self,
        task: AgentTask,
    ) -> None:
        self.tasks.append(task)

    def get_task(
        self,
        task_id: int,
    ) -> AgentTask | None:

        for task in self.tasks:
            if task.id == task_id:
                return task

        return None

    def next_pending_task(
        self,
    ) -> AgentTask | None:

        for task in self.tasks:
            if task.status == TaskStatus.PENDING:
                return task

        return None

    def mark_running(
        self,
        task_id: int,
    ) -> None:

        task = self.get_task(task_id)

        if task:
            task.status = TaskStatus.RUNNING

    def mark_completed(
        self,
        task_id: int,
        result: dict,
    ) -> None:

        task = self.get_task(task_id)

        if task:
            task.status = TaskStatus.COMPLETED
            task.result = result

    def mark_failed(
        self,
        task_id: int,
        error: str,
    ) -> None:

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
    def pending_tasks(self) -> int:
        return sum(task.status == TaskStatus.PENDING for task in self.tasks)

    @property
    def failed_tasks(self) -> int:
        return sum(task.status == TaskStatus.FAILED for task in self.tasks)
