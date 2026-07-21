"""
Agent Service

Coordinates AI interactions.
"""

from agentops.core.logger import logger
from agentops.domains.agents.agent_result import AgentResult
from agentops.domains.agents.planner import Planner
from agentops.domains.agents.registry import AgentRegistry


class AgentService:
    """
    Coordinates AI workers.
    """

    def __init__(
        self,
        planner: Planner | None = None,
        registry: AgentRegistry | None = None,
    ) -> None:
        self.planner = planner or Planner()
        self.registry = registry or AgentRegistry()

    def chat(
        self,
        message: str,
    ) -> AgentResult:
        logger.info("Processing chat request: %s", message)

        agent_type = self.planner.decide(message)

        logger.info("Planner selected agent: %s", agent_type)

        agent = self.registry.get(agent_type)

        result = agent.execute(message)

        logger.info("Agent completed successfully.")

        return result