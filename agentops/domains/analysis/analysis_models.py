"""
Analysis Domain Models.

Defines the structured business intelligence returned by the
Analysis Engine.
"""

from __future__ import annotations

from enum import Enum

from pydantic import BaseModel, Field


class Recommendation(str, Enum):
    """
    Overall investment recommendation.
    """

    STRONG_BUY = "Strong Buy"
    BUY = "Buy"
    HOLD = "Hold"
    SELL = "Sell"
    STRONG_SELL = "Strong Sell"


class Severity(str, Enum):
    """
    Severity of a business risk.
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class Impact(str, Enum):
    """
    Expected business impact.
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"


class SWOTAnalysis(BaseModel):
    """
    SWOT analysis.
    """

    strengths: list[str] = Field(default_factory=list)

    weaknesses: list[str] = Field(default_factory=list)

    opportunities: list[str] = Field(default_factory=list)

    threats: list[str] = Field(default_factory=list)


class RiskItem(BaseModel):
    """
    Business risk.
    """

    title: str

    description: str

    severity: Severity = Severity.MEDIUM


class OpportunityItem(BaseModel):
    """
    Growth opportunity.
    """

    title: str

    description: str

    impact: Impact = Impact.MEDIUM


class AnalysisResult(BaseModel):
    """
    Complete AI-generated business analysis.
    """

    executive_summary: str = ""

    business_overview: str = ""

    financial_health: str = ""

    market_position: str = ""

    swot: SWOTAnalysis = Field(default_factory=SWOTAnalysis)

    risks: list[RiskItem] = Field(default_factory=list)

    opportunities: list[OpportunityItem] = Field(default_factory=list)

    recommendation: Recommendation = Recommendation.HOLD

    confidence_score: float = 0.0
