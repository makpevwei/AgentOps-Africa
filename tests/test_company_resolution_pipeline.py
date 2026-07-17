from agentops.domains.companies.company_resolver import CompanyResolver


def main():

    resolver = CompanyResolver()

    companies = [

        "GTB",

        "Zenit",

        "Tesla",

        "Moniepoint",

        "Flutterwave",

        "Paystack",

        "Nomba",

        "PiggyVest",

        "PalmPay",

    ]

    for name in companies:

        print()

        print("=" * 70)

        print(name)

        print()

        result = resolver.resolve(name)

        print(result)


if __name__ == "__main__":
    main()