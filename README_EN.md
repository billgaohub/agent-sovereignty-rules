# Agent Sovereignty Rules

> Decision Rights Protection Framework for AI Agent Systems

---

## Core Positioning

*"The system is just a cognitive amplifier — it reminds me what to consider in decisions. I can't rely on automation for everything. In the end, I still have to rely on myself."*

Agent Sovereignty Rules is a framework designed to ensure human decision-making authority is never compromised by AI systems.

---

## Five Core Principles

| # | Principle | Meaning |
|---|----------|--------|
| **1** | **Decision Rights Conservation** | System reduces cost, not authority |
| **2** | **Amplify Cognition, Not Narrow Choices** | AI can rank, never hide |
| **3** | **Traceability** | Every suggestion has a source citation |
| **4** | **Explainability** | All rankings have human-readable reasons |
| **5** | **Reversibility** | Every output has a clear override option |

---

## Five-Point Checklist

```
□ Is decision authority in the user's hands?
□ Is the choice space complete (nothing hidden)?
□ Is the suggestion labeled with its source?
□ Is the ranking explained in plain language?
□ Can the user directly override?
```

---

## Quick Start

```bash
pip install agent-sovereignty-rules

from agent_sovereignty import SovereigntyChecker

checker = SovereigntyChecker()
result = checker.evaluate(
    suggestion="Reduce carbs today",
    context={"weight_trend": "rising"},
    source="health_tracker"
)
print(result)
# {'approved': True, 'reversible': True, 'source': 'health_tracker'}
```

---

## License

MIT License — see [LICENSE](LICENSE)
