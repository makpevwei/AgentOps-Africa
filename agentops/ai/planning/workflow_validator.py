"""
Workflow Validator

Validates AI-generated workflow plans before execution.
"""

from agentops.ai.planning.models import WorkflowPlan


class WorkflowValidationError(ValueError):
    """Raised when a workflow plan is invalid."""


class WorkflowValidator:
    """
    Validates an AI-generated workflow plan.
    """

    def validate(
        self,
        plan: WorkflowPlan,
    ) -> WorkflowPlan:
        """
        Validate the workflow plan.

        Returns:
            The validated plan.

        Raises:
            WorkflowValidationError
        """

        self._validate_unique_ids(plan)

        self._validate_dependencies(plan)

        return plan

    def _validate_unique_ids(
        self,
        plan: WorkflowPlan,
    ) -> None:

        ids = [task.id for task in plan.tasks]

        if len(ids) != len(set(ids)):
            raise WorkflowValidationError(
                "Duplicate task IDs detected."
            )

    def _validate_dependencies(
        self,
        plan: WorkflowPlan,
    ) -> None:

        ids = {task.id for task in plan.tasks}

        for task in plan.tasks:
            for dependency in task.depends_on:
                if dependency not in ids:
                    raise WorkflowValidationError(
                        f"Task {task.id} depends on missing task {dependency}."
                    )