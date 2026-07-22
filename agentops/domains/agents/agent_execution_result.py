"""
Agent Workflow Execution Result
"""

from typing import Any

from pydantic import BaseModel


class AgentExecutionResult(BaseModel):
    """
    Represents the outcome of an executed workflow.
    """

    workflow_id: str

    workflow_name: str

    planner: str

    status: str

    message: str

    data: Any