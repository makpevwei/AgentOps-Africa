"""
Finance Snapshot

Represents everything retrieved from a financial
data provider during a single request.
"""

from pydantic import BaseModel, Field

from agentops.domains.finance.finance_models import (
    CompanyFundamentals,
    PriceHistoryPoint,
    StockQuote,
)


class FinanceSnapshot(BaseModel):
    """
    Complete financial snapshot for one company.
    """

    quote: StockQuote | None = None

    fundamentals: CompanyFundamentals | None = None

    history: list[PriceHistoryPoint] = Field(default_factory=list)

    news: list[dict] = Field(default_factory=list)
