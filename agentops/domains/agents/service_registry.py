"""
Agent Service Registry
"""

from __future__ import annotations

from agentops.domains.agents.base_agent_service import BaseAgentService
from agentops.domains.agents.company_agent_service import CompanyAgentService
from agentops.domains.agents.finance_agent_service import FinanceAgentService


class ServiceRegistry:
    def __init__(self):

        self._services: dict[str, BaseAgentService] = {}

        self._register_defaults()

    def _register_defaults(self):

        self.register(CompanyAgentService())

        self.register(FinanceAgentService())

    def register(
        self,
        service: BaseAgentService,
    ):

        self._services[service.name] = service

    def get(
        self,
        name: str,
    ) -> BaseAgentService | None:

        return self._services.get(name)

    def services(
        self,
    ) -> list[BaseAgentService]:

        return list(self._services.values())
