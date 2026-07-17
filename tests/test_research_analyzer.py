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

    print("\nBusiness Overview:")
    print(report.business.overview)

    print("\nIndustry:")
    print(report.business.industry)

    print("\nBusiness Model:")
    print(report.business.business_model)

    print("\nRecommendation:")
    print(report.recommendation.action)

    print("\nRecommendation Rationale:")
    print(report.recommendation.rationale)

    print("\nRecommendation Confidence:")
    print(report.recommendation.confidence)

    print("\nOverall Risk:")
    print(report.risks.overall_risk)

    print("\nFinancial Risk:")
    print(report.risks.financial_risk)

    print("\nSWOT Analysis")

    print("\nStrengths:")
    for strength in report.swot.strengths:
        print(f"  • {strength}")

    print("\nWeaknesses:")
    for weakness in report.swot.weaknesses:
        print(f"  • {weakness}")

    print("\nOpportunities:")
    for opportunity in report.swot.opportunities:
        print(f"  • {opportunity}")

    print("\nThreats:")
    for threat in report.swot.threats:
        print(f"  • {threat}")

    print("\nSections:")
    for section in report.sections:
        print(f"  • {section.title}")


if __name__ == "__main__":
    test_company("Apple")