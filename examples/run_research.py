from agentops.domains.research.research_engine import ResearchEngine

engine = ResearchEngine()

context = engine.build_context("Apple Inc.")

print("\nCompany")
print(context.company)

print("\nFinance")
print(context.finance)

print("\nResearch")
print(context.research)
