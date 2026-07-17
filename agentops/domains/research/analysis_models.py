"""
Analysis Models

Intermediate outputs produced by specialized analyzers.
"""

from pydantic import BaseModel


class BusinessAnalysis(BaseModel):
    """
    Structured business analysis.
    """

    overview: str

    industry: str

    headquarters: str

    business_model: str

    competitive_position: str


class FinancialAnalysis(BaseModel):
    """
    Structured financial analysis.
    """

    summary: str

    valuation: str

    profitability: str

    growth: str

    financial_strength: str


class RiskAnalysis(BaseModel):
    """
    Structured risk assessment.
    """

    overall_risk: str

    financial_risk: str

    operational_risk: str

    regulatory_risk: str

    confidence: float


class RecommendationAnalysis(BaseModel):
    """
    Structured investment recommendation.
    """

    action: str

    rationale: str

    investment_horizon: str

    confidence: float


class SWOTAnalysis(BaseModel):
    """
    SWOT analysis produced independently of
    financial or business analysis.
    """

    strengths: list[str]

    weaknesses: list[str]

    opportunities: list[str]

    threats: list[str]

class ExecutiveAnalysis(BaseModel):
    """
    Complete executive analysis produced by combining
    all specialized analyzers.
    """

    executive_summary: str

    business: BusinessAnalysis

    financial: FinancialAnalysis

    risks: RiskAnalysis

    swot: SWOTAnalysis

    recommendation: RecommendationAnalysis

class CompanyAnalysis(BaseModel):
    """
    Aggregated company analysis produced by combining
    specialized analyzers.
    """

    company_name: str

    business: BusinessAnalysis

    financial: FinancialAnalysis

    risk: RiskAnalysis | None = None

    swot: SWOTAnalysis | None = None

    recommendation: RecommendationAnalysis | None = None