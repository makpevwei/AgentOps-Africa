from typing import List

from agentops.clients.tavily_client import TavilyClientService
from agentops.core.logger import logger
from agentops.domains.research.models import ResearchResult


class TavilyResearchTool:
    """
    Converts Tavily responses into
    ResearchResult objects.
    """

    def __init__(self):

        self.client = TavilyClientService()

    def search(
        self,
        query: str,
        max_results: int = 5,
    ) -> List[ResearchResult]:

        response = self.client.search(
            query=query,
            max_results=max_results,
        )

        findings = []

        for item in response.get("results", []):

            findings.append(

                ResearchResult(

                    source="Tavily",

                    title=item.get("title", ""),

                    summary=item.get("content", ""),

                    url=item.get("url"),

                    confidence=0.90,

                    metadata={
                        "score": item.get("score"),
                    },
                )

            )

        logger.info(
            f"Normalized {len(findings)} Tavily result(s)"
        )

        return findings