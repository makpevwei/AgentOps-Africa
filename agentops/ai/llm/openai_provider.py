"""
OpenAI Provider

Temporary provider implementation.

The real GPT-5 integration will be added in the next commit.
"""


class OpenAIProvider:
    """
    OpenAI implementation.
    """

    def generate(
        self,
        prompt: str,
    ) -> str:
        """
        Temporary implementation.
        """

        return f"LLM Placeholder Response: {prompt}"