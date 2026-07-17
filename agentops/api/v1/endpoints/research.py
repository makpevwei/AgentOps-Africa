from fastapi import APIRouter

from agentops.api.schemas.research import (
    ResearchRequest,
    ResearchResponse,
)
from agentops.domains.research.research_engine import ResearchEngine

router = APIRouter(
    prefix="/research",
    tags=["Research"],
)

engine = ResearchEngine()


@router.post(
    "",
    response_model=ResearchResponse,
)
def research_company(
    request: ResearchRequest,
):
    context = engine.build_context(request.company)

    return ResearchResponse(
        company=context.company.company_name,
        industry=context.company.industry,
        country=context.company.country,
        ticker=context.company.ticker,
    )