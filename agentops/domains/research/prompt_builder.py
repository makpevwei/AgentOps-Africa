"""
Research Prompt Builder

Builds prompts for the Enterprise Research Analyzer.
"""

from agentops.domains.research.research_context import ResearchContext


class ResearchPromptBuilder:
    """
    Converts a ResearchContext into an enterprise
    research prompt.
    """

    @staticmethod
    def build(
        context: ResearchContext,
    ) -> str:

        company = context.company
        finance = context.finance

        quote = finance.quote if finance else None
        fundamentals = finance.fundamentals if finance else None

        price = quote.price if quote else "N/A"
        market_cap = quote.market_cap if quote else "N/A"

        description = (
            fundamentals.description
            if fundamentals and fundamentals.description
            else "N/A"
        )

        prompt = f"""
You are a Senior Equity Research Analyst working for a global investment firm.

Your task is to produce a professional institutional-quality research report.

Use the information below.

====================================================
COMPANY INFORMATION
====================================================

Company: {company.company_name}

Country: {company.country}

Industry: {company.industry}

Exchange: {company.exchange or "Private"}

Ticker: {company.ticker or "N/A"}

Current Price: {price}

Market Capitalization: {market_cap}

Business Description:
{description}

====================================================
INSTRUCTIONS
====================================================

Perform a professional business and investment analysis.

Use sound financial reasoning.

If information is unavailable, make reasonable professional assumptions and clearly state them.

Return ONLY valid JSON.

Do NOT include markdown.

Do NOT wrap the response inside ```json.

Do NOT explain your reasoning.

====================================================
JSON STRUCTURE
====================================================

{{
  "company": "string",

  "executive_summary": "string",

  "business": {{
    "overview": "string",
    "industry": "string",
    "headquarters": "string",
    "business_model": "string"
  }},

  "swot": {{
    "strengths": [
      "string"
    ],
    "weaknesses": [
      "string"
    ],
    "opportunities": [
      "string"
    ],
    "threats": [
      "string"
    ]
  }},

  "risks": {{
    "overall_risk": "Low | Medium | High",
    "financial_risk": "string",
    "operational_risk": "string",
    "regulatory_risk": "string",
    "confidence": 0.90
  }},

  "recommendation": {{
    "action": "Strong Buy | Buy | Hold | Sell | Strong Sell",
    "rationale": "string",
    "investment_horizon": "Short Term | Medium Term | Long Term",
    "confidence": 0.90
  }},

  "sections": [
    {{
      "title": "string",
      "summary": "string",
      "findings": [
        {{
          "title": "string",
          "summary": "string",
          "confidence": 0.90,
          "sources": [
            "string"
          ]
        }}
      ]
    }}
  ],

  "metadata": {{}}
}}

The JSON MUST conform exactly to this structure.
"""

        return prompt.strip()
