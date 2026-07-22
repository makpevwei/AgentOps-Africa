from tavily import TavilyClient

from agentops.config import settings
from agentops.core.logger import logger


class TavilyClientService:
    """
    Enterprise Tavily API Client.

    Responsible ONLY for communicating
    with Tavily.
    """

    def __init__(self):

        if not settings.TAVILY_API_KEY:
            raise ValueError("Missing TAVILY_API_KEY.")

        self.client = TavilyClient(api_key=settings.TAVILY_API_KEY)

    def search(
        self,
        query: str,
        max_results: int = 5,
        search_depth: str = "advanced",
    ):

        logger.info("Tavily Client -> %s", query)

        return self.client.search(
            query=query,
            max_results=max_results,
            search_depth=search_depth,
        )
