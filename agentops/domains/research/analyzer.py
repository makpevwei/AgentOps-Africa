"""
Research Analyzer

Uses an LLM to convert a ResearchContext into
a structured ResearchReport.
"""

import json

from pydantic import ValidationError

from agentops.domains.research.prompt_builder import ResearchPromptBuilder
from agentops.domains.research.report_models import ResearchReport
from agentops.domains.research.research_context import ResearchContext
from agentops.providers.model_provider import ChatModelProvider


class ResearchAnalyzer:
    """
    AI-powered research analyzer.
    """

    def __init__(self):

        self._llm = ChatModelProvider.create()

    def analyze(
        self,
        context: ResearchContext,
    ) -> ResearchReport:

        prompt = ResearchPromptBuilder.build(context)

        response = self._llm.invoke(prompt)

        content = response.content

        if not isinstance(content, str):
            raise ValueError("Expected string response from LLM.")

        try:
            data = json.loads(content)

            return ResearchReport.model_validate(data)

        except json.JSONDecodeError as ex:
            raise ValueError(
                "LLM did not return valid JSON."
            ) from ex

        except ValidationError as ex:
            raise ValueError(
                "LLM JSON does not match ResearchReport schema."
            ) from ex