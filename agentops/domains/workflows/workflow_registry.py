"""
Workflow Registry

Stores reusable business workflows.
"""

from __future__ import annotations

from agentops.domains.workflows.workflow import Workflow


class WorkflowRegistry:
    """
    Registry of reusable workflows.
    """

    def __init__(self) -> None:
        self._workflows: dict[str, Workflow] = {}

    def register(
        self,
        workflow: Workflow,
    ) -> None:
        """
        Register a workflow.
        """

        self._workflows[workflow.name] = workflow

    def get(
        self,
        name: str,
    ) -> Workflow:
        """
        Retrieve a workflow.
        """

        try:
            return self._workflows[name]

        except KeyError as exc:
            raise ValueError(f"No workflow registered for '{name}'.") from exc

    @property
    def workflows(
        self,
    ) -> list[str]:
        """
        Registered workflow names.
        """

        return sorted(self._workflows.keys())
