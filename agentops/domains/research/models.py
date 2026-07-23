"""
Research Domain Models
"""

from dataclasses import dataclass, field
from datetime import UTC, datetime


@dataclass
class ResearchSource:
    """
    Represents a research source.
    """

    title: str
    url: str
    provider: str

@dataclass
class ResearchResult:
    """
    Legacy research result.

    Maintained for backward compatibility while
    the codebase migrates to ResearchReport.
    """

    title: str
    summary: str
    url: str
    confidence: float = 0.0

@dataclass
class ResearchFinding:
    """
    Represents one research finding.
    """

    title: str
    summary: str
    url: str
    confidence: float = 0.0


@dataclass
class ResearchReport:
    """
    Final research report returned by the
    Research Engine.
    """

    query: str

    findings: list[ResearchFinding] = field(default_factory=list)

    sources: list[ResearchSource] = field(default_factory=list)

    summary: str = ""

    generated_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    execution_time_ms: int = 0