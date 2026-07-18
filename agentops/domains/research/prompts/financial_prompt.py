"""
Financial Prompt Builder

Builds prompts for financial analysis.
"""

from agentops.ai.prompt_template import PromptTemplate
from agentops.ai.prompts.base_prompt_builder import BasePromptBuilder
from agentops.domains.research.research_context import ResearchContext


class FinancialPromptBuilder(BasePromptBuilder[ResearchContext]):
    """
    Builds prompts for financial analysis.
    """

    def build(
        self,
        context: ResearchContext,
    ) -> PromptTemplate:
        """
        Build the financial analysis prompt.
        """

        company = context.company
        finance = context.finance

        quote = finance.quote
        fundamentals = finance.fundamentals

        system = """
You are a Senior Equity Research Analyst.

Your responsibility is to perform a professional financial analysis of a company using ONLY the financial information provided.

Do not invent financial metrics that are missing.

Return ONLY valid JSON.

Do not include markdown.

Do not wrap the response inside code fences.

Be concise but insightful.
"""

        user = f"""
Analyze the following company.

=========================
COMPANY
=========================

Company:
{company.company_name}

Industry:
{company.industry}

Country:
{company.country}

=========================
MARKET DATA
=========================

Ticker:
{quote.symbol if quote else "N/A"}

Exchange:
{quote.exchange if quote else "N/A"}

Current Price:
{quote.price if quote else "N/A"}

Previous Close:
{quote.previous_close if quote else "N/A"}

Price Change:
{quote.change if quote else "N/A"}

Change Percent:
{quote.change_percent if quote else "N/A"}

Currency:
{quote.currency if quote else "N/A"}

Market Cap:
{quote.market_cap if quote else "N/A"}

Volume:
{quote.volume if quote else "N/A"}

=========================
COMPANY INFORMATION
=========================

Sector:
{fundamentals.sector if fundamentals else "N/A"}

Industry:
{fundamentals.industry if fundamentals else "N/A"}

Employees:
{fundamentals.employees if fundamentals else "N/A"}

Website:
{fundamentals.website if fundamentals else "N/A"}

Description:
{fundamentals.description if fundamentals else "N/A"}

=========================
OUTPUT FORMAT
=========================

Return ONLY valid JSON.

{{
    "summary": "...",
    "valuation": "...",
    "profitability": "...",
    "growth": "...",
    "financial_strength": "..."
}}
"""

        return PromptTemplate(
            system=system.strip(),
            user=user.strip(),
        )
