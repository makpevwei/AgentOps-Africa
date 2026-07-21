from datetime import UTC, datetime
from time import perf_counter

from fastapi import APIRouter, HTTPException

from agentops.api.schemas.research import (
    ResearchRequest,
    ResearchResponse,
)
from agentops.core.logger import logger
from agentops.domains.research.research_engine import ResearchEngine

router = APIRouter(
    prefix="/research",
    tags=["Research"],
)

engine = ResearchEngine()


@router.post(
    "",
    response_model=ResearchResponse,
    summary="Research a company",
)
def research_company(
    request: ResearchRequest,
) -> ResearchResponse:
    started = perf_counter()

    try:
        context = engine.build_context(request.company)

        execution_time = round(perf_counter() - started, 2)

        return ResearchResponse(
            company=context.company.company_name,
            industry=context.company.industry,
            country=context.company.country,
            ticker=context.company.ticker,
            execution_time=execution_time,
            generated_at=datetime.now(UTC),
        )

    except Exception as ex:
        logger.exception("Research endpoint failed")

        raise HTTPException(
            status_code=500,
            detail="Internal server error",
        ) from ex
