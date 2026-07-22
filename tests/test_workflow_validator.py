import pytest

from agentops.ai.planning.models import WorkflowPlan, WorkflowTask
from agentops.ai.planning.workflow_validator import (
    WorkflowValidationError,
    WorkflowValidator,
)


def test_valid_workflow():

    plan = WorkflowPlan(
        tasks=[
            WorkflowTask(
                id=1,
                name="A",
                service="research",
                action="search",
                description="Search",
            ),
            WorkflowTask(
                id=2,
                name="B",
                service="finance",
                action="analyze",
                description="Analyze",
                depends_on=[1],
            ),
        ]
    )

    WorkflowValidator().validate(plan)


def test_duplicate_ids():

    plan = WorkflowPlan(
        tasks=[
            WorkflowTask(
                id=1,
                name="A",
                service="research",
                action="search",
                description="Search",
            ),
            WorkflowTask(
                id=1,
                name="B",
                service="finance",
                action="analyze",
                description="Analyze",
            ),
        ]
    )

    with pytest.raises(WorkflowValidationError):
        WorkflowValidator().validate(plan)


def test_missing_dependency():

    plan = WorkflowPlan(
        tasks=[
            WorkflowTask(
                id=1,
                name="A",
                service="research",
                action="search",
                description="Search",
                depends_on=[99],
            )
        ]
    )

    with pytest.raises(WorkflowValidationError):
        WorkflowValidator().validate(plan)