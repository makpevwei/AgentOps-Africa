"""
Business Prompt Builder
"""

from agentops.ai.prompt_template import PromptTemplate
from agentops.ai.prompts.base_prompt_builder import BasePromptBuilder
from agentops.domains.research.research_context import ResearchContext


class BusinessPromptBuilder(BasePromptBuilder[ResearchContext]):
    """
    Builds prompts for business analysis.
    """

    def build(
        self,
        context: ResearchContext,
    ) -> PromptTemplate:

        company = context.company

        system = """
You are a Senior Business Strategy Consultant.

Your job is to analyze companies objectively.

Return ONLY valid JSON.

Do not include markdown.

Do not wrap the response in code fences.
"""

        user = f"""
Analyze the following company.

Company:
{company.company_name}

Country:
{company.country}

Industry:
{company.industry}

Return JSON in the following format:

{{
    "overview": "...",
    "industry": "...",
    "headquarters": "...",
    "business_model": "...",
    "competitive_position": "..."
}}
"""

        return PromptTemplate(
            system=system.strip(),
            user=user.strip(),
        )
