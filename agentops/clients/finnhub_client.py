"""
Finnhub Client

Responsible only for communicating with the Finnhub API.
"""

from __future__ import annotations

import os

import requests

from agentops.core.logger import logger


class FinnhubClient:
    """
    Low-level client for the Finnhub REST API.
    """

    BASE_URL = "https://finnhub.io/api/v1"

    def __init__(self):
        self.api_key = os.getenv("FINNHUB_API_KEY")

        if not self.api_key:
            raise ValueError("FINNHUB_API_KEY not found in environment variables.")

    def get(self, endpoint: str, **params) -> dict:
        """
        Execute a GET request against Finnhub.
        """

        url = f"{self.BASE_URL}/{endpoint}"

        params["token"] = self.api_key

        logger.info("Finnhub -> GET %s", endpoint)

        response = requests.get(
            url,
            params=params,
            timeout=30,
        )

        response.raise_for_status()

        return response.json()

    def quote(
        self,
        symbol: str,
    ) -> dict:
        """
        Get latest market quote.
        """

        return self.get(
            "quote",
            symbol=symbol,
        )

    def company_profile(
        self,
        symbol: str,
    ) -> dict:
        """
        Get company profile.
        """

        return self.get(
            "stock/profile2",
            symbol=symbol,
        )

    def company_news(
        self,
        symbol: str,
        from_date: str,
        to_date: str,
    ) -> list:
        """
        Get company news.
        """

        return self.get(
            "company-news",
            symbol=symbol,
            _from=from_date,
            to=to_date,
        )

    def basic_financials(
        self,
        symbol: str,
    ) -> dict:
        """
        Get company financial metrics.
        """

        return self.get(
            "stock/metric",
            symbol=symbol,
            metric="all",
        )
