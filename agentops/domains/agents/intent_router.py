"""
Intent Router

Determines which agent domain should handle a user's request.
"""

from enum import StrEnum


class AgentType(StrEnum):
    RESEARCH = "research"
    PROPOSAL = "proposal"
    FINANCE = "finance"
    EXECUTIVE = "executive"
    SALES = "sales"
    GENERAL = "general"


class IntentRouter:
    """
    Determines user intent from a natural language request.
    """

    def decide(
        self,
        message: str,
    ) -> AgentType:

        message = message.lower()

        if any(
            word in message
            for word in [
                "research",
                "analyse",
                "analyze",
                "company",
                "competitor",
            ]
        ):
            return AgentType.RESEARCH

        if any(
            word in message
            for word in [
                "proposal",
                "quotation",
                "rfp",
            ]
        ):
            return AgentType.PROPOSAL

        if any(
            word in message
            for word in [
                "invoice",
                "finance",
                "cash",
                "budget",
            ]
        ):
            return AgentType.FINANCE

        return AgentType.GENERAL