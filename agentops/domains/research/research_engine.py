"""
Enterprise Research Engine

High-level orchestration for company research.
"""

from agentops.domains.research.company_service import CompanyService
from agentops.domains.research.finance_service import FinanceService


class ResearchEngine:

    def __init__(self):

        self.company_service = CompanyService()
        self.finance_service = FinanceService()

    def get_quote(
        self,
        company_name: str,
    ):

        company = self.company_service.resolve(company_name)

        return self.finance_service.get_quote(company)

    def get_company_info(
        self,
        company_name: str,
    ):

        company = self.company_service.resolve(company_name)

        return self.finance_service.get_company_info(company)

    def get_price_history(
        self,
        company_name: str,
        period: str = "1y",
    ):

        company = self.company_service.resolve(company_name)

        return self.finance_service.get_price_history(
            company,
            period,
        )

    def get_news(
        self,
        company_name: str,
    ):

        company = self.company_service.resolve(company_name)

        return self.finance_service.get_news(company)