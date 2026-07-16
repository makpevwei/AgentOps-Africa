from abc import ABC, abstractmethod

from agentops.tools.research.research_result import ResearchResult


class BaseResearchTool(ABC):
    """
    Base class for every research tool.

    All research tools must inherit from this class.
    """

    name: str = "Base Research Tool"

    description: str = ""

    @abstractmethod
    def search(self, query: str) -> list[ResearchResult]:
        """
        Execute a search and return a list of ResearchResult objects.
        """
        raise NotImplementedError