from agentops.domains.research.research_engine import ResearchEngine


def test_company(engine, company):

    print()
    print("=" * 90)
    print(company)
    print("=" * 90)

    context = engine.build_context(company)

    print()

    print("Resolved Company:")
    print(context.company.company_name)

    print()

    if context.finance.quote:
        print("Quote:")
        print(context.finance.quote.price)

    print()

    print("History:", len(context.finance.history))

    print("News:", len(context.finance.news))


def main():

    engine = ResearchEngine()

    companies = [

        "Apple",
        "GTB",
        "Zenith Bank",
        "Moniepoint",
        "Flutterwave",
        "Stripe",

    ]

    for company in companies:

        try:

            test_company(engine, company)

        except Exception as e:

            print(f"ERROR: {company}")

            print(e)


if __name__ == "__main__":

    main()