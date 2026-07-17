"""
Enterprise Finance Provider Interface.
"""

from abc import ABC, abstractmethod

from agentops.domains.research.finance_models import (
    CompanyFundamentals,
    PriceHistoryPoint,
    StockQuote,
)
from agentops.domains.research.models import CompanyProfile


class BaseFinanceProvider(ABC):

    @abstractmethod
    def get_quote(
        self,
        company: CompanyProfile,
    ) -> StockQuote:
        pass

    @abstractmethod
    def get_company_info(
        self,
        company: CompanyProfile,
    ) -> CompanyFundamentals:
        pass

    @abstractmethod
    def get_news(
        self,
        company: CompanyProfile,
    ):
        pass

    @abstractmethod
    def get_price_history(
        self,
        company: CompanyProfile,
        period: str = "1y",
    ) -> list[PriceHistoryPoint]:
        pass