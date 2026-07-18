"""
Chat API Schemas
"""

from pydantic import BaseModel

from agentops.domains.research.analysis_models import CompanyAnalysis


class ChatRequest(BaseModel):
    """
    Chat request payload.
    """

    message: str


class ChatResponse(BaseModel):
    """
    Chat response containing the structured company analysis.
    """

    response: CompanyAnalysis
