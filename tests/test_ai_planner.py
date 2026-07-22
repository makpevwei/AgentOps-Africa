from unittest.mock import MagicMock

from agentops.ai.planning.ai_planner import AIPlanner
from agentops.ai.planning.models import WorkflowPlan


def test_ai_planner_calls_analyzer(monkeypatch):
    planner = AIPlanner()

    fake_plan = WorkflowPlan(
        tasks=[]
    )

    mock_run = MagicMock(return_value=fake_plan)

    planner._analyzer.run = mock_run

    result = planner.plan(
        "Research Microsoft"
    )

    assert result == fake_plan

    mock_run.assert_called_once()

    _, response_model = mock_run.call_args.args

    assert response_model is WorkflowPlan