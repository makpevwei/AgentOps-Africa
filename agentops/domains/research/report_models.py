"""
Research Report Domain Models

Structured output produced by the Research Analyzer.
"""

from pydantic import BaseModel, Field


class ResearchFinding(BaseModel):
    """
    A single finding discovered during analysis.
    """

    title: str

    summary: str

    confidence: float = 1.0

    sources: list[str] = Field(default_factory=list)


class ResearchSection(BaseModel):
    """
    A logical section within a research report.
    """

    title: str

    content: str

    findings: list[ResearchFinding] = Field(default_factory=list)


class ResearchReport(BaseModel):
    """
    Complete AI-generated research report.
    """

    company: str

    executive_summary: str

    recommendation: str

    confidence: float

    sections: list[ResearchSection] = Field(default_factory=list)

    metadata: dict = Field(default_factory=dict)