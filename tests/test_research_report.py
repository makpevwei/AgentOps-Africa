from agentops.domains.research.models import (
    ResearchFinding,
    ResearchReport,
    ResearchSource,
)


def test_research_report_creation():

    report = ResearchReport(
        query="Artificial Intelligence",
        findings=[
            ResearchFinding(
                title="OpenAI",
                summary="AI Company",
                url="https://openai.com",
                confidence=0.95,
            )
        ],
        sources=[
            ResearchSource(
                title="OpenAI",
                url="https://openai.com",
                provider="tavily",
            )
        ],
        summary="One finding.",
        execution_time_ms=100,
    )

    assert report.query == "Artificial Intelligence"

    assert len(report.findings) == 1

    assert len(report.sources) == 1

    assert report.execution_time_ms == 100