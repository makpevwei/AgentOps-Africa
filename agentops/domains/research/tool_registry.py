"""
Research Tool Registry

Registers and resolves research tools.
"""

from agentops.tools.research.tavily_tool import TavilyResearchTool


class ResearchToolRegistry:
    """
    Registry for all research tools.

    New tools are registered here instead
    of modifying the executor.
    """

    def __init__(self):

        self._tools = {
            "tavily": TavilyResearchTool(),
        }

    def get(self, tool_name: str):

        return self._tools.get(tool_name)

    def register(
        self,
        name: str,
        tool,
    ):

        self._tools[name] = tool

    def available_tools(self):

        return list(self._tools.keys())