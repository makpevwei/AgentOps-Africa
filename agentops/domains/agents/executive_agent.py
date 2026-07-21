"""
Executive AI Agent.
"""

from agentops.domains.agents.base_agent import BaseAgent
from agentops.domains.research.analysis_models import CompanyAnalysis
from agentops.domains.research.analyzers.executive_analyzer import (
    ExecutiveAnalyzer,
)
from agentops.domains.research.research_engine import ResearchEngine


class ExecutiveAgent(BaseAgent):
    """
    Default executive AI worker.
    """

    def __init__(self) -> None:
        self.research = ResearchEngine()
        self.analyzer = ExecutiveAnalyzer()

    def execute(
        self,
        message: str,
    ) -> CompanyAnalysis:
        context = self.research.build_context(message)
        return self.analyzer.analyze(context)