"""
Agent Service

Coordinates AI interactions.
"""

from agentops.core.logger import logger
from agentops.domains.research.analysis_models import CompanyAnalysis
from agentops.domains.research.analyzers.executive_analyzer import (
    ExecutiveAnalyzer,
)
from agentops.domains.research.research_engine import ResearchEngine


class AgentService:
    """
    Service responsible for coordinating AI-powered company analysis.
    """

    def __init__(
        self,
        research_engine: ResearchEngine | None = None,
    ) -> None:
        self.research_engine = research_engine or ResearchEngine()
        self.executive = ExecutiveAnalyzer()

    def chat(
        self,
        message: str,
    ) -> CompanyAnalysis:
        """
        Analyze a company based on the user's message.
        """

        logger.info("Processing chat request: %s", message)

        context = self.research_engine.build_context(message)

        analysis = self.executive.analyze(context)

        logger.info(
            "Completed analysis for %s",
            analysis.company_name,
        )

        return analysis
