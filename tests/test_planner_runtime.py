from agentops.domains.agents.planner import Planner


def test_planner_creates_execution_plan():
    planner = Planner()

    plan = planner.create_plan("Analyze Apple Inc.")

    assert plan.goal == "Analyze Apple Inc."

    assert len(plan.tasks) == 3

    assert plan.tasks[0].id == 1
    assert plan.tasks[0].service == "company"
    assert plan.tasks[0].action == "resolve_company"

    assert plan.tasks[1].id == 2
    assert plan.tasks[1].service == "research"
    assert plan.tasks[1].action == "company_profile"
    assert plan.tasks[1].depends_on == [1]

    assert plan.tasks[2].id == 3
    assert plan.tasks[2].service == "finance"
    assert plan.tasks[2].action == "financial_snapshot"
    assert plan.tasks[2].depends_on == [1]