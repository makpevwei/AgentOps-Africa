from agentops.domains.research.planner import ResearchPlanner


def main():

    planner = ResearchPlanner()

    plan = planner.create_plan("Should I invest in Zenith Bank?")

    print()

    print("=" * 60)

    for task in plan:
        print(task)


if __name__ == "__main__":
    main()
