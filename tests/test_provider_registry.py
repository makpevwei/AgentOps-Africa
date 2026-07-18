from agentops.domains.finance.provider_registry import ProviderRegistry

registry = ProviderRegistry()

for provider in registry.providers():
    print(provider.name)