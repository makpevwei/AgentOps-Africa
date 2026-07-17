"""
Finance Domain Models

Pure business models.
No Yahoo, Finnhub or API-specific code.
"""

from datetime import datetime

from pydantic import BaseModel


class StockQuote(BaseModel):
    symbol: str

    company_name: str

    exchange: str | None = None

    currency: str | None = None

    price: float | None = None

    previous_close: float | None = None

    change: float | None = None

    change_percent: float | None = None

    market_cap: float | None = None

    volume: int | None = None

    timestamp: datetime | None = None


class CompanyFundamentals(BaseModel):
    company_name: str

    sector: str | None = None

    industry: str | None = None

    website: str | None = None

    employees: int | None = None

    description: str | None = None


class PriceHistoryPoint(BaseModel):
    date: datetime

    open: float

    high: float

    low: float

    close: float

    volume: int
