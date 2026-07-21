from agentops.domains.workflows.workflow import Workflow
from agentops.domains.workflows.workflow_engine import WorkflowEngine
from agentops.domains.workflows.workflow_step import WorkflowStep


def test_build_execution_plan():
    workflow = Workflow(
        name="Research Workflow",
        description="Research a company",
    )

    workflow.add_step(
        WorkflowStep(
            id=1,
            name="Research Company",
            service="research",
            action="company_profile",
            description="Research company profile",
            payload={"company": "Apple"},
            depends_on=[],
        )
    )

    workflow.add_step(
        WorkflowStep(
            id=2,
            name="Analyze Financials",
            service="finance",
            action="financial_analysis",
            description="Analyze company financials",
            payload={"ticker": "AAPL"},
            depends_on=[1],
        )
    )

    engine = WorkflowEngine()

    plan = engine.build_execution_plan(
        workflow=workflow,
        goal="Research Apple",
    )

    assert plan.goal == "Research Apple"
    assert len(plan.tasks) == 2

    task1 = plan.tasks[0]
    assert task1.id == 1
    assert task1.name == "Research Company"
    assert task1.service == "research"
    assert task1.action == "company_profile"
    assert task1.description == "Research company profile"
    assert task1.payload == {"company": "Apple"}
    assert task1.depends_on == []

    task2 = plan.tasks[1]
    assert task2.id == 2
    assert task2.name == "Analyze Financials"
    assert task2.service == "finance"
    assert task2.action == "financial_analysis"
    assert task2.description == "Analyze company financials"
    assert task2.payload == {"ticker": "AAPL"}
    assert task2.depends_on == [1]