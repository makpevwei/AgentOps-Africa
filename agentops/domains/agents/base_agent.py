"""
Base interface for AI workers.
"""

from abc import ABC, abstractmethod

from agentops.domains.agents.agent_result import AgentResult


class BaseAgent(ABC):
    """
    Base class for all AI workers.
    """

    @abstractmethod
    def execute(
        self,
        message: str,
    ) -> AgentResult:
        """
        Execute a task.
        """
        raise NotImplementedError
