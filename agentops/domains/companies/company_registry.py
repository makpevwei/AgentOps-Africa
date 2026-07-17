"""
Enterprise Company Registry

Stores discovered companies locally.

Today:
    JSON

Later:
    SQLite

Eventually:
    PostgreSQL
"""

import json
from pathlib import Path

from agentops.domains.companies.models import CompanyProfile


class CompanyRegistry:

    def __init__(self):

        self.db = (
            Path(__file__)
            .resolve()
            .parent.parent.parent.parent
            / "data"
            / "companies.json"
        )

    def load(self) -> list[CompanyProfile]:

        if not self.db.exists():

            return []

        data = json.loads(
            self.db.read_text()
        )

        return [
            CompanyProfile(**item)
            for item in data
        ]

    def save(
        self,
        company: CompanyProfile,
    ):

        companies = self.load()

        if any(
            c.company_name.lower()
            == company.company_name.lower()
            for c in companies
        ):
            return

        companies.append(company)

        self.db.write_text(

            json.dumps(
                [
                    c.model_dump()
                    for c in companies
                ],
                indent=4,
            )

        )