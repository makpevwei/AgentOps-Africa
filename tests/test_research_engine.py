"""
Test the Research Engine.
"""

from agentops.domains.research.research_engine import ResearchEngine


def main():

    engine = ResearchEngine()

    context = engine.build_context("Apple")

    print()
    print("=" * 70)
    print("COMPANY")
    print()

    print(context.company)

    print()
    print("=" * 70)
    print("FINANCE")
    print()

    print(context.finance)


if __name__ == "__main__":
    main()
