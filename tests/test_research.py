from agentops.domains.research.models import ResearchResult


def main():

    result = ResearchResult(
        source="Wikipedia",
        title="Zenith Bank Plc",
        summary="One of Nigeria's largest commercial banks.",
        url="https://en.wikipedia.org/wiki/Zenith_Bank",
        confidence=0.98,
    )

    print(result)

    print()

    print(result.model_dump())


if __name__ == "__main__":
    main()