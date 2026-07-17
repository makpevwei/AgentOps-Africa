"""
Provider Result

Represents the outcome of a finance provider request.

Every finance provider (Finnhub, Alpha Vantage,
Yahoo Finance, NGX, etc.) returns a ProviderResult.

The Finance Orchestrator uses this object to determine:

- whether the provider succeeded
- whether to try another provider
- how long the request took
- which provider supplied the data
"""

from __future__ import annotations

from datetime import datetime

from pydantic import BaseModel, Field

from agentops.domains.finance.finance_snapshot import FinanceSnapshot


class ProviderResult(BaseModel):
    """
    Standard response from every finance provider.
    """

    provider: str

    success: bool = False

    snapshot: FinanceSnapshot = Field(
        default_factory=FinanceSnapshot,
    )

    errors: list[str] = Field(
        default_factory=list,
    )

    response_time_ms: float | None = None

    timestamp: datetime = Field(
        default_factory=datetime.utcnow,
    )

    @property
    def has_quote(self) -> bool:
        return (
            self.snapshot.quote is not None
            and self.snapshot.quote.price is not None
        )

    @property
    def has_fundamentals(self) -> bool:
        return self.snapshot.fundamentals is not None

    @property
    def is_empty(self) -> bool:
        return (
            self.snapshot.quote is None
            and self.snapshot.fundamentals is None
            and len(self.snapshot.history) == 0
            and len(self.snapshot.news) == 0
        )