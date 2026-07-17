"""
Base Analyzer

Defines the contract for all research analyzers.
"""

from abc import ABC, abstractmethod

from agentops.domains.research.research_context import ResearchContext


class BaseAnalyzer(ABC):
    """
    Base class for every specialized analyzer.
    """

    @abstractmethod
    def analyze(
        self,
        context: ResearchContext,
    ):
        """
        Analyze a ResearchContext and return
        a domain-specific result.
        """
        raise NotImplementedError
