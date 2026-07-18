"""
Base interface for all agent services.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.task import AgentTask


class BaseAgentService(ABC):
    """
    Base class for all Agent Services.
    """

    name: str

    @abstractmethod
    def execute(
        self,
        task: AgentTask,
        context: AgentContext,
    ) -> dict:
        """
        Execute an AgentTask using the shared execution context.
        """
        raise NotImplementedError
