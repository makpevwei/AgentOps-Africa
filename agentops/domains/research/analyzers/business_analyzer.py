"""
Business Analyzer

Generates a structured business analysis for a company.
"""

from agentops.ai.llm_analyzer import LLMAnalyzer
from agentops.domains.research.analysis_models import BusinessAnalysis
from agentops.domains.research.analyzers.base_analyzer import BaseAnalyzer
from agentops.domains.research.prompts.business_prompt import (
    BusinessPromptBuilder,
)
from agentops.domains.research.research_context import ResearchContext


class BusinessAnalyzer(BaseAnalyzer):
    """
    Specialized analyzer for business analysis.
    """

    def __init__(self):
        self.ai = LLMAnalyzer()
        self.prompt_builder = BusinessPromptBuilder()

    def analyze(
        self,
        context: ResearchContext,
    ) -> BusinessAnalysis:

        prompt = self.prompt_builder.build(context)

        return self.ai.run(
            prompt=prompt,
            response_model=BusinessAnalysis,
        )