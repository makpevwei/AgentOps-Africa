from langchain_core.tools import tool

from agentops.tools.research.tavily_tool import TavilyResearchTool


_tavily = TavilyResearchTool()


@tool
def tavily_search(query: str) -> str:
    """
    Search the web using Tavily.
    """

    results = _tavily.search(query)

    output = []

    for item in results:

        output.append(

            f"""
Title:
{item.title}

Summary:
{item.summary}

URL:
{item.url}
"""
        )

    return "\n\n".join(output)