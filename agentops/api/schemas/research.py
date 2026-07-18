from datetime import datetime

from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    company: str = Field(
        ...,
        description="Company name to research",
        examples=["MTN Nigeria"],
    )


class ResearchResponse(BaseModel):
    company: str = Field(
        ...,
        description="Company name",
    )

    industry: str = Field(
        ...,
        description="Industry sector",
    )

    country: str = Field(
        ...,
        description="Country of operation",
    )

    ticker: str | None = Field(
        default=None,
        description="Public stock ticker if available",
    )

    execution_time: float = Field(
        ...,
        description="Time taken to complete the research in seconds",
        examples=[1.27],
    )

    generated_at: datetime = Field(
        ...,
        description="UTC timestamp when the research was generated",
    )
