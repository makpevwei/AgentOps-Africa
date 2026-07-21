"""
Agent Registry
"""

from __future__ import annotations

from agentops.ai.runtime.base_agent import BaseAgent


class AgentRegistry:
    """Registry of all AI agents."""

    def __init__(self) -> None:
        self._agents: dict[str, BaseAgent] = {}

    def register(
        self,
        agent: BaseAgent,
    ) -> None:
        """
        Register an agent.
        """

        self._agents[
            agent.metadata.agent_id
        ] = agent

    def get(
        self,
        agent_id: str,
    ) -> BaseAgent:

        if agent_id not in self._agents:
            raise KeyError(
                f"Agent '{agent_id}' is not registered."
            )

        return self._agents[agent_id]

    def exists(
        self,
        agent_id: str,
    ) -> bool:

        return agent_id in self._agents

    def unregister(
        self,
        agent_id: str,
    ) -> None:

        self._agents.pop(agent_id, None)

    def list_agents(
        self,
    ) -> list[str]:

        return sorted(
            self._agents.keys()
        )


agent_registry = AgentRegistry()