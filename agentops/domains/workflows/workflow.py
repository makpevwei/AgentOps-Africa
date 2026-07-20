"""
Workflow Definition

Represents a reusable business workflow.
"""

from __future__ import annotations

from dataclasses import dataclass, field

from agentops.domains.workflows.workflow_step import WorkflowStep


@dataclass(slots=True)
class Workflow:
    """
    A reusable workflow.
    """

    name: str
    description: str
    steps: list[WorkflowStep] = field(default_factory=list)

    def add_step(
        self,
        step: WorkflowStep,
    ) -> None:
        self.steps.append(step)

    @property
    def total_steps(self) -> int:
        return len(self.steps)
