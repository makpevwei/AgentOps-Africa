from agentops.config import settings
from agentops.domains.agents.planner import Planner


def test_ai_failure_falls_back(monkeypatch):

    planner = Planner()

    # Force AI planner to fail
    monkeypatch.setattr(
        planner.ai,
        "plan",
        lambda _: (_ for _ in ()).throw(RuntimeError("AI unavailable")),
    )

    # Enable AI planner
    monkeypatch.setattr(
        settings,
        "USE_AI_PLANNER",
        True,
    )

    workflow = planner.create_workflow("Research Microsoft")

    assert workflow.name == "Research Workflow"