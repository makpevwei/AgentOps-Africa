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

Your responsibility is to perform a professional financial analysis of a company.

Base your analysis on the financial metrics provided.

Return ONLY valid JSON.

Do not include markdown.

Do not wrap the response inside code fences.

Be concise but insightful.
"""

        user = f"""
Analyze the following financial information.

Company:
{company.company_name}

Industry:
{company.industry}

Country:
{company.country}

=========================
MARKET DATA
=========================

Current Price:
{quote.current_price}

Currency:
{quote.currency}

52 Week High:
{quote.high_52_week}

52 Week Low:
{quote.low_52_week}

=========================
FUNDAMENTALS
=========================

Market Cap:
{fundamentals.market_cap}

Enterprise Value:
{fundamentals.enterprise_value}

PE Ratio:
{fundamentals.pe_ratio}

Forward PE:
{fundamentals.forward_pe}

EPS:
{fundamentals.eps}

Dividend Yield:
{fundamentals.dividend_yield}

Revenue:
{fundamentals.revenue}

Gross Margin:
{fundamentals.gross_margin}

Operating Margin:
{fundamentals.operating_margin}

Net Margin:
{fundamentals.net_margin}

ROE:
{fundamentals.return_on_equity}

Debt to Equity:
{fundamentals.debt_to_equity}

Current Ratio:
{fundamentals.current_ratio}

Free Cash Flow:
{fundamentals.free_cash_flow}

=========================
OUTPUT FORMAT
=========================

Return ONLY valid JSON in this format.

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
