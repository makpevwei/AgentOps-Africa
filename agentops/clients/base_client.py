"""
Base Client

Every external API client should inherit from this class.
"""

from abc import ABC


class BaseClient(ABC):
    """
    Base class for external service clients.
    """

    service_name: str = "Unknown Service"