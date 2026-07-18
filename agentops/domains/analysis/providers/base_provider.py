"""
Base Analysis Provider.

Defines the interface implemented by all Analysis Providers.
"""

from __future__ import annotations

from abc import ABC, abstractmethod

from agentops.domains.analysis.analysis_models import AnalysisResult


class BaseAnalysisProvider(ABC):
    """
    Base class for all Analysis Providers.
    """

    name: str

    @abstractmethod
    def analyze(
        self,
        prompt: str,
    ) -> AnalysisResult:
        """
        Execute analysis using a prepared prompt.
        """
        raise NotImplementedError
