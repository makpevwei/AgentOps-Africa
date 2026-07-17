"""
Generic LLM Analyzer

Reusable AI execution layer for all analyzers.
"""

import json
from typing import Type

from pydantic import BaseModel, ValidationError

from agentops.providers.model_provider import ChatModelProvider


class LLMAnalyzer:
    """
    Executes prompts against an LLM and validates
    the response into a Pydantic model.
    """

    def __init__(self):

        self._llm = ChatModelProvider.create()

    def run(
        self,
        prompt: str,
        response_model: Type[BaseModel],
    ) -> BaseModel:
        """
        Execute the prompt and validate the response.

        Args:
            prompt:
                Prompt sent to the LLM.

            response_model:
                Expected Pydantic model.

        Returns:
            Instance of response_model.
        """

        response = self._llm.invoke(prompt)

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