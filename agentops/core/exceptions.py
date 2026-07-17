class AgentOpsError(Exception):
    """Base application exception."""


class ConfigurationError(AgentOpsError):
    """Raised when configuration is invalid."""


class ProviderError(AgentOpsError):
    """Raised when an LLM provider fails."""
