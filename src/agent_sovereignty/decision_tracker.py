"""
DecisionTracker — 决策追踪器

记录所有决策，确保可追溯、可回溯
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any, List


class DecisionTracker:
    """
    决策追踪器

    记录格式：
    - decision_time: 决策时间
    - decision_content: 决策内容
    - decision_context: 决策背景
    - options_considered: 考虑的选项
    - final_choice: 最终选择
    - reasoning: 决策理由
    - source_cited: 引用来源
    - follow_up: 后续追踪
    """

    def __init__(self, storage_path: str = "./decisions"):
        self.storage_path = Path(storage_path)
        self.storage_path.mkdir(parents=True, exist_ok=True)
        self._ensure_index()

    def _ensure_index(self):
        """确保索引文件存在"""
        idx_file = self.storage_path / "index.json"
        if not idx_file.exists():
            idx_file.write_text(json.dumps({"decisions": [], "updated": None}))

    def _load_index(self) -> Dict:
        return json.loads((self.storage_path / "index.json").read_text())

    def _save_index(self, index: Dict):
        index["updated"] = datetime.now().isoformat()
        (self.storage_path / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2))

    def record(
        self,
        decision_id: str,
        content: str,
        context: Dict[str, Any],
        options: List[str],
        final_choice: str,
        reasoning: str,
        sources: List[str],
        follow_up: Optional[str] = None,
    ) -> Dict[str, Any]:
        """
        记录一个决策

        Args:
            decision_id: 决策唯一标识
            content: 决策内容摘要
            context: 决策背景
            options: 考虑的选项
            final_choice: 最终选择
            reasoning: 决策理由
            sources: 引用来源
            follow_up: 后续追踪任务
        """
        now = datetime.now().isoformat()
        record = {
            "id": decision_id,
            "content": content,
            "timestamp": now,
            "context": context,
            "options_considered": options,
            "final_choice": final_choice,
            "reasoning": reasoning,
            "sources_cited": sources,
            "follow_up": follow_up,
            "status": "active",
        }

        # 保存决策记录
        record_file = self.storage_path / f"{decision_id}.json"
        record_file.write_text(json.dumps(record, ensure_ascii=False, indent=2))

        # 更新索引
        index = self._load_index()
        index["decisions"].append({
            "id": decision_id,
            "timestamp": now,
            "content": content,
        })
        self._save_index(index)

        return {"success": True, "id": decision_id}

    def get(self, decision_id: str) -> Optional[Dict]:
        """获取单个决策记录"""
        record_file = self.storage_path / f"{decision_id}.json"
        if record_file.exists():
            return json.loads(record_file.read_text())
        return None

    def list_recent(self, limit: int = 10) -> List[Dict]:
        """列出最近的决策"""
        index = self._load_index()
        decisions = index.get("decisions", [])[-limit:]
        return [self.get(d["id"]) for d in decisions if self.get(d["id"])]

    def trace_back(
        self, keyword: str, limit: int = 5
    ) -> List[Dict]:
        """回溯特定主题的过往决策"""
        results = []
        for record_file in self.storage_path.glob("*.json"):
            if record_file.name == "index.json":
                continue
            try:
                record = json.loads(record_file.read_text())
                if keyword in record.get("content", "") or keyword in record.get("reasoning", ""):
                    results.append(record)
                    if len(results) >= limit:
                        break
            except Exception:
                continue
        return results
