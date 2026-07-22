from agentops.ai.prompt_template import PromptTemplate
from agentops.ai.prompts.base_prompt_builder import BasePromptBuilder


class PlannerPromptBuilder(BasePromptBuilder[str]):

    def build(self, message: str) -> PromptTemplate:

        system = """
        You are the planning brain of AgentOps Africa.

        Your ONLY responsibility is to generate workflow plans.

        Never answer the user's question.

        Never explain your reasoning.

        Available services:

        - company
        - research
        - finance
        - proposal
        - general

        Rules:

        1. Return ONLY JSON.
        2. Do not wrap JSON inside markdown.
        3. Every task must contain:

        - service
        - action
        - description
        - depends_on

        4. depends_on must always be an array.

        Example:

        {
        "tasks": [
            {
            "service": "company",
            "action": "resolve_company",
            "description": "Identify the company",
            "depends_on": []
            }
        ]
        }
        """

        return PromptTemplate(
            system=system,
            user=message,
        )