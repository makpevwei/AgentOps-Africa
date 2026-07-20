"""
Base Agent

Defines the contract implemented by every executable agent.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any

from agentops.domains.agents.execution_context import ExecutionContext
from agentops.domains.agents.task import AgentTask


class BaseAgent(ABC):
    """
    Base class for all executable agents.
    """

    @property
    @abstractmethod
    def service_name(self) -> str:
        """
        Name used by the planner.
        """

    @abstractmethod
    def execute(
        self,
        task: AgentTask,
        context: ExecutionContext,
    ) -> Any:
        """
        Execute a task and return a domain object.
        """
