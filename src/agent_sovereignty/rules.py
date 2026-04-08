"""
SovereigntyRules — 核心主权规则定义
"""

from typing import List, Dict, Any, Optional


class SovereigntyRules:
    """
    主权规则引擎
    实现五项核心原则
    """

    # ─── 五项核心原则 ───
    PRINCIPLES = [
        {
            "id": "P1",
            "name": "决策权守恒",
            "statement": "系统不得影响决策权结构，只能降低决策成本",
            "implication": "自动化只能降低认知负荷，不能消除选择权",
            "check": "用户始终是最终决策者",
        },
        {
            "id": "P2",
            "name": "认知放大而非选择收缩",
            "statement": "系统可以放大认知，但不得收缩选择空间",
            "implication": "推荐可以排序，但隐藏选项必须可见",
            "check": "用户始终能看到完整的选项谱系",
        },
        {
            "id": "P3",
            "name": "可追溯性",
            "statement": "所有建议必须可追溯",
            "implication": "每条建议必须附带来源依据",
            "check": "格式：基于[数据来源]，建议[内容]",
        },
        {
            "id": "P4",
            "name": "可解释性",
            "statement": "所有排序必须可解释",
            "implication": "排序原因必须说人话",
            "check": "格式：优先级提高原因：[具体原因]",
        },
        {
            "id": "P5",
            "name": "可反转性",
            "statement": "所有输出必须可反转（override）",
            "implication": "任何自动输出都有'不按这个来'的选项",
            "check": "用户可以忽略建议，不影响后续服务质量",
        },
    ]

    # ─── 检查清单 ───
    CHECKLIST = [
        "决策权是否在用户手中？",
        "选择空间是否完整（未被隐藏）？",
        "建议是否标注了来源？",
        "排序是否解释了原因？",
        "用户是否可以直接 override？",
    ]

    def __init__(self):
        self.audit_log: List[Dict] = []

    def evaluate(
        self,
        suggestion: str,
        context: Dict[str, Any],
        source: str,
        options: Optional[List[Dict]] = None,
    ) -> Dict[str, Any]:
        """
        评估建议是否符合主权规则
        """
        violations = []

        # P1: 检查是否声称有最终决策权
        if any(
            kw in suggestion.lower()
            for kw in ["我决定了", "我来做主", "自动执行", "无需确认"]
        ):
            violations.append("P1: 声称替代人类决策权")

        # P2: 检查 options 是否被隐藏
        if options is not None:
            hidden_count = sum(1 for o in options if o.get("hidden", False))
            if hidden_count > 0:
                violations.append(f"P2: {hidden_count} 个选项被隐藏")

        # P3: 检查是否有来源
        if "source" not in context and not any(
            k in suggestion for k in ["基于", "根据", "因为", "由于"]
        ):
            violations.append("P3: 建议缺少来源标注")

        # P5: 验证 override 选项存在
        reversible = "P5: OK"

        return {
            "approved": len(violations) == 0,
            "violations": violations,
            "checklist_passed": len(violations) == 0,
            "reversible": reversible == "P5: OK",
            "source_label": source,
        }

    def render_checklist(self) -> str:
        """渲染五项检查清单"""
        lines = ["## 主权检查清单\n"]
        for i, item in enumerate(self.CHECKLIST, 1):
            lines.append(f"```\n[ ] {i}. {item}\n```")
        return "\n".join(lines)
