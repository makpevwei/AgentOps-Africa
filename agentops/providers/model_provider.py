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

from langchain_core.language_models.chat_models import BaseChatModel
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
from langchain_openai import ChatOpenAI

from agentops.config.providers import LLMProvider
from agentops.config.settings import settings
from agentops.core.exceptions import ProviderError
from agentops.core.logger import logger


class ChatModelProvider:
    """
    Enterprise Chat Model Factory.

    Creates and returns the configured LLM provider
    based on application settings.

    Supported Providers:
        - OpenAI
        - Google Gemini
        - Groq
        - OpenRouter

    The provider is selected from the application
    configuration.

    Example:

        LLM_PROVIDER=openai
        OPENAI_MODEL=gpt-5.5
    """

    @staticmethod
    def create() -> BaseChatModel:
        """
        Create and return the configured chat model.

        Returns:
            BaseChatModel

        Raises:
            ProviderError:
                If an unsupported provider is configured.
        """

        provider = settings.LLM_PROVIDER.lower()

        # ============================================================
        # Resolve Model Name
        # ============================================================

        if provider == LLMProvider.OPENAI:
            model_name = settings.OPENAI_MODEL

        elif provider == LLMProvider.GROQ:
            model_name = settings.GROQ_MODEL

        elif provider == LLMProvider.GEMINI:
            model_name = settings.GEMINI_MODEL

        elif provider == LLMProvider.OPENROUTER:
            model_name = settings.OPENROUTER_MODEL

        else:
            raise ProviderError(
                f"Unsupported LLM Provider: {provider}"
            )

        logger.info("Initializing LLM Provider: %s", provider)
        logger.info("Using Model: %s", model_name)

        # ============================================================
        # OpenAI
        # ============================================================

        if provider == LLMProvider.OPENAI:
            return ChatOpenAI(
                model=model_name,
                temperature=settings.TEMPERATURE,
                timeout=settings.REQUEST_TIMEOUT,
                streaming=settings.STREAMING,
                max_retries=5,
            )

        # ============================================================
        # Google Gemini
        # ============================================================

        if provider == LLMProvider.GEMINI:
            return ChatGoogleGenerativeAI(
                model=model_name,
                temperature=settings.TEMPERATURE,
            )

        # ============================================================
        # Groq
        # ============================================================

        if provider == LLMProvider.GROQ:
            return ChatGroq(
                model=model_name,
                temperature=settings.TEMPERATURE,
            )

        # ============================================================
        # OpenRouter
        # ============================================================

        if provider == LLMProvider.OPENROUTER:
            return ChatOpenAI(
                api_key=settings.OPENROUTER_API_KEY,
                base_url=settings.OPENROUTER_BASE_URL,
                model=model_name,
                temperature=settings.TEMPERATURE,
                timeout=settings.REQUEST_TIMEOUT,
                streaming=settings.STREAMING,
                max_retries=5,
            )

        # ============================================================
        # Safety Check
        # ============================================================

        raise ProviderError(
            f"Failed to initialize provider: {provider}"
        )