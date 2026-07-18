"""
Base Workflow.

Defines the contract implemented by all workflows in AgentOps.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.agents.execution_plan import ExecutionPlan

TResult = TypeVar("TResult")


class BaseWorkflow(ABC, Generic[TResult]):
    """
    Base class for all workflows.

    A workflow defines *what* should happen to achieve a business goal.
    The Runtime is responsible for *executing* the resulting execution plan.
    """

    #: Unique workflow name.
    name: str

    @abstractmethod
    def validate(
        self,
        context: AgentContext,
    ) -> None:
        """
        Validate the workflow inputs.

        Raises:
            ValueError: If required input is missing.
        """
        raise NotImplementedError

    @abstractmethod
    def build_plan(
        self,
        context: AgentContext,
    ) -> ExecutionPlan:
        """
        Build the execution plan for this workflow.
        """
        raise NotImplementedError

    @abstractmethod
    def process(
        self,
        context: AgentContext,
    ) -> TResult:
        """
        Transform the populated AgentContext into a business result.
        """
        raise NotImplementedError

    def finalize(
        self,
        context: AgentContext,
        result: TResult,
    ) -> TResult:
        """
        Perform optional post-processing.

        Subclasses may override this to generate reports,
        persist artifacts, publish events, or record metrics.
        """
        return result
