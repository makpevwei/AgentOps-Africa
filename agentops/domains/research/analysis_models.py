"""
Analysis Models

Intermediate outputs produced by specialized analyzers.
"""

from pydantic import BaseModel, Field


class BusinessAnalysis(BaseModel):
    """
    Business analysis.
    """

    overview: str

    industry: str

    headquarters: str

    business_model: str

    competitive_position: str


class FinancialAnalysis(BaseModel):
    """
    Financial analysis.
    """

    summary: str

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    opportunities: list[str] = Field(default_factory=list)

    threats: list[str] = Field(default_factory=list)


class RiskAnalysis(BaseModel):
    """
    Risk analysis.
    """

    overall_risk: str

    financial_risk: str

    operational_risk: str

    regulatory_risk: str

    confidence: float


class RecommendationAnalysis(BaseModel):
    """
    Investment recommendation.
    """

    action: str

    rationale: str

    investment_horizon: str

    confidence: float