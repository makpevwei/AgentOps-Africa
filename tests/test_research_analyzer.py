from agentops.domains.research.analyzer import ResearchAnalyzer
from agentops.domains.research.company_service import CompanyService
from agentops.domains.research.finance_service import FinanceService
from agentops.domains.research.research_context import ResearchContext


def test_company(name: str):

    print("\n" + "=" * 90)
    print(name)
    print("=" * 90)

    company_service = CompanyService()
    finance_service = FinanceService()
    analyzer = ResearchAnalyzer()

    company = company_service.resolve(name)

    if company is None:
        print("Company not found")
        return

    finance = finance_service.get_snapshot(company)

    context = ResearchContext(
        query=f"Analyze {name} for investment",
        company=company,
        finance=finance,
    )

    report = analyzer.analyze(context)

    print("\nCompany:")
    print(report.company)

    print("\nExecutive Summary:")
    print(report.executive_summary)

    print("\nRecommendation:")
    print(report.recommendation)

    print("\nConfidence:")
    print(report.confidence)

    print("\nSections:")
    print(len(report.sections))

    for section in report.sections:
        print(f"  • {section.title}")


if __name__ == "__main__":
    test_company("Apple")