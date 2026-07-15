> ⚠️ **Deprecated — legacy AIUCE family.** This repo is being consolidated into **SONUV** / **AIOBR** / a unified history archive (2026). No new work is accepted. Current status: **[aiuce.com](https://aiuce.com)**. _Marked 2026-07-15._
>
> _本仓库属旧 AIUCE 体系，正整合进 SONUV / AIOBR / 统一历史归档，不再接受新改动；最新状态见 aiuce.com。_
> **Disposition**: **Migrate → SONUV / AIOBR**
> **处置**：可验证接口/测试将整合进 SONUV 或 AIOBR（运行时/治理能力）；本仓不再作为独立产品维护，源码迁移待目标仓就绪。


# Agent Sovereignty Rules

> AI Agent 决策权保护框架 / Decision Rights Protection Framework for AI Agents

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Archived](https://img.shields.io/badge/Status-Arhived-lightgrey.svg)](#)

[中文](README.md) · [English](README_EN.md)

---

## What It Is

Agent Sovereignty Rules is a decision rights protection framework for AI Agent systems, ensuring **humans always retain final decision-making authority**.

> 🤝 AI amplifies cognition — it never replaces human judgment.

**核心定位：** 系统只是认知放大，提醒决策风险，不替代人类做决定。

---

## Five Core Principles

| # | Principle | 含义 |
|---|-----------|------|
| **1** | **决策权守恒 / Decision Rights Conservation** | System lowers decision cost; never alters decision rights structure |
| **2** | **认知放大 / Cognitive Amplification** | AI may rank options; must never hide options |
| **3** | **来源可追溯 / Traceability** | Every recommendation must cite its source |
| **4** | **排序可解释 / Explainability** | All rankings must be human-readable |
| **5** | **输出可反转 / Reversibility** | Every output has a clear "override this" path |

---

## Quick Start

```bash
pip install agent-sovereignty-rules

from agent_sovereignty import SovereigntyChecker

checker = SovereigntyChecker()

result = checker.evaluate(
    suggestion="建议减少碳水摄入",
    context={"weight_trend": "rising", "days": 3},
    source="health_tracker"
)
print(result)
# {'approved': True, 'source': 'health_tracker', 'reversible': True}
```

---

## Decision Review Checklist

```
□ 决策权是否在用户手中？/ Is decision authority with the user?
□ 选择空间是否完整？/ Is the option space complete?
□ 建议是否标注来源？/ Is the source cited?
□ 排序是否解释原因？/ Is the ranking explained?
□ 用户是否可直接 override？/ Can user override directly?
```

---

## Architecture

```
agent-sovereignty-rules/
├── src/agent_sovereignty/
│   ├── __init__.py
│   ├── rules.py             # 核心规则引擎
│   ├── checker.py            # 建议审查器
│   └── decision_tracker.py   # 决策追踪器
├── docs/
│   ├── PRINCIPLES.md         # 七条意志原则详解
│   └── IMPLEMENTATION.md     # 集成指南
├── examples/
│   └── basic_usage.py
├── tests/
│   └── test_rules.py
├── README.md / README_EN.md
└── LICENSE
```

---

## Origin

Derived from **SONUV** system — an 11-layer personal AI governance framework. This project implements the **sovereignty layer** practice.

> *"If you're worried AI quietly makes decisions for you, Agent Sovereignty Rules is your guardrail."*

---

## Status

⚠️ **Archived** — This project has been merged into [AI Governance Framework](https://github.com/billgaohub/AIUCE).

New file organization tool: [IPIPQ](https://github.com/billgaohub/ipipq)

---

## License

MIT License · See [LICENSE](LICENSE)
