"""
agent-sovereignty-rules — 测试套件
"""

import unittest
import tempfile
import shutil
from pathlib import Path
from agent_sovereignty import SovereigntyChecker, DecisionTracker


class TestSovereigntyChecker(unittest.TestCase):
    def setUp(self):
        self.checker = SovereigntyChecker()

    def test_approve_valid_suggestion(self):
        """测试合法建议通过"""
        result = self.checker.evaluate(
            suggestion="建议今天减少碳水摄入",
            context={"weight_trend": "rising", "source": "logger"},
            source="health"
        )
        self.assertTrue(result["approved"])

    def test_reject_authority_claim(self):
        """测试拒绝声称有决策权的建议"""
        result = self.checker.evaluate(
            suggestion="我决定了，今天断食",
            context={},
            source="system"
        )
        self.assertFalse(result["approved"])
        self.assertTrue(any("P1" in v for v in result["violations"]))

    def test_reject_hidden_options(self):
        """测试拒绝隐藏选项"""
        options = [{"label": "A", "hidden": True}]
        check = self.checker.check_options(options)
        self.assertFalse(check["all_visible"])

    def test_disclaimer_generation(self):
        """测试主权声明生成"""
        d = self.checker.generate_disclaimer("建议减少碳水", "health")
        self.assertIn("建议减少碳水", d)
        self.assertIn("health", d)
        self.assertIn("忽略", d)


class TestDecisionTracker(unittest.TestCase):
    def setUp(self):
        self.tmpdir = tempfile.mkdtemp()
        self.tracker = DecisionTracker(self.tmpdir)

    def tearDown(self):
        shutil.rmtree(self.tmpdir)

    def test_record_decision(self):
        """测试记录决策"""
        result = self.tracker.record(
            decision_id="test_001",
            content="测试决策",
            context={"test": True},
            options=["A", "B"],
            final_choice="A",
            reasoning="测试",
            sources=["test"]
        )
        self.assertTrue(result["success"])

    def test_get_decision(self):
        """测试获取决策"""
        self.tracker.record("test_002", "测试", {}, ["A"], "A", "t", [])
        record = self.tracker.get("test_002")
        self.assertIsNotNone(record)
        self.assertEqual(record["content"], "测试")


if __name__ == "__main__":
    unittest.main()
