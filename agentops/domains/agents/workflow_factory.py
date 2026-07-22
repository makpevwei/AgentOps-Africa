"""
Workflow Factory

Creates workflows for each supported agent domain.
"""

from agentops.domains.agents.intent_router import AgentType
from agentops.domains.workflows.workflow import Workflow
from agentops.domains.workflows.workflow_step import WorkflowStep


class WorkflowFactory:
    """
    Builds workflows for each supported intent.
    """

    def create(
        self,
        intent: AgentType,
        message: str,
    ) -> Workflow:

        if intent == AgentType.RESEARCH:
            return self._research_workflow(message)

        if intent == AgentType.FINANCE:
            return self._finance_workflow(message)

        if intent == AgentType.PROPOSAL:
            return self._proposal_workflow(message)

        return self._general_workflow(message)

    # ----------------------------------------------------
    # Workflow Builders
    # ----------------------------------------------------

    def _research_workflow(
        self,
        message: str,
    ) -> Workflow:

        return Workflow(
            name="Research Workflow",
            description="Research a company",
            steps=[
                WorkflowStep(
                    id=1,
                    name="Resolve Company",
                    service="company",
                    action="resolve_company",
                    description="Resolve company information",
                    payload={"query": message},
                ),
                WorkflowStep(
                    id=2,
                    name="Research Company",
                    service="research",
                    action="company_profile",
                    description="Research company",
                    depends_on=[1],
                ),
                WorkflowStep(
                    id=3,
                    name="Financial Snapshot",
                    service="finance",
                    action="financial_snapshot",
                    description="Collect financial data",
                    depends_on=[1],
                ),
            ],
        )

    def _finance_workflow(
        self,
        message: str,
    ) -> Workflow:

        return Workflow(
            name="Finance Workflow",
            description="Financial analysis",
            steps=[
                WorkflowStep(
                    id=1,
                    name="Resolve Company",
                    service="company",
                    action="resolve_company",
                    description="Resolve company",
                    payload={"query": message},
                ),
                WorkflowStep(
                    id=2,
                    name="Financial Snapshot",
                    service="finance",
                    action="financial_snapshot",
                    description="Collect financial data",
                    depends_on=[1],
                ),
            ],
        )

    def _proposal_workflow(
        self,
        message: str,
    ) -> Workflow:

        return Workflow(
            name="Proposal Workflow",
            description="Generate proposal",
            steps=[
                WorkflowStep(
                    id=1,
                    name="Generate Proposal",
                    service="proposal",
                    action="generate_proposal",
                    description="Generate proposal",
                    payload={"request": message},
                ),
            ],
        )

    def _general_workflow(
        self,
        message: str,
    ) -> Workflow:

        return Workflow(
            name="General Workflow",
            description="General assistant",
            steps=[
                WorkflowStep(
                    id=1,
                    name="General Response",
                    service="general",
                    action="general_response",
                    description="Respond to the user",
                    payload={"message": message},
                ),
            ],
        )