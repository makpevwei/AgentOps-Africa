"""
Research Prompt Builder

Builds prompts for the Research Analyzer.
"""

from agentops.domains.research.research_context import ResearchContext


class ResearchPromptBuilder:
    """
    Converts a ResearchContext into a prompt
    suitable for LLM analysis.
    """

    @staticmethod
    def build(
        context: ResearchContext,
    ) -> str:

        company = context.company
        finance = context.finance

        quote = finance.quote if finance else None
        fundamentals = finance.fundamentals if finance else None

        prompt = f"""
You are a senior financial research analyst.

Analyze the following company and produce a structured investment research report.

Company:
{company.company_name}

Country:
{company.country}

Industry:
{company.industry}

Ticker:
{company.ticker}

Current Price:
{quote.price if quote else "N/A"}

Market Cap:
{quote.market_cap if quote else "N/A"}

Business Description:
{fundamentals.description if fundamentals else "N/A"}

The report should include:

1. Executive Summary
2. Business Overview
3. Industry Position
4. Strengths
5. Risks
6. Opportunities
7. Recommendation
8. Confidence Score

Respond ONLY with valid JSON.

The JSON MUST match this schema exactly:

{{
  "company": "...",
  "executive_summary": "...",
  "recommendation": "...",
  "confidence": 0.95,
  "sections": [
    {{
      "title": "...",
      "content": "...",
      "findings": [
        {{
          "title": "...",
          "summary": "...",
          "confidence": 0.95,
          "sources": []
        }}
      ]
    }}
  ],
  "metadata": {{}}
}}

Rules:
- Return ONLY valid JSON.
- Do NOT include markdown.
- Do NOT wrap the JSON in ```json fences.
- Do NOT add explanations.
- Ensure all required fields are present.
- Ensure confidence is a number between 0 and 1.
"""

        return prompt.strip()