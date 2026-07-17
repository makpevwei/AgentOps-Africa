"""
Enterprise Company Discovery Service
"""

from agentops.tools.research.tavily_tool import TavilyResearchTool


class CompanyDiscovery:
    def __init__(self):
        self.tool = TavilyResearchTool()

    def search(self, company_name: str):
        return self.tool.search(company_name)
