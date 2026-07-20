"""
Opportunity API Endpoints
"""

from __future__ import annotations

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from agentops.db.session import get_db
from agentops.domains.opportunities.schemas import (
    OpportunityCreate,
    OpportunityResponse,
    OpportunityUpdate,
)
from agentops.domains.opportunities.service import OpportunityService
from agentops.repositories.sqlalchemy_opportunity_repository import (
    SQLAlchemyOpportunityRepository,
)

router = APIRouter(
    prefix="/opportunities",
    tags=["Opportunities"],
)


def get_opportunity_service(
    db: AsyncSession = Depends(get_db),
) -> OpportunityService:
    """Create the opportunity service."""

    repository = SQLAlchemyOpportunityRepository(
        db,
    )

    return OpportunityService(
        repository=repository,
    )


@router.post(
    "/",
    response_model=OpportunityResponse,
)
async def create_opportunity(
    request: OpportunityCreate,
    service: OpportunityService = Depends(get_opportunity_service),
) -> OpportunityResponse:
    """Create a new opportunity."""

    return await service.create_opportunity(
        organization_id="demo-org",
        request=request,
    )


@router.get(
    "/",
    response_model=list[OpportunityResponse],
)
async def list_opportunities(
    service: OpportunityService = Depends(get_opportunity_service),
) -> list[OpportunityResponse]:
    """List all opportunities."""

    return await service.list_opportunities(
        organization_id="demo-org",
    )


@router.get(
    "/{opportunity_id}",
    response_model=OpportunityResponse,
)
async def get_opportunity(
    opportunity_id: str,
    service: OpportunityService = Depends(get_opportunity_service),
) -> OpportunityResponse:
    """Retrieve an opportunity."""

    return await service.get_opportunity(
        opportunity_id,
    )


@router.patch(
    "/{opportunity_id}",
    response_model=OpportunityResponse,
)
async def update_opportunity(
    opportunity_id: str,
    request: OpportunityUpdate,
    service: OpportunityService = Depends(get_opportunity_service),
) -> OpportunityResponse:
    """Update an existing opportunity."""

    return await service.update_opportunity(
        opportunity_id=opportunity_id,
        request=request,
    )