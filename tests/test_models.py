from agentops.domains.companies.models import CompanyProfile
from agentops.domains.research.models import (
    ResearchReport,
    ResearchResult,
)


def main():

    company = CompanyProfile(
        company_name="Zenith Bank Plc",
        aliases=["Zenith", "Zenith Bank"],
        ticker="ZENITHBANK",
        exchange="NGX",
        country="Nigeria",
        industry="Banking",
    )

    result = ResearchResult(
        source="Wikipedia",
        title="Zenith Bank",
        summary="One of Nigeria's largest commercial banks.",
        confidence=0.97,
    )

    report = ResearchReport(
        query="Should I invest in Zenith Bank?",
        summary="Research has started.",
        findings=[result],
    )

    print(company.model_dump())

    print()

    print(result.model_dump())

    print()

    print(report.model_dump())


if __name__ == "__main__":
    main()
