"""
Financial Analyzer

Performs structured financial analysis.
"""

from agentops.ai.llm_analyzer import LLMAnalyzer
from agentops.domains.research.analysis_models import FinancialAnalysis
from agentops.domains.research.analyzers.base_analyzer import BaseAnalyzer
from agentops.domains.research.prompts.financial_prompt import (
    FinancialPromptBuilder,
)
from agentops.domains.research.research_context import ResearchContext


class FinancialAnalyzer(BaseAnalyzer):
    """
    Performs financial analysis using the configured LLM.
    """

    def __init__(self):
        self.ai = LLMAnalyzer()
        self.prompt_builder = FinancialPromptBuilder()

    def analyze(
        self,
        context: ResearchContext,
    ) -> FinancialAnalysis:
        """
        Analyze the financial position of a company.

        Args:
            context:
                Research context.

        Returns:
            FinancialAnalysis
        """

        prompt = self.prompt_builder.build(context)

        return self.ai.run(
            prompt=prompt,
            response_model=FinancialAnalysis,
        )
