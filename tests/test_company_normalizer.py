from agentops.domains.research.company_discovery import CompanyDiscovery
from agentops.domains.research.company_normalizer import CompanyNormalizer


def main():

    discovery = CompanyDiscovery()

    normalizer = CompanyNormalizer()

    findings = discovery.search("Moniepoint")

    company = normalizer.normalize(
        "Moniepoint",
        findings,
    )

    print()

    print("=" * 60)

    print()

    print(company)

    print()

    print(company.model_dump())


if __name__ == "__main__":
    main()