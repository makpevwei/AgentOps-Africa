from agentops.config import settings
from agentops.domains.agents.planner import Planner


def test_ai_failure_falls_back(monkeypatch):
    planner = Planner()

    # Force the AI planner inside the pipeline to fail
    monkeypatch.setattr(
        planner.pipeline.ai_planner,
        "plan",
        lambda _: (_ for _ in ()).throw(RuntimeError("AI unavailable")),
    )

    # Enable AI planning
    monkeypatch.setattr(
        settings,
        "USE_AI_PLANNER",
        True,
        raising=False,
    )

    workflow = planner.create_workflow("Research Microsoft")

    assert workflow.name == "Research Workflow"