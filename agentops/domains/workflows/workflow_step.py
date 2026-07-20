"""
Workflow Step

Represents a single step within a workflow.
"""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class WorkflowStep:
    """
    A single executable workflow step.
    """

    id: str
    name: str
    service: str
    description: str = ""
    depends_on: list[str] = field(default_factory=list)
    payload: dict = field(default_factory=dict)
