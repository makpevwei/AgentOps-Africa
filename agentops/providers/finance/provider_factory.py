"""
Finance Provider Factory

Selects the most appropriate finance provider
for a company based on its profile.
"""

from agentops.domains.research.models import CompanyProfile
from agentops.providers.finance.base_provider import BaseFinanceProvider
from agentops.providers.finance.ngx_provider import NgxFinanceProvider
from agentops.providers.finance.private_provider import PrivateCompanyProvider
from agentops.providers.finance.yahoo_provider import YahooFinanceProvider


class FinanceProviderFactory:
    """
    Factory responsible for selecting the appropriate
    finance provider.
    """

    @staticmethod
    def create(
        company: CompanyProfile,
    ) -> BaseFinanceProvider:

        # ---------------------------------------------
        # Private Companies
        # ---------------------------------------------

        if not company.ticker:

            return PrivateCompanyProvider()

        # ---------------------------------------------
        # Nigerian Exchange
        # ---------------------------------------------

        if company.exchange:

            exchange = company.exchange.upper()

            if exchange == "NGX":

                return NgxFinanceProvider()

            if exchange in {

                "NASDAQ",
                "NYSE",
                "NMS",
                "NYSEARCA",
                "AMEX",

            }:

                return YahooFinanceProvider()

        # ---------------------------------------------
        # Default
        # ---------------------------------------------

        return YahooFinanceProvider()