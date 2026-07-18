from agentops.domains.companies.models import CompanyProfile
from agentops.providers.finance.finnhub_provider import FinnhubProvider

company = CompanyProfile(
    company_name="Apple Inc",
    ticker="AAPL",
    finance_symbol="AAPL",
)

provider = FinnhubProvider()

snapshot = provider.get_snapshot(company)

print(snapshot.model_dump())
