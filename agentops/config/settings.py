"""
Application Settings

Central configuration for the AgentOps platform.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # ------------------------------------------------------------------
    # Application
    # ------------------------------------------------------------------

    APP_NAME: str = "AgentOps Africa"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # ------------------------------------------------------------------
    # Database
    # ------------------------------------------------------------------

    DATABASE_URL: str = "sqlite:///./agentops.db"

    # ------------------------------------------------------------------
    # JWT
    # ------------------------------------------------------------------

    JWT_SECRET_KEY: str = "change-this-secret"
    JWT_ALGORITHM: str = "HS256"

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # ------------------------------------------------------------------
    # LLM Provider
    # ------------------------------------------------------------------

    LLM_PROVIDER: str = "openai"

    DEFAULT_MODEL: str = "gpt-5.5"

    OPENAI_MODEL: str = "gpt-5.5"
    GEMINI_MODEL: str = "gemini-2.5-pro"
    GROQ_MODEL: str = "llama-3.3-70b-versatile"
    OPENROUTER_MODEL: str = "openai/gpt-5.5"

    # ------------------------------------------------------------------
    # API Keys
    # ------------------------------------------------------------------

    OPENAI_API_KEY: str | None = None
    OPENROUTER_API_KEY: str | None = None
    OPENROUTER_BASE_URL: str = "https://openrouter.ai/api/v1"

    TAVILY_API_KEY: str | None = None

    # ------------------------------------------------------------------
    # Model Behaviour
    # ------------------------------------------------------------------

    TEMPERATURE: float = 0.1
    REQUEST_TIMEOUT: int = 120
    STREAMING: bool = False

    # ------------------------------------------------------------------
    # Feature Flags
    # ------------------------------------------------------------------

    USE_AI_PLANNER: bool = False

    @property
    def use_ai_planner(self) -> bool:
        """
        Backward compatibility while the codebase migrates.
        """
        return self.USE_AI_PLANNER

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()