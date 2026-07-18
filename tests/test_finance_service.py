from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_service import FinanceService

company = CompanyProfile(
    company_name="Apple Inc",
    ticker="AAPL",
    finance_symbol="AAPL",
)

service = FinanceService()

snapshot = service.get_snapshot(company)

print(snapshot.model_dump())