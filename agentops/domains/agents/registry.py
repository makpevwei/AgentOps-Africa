"""
Agent Registry

Maintains the available executable agents.
"""

from __future__ import annotations

from agentops.domains.agents.base_agent import BaseAgent
from agentops.domains.agents.implementations.company_agent import CompanyAgent
from agentops.domains.agents.implementations.finance_agent import FinanceAgent
from agentops.domains.agents.implementations.research_agent import ResearchAgent


class AgentRegistry:
    """
    Registry of executable agents.
    """

    def __init__(self) -> None:
        self._agents: dict[str, BaseAgent] = {}

    def register(self, agent: BaseAgent) -> None:
        self._agents[agent.service_name] = agent

    def register_defaults(self) -> None:
        """
        Register all built-in agents.
        """

        self.register(CompanyAgent())
        self.register(FinanceAgent())
        self.register(ResearchAgent())

    def get(self, service_name: str) -> BaseAgent:
        try:
            return self._agents[service_name]
        except KeyError as exc:
            raise ValueError(f"No agent registered for '{service_name}'.") from exc

    @property
    def services(self) -> list[str]:
        return sorted(self._agents.keys())
