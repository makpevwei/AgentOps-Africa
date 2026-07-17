"""
Enterprise Company Normalizer

Uses the configured LLM to convert research
findings into a structured CompanyProfile.
"""

from langchain_core.messages import HumanMessage

from agentops.providers.model_provider import ChatModelProvider
from agentops.domains.companies.models import CompanyProfile
from agentops.domains.research.models import ResearchResult


class CompanyNormalizer:

    def __init__(self):

        model = ChatModelProvider.create()

        # GPT-5 / Gemini support structured output
        self.model = model.with_structured_output(
            CompanyProfile
        )

    def normalize(
        self,
        query: str,
        findings: list[ResearchResult],
    ) -> CompanyProfile:

        context = ""

        for item in findings:

            context += f"""

Source:
{item.source}

Title:
{item.title}

Summary:
{item.summary}

URL:
{item.url}

"""

        prompt = f"""
You are an expert financial analyst.

A user searched for:

{query}

Using ONLY the information below, determine the following fields:

1. Official company name.

2. Aliases.
Include:
- common abbreviations
- former company names
- well-known brand names
- common search terms

Examples:

Moniepoint →
["Moniepoint","Moniepoint Inc.","TeamApt"]

GTCO →
["GTCO","GTB","Guaranty Trust Bank"]

Google →
["Google","Alphabet"]

Tesla →
["Tesla","Tesla Inc."]

If no aliases are known,
return an empty list.

3. Stock ticker (if publicly traded)

4. Stock exchange

5. Country

6. Industry

7. Sector

8. Official website

Return ONLY valid structured data.

If information is unknown,
leave the field empty.

Research:

{context}
"""

        return self.model.invoke(
            [
                HumanMessage(
                    content=prompt
                )
            ]
        )