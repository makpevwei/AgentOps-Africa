"""
Yahoo Finance Provider

Retrieves all available financial information from
Yahoo Finance in a single provider session.
"""

from datetime import datetime

from agentops.clients.yahoo_client import YahooClient
from agentops.domains.research.finance_models import (
    CompanyFundamentals,
    PriceHistoryPoint,
    StockQuote,
)
from agentops.domains.research.finance_snapshot import FinanceSnapshot
from agentops.domains.research.models import CompanyProfile
from agentops.providers.finance.base_provider import BaseFinanceProvider


class YahooFinanceProvider(BaseFinanceProvider):
    """
    Yahoo Finance implementation of the BaseFinanceProvider.
    """

    def __init__(self):

        self.client = YahooClient()

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> FinanceSnapshot:

        # -------------------------------------------------
        # Create ONE Yahoo ticker instance
        # -------------------------------------------------

        ticker = self.client.get_ticker(company.ticker)

        info = ticker.info

        # -------------------------------------------------
        # Quote
        # -------------------------------------------------

        quote = StockQuote(
            symbol=company.ticker,
            company_name=company.company_name,
            exchange=info.get("exchange"),
            currency=info.get("currency"),
            price=info.get("currentPrice"),
            previous_close=info.get("previousClose"),
            change=(info.get("currentPrice") or 0)
            - (info.get("previousClose") or 0),
            change_percent=info.get("regularMarketChangePercent"),
            market_cap=info.get("marketCap"),
            volume=info.get("volume"),
            timestamp=datetime.utcnow(),
        )

        # -------------------------------------------------
        # Fundamentals
        # -------------------------------------------------

        fundamentals = CompanyFundamentals(
            company_name=company.company_name,
            sector=info.get("sector"),
            industry=info.get("industry"),
            website=info.get("website"),
            employees=info.get("fullTimeEmployees"),
            description=info.get("longBusinessSummary"),
        )

        # -------------------------------------------------
        # Price History
        # -------------------------------------------------

        history = []

        dataframe = ticker.history(period="1y")

        for index, row in dataframe.iterrows():

            history.append(
                PriceHistoryPoint(
                    date=index.to_pydatetime(),
                    open=float(row.Open),
                    high=float(row.High),
                    low=float(row.Low),
                    close=float(row.Close),
                    volume=int(row.Volume),
                )
            )

        # -------------------------------------------------
        # News
        # -------------------------------------------------

        news = ticker.news

        # -------------------------------------------------
        # Snapshot
        # -------------------------------------------------

        return FinanceSnapshot(
            quote=quote,
            fundamentals=fundamentals,
            history=history,
            news=news,
        )