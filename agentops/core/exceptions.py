"""
Application exceptions.

Centralized exceptions used across the AgentOps platform.
"""

from __future__ import annotations


class AgentOpsException(Exception):
    """Base exception for all application-specific errors."""

    def __init__(self, message: str) -> None:
        self.message = message
        super().__init__(message)


# ============================================================
# Business Exceptions
# ============================================================


class NotFoundException(AgentOpsException):
    """Raised when a requested resource cannot be found."""


class ValidationException(AgentOpsException):
    """Raised when validation fails."""


class BusinessRuleException(AgentOpsException):
    """Raised when a business rule is violated."""


class AuthenticationException(AgentOpsException):
    """Raised when authentication fails."""


class AuthorizationException(AgentOpsException):
    """Raised when authorization fails."""


# ============================================================
# AI / Provider Exceptions
# ============================================================


class AIException(AgentOpsException):
    """Base exception for AI-related operations."""


class ProviderError(AIException):
    """Raised when an AI provider cannot be initialized or used."""


class ModelError(AIException):
    """Raised when the selected AI model fails."""


class PromptError(AIException):
    """Raised when prompt generation fails."""


class ResearchError(AIException):
    """Raised when research generation fails."""
