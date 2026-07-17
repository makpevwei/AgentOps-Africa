"""
Unit tests for ResearchEngine.

These tests do NOT call:

- Yahoo Finance
- Tavily
- OpenAI
- Internet

Everything is mocked using fake services.
"""

from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_snapshot import FinanceSnapshot
from agentops.domains.research.research_engine import ResearchEngine


class FakeCompanyService:
    """Fake company service for testing."""

    def resolve(self, company_name: str) -> CompanyProfile:
        return CompanyProfile(
            company_name="Apple Inc.",
            aliases=[],
            ticker="AAPL",
            exchange="NASDAQ",
            country="USA",
            industry="Technology",
            sector="Technology",
            website="https://apple.com",
        )


class FakeFinanceService:
    """Fake finance service for testing."""

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:

        return FinanceSnapshot(
            quote=None,
            fundamentals=None,
            history=[],
        )


def test_build_context():

    engine = ResearchEngine(
        company_service=FakeCompanyService(),
        finance_service=FakeFinanceService(),
    )

    context = engine.build_context("Apple")

    assert context.query == "Apple"

    assert context.company.company_name == "Apple Inc."

    assert context.company.ticker == "AAPL"

    assert context.finance is not None
