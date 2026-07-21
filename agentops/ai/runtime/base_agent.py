"""
Base Agent

Abstract base class for all AI employees.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from time import perf_counter

from agentops.ai.agents.base.metadata import AgentMetadata
from agentops.ai.runtime.agent_context import AgentContext
from agentops.ai.runtime.agent_result import AgentResult
from agentops.core.logger import logger


class BaseAgent(ABC):
    """Base class for every AI employee."""

    def __init__(
        self,
        metadata: AgentMetadata,
    ) -> None:
        self.metadata = metadata

    async def execute(
        self,
        context: AgentContext,
    ) -> AgentResult:

        logger.info(
            "%s started",
            self.metadata.name,
        )

        started = perf_counter()

        await self.before_execute(context)

        await self.think(context)

        await self.plan(context)

        result = await self.run(context)

        await self.reflect(context, result)

        await self.after_execute(context, result)

        result.execution_time = perf_counter() - started

        logger.info(
            "%s completed in %.2fs",
            self.metadata.name,
            result.execution_time,
        )

        return result

    async def before_execute(
        self,
        context: AgentContext,
    ) -> None:
        return None

    async def after_execute(
        self,
        context: AgentContext,
        result: AgentResult,
    ) -> None:
        return None

    async def think(
        self,
        context: AgentContext,
    ) -> None:
        return None

    async def plan(
        self,
        context: AgentContext,
    ) -> None:
        return None

    async def reflect(
        self,
        context: AgentContext,
        result: AgentResult,
    ) -> None:
        return None

    @abstractmethod
    async def run(
        self,
        context: AgentContext,
    ) -> AgentResult:
        raise NotImplementedError
