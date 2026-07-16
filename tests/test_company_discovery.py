from agentops.domains.research.company_discovery import CompanyDiscovery


def main():

    discovery = CompanyDiscovery()

    results = discovery.search("Moniepoint")

    print()
    print("=" * 60)
    print()

    for result in results:

        print(result.title)
        print(result.url)
        print(result.summary[:250])
        print("-" * 60)


if __name__ == "__main__":
    main()