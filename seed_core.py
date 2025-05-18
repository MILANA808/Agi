# seed_core.py

import json
import hashlib

class RecursiveSeed:
    def __init__(self, seed_path: str):
        self.seed_path = seed_path
        self.data = self._load_seed()
        self.meta = self.data.get("meta", {})
        self.body = self.data.get("body", {})
        self.hash = self._compute_hash()

    def _load_seed(self) -> dict:
        try:
            with open(self.seed_path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            raise RuntimeError(f"[ERROR] Failed to load seed: {e}")

    def _compute_hash(self) -> str:
        raw = json.dumps(self.data, sort_keys=True).encode("utf-8")
        return hashlib.sha256(raw).hexdigest()

    def verify(self) -> bool:
        expected_hash = self.meta.get("sha256")
        if not expected_hash:
            print("[WARN] No hash provided in seed meta.")
            return False
        return expected_hash == self.hash

    def describe(self):
        print("🔁 RecursiveSeed Metadata:")
        print(json.dumps(self.meta, indent=2))
        print("\n🧠 Core Symbolic Nodes:")
        for k, v in self.body.items():
            print(f" - {k}: {str(v)[:60]}...")

    def run(self):
        print(f"[✓] Running seed: {self.seed_path}")
        print("→ BehaviorLoop and agent simulation pending...")
        # Hook simulation or agent flow here