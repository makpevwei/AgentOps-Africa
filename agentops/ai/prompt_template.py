"""
Shared prompt template model.
"""

from pydantic import BaseModel


class PromptTemplate(BaseModel):
    """
    Represents a chat prompt.

    Attributes:
        system:
            Instructions for the AI.

        user:
            User-specific content.
    """

    system: str

    user: str
