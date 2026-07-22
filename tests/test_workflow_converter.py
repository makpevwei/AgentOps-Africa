from agentops.ai.planning.models import WorkflowPlan, WorkflowTask
from agentops.ai.planning.workflow_converter import WorkflowConverter


def test_convert_workflow_plan_to_workflow():

    plan = WorkflowPlan(
        tasks=[
            WorkflowTask(
                id=1,
                name="Resolve Company",
                service="company",
                action="resolve_company",
                description="Resolve company",
                payload={"query": "Microsoft"},
                depends_on=[],
            )
        ]
    )

    converter = WorkflowConverter()

    workflow = converter.convert(plan)

    assert workflow.name == "AI Workflow"

    assert len(workflow.steps) == 1

    step = workflow.steps[0]

    assert step.id == 1
    assert step.name == "Resolve Company"
    assert step.service == "company"
    assert step.action == "resolve_company"
    assert step.payload["query"] == "Microsoft"