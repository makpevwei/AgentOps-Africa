"""
Generic LLM Analyzer

Reusable AI execution layer for all analyzers.
"""

import json
from typing import Type

from langchain_core.messages import HumanMessage, SystemMessage
from pydantic import BaseModel, ValidationError

from agentops.ai.prompt_template import PromptTemplate
from agentops.ai.ai_client import AIClient


class LLMAnalyzer:
    """
    Executes prompts against an LLM and validates
    the response into a Pydantic model.
    """

    def __init__(self):
        self._client = AIClient()

    def run(
        self,
        prompt: PromptTemplate,
        response_model: Type[BaseModel],
    ) -> BaseModel:
        """
        Execute the prompt and validate the response.
        """

        messages = [
            SystemMessage(content=prompt.system),
            HumanMessage(content=prompt.user),
        ]

        response = self._client.invoke(messages)

        content = response.content

        if not isinstance(content, str):
            raise ValueError(
                "Expected string response from LLM."
            )

        try:
            data = json.loads(content)
            return response_model.model_validate(data)

        except json.JSONDecodeError as ex:
            raise ValueError(
                "LLM returned invalid JSON."
            ) from ex

        except ValidationError as ex:
            raise ValueError(
                f"{response_model.__name__} validation failed."
            ) from ex