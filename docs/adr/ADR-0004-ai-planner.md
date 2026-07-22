# ADR-0004: Introduce AI Planner

## Status

Accepted

## Context

The initial planner relied on deterministic rule matching.

Although predictable, it could only execute workflows that had been
explicitly programmed.

To support dynamic reasoning and natural language task planning,
the platform requires an AI-based planner.

## Decision

Introduce a new AIPlanner component.

The AIPlanner uses:

- PlannerPromptBuilder
- PromptTemplate
- LLMAnalyzer
- WorkflowPlan

The AI planner remains separate from the existing rule-based planner.

The existing planner continues to act as the fallback implementation.

## Consequences

Positive

- Enables natural language planning.
- Supports future multi-agent orchestration.
- Reuses existing AI infrastructure.
- Keeps the current runtime stable.

Negative

- Requires LLM availability.
- Requires prompt engineering.
- Requires additional testing.