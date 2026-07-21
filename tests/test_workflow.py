"""
Unit tests for Workflow.
"""

from agentops.domains.workflows.workflow import Workflow
from agentops.domains.workflows.workflow_step import WorkflowStep


def test_workflow_add_step():
    workflow = Workflow(
        name="Test Workflow",
        description="Testing",
    )

    assert workflow.total_steps == 0

    workflow.add_step(
        WorkflowStep(
            id=1,
            name="Step One",
            service="research",
            action="company_profile",
            description="Research company profile",
            payload={},
            depends_on=[],
        )
    )

    assert workflow.total_steps == 1

    step = workflow.steps[0]

    assert step.id == 1
    assert step.name == "Step One"
    assert step.service == "research"
    assert step.action == "company_profile"
    assert step.description == "Research company profile"
    assert step.payload == {}
    assert step.depends_on == []


def test_workflow_multiple_steps():
    workflow = Workflow(
        name="Workflow",
        description="Multiple steps",
    )

    for i in range(3):
        workflow.add_step(
            WorkflowStep(
                id=i + 1,
                name=f"Step {i + 1}",
                service="research",
                action=f"action_{i + 1}",
                description=f"Description {i + 1}",
                payload={},
                depends_on=[] if i == 0 else [i],
            )
        )

    assert workflow.total_steps == 3

    assert workflow.steps[0].id == 1
    assert workflow.steps[1].id == 2
    assert workflow.steps[2].id == 3

    assert workflow.steps[0].action == "action_1"
    assert workflow.steps[1].action == "action_2"
    assert workflow.steps[2].action == "action_3"

    assert workflow.steps[0].depends_on == []
    assert workflow.steps[1].depends_on == [1]
    assert workflow.steps[2].depends_on == [2]