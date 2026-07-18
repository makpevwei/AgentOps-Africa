from agentops.domains.companies.company_resolver import CompanyResolver
from agentops.domains.finance.finance_service import FinanceService


def main():
    resolver = CompanyResolver()
    finance = FinanceService()

    company = resolver.resolve("Apple")

    snapshot = finance.get_snapshot(company)

    print()
    print("=" * 60)
    print("COMPANY")
    print()
    print(company)

    print()
    print("=" * 60)
    print("QUOTE")
    print()

    if snapshot.quote:
        print(snapshot.quote)
        print()
        print(snapshot.quote.model_dump())

    print()
    print("=" * 60)
    print("FUNDAMENTALS")
    print()

    if snapshot.fundamentals:
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