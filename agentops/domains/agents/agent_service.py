"""
Agent Service

Coordinates AI interactions.
"""

from agentops.domains.research.analyzers.executive_analyzer import (
    ExecutiveAnalyzer,
)
from agentops.domains.research.research_engine import ResearchEngine


class AgentService:
    def __init__(
        self,
        research_engine: ResearchEngine | None = None,
    ):
        self.research_engine = research_engine or ResearchEngine()
        self.executive = ExecutiveAnalyzer()

    def chat(
        self,
        message: str,
    ):

        context = self.research_engine.build_context(message)

        return self.executive.analyze(context)
