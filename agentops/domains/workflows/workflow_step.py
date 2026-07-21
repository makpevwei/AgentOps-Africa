from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(slots=True)
class WorkflowStep:
    id: int
    name: str
    service: str
    action: str
    description: str = ""
    depends_on: list[int] = field(default_factory=list)
    payload: dict = field(default_factory=dict)