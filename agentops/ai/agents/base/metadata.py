from dataclasses import dataclass

from agentops.ai.agents.base.capabilities import Capability


@dataclass(slots=True, frozen=True)
class AgentMetadata:
    """Metadata describing an AI agent."""

    agent_id: str

    name: str

    description: str

    version: str = "1.0.0"

    capabilities: tuple[Capability, ...] = ()

    tags: tuple[str, ...] = ()
