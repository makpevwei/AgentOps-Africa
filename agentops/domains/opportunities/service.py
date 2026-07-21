"""
Opportunity Service

Business logic for Opportunity Management.
"""

from uuid import uuid4

from agentops.core.exceptions import NotFoundException
from agentops.core.logger import logger
from agentops.domains.opportunities.models import Opportunity
from agentops.domains.opportunities.repository import OpportunityRepository
from agentops.domains.opportunities.schemas import (
    OpportunityCreate,
    OpportunityUpdate,
)


class OpportunityService:
    """Business service for managing opportunities."""

    def __init__(
        self,
        repository: OpportunityRepository,
    ) -> None:
        self.repository = repository

    async def create_opportunity(
        self,
        organization_id: str,
        request: OpportunityCreate,
    ) -> Opportunity:
        """Create a new opportunity."""

        logger.info(
            "Creating opportunity for company: %s",
            request.company_name,
        )

        opportunity = Opportunity(
            id=str(uuid4()),
            organization_id=organization_id,
            title=request.title,
            description=request.description,
            company_name=request.company_name,
            contact_name=request.contact_name,
            email=request.email,
            phone=request.phone,
            source=request.source,
        )

        created = await self.repository.create(opportunity)

        logger.info(
            "Opportunity created successfully: %s",
            created.id,
        )

        return created

    async def get_opportunity(
        self,
        opportunity_id: str,
    ) -> Opportunity:
        """Retrieve an opportunity."""

        opportunity = await self.repository.get(
            opportunity_id,
        )

        if opportunity is None:
            raise NotFoundException(
                "Opportunity not found",
            )

        return opportunity

    async def list_opportunities(
        self,
        organization_id: str,
    ) -> list[Opportunity]:
        """List opportunities for an organization."""

        return await self.repository.list_by_organization(
            organization_id=organization_id,
        )

    async def update_opportunity(
        self,
        opportunity_id: str,
        request: OpportunityUpdate,
    ) -> Opportunity:
        """Update an existing opportunity."""

        opportunity = await self.repository.get(
            opportunity_id,
        )

        if opportunity is None:
            raise NotFoundException(
                "Opportunity not found",
            )

        update_data = request.model_dump(
            exclude_unset=True,
        )

        for field, value in update_data.items():
            setattr(opportunity, field, value)

        updated = await self.repository.update(
            opportunity,
        )

        logger.info(
            "Opportunity updated successfully: %s",
            updated.id,
        )

        return updated

    async def delete_opportunity(
        self,
        opportunity_id: str,
    ) -> None:
        """Delete an opportunity."""

        opportunity = await self.repository.get(
            opportunity_id,
        )

        if opportunity is None:
            raise NotFoundException(
                "Opportunity not found",
            )

        await self.repository.delete(
            opportunity_id,
        )

        logger.info(
            "Opportunity deleted successfully: %s",
            opportunity_id,
        )

    async def start_research(
        self,
        opportunity_id: str,
    ) -> Opportunity:
        raise NotImplementedError

    async def generate_proposal(
        self,
        opportunity_id: str,
    ) -> Opportunity:
        raise NotImplementedError

    async def generate_quotation(
        self,
        opportunity_id: str,
    ) -> Opportunity:
        raise NotImplementedError
