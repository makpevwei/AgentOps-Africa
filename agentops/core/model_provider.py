"""
Enterprise Model Factory

This module centralizes the creation of all LLM providers.

Supported Providers
-------------------
- OpenAI
- Google Gemini
- Groq
- OpenRouter

Future Providers
----------------
- Azure OpenAI
- Ollama
- NVIDIA NIM
"""

from langchain_openai import ChatOpenAI
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

from agentops.config.settings import settings
from agentops.config.providers import LLMProvider
from agentops.core.exceptions import ProviderError
from agentops.core.logger import logger


class ChatModelProvider:
    """
    Creates the configured chat model.

    The provider is selected from the .env file.

    Example:

        LLM_PROVIDER=openai

        DEFAULT_MODEL=gpt-4o-mini
    """

    @staticmethod
    def create():

        provider = settings.LLM_PROVIDER.lower()

        logger.info(f"Initializing LLM Provider: {provider}")

        # ============================================================
        # OpenAI
        # ============================================================

        if provider == LLMProvider.OPENAI:

            return ChatOpenAI(
                model=settings.DEFAULT_MODEL,
                temperature=settings.TEMPERATURE,
                timeout=settings.REQUEST_TIMEOUT,
                streaming=settings.STREAMING,
            )

        # ============================================================
        # Gemini
        # ============================================================

        elif provider == LLMProvider.GEMINI:

            return ChatGoogleGenerativeAI(
                model=settings.DEFAULT_MODEL,
                temperature=settings.TEMPERATURE,
            )

        # ============================================================
        # Groq
        # ============================================================

        elif provider == LLMProvider.GROQ:

            return ChatGroq(
                model=settings.DEFAULT_MODEL,
                temperature=settings.TEMPERATURE,
            )

        # ============================================================
        # OpenRouter
        # ============================================================

        elif provider == LLMProvider.OPENROUTER:

            return ChatOpenAI(
                api_key=settings.OPENROUTER_API_KEY,
                base_url=settings.OPENROUTER_BASE_URL,
                model=settings.DEFAULT_MODEL,
                temperature=settings.TEMPERATURE,
                timeout=settings.REQUEST_TIMEOUT,
                streaming=settings.STREAMING,
            )

        # ============================================================
        # Unsupported
        # ============================================================

        raise ProviderError(
            f"Unsupported LLM Provider: {provider}"
        )