"""
Integration test for the Finnhub client.

Run manually:

pytest tests/test_finnhub.py -m integration
"""

import pytest

from agentops.clients.finnhub_client import FinnhubClient


@pytest.mark.integration
def test_company_profile():
    """
    Verify that Finnhub returns a valid company profile.

    Requires:
        FINNHUB_API_KEY
        Internet connection
    """

    client = FinnhubClient()

    profile = client.company_profile("AAPL")

    assert isinstance(profile, dict)

    assert profile["ticker"] == "AAPL"