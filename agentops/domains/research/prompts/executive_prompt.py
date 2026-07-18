"""
Executive Prompt Builder

Builds the executive analysis prompt from a ResearchContext.
"""

from agentops.ai.prompt_template import PromptTemplate
from agentops.domains.research.research_context import ResearchContext


class ExecutivePromptBuilder:
    """
    Builds prompts for executive-level company analysis.
    """

    def build(
        self,
        context: ResearchContext,
    ) -> PromptTemplate:

        company = context.company
        finance = context.finance

        system = """
You are a world-class Management Consultant,
Investment Banker and Financial Analyst.

Your responsibility is to analyse companies using
the supplied structured business information.

Always return ONLY valid JSON.

Do not include markdown.

Do not include explanations.

Do not include code fences.

The JSON MUST exactly match the requested schema.
"""

        user = f"""
Analyse the following company.

Company Name:
{company.company_name}

Industry:
{company.industry}

Country:
{company.country}

Ticker:
{company.ticker}

Financial Snapshot:
{finance}

Generate:

1. Executive Summary

2. Business Analysis

3. Financial Analysis

4. SWOT Analysis

5. Risk Assessment

6. Investment Recommendation
"""

        return PromptTemplate(
            system=system.strip(),
            user=user.strip(),
        )
