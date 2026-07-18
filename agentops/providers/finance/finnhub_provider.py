"""
Finnhub Finance Provider

Primary financial data provider for AgentOps Enterprise.

Responsibilities
----------------
1. Retrieve live market quote
2. Retrieve company profile
3. Retrieve financial metrics
4. Map Finnhub responses into domain models
5. Never expose Finnhub JSON outside this provider
"""

from __future__ import annotations

from datetime import datetime
from time import perf_counter

from agentops.clients.finnhub_client import FinnhubClient
from agentops.core.logger import logger
from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_models import (
    CompanyFundamentals,
    StockQuote,
)
from agentops.domains.finance.finance_snapshot import FinanceSnapshot
from agentops.domains.finance.provider_result import ProviderResult
from agentops.providers.finance.base_provider import BaseFinanceProvider


class FinnhubProvider(BaseFinanceProvider):
    """
    Finnhub implementation of BaseFinanceProvider.
    """

    name = "Finnhub"

    def __init__(self):
        self.client = FinnhubClient()

    def get_snapshot(
        self,
        company: CompanyProfile,
    ) -> ProviderResult:
        """
        Retrieve a complete financial snapshot.

        Any provider failure returns a ProviderResult so that the
        Finance Orchestrator can continue with the next provider.
        """

        start = perf_counter()

        try:
            symbol = company.finance_symbol or company.ticker

            if not symbol:
                logger.warning(
                    "Finnhub skipped because no finance symbol exists for %s",
                    company.company_name,
                )

                return ProviderResult(
                    provider=self.name,
                    success=False,
                    errors=["No finance symbol available."],
                    response_time_ms=(perf_counter() - start) * 1000,
                )

            logger.info("Finnhub Provider -> %s", symbol)

            quote_data = self.client.quote(symbol)
            profile = self.client.company_profile(symbol)

            # Reserved for future use
            _ = self.client.basic_financials(symbol)

            quote = StockQuote(
                symbol=symbol,
                company_name=company.company_name,
                exchange=profile.get("exchange"),
                currency=profile.get("currency"),
                price=quote_data.get("c"),
                previous_close=quote_data.get("pc"),
                change=quote_data.get("d"),
                change_percent=quote_data.get("dp"),
                market_cap=profile.get("marketCapitalization"),
                volume=quote_data.get("v"),
                timestamp=datetime.utcnow(),
            )

            fundamentals = CompanyFundamentals(
                company_name=company.company_name,
                sector=profile.get("finnhubIndustry"),
                industry=profile.get("finnhubIndustry"),
                website=profile.get("weburl"),
                employees=None,
                description=None,
            )

            snapshot = FinanceSnapshot(
                quote=quote,
                fundamentals=fundamentals,
                history=[],
                news=[],
            )

            logger.info(
                "Finnhub snapshot created: %s",
                snapshot.model_dump(),
            )

            return ProviderResult(
                provider=self.name,
                success=True,
                snapshot=snapshot,
                response_time_ms=(perf_counter() - start) * 1000,
            )

        except Exception as ex:
            logger.exception(
                "Finnhub provider failed for %s: %s",
                company.company_name,
                ex,
            )

            return ProviderResult(
                provider=self.name,
                success=False,
                errors=[str(ex)],
                response_time_ms=(perf_counter() - start) * 1000,
            )
