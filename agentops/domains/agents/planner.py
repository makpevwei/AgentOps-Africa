"""
Workflow Planner

Determines the user's intent and builds the appropriate workflow.
"""

from enum import StrEnum

from agentops.domains.agents.execution_plan import ExecutionPlan
from agentops.domains.agents.task import AgentTask
from agentops.domains.workflows.workflow import Workflow
from agentops.domains.workflows.workflow_step import WorkflowStep


class AgentType(StrEnum):
    RESEARCH = "research"
    PROPOSAL = "proposal"
    FINANCE = "finance"
    EXECUTIVE = "executive"
    SALES = "sales"
    GENERAL = "general"


class Planner:
    """
    Determines user intent and creates the workflow
    required to satisfy the request.
    """

    def decide(
        self,
        message: str,
    ) -> AgentType:

        message = message.lower()

        if any(
            word in message
            for word in [
                "research",
                "analyse",
                "analyze",
                "company",
                "competitor",
            ]
        ):
            return AgentType.RESEARCH

        if any(
            word in message
            for word in [
                "proposal",
                "quotation",
                "rfp",
            ]
        ):
            return AgentType.PROPOSAL

        if any(
            word in message
            for word in [
                "invoice",
                "finance",
                "cash",
                "budget",
            ]
        ):
            return AgentType.FINANCE

        return AgentType.GENERAL

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

        intent = self.decide(message)

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

        workflow = self.create_workflow(message)

        plan = ExecutionPlan(goal=message)

        id_map: dict[str, int] = {}

        # First pass: assign numeric ids
        for index, step in enumerate(workflow.steps, start=1):
            id_map[step.id] = index

        # Second pass: build tasks
        for index, step in enumerate(workflow.steps, start=1):
            plan.add_task(
                AgentTask(
                    id=index,
                    name=step.name,
                    service=step.service,
                    action=step.name.lower().replace(" ", "_"),
                    description=step.description,
                    depends_on=[id_map[d] for d in step.depends_on],
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
                    id="company",
                    name="Resolve Company",
                    service="company",
                    description="Resolve company information",
                ),
                WorkflowStep(
                    id="research",
                    name="Research Company",
                    service="research",
                    description="Research company",
                    depends_on=["company"],
                ),
                WorkflowStep(
                    id="finance",
                    name="Financial Snapshot",
                    service="finance",
                    description="Collect financial data",
                    depends_on=["company"],
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
                    id="company",
                    name="Resolve Company",
                    service="company",
                    description="Resolve company",
                ),
                WorkflowStep(
                    id="finance",
                    name="Financial Snapshot",
                    service="finance",
                    description="Collect financial data",
                    depends_on=["company"],
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
            steps=[],
        )

    def _general_workflow(
        self,
        message: str,
    ) -> Workflow:

        return Workflow(
            name="General Workflow",
            description="General assistant",
            steps=[],
        )
