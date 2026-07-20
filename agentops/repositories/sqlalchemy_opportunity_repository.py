from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from agentops.db.models.opportunity import Opportunity as OpportunityModel
from agentops.domains.opportunities.models import Opportunity
from agentops.domains.opportunities.repository import OpportunityRepository


class SQLAlchemyOpportunityRepository(OpportunityRepository):
    def __init__(self, db: AsyncSession) -> None:
        self.db = db

    def _to_domain(self, model: OpportunityModel) -> Opportunity:
        return Opportunity(
            id=str(model.id),
            organization_id=model.organization_id,
            title=model.title,
            description=model.description,
            company_name=model.company_name,
            contact_name=model.contact_name,
            email=model.email,
            phone=model.phone,
            status=model.status,
            priority=model.priority,
            source=model.source,
            created_at=model.created_at,
            updated_at=model.updated_at,
        )

    async def create(self, opportunity: Opportunity) -> Opportunity:
        model = OpportunityModel(
            id=opportunity.id,
            organization_id=opportunity.organization_id,
            title=opportunity.title,
            description=opportunity.description,
            company_name=opportunity.company_name,
            contact_name=opportunity.contact_name,
            email=opportunity.email,
            phone=opportunity.phone,
            status=opportunity.status,
            priority=opportunity.priority,
            source=opportunity.source,
        )

        self.db.add(model)

        await self.db.commit()
        await self.db.refresh(model)

        return self._to_domain(model)

    async def get(self, opportunity_id: str) -> Opportunity | None:
        stmt = select(OpportunityModel).where(OpportunityModel.id == opportunity_id)

        result = await self.db.execute(stmt)

        model = result.scalar_one_or_none()

        if model is None:
            return None

        return self._to_domain(model)

    async def list_by_organization(
        self,
        organization_id: str,
    ) -> list[Opportunity]:
        stmt = select(OpportunityModel).where(
            OpportunityModel.organization_id == organization_id
        )

        result = await self.db.execute(stmt)

        models = result.scalars().all()

        return [self._to_domain(model) for model in models]

    async def update(
        self,
        opportunity: Opportunity,
    ) -> Opportunity:
        stmt = select(OpportunityModel).where(
            OpportunityModel.id == opportunity.id
        )

        result = await self.db.execute(stmt)

        model = result.scalar_one_or_none()

        if model is None:
            raise ValueError("Opportunity not found")

        model.title = opportunity.title
        model.description = opportunity.description
        model.company_name = opportunity.company_name
        model.contact_name = opportunity.contact_name
        model.email = opportunity.email
        model.phone = opportunity.phone
        model.status = opportunity.status
        model.priority = opportunity.priority
        model.source = opportunity.source

        await self.db.commit()
        await self.db.refresh(model)

        return self._to_domain(model)

    async def delete(
        self,
        opportunity_id: str,
    ) -> None:
        stmt = select(OpportunityModel).where(OpportunityModel.id == opportunity_id)

        result = await self.db.execute(stmt)

        model = result.scalar_one_or_none()

        if model is None:
            return

        await self.db.delete(model)

        await self.db.commit()
