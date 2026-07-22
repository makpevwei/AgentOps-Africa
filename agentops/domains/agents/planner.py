"""
Workflow Planner

Determines the user's intent and builds the appropriate workflow.
"""

from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.intent_router import (
    AgentType,
    IntentRouter,
)
from agentops.domains.agents.task import AgentTask
from agentops.domains.workflows.workflow import Workflow
from agentops.domains.workflows.workflow_step import WorkflowStep


class Planner:
    """
    Determines user intent and creates the workflow
    required to satisfy the request.
    """

    def __init__(self):

        self.router = IntentRouter()

    # ----------------------------------------------------
    # Workflow Creation
    # ----------------------------------------------------

    def create_workflow(
        self,
        message: str,
    ) -> Workflow:
        """
        Build a workflow based on the detected intent.
        """

        intent = self.router.decide(message)

        if intent == AgentType.RESEARCH:
            return self._research_workflow(message)

        if intent == AgentType.FINANCE:
            return self._finance_workflow(message)

        if intent == AgentType.PROPOSAL:
            return self._proposal_workflow(message)

        return self._general_workflow(message)

    # ----------------------------------------------------
    # Backward Compatibility
    # ----------------------------------------------------

    def create_plan(
        self,
        message: str,
    ) -> ExecutionPlan:
        """
        Backward compatibility for legacy callers.
        """

        workflow = self.create_workflow(message)

        plan = ExecutionPlan(goal=message)

        for step in workflow.steps:
            plan.add_task(
                AgentTask(
                    id=step.id,
                    name=step.name,
                    service=step.service,
                    action=step.action,
                    description=step.description,
                    payload=step.payload,
                    depends_on=step.depends_on,
                )
            )

        return plan

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