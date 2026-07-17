"""
Finance Provider Factory
"""

from agentops.providers.finance.yahoo_provider import YahooFinanceProvider


class FinanceProviderFactory:

    @staticmethod
    def create(company):

        #
        # For now
        #
        # Everything uses Yahoo.
        #
        # Later we'll route based on
        # country, exchange and asset type.
        #

        return YahooFinanceProvider()