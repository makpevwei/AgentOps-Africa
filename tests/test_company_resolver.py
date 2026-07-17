from agentops.domains.companies.company_resolver import CompanyResolver


def main():

    resolver = CompanyResolver()

    tests = [
        "GTB",
        "GTCO",
        "Zenith",
        "Zenit",
        "Access",
        "Access Bank",
        "Guaranty",
        "Dangot",
        "Tesla",
        "Tesal",
        "Microsoft",
        "Microsft",
    ]

    for query in tests:
        company = resolver.resolve(query)

        print("=" * 60)
        print(query)
        print(company)


if __name__ == "__main__":
    main()
