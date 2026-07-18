from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_orchestrator import (
    FinanceOrchestrator,
)

company = CompanyProfile(
    company_name="Apple Inc",
    ticker="AAPL",
    finance_symbol="AAPL",
)

orchestrator = FinanceOrchestrator()

snapshot = orchestrator.get_snapshot(company)

print(snapshot.model_dump())
