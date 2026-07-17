from agentops.domains.companies.company_service import CompanyService


def main():

    service = CompanyService()

    companies = [
        "GTB",
        "Zenit",
        "Moniepoint",
        "Flutterwave",
        "PiggyVest",
        "Stripe",
    ]

    for company in companies:
        print()

        print("=" * 70)

        print(company)

        print()

        result = service.resolve(company)

        print(result)


if __name__ == "__main__":
    main()
