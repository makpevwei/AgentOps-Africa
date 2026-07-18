"""
OpenAI Analysis Provider.

Executes structured business analysis using an OpenAI model.
"""

from __future__ import annotations

import json

from openai import OpenAI

from agentops.domains.analysis.analysis_models import AnalysisResult
from agentops.domains.analysis.providers.base_provider import (
    BaseAnalysisProvider,
)


class OpenAIAnalysisProvider(BaseAnalysisProvider):
    """
    OpenAI implementation of the Analysis Provider.
    """

    name = "openai"

    def __init__(
        self,
        model: str = "gpt-5",
    ) -> None:
        self.client = OpenAI()
        self.model = model

    def analyze(
        self,
        prompt: str,
    ) -> AnalysisResult:
        """
        Execute business analysis using OpenAI.
        """

        response = self.client.chat.completions.create(
            model=self.model,
            response_format={
                "type": "json_object",
            },
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        content = response.choices[0].message.content

        if content is None:
            raise ValueError("Model returned no content.")

        data = json.loads(content)

        return AnalysisResult.model_validate(data)
