"""
Agent Service Registry
"""

from __future__ import annotations

from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.company_agent_service import (
    CompanyAgentService,
)
from agentops.domains.agents.finance_agent_service import (
    FinanceAgentService,
)
from agentops.domains.agents.research_agent_service import (
    ResearchAgentService,
)


class ServiceRegistry:
    """
    Registry of all Agent Services available to the runtime.
    """

    def __init__(self) -> None:
        self._services: dict[str, BaseAgentService] = {}

        self._register_defaults()

    def _register_defaults(self) -> None:
        """
        Register the built-in agent services.
        """

        self.register(CompanyAgentService())

        self.register(FinanceAgentService())

        self.register(ResearchAgentService())

    def register(
        self,
        service: BaseAgentService,
    ) -> None:
        """
        Register an Agent Service.
        """

        self._services[service.name] = service

    def get(
        self,
        name: str,
    ) -> BaseAgentService | None:
        """
        Retrieve a registered Agent Service.
        """

        return self._services.get(name)

    def services(
        self,
    ) -> list[BaseAgentService]:
        """
        Return all registered services.
        """

        return list(self._services.values())
