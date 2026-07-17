from pydantic import BaseModel, Field


class ResearchRequest(BaseModel):
    company: str = Field(
        ...,
        description="Company name to research",
        examples=["MTN Nigeria"],
    )
    
class ResearchResponse(BaseModel):
    company: str
    industry: str
    country: str
    ticker: str | None = None