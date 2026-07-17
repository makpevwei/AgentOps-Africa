"""
Enterprise Finance Service

Coordinates all financial market data requests.

The Finance Service is responsible for selecting
the appropriate provider and returning domain models.
"""

from agentops.domains.research.finance_models import (
    CompanyFundamentals,
    PriceHistoryPoint,
    StockQuote,
)
from agentops.domains.research.models import CompanyProfile
from agentops.providers.finance.provider_factory import FinanceProviderFactory


class FinanceService:

    def __init__(self):

        self.factory = FinanceProviderFactory()

    def get_quote(
        self,
        company: CompanyProfile,
    ) -> StockQuote:

        provider = self.factory.create(company)

        return provider.get_quote(company)

    def get_company_info(
        self,
        company: CompanyProfile,
    ) -> CompanyFundamentals:

        provider = self.factory.create(company)

        return provider.get_company_info(company)

    def get_price_history(
        self,
        company: CompanyProfile,
        period: str = "1y",
    ) -> list[PriceHistoryPoint]:

        provider = self.factory.create(company)

        return provider.get_price_history(
            company,
            period,
        )

    def get_news(
        self,
        company: CompanyProfile,
    ):

        provider = self.factory.create(company)

        return provider.get_news(company)