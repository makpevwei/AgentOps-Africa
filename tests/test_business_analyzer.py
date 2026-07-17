from agentops.domains.companies.company_service import CompanyService
from agentops.domains.finance.finance_service import FinanceService
from agentops.domains.research.analyzers.business_analyzer import BusinessAnalyzer
from agentops.domains.research.research_context import ResearchContext


def main():

    company_service = CompanyService()
    finance_service = FinanceService()

    company = company_service.resolve("Apple")
    finance = finance_service.get_snapshot(company)

    context = ResearchContext(
        query="Analyze Apple",
        company=company,
        finance=finance,
    )

    analyzer = BusinessAnalyzer()

    result = analyzer.analyze(context)

    print(result.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
