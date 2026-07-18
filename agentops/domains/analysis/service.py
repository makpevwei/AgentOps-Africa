"""
Analysis Service.
"""

from __future__ import annotations

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.analysis.analysis_models import AnalysisResult
from agentops.domains.analysis.orchestrator import AnalysisOrchestrator
from agentops.domains.analysis.providers.provider_factory import (
    AnalysisProviderFactory,
)


class AnalysisService:
    """
    High-level service for generating business analysis.
    """

    def __init__(
        self,
        provider: str = "openai",
    ) -> None:
        factory = AnalysisProviderFactory()

        self.orchestrator = AnalysisOrchestrator(factory.get(provider))

    def analyze(
        self,
        context: AgentContext,
    ) -> AnalysisResult:
        """
        Generate a business analysis.
        """
        return self.orchestrator.analyze(context)
