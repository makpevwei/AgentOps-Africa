"""
Business Analyzer

Generates a structured business analysis for a company.
"""

from agentops.ai.llm_analyzer import LLMAnalyzer
from agentops.domains.research.analysis_models import BusinessAnalysis
from agentops.domains.research.analyzers.base_analyzer import BaseAnalyzer
from agentops.domains.research.research_context import ResearchContext


class BusinessAnalyzer(BaseAnalyzer):
    """
    Specialized analyzer for business analysis.
    """

    def __init__(self):

        self.ai = LLMAnalyzer()

    def analyze(
        self,
        context: ResearchContext,
    ) -> BusinessAnalysis:

        company = context.company

        prompt = f"""
You are a senior business strategy consultant.

Analyze the following company.

Company:
{company.company_name}

Country:
{company.country}

Industry:
{company.industry}

Return ONLY valid JSON.

{{
    "overview": "...",
    "industry": "...",
    "headquarters": "...",
    "business_model": "...",
    "competitive_position": "..."
}}

Do not include markdown.

Do not wrap the JSON in code fences.
"""

        return self.ai.run(
            prompt=prompt,
            response_model=BusinessAnalysis,
        )