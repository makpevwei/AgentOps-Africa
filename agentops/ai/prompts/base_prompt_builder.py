"""
Base Prompt Builder

Defines the contract for all prompt builders.
"""

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from agentops.ai.prompt_template import PromptTemplate

ContextType = TypeVar("ContextType")


class BasePromptBuilder(ABC, Generic[ContextType]):
    """
    Base class for all prompt builders.
    """

    @abstractmethod
    def build(
        self,
        context: ContextType,
    ) -> PromptTemplate:
        """
        Build a prompt template.

        Args:
            context:
                Domain-specific context.

        Returns:
            PromptTemplate
        """
        raise NotImplementedError