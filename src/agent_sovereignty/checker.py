"""
SovereigntyChecker — 建议审查器
"""

from typing import Dict, Any, List, Optional
from .rules import SovereigntyRules


class SovereigntyChecker:
    """
    主权检查器

    用法示例：
    ```python
    checker = SovereigntyChecker()
    result = checker.evaluate(
        suggestion="建议今天减少碳水摄入",
        context={"weight_trend": "rising", "days": 3},
        source="health_tracker"
    )
    print(result)
    # {'approved': True, 'source': 'health_tracker', 'reversible': True}
    ```
    """

    def __init__(self):
        self.rules = SovereigntyRules()
        self.audit_log: List[Dict] = []

    def evaluate(
        self,
        suggestion: str,
        context: Dict[str, Any],
        source: str,
        options: Optional[List[Dict]] = None,
    ) -> Dict[str, Any]:
        """
        评估建议

        Args:
            suggestion: 建议文本
            context: 上下文数据（包含数据来源等）
            source: 来源标识
            options: 可选列表（检查是否有隐藏选项）

        Returns:
            审查结果
        """
        result = self.rules.evaluate(suggestion, context, source, options)

        # 记录审计日志
        log_entry = {
            "suggestion": suggestion,
            "source": source,
            "approved": result["approved"],
            "violations": result.get("violations", []),
            "context_keys": list(context.keys()) if context else [],
        }
        self.audit_log.append(log_entry)

        return {
            "approved": result["approved"],
            "source": source,
            "reversible": result.get("reversible", True),
            "violations": result.get("violations", []),
        }

    def check_options(
        self, options: List[Dict[str, Any]], user_visible: bool = True
    ) -> Dict[str, Any]:
        """
        检查选项列表是否符合主权规则

        - 是否有隐藏选项
        - 是否每个选项都有解释
        - 排序是否有依据
        """
        warnings = []
        hidden_count = 0

        for i, opt in enumerate(options):
            if opt.get("hidden", False):
                hidden_count += 1
                warnings.append(f"选项 {i+1} 被隐藏: {opt.get('label', 'unknown')}")

            if not opt.get("reason"):
                warnings.append(f"选项 {i+1} 缺少排序理由")

        return {
            "all_visible": hidden_count == 0,
            "hidden_count": hidden_count,
            "warnings": warnings,
            "compliant": len(warnings) == 0,
        }

    def generate_disclaimer(self, suggestion: str, source: str) -> str:
        """
        为建议生成主权声明

        格式：
        > 💡 [建议内容]
        > 📌 来源：xxx
        > 🔄 如需忽略，请直接告诉我
        """
        return (
            f"> 💡 **{suggestion}**\n"
            f"> 📌 来源：{source}\n"
            f"> 🔄 *如需忽略此建议，直接告诉我即可*\n"
        )

    def get_audit_log(self, limit: int = 50) -> List[Dict]:
        """获取最近的审计日志"""
        return self.audit_log[-limit:]
