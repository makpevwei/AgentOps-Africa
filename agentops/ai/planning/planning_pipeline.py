"""
Planning Pipeline

Coordinates AI planning, validation and conversion into
the runtime workflow model.
"""

from agentops.ai.planning.ai_planner import AIPlanner
from agentops.ai.planning.workflow_converter import WorkflowConverter
from agentops.ai.planning.workflow_validator import WorkflowValidator
from agentops.domains.workflows.workflow import Workflow


class PlanningPipeline:
    """
    End-to-end AI planning pipeline.
    """

    def __init__(self) -> None:
        self.ai_planner = AIPlanner()
        self.validator = WorkflowValidator()
        self.converter = WorkflowConverter()

    def plan(
        self,
        message: str,
    ) -> Workflow:
        """
        Generate a validated runtime workflow.
        """

        workflow_plan = self.ai_planner.plan(message)

        self.validator.validate(workflow_plan)

        return self.converter.convert(workflow_plan)