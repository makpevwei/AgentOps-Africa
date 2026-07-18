"""
Analysis Orchestrator.

Coordinates prompt generation and LLM execution.
"""

from __future__ import annotations

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.analysis.analysis_models import AnalysisResult
from agentops.domains.analysis.prompt_builder import PromptBuilder
from agentops.domains.analysis.providers.base_provider import BaseAnalysisProvider


class AnalysisOrchestrator:
    """
    Coordinates the end-to-end analysis workflow.
    """

    def __init__(
        self,
        provider: BaseAnalysisProvider,
    ) -> None:
        self.provider = provider
        self.prompt_builder = PromptBuilder()

    def analyze(
        self,
        context: AgentContext,
    ) -> AnalysisResult:
        """
        Generate an analysis from the supplied context.
        """

        prompt = self.prompt_builder.build(context)

        return self.provider.analyze(prompt)
