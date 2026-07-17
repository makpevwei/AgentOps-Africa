from typing import Protocol

from agentops.domains.companies.models import CompanyProfile


class CompanyResolver(Protocol):

    def resolve(
        self,
        company_name: str,
    ) -> CompanyProfile | None:
        ...