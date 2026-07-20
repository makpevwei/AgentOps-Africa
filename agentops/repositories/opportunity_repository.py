"""
In-memory Opportunity Repository.

This will later be replaced with a SQLAlchemy implementation.
"""

from agentops.domains.opportunities.models import Opportunity
from agentops.domains.opportunities.repository import OpportunityRepository


class InMemoryOpportunityRepository(OpportunityRepository):
    """Temporary repository for development."""

    def __init__(self) -> None:
        self._items: dict[str, Opportunity] = {}

    async def create(self, opportunity: Opportunity) -> Opportunity:
        self._items[opportunity.id] = opportunity
        return opportunity

    async def get_by_id(self, opportunity_id: str) -> Opportunity | None:
        return self._items.get(opportunity_id)

    async def update(self, opportunity: Opportunity) -> Opportunity:
        self._items[opportunity.id] = opportunity
        return opportunity

    async def delete(self, opportunity_id: str) -> None:
        self._items.pop(opportunity_id, None)

    async def list(
        self,
        organization_id: str,
    ) -> list[Opportunity]:
        return [
            opportunity
            for opportunity in self._items.values()
            if opportunity.organization_id == organization_id
        ]
