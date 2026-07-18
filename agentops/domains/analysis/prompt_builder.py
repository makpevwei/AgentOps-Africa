"""
Prompt Builder for the Analysis Domain.

Transforms an AgentContext into a structured prompt that can be
submitted to an LLM.
"""

from __future__ import annotations

from agentops.domains.agents.agent_context import AgentContext
from agentops.domains.analysis.prompts.system import SYSTEM_PROMPT


class PromptBuilder:
    """
    Builds prompts for Analysis Providers.
    """

    def build(self, context: AgentContext) -> str:
        """
        Build a complete analysis prompt.
        """

        company = context.company.model_dump_json(indent=2) if context.company else "{}"

        finance = context.finance.model_dump_json(indent=2) if context.finance else "{}"

        research = (
            context.research.result.model_dump_json(indent=2)
            if context.research and context.research.result
            else "{}"
        )

        return f"""{SYSTEM_PROMPT}

Analyze the following company.

## Company

{company}

## Financial Data

{finance}

## Research

{research}

Return ONLY valid JSON that conforms to the AnalysisResult schema.
"""
