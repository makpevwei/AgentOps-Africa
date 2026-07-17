from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict

# ==============================================================================
# PROJECT ROOT
# ==============================================================================

BASE_DIR = Path(__file__).resolve().parent.parent.parent


# ==============================================================================
# APPLICATION SETTINGS
# ==============================================================================


class Settings(BaseSettings):
    """
    Global application settings.

    All configuration values are loaded from the .env file.
    """

    # ==========================================================================
    # APPLICATION
    # ==========================================================================

    APP_NAME: str = "AgentOps Africa"

    APP_VERSION: str = "0.1.0"

    ENVIRONMENT: str = "development"

    DEBUG: bool = True

    LOG_LEVEL: str = "INFO"

    # ==========================================================================
    # LLM CONFIGURATION
    # ==========================================================================

    # LLM_PROVIDER: str = Field(default="groq")

    LLM_PROVIDER: str = Field(default="openai")

    OPENAI_MODEL: str = Field(default="gpt-4o-mini")

    GROQ_MODEL: str = Field(default="llama-3.3-70b-versatile")

    GEMINI_MODEL: str = Field(default="gemini-2.5-pro")

    OPENROUTER_MODEL: str = Field(default="openai/gpt-4.1")

    TEMPERATURE: float = Field(default=0.0)

    MAX_TOKENS: int = Field(default=4096)

    STREAMING: bool = Field(default=True)

    REQUEST_TIMEOUT: int = Field(default=120)

    # ==========================================================================
    # AI PROVIDER API KEYS
    # ==========================================================================

    OPENAI_API_KEY: str | None = None

    GOOGLE_API_KEY: str | None = None

    GROQ_API_KEY: str | None = None

    OPENROUTER_API_KEY: str | None = None

    NVIDIA_API_KEY: str | None = None

    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    # ==========================================================================
    # RESEARCH & SEARCH
    # ==========================================================================

    TAVILY_API_KEY: str | None = None

    GOOGLE_CSE_ID: str | None = None

    GOOGLE_CSE_API_KEY: str | None = None

    NEWSAPI_API_KEY: str | None = None

    WIKIPEDIA_LANGUAGE: str = "en"

    # ==========================================================================
    # FINANCE
    # ==========================================================================

    ALPHA_VANTAGE_API_KEY: str | None = None

    FINNHUB_API_KEY: str | None = None

    EXCHANGE_RATE_API_KEY: str | None = None

    # ==========================================================================
    # GOOGLE WORKSPACE
    # ==========================================================================

    GOOGLE_CREDENTIALS_FILE: str = "credentials.json"

    # ==========================================================================
    # TELEGRAM
    # ==========================================================================

    TELEGRAM_BOT_TOKEN: str | None = None

    TELEGRAM_CHAT_ID: str | None = None

    # ==========================================================================
    # WEATHER
    # ==========================================================================

    OPENWEATHER_API_KEY: str | None = None

    # ==========================================================================
    # LANGSMITH
    # ==========================================================================

    LANGSMITH_API_KEY: str | None = None

    LANGSMITH_TRACING: bool = True

    LANGSMITH_PROJECT: str = "AgentOps-Africa"

    # ==========================================================================
    # REPORTING
    # ==========================================================================

    REPORT_OUTPUT_DIR: str = "reports"

    DEFAULT_REPORT_FORMAT: str = "markdown"

    # ==========================================================================
    # PYDANTIC SETTINGS
    # ==========================================================================

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="ignore",
    )


# ==============================================================================
# GLOBAL SETTINGS INSTANCE
# ==============================================================================

settings = Settings()
