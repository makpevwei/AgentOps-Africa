from agentops.ai.llm_analyzer import LLMAnalyzer

from .models import WorkflowPlan
from .planner_prompt_builder import PlannerPromptBuilder


class AIPlanner:

    def __init__(self):

        self._builder = PlannerPromptBuilder()
        self._analyzer = LLMAnalyzer()

    def plan(
        self,
        message: str,
    ) -> WorkflowPlan:

        prompt = self._builder.build(message)

        return self._analyzer.run(
            prompt,
            WorkflowPlan,
        )