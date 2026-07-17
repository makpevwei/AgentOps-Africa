"""
Yahoo Finance Client

Responsible only for communicating with Yahoo Finance.
"""

import yfinance as yf

from agentops.core.logger import logger


class YahooClient:
    def get_ticker(self, symbol: str):

        logger.info("Yahoo Finance -> %s", symbol)

        return yf.Ticker(symbol)
