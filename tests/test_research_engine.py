from agentops.domains.research.research_engine import ResearchEngine


def main():

    engine = ResearchEngine()

    quote = engine.get_quote("Apple")

    print()

    print("=" * 70)

    print("QUOTE")

    print()

    print(quote)

    info = engine.get_company_info("Apple")

    print()

    print("=" * 70)

    print("COMPANY")

    print()

    print(info)


if __name__ == "__main__":
    main()