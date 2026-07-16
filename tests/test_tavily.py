from agentops.tools.research.tavily_tool import TavilyResearchTool


def main():

    tool = TavilyResearchTool()

    results = tool.search(
        "Latest AI news in Africa",
        max_results=3,
    )

    print()

    print("=" * 60)

    for result in results:

        print()

        print(result.title)

        print(result.url)

        print(result.summary[:250])

        print("-" * 60)


if __name__ == "__main__":
    main()