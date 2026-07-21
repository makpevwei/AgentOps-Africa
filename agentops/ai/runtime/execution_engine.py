"""
Execution Engine

Coordinates execution of AI agents.
"""

from __future__ import annotations

from agentops.ai.runtime.agent_context import AgentContext
from agentops.ai.runtime.agent_registry import agent_registry
from agentops.ai.runtime.agent_result import AgentResult
from agentops.core.logger import logger


class ExecutionEngine:
    """Coordinates execution of AI agents."""

    async def execute(
        self,
        *,
        agent_id: str,
        context: AgentContext,
    ) -> AgentResult:
        """
        Execute a registered AI agent.
        """

        logger.info(
            "Executing agent '%s'",
            agent_id,
        )

        agent = agent_registry.get(agent_id)

        result = await agent.execute(context)

        logger.info(
            "Agent '%s' completed successfully",
            agent_id,
        )

        return result


execution_engine = ExecutionEngine()