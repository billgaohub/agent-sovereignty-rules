"""
agent-sovereignty-rules — 基础用法示例
"""

from agent_sovereignty import SovereigntyChecker, DecisionTracker

# ─── 1. 主权检查器 ───
print("=== SovereigntyChecker ===")
checker = SovereigntyChecker()

# 合法建议
result = checker.evaluate(
    suggestion="建议今天减少碳水摄入",
    context={"weight_trend": "rising", "days": 3, "source": "health_logger"},
    source="health_tracker"
)
print(f"合法建议: {result}")

# 生成主权声明
disclaimer = checker.generate_disclaimer(
    suggestion="建议今天减少碳水摄入",
    source="health_tracker"
)
print(f"\n主权声明:\n{disclaimer}")

# ─── 2. 选项检查 ───
print("\n=== 检查选项列表 ===")
options = [
    {"label": "A方案", "reason": "成本最低"},
    {"label": "B方案", "hidden": True, "reason": ""},  # 隐藏选项
]
check = checker.check_options(options)
print(f"选项合规检查: {check}")

# ─── 3. 决策追踪 ───
print("\n=== DecisionTracker ===")
tracker = DecisionTracker("./test_decisions")

tracker.record(
    decision_id="dec_20260408_001",
    content="是否升级到 V3 系统",
    context={"current_version": "v2", "risk": "medium"},
    options=["升级到V3", "维持V2", "延后3个月"],
    final_choice="升级到V3",
    reasoning="V3稳定性已验证，收益大于风险",
    sources=["V3测试报告", "团队反馈"],
    follow_up="3个月后评估效果"
)

# 回溯过往决策
past = tracker.trace_back("升级")
print(f"相关过往决策: {len(past)} 条")
for d in past:
    print(f"  - {d['timestamp'][:10]}: {d['content']}")
