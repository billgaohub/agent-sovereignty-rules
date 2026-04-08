"""
Agent Sovereignty Rules — 决策权保护框架

五大原则：
1. 决策权守恒 — 系统只降低决策成本，不影响决策权结构
2. 认知放大而非选择收缩 — AI 可以排序选项，但不能隐藏选项
3. 可追溯性 — 每条建议必须附带来源依据
4. 可解释性 — 所有排序必须说人话
5. 可反转性 — 任何输出都有明确的 override 选项
"""

__version__ = "0.1.0"
__author__ = "Bill & Agent Sovereignty Contributors"

from .checker import SovereigntyChecker
from .rules import SovereigntyRules
from .decision_tracker import DecisionTracker

__all__ = [
    "SovereigntyChecker",
    "SovereigntyRules",
    "DecisionTracker",
]
