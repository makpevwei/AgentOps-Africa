from agentops.domains.companies.company_normalizer import CompanyNormalizer
from agentops.domains.companies.company_registry import CompanyRegistry
from agentops.domains.research.company_discovery import CompanyDiscovery


def main():

    discovery = CompanyDiscovery()

    normalizer = CompanyNormalizer()

    registry = CompanyRegistry()

    findings = discovery.search("Moniepoint")

    company = normalizer.normalize(
        "Moniepoint",
        findings,
    )

    registry.save(company)

    print()

    print("=" * 60)

    print()

    for item in registry.load():
        print(item)


if __name__ == "__main__":
    main()
