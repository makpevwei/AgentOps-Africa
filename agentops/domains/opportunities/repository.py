"""
Opportunity Repository

Persistence abstraction for Opportunity entities.
"""

from abc import ABC, abstractmethod

from .models import Opportunity


class OpportunityRepository(ABC):
    """Repository contract for Opportunity persistence."""

    @abstractmethod
    async def create(
        self,
        opportunity: Opportunity,
    ) -> Opportunity:
        """Persist a new opportunity."""
        ...

    @abstractmethod
    async def get(
        self,
        opportunity_id: str,
    ) -> Opportunity | None:
        """Retrieve an opportunity by ID."""
        ...

    @abstractmethod
    async def update(
        self,
        opportunity: Opportunity,
    ) -> Opportunity:
        """Persist updates to an opportunity."""
        ...

    @abstractmethod
    async def delete(
        self,
        opportunity_id: str,
    ) -> None:
        """Delete an opportunity."""
        ...

    @abstractmethod
    async def list_by_organization(
        self,
        organization_id: str,
    ) -> list[Opportunity]:
        """List opportunities for an organization."""
        ...

   