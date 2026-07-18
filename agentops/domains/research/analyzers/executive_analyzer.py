"""
Executive Analyzer

Coordinates all specialized analyzers to produce a
complete company analysis.
"""

from agentops.domains.research.analysis_models import CompanyAnalysis
from agentops.domains.research.analyzers.base_analyzer import BaseAnalyzer
from agentops.domains.research.analyzers.business_analyzer import (
    BusinessAnalyzer,
)
from agentops.domains.research.analyzers.financial_analyzer import (
    FinancialAnalyzer,
)
from agentops.domains.research.research_context import ResearchContext


class ExecutiveAnalyzer(BaseAnalyzer):
    """
    Coordinates all specialized analyzers.

    This class does not call the LLM directly.

    Instead, it delegates work to dedicated analyzers and
    combines their results into a single CompanyAnalysis.
    """

    def __init__(self):
        self.business = BusinessAnalyzer()
        self.financial = FinancialAnalyzer()

    def analyze(
        self,
        context: ResearchContext,
    ) -> CompanyAnalysis:
        """
        Generate a complete company analysis.
        """

        business = self.business.analyze(context)

        financial = self.financial.analyze(context)

        return CompanyAnalysis(
            company_name=context.company.company_name,
            business=business,
            financial=financial,
        )
