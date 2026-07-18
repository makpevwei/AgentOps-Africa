from rich import print

from agentops.domains.agents.service_registry import ServiceRegistry


def main():

    registry = ServiceRegistry()

    print("=" * 60)
    print("Registered Services")
    print("=" * 60)

    for service in registry.services():
        print(f"• {service.name}")

    print()

    company = registry.get("company")
    finance = registry.get("finance")

    assert company is not None
    assert finance is not None

    print("Company Service :", company.__class__.__name__)
    print("Finance Service :", finance.__class__.__name__)

    print()
    print("✅ Service Registry test passed.")


if __name__ == "__main__":
    main()
