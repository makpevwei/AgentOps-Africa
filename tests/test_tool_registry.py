from agentops.domains.research.tool_registry import (
    ResearchToolRegistry,
)


def test_registry_contains_tavily():

    registry = ResearchToolRegistry()

    assert registry.get("tavily") is not None


def test_register_new_tool():

    class DummyTool:

        def search(self, query):

            return []

    registry = ResearchToolRegistry()

    registry.register(
        "dummy",
        DummyTool(),
    )

    assert registry.get("dummy") is not None