from agentops.domains.companies.company_resolver import CompanyResolver
from agentops.providers.finance.provider_factory import FinanceProviderFactory


def main():
    resolver = CompanyResolver()

    company = resolver.resolve("Apple")

    provider = FinanceProviderFactory.create(company)

    snapshot = provider.get_snapshot(company)

    print()
    print("=" * 60)
    print("COMPANY")
    print()
    print(company)

    print()
    print("=" * 60)
    print("QUOTE")
    print()
    print(snapshot.quote)
    print()
    print(snapshot.quote.model_dump())

    print()
    print("=" * 60)
    print("FUNDAMENTALS")
    print()
    print(snapshot.fundamentals)
    print()
    print(snapshot.fundamentals.model_dump())

    print()
    print("=" * 60)
    print("PRICE HISTORY")
    print()
    print(f"Records: {len(snapshot.history)}")

    if snapshot.history:
        print("First Record:")
        print(snapshot.history[0].model_dump())

        print()
        print("Latest Record:")
        print(snapshot.history[-1].model_dump())


if __name__ == "__main__":
    main()