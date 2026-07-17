"""
Enterprise Agent Builder

Responsible for constructing AI Agents for AgentOps Africa.

Supported Builders
------------------
- Deep Agent (DeepAgents)
- Chat Agent (LangGraph / LangChain)

Future Builders
---------------
- Multi-Agent Supervisor
- Planning Agent
- Human-in-the-Loop Agent
"""

from deepagents import create_deep_agent

from langgraph.prebuilt import create_react_agent

from agentops.providers.model_provider import ChatModelProvider
from agentops.core.logger import logger


class AgentBuilder:
    """
    Enterprise factory responsible for constructing AI agents.

    Every agent in the platform should be created through this class.

    This allows the implementation of the agent to change later without
    affecting the business logic.
    """

    # ==========================================================
    # Deep Research Agent
    # ==========================================================

    @staticmethod
    def build_deep_agent(
        *,
        tools,
        system_prompt: str,
        name: str = "DeepResearchAgent",
    ):
        """
        Build a DeepAgents research agent.

        Best suited for:

        - Deep Research
        - Long reasoning
        - Multi-step planning
        - Report generation
        """

        logger.info("Building Deep Agent: %s", name)

        model = ChatModelProvider.create()

        return create_deep_agent(
            model=model,
            tools=tools,
            system_prompt=system_prompt,
            name=name,
        )

    # ==========================================================
    # Standard Chat Agent
    # ==========================================================

    @staticmethod
    def build_chat_agent(
        *,
        tools,
        system_prompt: str,
        name: str = "ChatAgent",
    ):
        """
        Build a standard ReAct Agent.

        Best suited for:

        - Executive Assistant
        - Gmail
        - Telegram
        - Google Sheets
        - Google Drive
        - Business automation
        """

        logger.info("Building Chat Agent: %s", name)

        model = ChatModelProvider.create()

        return create_react_agent(
            model=model,
            tools=tools,
            prompt=system_prompt,
        )