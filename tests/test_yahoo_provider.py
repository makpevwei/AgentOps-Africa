from agentops.domains.research.company_resolver import CompanyResolver
from agentops.providers.finance.provider_factory import FinanceProviderFactory


def main():

    resolver = CompanyResolver()

    company = resolver.resolve("Apple")

    provider = FinanceProviderFactory.create(company)

    quote = provider.get_quote(company)

    print()

    print("=" * 60)

    print()

    print(quote)

    print()

    print(quote.model_dump())


if __name__ == "__main__":

    main()