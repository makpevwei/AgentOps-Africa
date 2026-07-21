"""
Agent Registry.
"""

from agentops.domains.agents.base_agent import BaseAgent
from agentops.domains.agents.executive_agent import ExecutiveAgent
from agentops.domains.agents.planner import AgentType


class AgentRegistry:
    """
    Registry of available AI workers.
    """

    def __init__(self) -> None:
        self._agents: dict[AgentType, BaseAgent] = {
            AgentType.RESEARCH: ExecutiveAgent(),
            AgentType.EXECUTIVE: ExecutiveAgent(),
            AgentType.PROPOSAL: ExecutiveAgent(),
            AgentType.FINANCE: ExecutiveAgent(),
            AgentType.SALES: ExecutiveAgent(),
            AgentType.GENERAL: ExecutiveAgent(),
        }

    def get(
        self,
        agent_type: AgentType,
    ) -> BaseAgent:
        """
        Return an agent instance.
        """
        return self._agents[agent_type]