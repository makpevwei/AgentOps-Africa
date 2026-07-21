"""
Execution Context

Shared runtime context used by all agent services.
"""

from __future__ import annotations

from typing import Any

from pydantic import BaseModel, Field

from agentops.domains.agents.models.analysis_data import AnalysisData
from agentops.domains.agents.models.research_data import ResearchData
from agentops.domains.companies.models import CompanyProfile
from agentops.domains.finance.finance_snapshot import FinanceSnapshot


class ExecutionContext(BaseModel):
    """
    Shared runtime context.
    """

    company: CompanyProfile | None = None

    finance: FinanceSnapshot | None = None

    research: ResearchData = Field(default_factory=ResearchData)

    analysis: AnalysisData = Field(default_factory=AnalysisData)

    summary: str | None = None

    metadata: dict[str, Any] = Field(default_factory=dict)

    errors: list[str] = Field(default_factory=list)

    completed_tasks: list[int] = Field(default_factory=list)

    def set_result(
        self,
        service: str,
        result: Any,
    ) -> None:
        setattr(self, service, result)

    def get_result(
        self,
        service: str,
    ) -> Any:
        return getattr(self, service, None)

    def add_error(
        self,
        error: str,
    ) -> None:
        self.errors.append(error)

    def mark_completed(
        self,
        task_id: int,
    ) -> None:
        self.completed_tasks.append(task_id)

    @property
    def successful(self) -> bool:
        return not self.errors