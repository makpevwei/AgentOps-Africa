"""
Enterprise Research Report Models
"""

from pydantic import BaseModel, Field


class ResearchFinding(BaseModel):
    """
    A single evidence-backed finding.
    """

    title: str

    summary: str

    confidence: float = 1.0

    sources: list[str] = Field(default_factory=list)


class BusinessProfile(BaseModel):
    """
    Company profile.
    """

    overview: str

    industry: str

    headquarters: str

    business_model: str


class SWOTAnalysis(BaseModel):
    """
    SWOT Analysis.
    """

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    opportunities: list[str] = Field(default_factory=list)

    threats: list[str] = Field(default_factory=list)


class RiskAssessment(BaseModel):
    """
    Enterprise risk assessment.
    """

    overall_risk: str

    financial_risk: str

    operational_risk: str

    regulatory_risk: str

    confidence: float


class InvestmentRecommendation(BaseModel):
    """
    Final investment recommendation.
    """

    action: str

    rationale: str

    investment_horizon: str

    confidence: float


class ResearchSection(BaseModel):
    """
    Optional long-form narrative section.
    """

    title: str

    summary: str

    findings: list[ResearchFinding] = Field(default_factory=list)


class ResearchReport(BaseModel):
    """
    Enterprise Research Report.
    """

    company: str

    executive_summary: str

    business: BusinessProfile

    swot: SWOTAnalysis

    risks: RiskAssessment

    recommendation: InvestmentRecommendation

    sections: list[ResearchSection] = Field(default_factory=list)

    metadata: dict = Field(default_factory=dict)