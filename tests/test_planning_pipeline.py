from agentops.ai.planning.models import WorkflowPlan, WorkflowTask
from agentops.ai.planning.planning_pipeline import PlanningPipeline


def test_pipeline_returns_workflow(monkeypatch):

    pipeline = PlanningPipeline()

    plan = WorkflowPlan(
        tasks=[
            WorkflowTask(
                id=1,
                name="Resolve Company",
                service="company",
                action="resolve_company",
                description="Resolve company",
                payload={"query": "Microsoft"},
            )
        ]
    )

    monkeypatch.setattr(
        pipeline.ai_planner,
        "plan",
        lambda _: plan,
    )

    workflow = pipeline.plan("Research Microsoft")

    assert workflow.name == "AI Workflow"
    assert len(workflow.steps) == 1
    assert workflow.steps[0].service == "company"