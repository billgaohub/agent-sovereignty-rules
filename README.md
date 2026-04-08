# Agent Sovereignty Rules

> AI Agent 的决策权保护框架

[English README](README_EN.md)

---

## 核心定位

**"系统只是认知放大，提醒我决策要注意哪些，不能什么都指望自动化。最终还是要靠自己的。"**

Agent Sovereignty Rules 是一套为 AI Agent 系统设计的决策权保护框架，确保：

> 🤝 **人类始终保持最终决策权，AI 永远只是认知放大器，而非决策替代者。**

---

## 五大核心原则

| # | 原则 | 含义 |
|---|------|------|
| **1** | **决策权守恒** | 系统只降低决策成本，不影响决策权结构 |
| **2** | **认知放大而非选择收缩** | AI 可以排序选项，但不能隐藏选项 |
| **3** | **可追溯性** | 每条建议必须附带来源依据 |
| **4** | **可解释性** | 所有排序必须说人话 |
| **5** | **可反转性** | 任何输出都有明确的"不按这个来"选项 |

---

## 快速开始

```bash
pip install agent-sovereignty-rules

from agent_sovereignty import SovereigntyChecker

checker = SovereigntyChecker()

# 检查建议是否符合主权规则
result = checker.evaluate(
    suggestion="建议今天减少碳水摄入",
    context={"weight_trend": "rising", "days": 3},
    source="health_tracker"
)
print(result)
# {'approved': True, 'source': 'health_tracker', 'reversible': True}
```

---

## 五项检查清单

每次系统输出建议时，对照检查：

```
□ 决策权是否在用户手中？
□ 选择空间是否完整（未被隐藏）？
□ 建议是否标注了来源？
□ 排序是否解释了原因？
□ 用户是否可以直接 override？
```

---

## 七条意志原则（来自 SONUV Manifesto）

```python
P1. 主权至上    # 任何绕过人类决策权的指令均属非法
P2. 现实胜于叙事  # 宁可在真相中沉默，不在叙事中喧哗
P3. 认知抗熵    # 拒绝空洞建议，无数据不推导
P4. 决策可追溯  # 所有推理链路必须留痕
P5. 经验硬化    # 失败必须转化为防御规则
P6. 计算中立    # 意志独立于底层 LLM
P7. 授权代行    # 自主权必须有明确边界
```

---

## 目录结构

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
├── README.md
├── README_EN.md
├── LICENSE
└── requirements.txt
```

---

## 适用场景

- **AI Agent 开发**：给 Agent 加上"决策权保险"
- **智能助手**：确保用户始终是最终决策者
- **自动化工作流**：防止"智能筛选"变成"不可见筛选"
- **企业 AI 治理**：建立 AI 使用规范

---

## 设计背景

本项目源于 [SONUV](https://github.com/billgaohub/AIUCE) 系统（一个十一层架构的个人 AI 治理框架）的主权层实践。

> 如果你担心 AI 会"悄悄"替你做决定，Agent Sovereignty Rules 是为你设计的护栏。

---

## License

MIT License — 详见 [LICENSE](LICENSE)
