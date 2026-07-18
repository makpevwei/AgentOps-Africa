from typing import Protocol

from agentops.domains.research.report_models import ResearchReport
from agentops.domains.research.research_context import ResearchContext


class Analyzer(Protocol):
    def analyze(
        self,
        context: ResearchContext,
    ) -> ResearchReport: ...
