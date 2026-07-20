"""
Opportunity Service

Business logic for Opportunity Management.
"""

from .models import Opportunity
from .schemas import OpportunityCreate, OpportunityUpdate


class OpportunityService:
    """Business service for managing opportunities."""

    def create_opportunity(
        self,
        organization_id: str,
        request: OpportunityCreate,
    ) -> Opportunity:
        """
        Create a new opportunity.
        """
        raise NotImplementedError

    def get_opportunity(
        self,
        opportunity_id: str,
    ) -> Opportunity:
        """
        Retrieve an opportunity.
        """
        raise NotImplementedError

    def update_opportunity(
        self,
        opportunity_id: str,
        request: OpportunityUpdate,
    ) -> Opportunity:
        """
        Update an opportunity.
        """
        raise NotImplementedError

    def delete_opportunity(
        self,
        opportunity_id: str,
    ) -> None:
        """
        Delete an opportunity.
        """
        raise NotImplementedError

    def start_research(
        self,
        opportunity_id: str,
    ) -> Opportunity:
        """
        Begin AI research on the opportunity.
        """
        raise NotImplementedError

    def generate_proposal(
        self,
        opportunity_id: str,
    ) -> Opportunity:
        """
        Generate a proposal.
        """
        raise NotImplementedError

    def generate_quotation(
        self,
        opportunity_id: str,
    ) -> Opportunity:
        """
        Generate a quotation.
        """
        raise NotImplementedError
