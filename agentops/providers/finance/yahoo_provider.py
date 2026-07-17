"""
Yahoo Finance Provider
"""

from datetime import datetime

from agentops.clients.yahoo_client import YahooClient
from agentops.domains.research.finance_models import (
    CompanyFundamentals,
    PriceHistoryPoint,
    StockQuote,
)
from agentops.domains.research.models import CompanyProfile
from agentops.providers.finance.base_provider import BaseFinanceProvider


class YahooFinanceProvider(BaseFinanceProvider):

    def __init__(self):

        self.client = YahooClient()

    def get_quote(
        self,
        company: CompanyProfile,
    ) -> StockQuote:

        ticker = self.client.get_ticker(company.ticker)

        info = ticker.info

        return StockQuote(
            symbol=company.ticker,
            company_name=company.company_name,
            exchange=info.get("exchange"),
            currency=info.get("currency"),
            price=info.get("currentPrice"),
            previous_close=info.get("previousClose"),
            change=info.get("currentPrice", 0)
            - info.get("previousClose", 0),
            change_percent=info.get("regularMarketChangePercent"),
            market_cap=info.get("marketCap"),
            volume=info.get("volume"),
            timestamp=datetime.utcnow(),
        )

    def get_company_info(
        self,
        company: CompanyProfile,
    ) -> CompanyFundamentals:

        ticker = self.client.get_ticker(company.ticker)

        info = ticker.info

        return CompanyFundamentals(
            company_name=company.company_name,
            sector=info.get("sector"),
            industry=info.get("industry"),
            website=info.get("website"),
            employees=info.get("fullTimeEmployees"),
            description=info.get("longBusinessSummary"),
        )

    def get_news(
        self,
        company: CompanyProfile,
    ):

        ticker = self.client.get_ticker(company.ticker)

        return ticker.news

    def get_price_history(
        self,
        company: CompanyProfile,
        period="1y",
    ) -> list[PriceHistoryPoint]:

        ticker = self.client.get_ticker(company.ticker)

        history = ticker.history(period=period)

        prices = []

        for index, row in history.iterrows():

            prices.append(

                PriceHistoryPoint(
                    date=index.to_pydatetime(),
                    open=float(row.Open),
                    high=float(row.High),
                    low=float(row.Low),
                    close=float(row.Close),
                    volume=int(row.Volume),
                )

            )

        return prices