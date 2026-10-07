"""
Basic tests for the skill evaluator modules.

Run with: python -m pytest tests/ -v
Or directly: python tests/test_evaluator.py
"""

import sys
import json
from pathlib import Path

PROJECT_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PROJECT_ROOT / "scripts"))

from scanner import scan_submissions
from completeness import check_completeness
from evaluator import evaluate_quality


def test_scan_finds_files():
    """Test that scanner finds files in the golden set."""
    golden_set_path = PROJECT_ROOT / "benchmark" / "golden_set"
    sample_path = golden_set_path / "sample_01_perfect"
    if sample_path.exists():
        results = scan_submissions(str(sample_path))
        assert results is not None, "Scanner should return results"
        print("[PASS] test_scan_finds_files")
    else:
        print("[SKIP] test_scan_finds_files - golden set not found")


def test_rubric_loads():
    """Test that rubric.json is valid and loadable."""
    rubric_path = PROJECT_ROOT / "references" / "rubric.json"
    if rubric_path.exists():
        with open(rubric_path, "r", encoding="utf-8") as f:
            rubric = json.load(f)
        assert "dimensions" in rubric, "Rubric should have dimensions"
        assert len(rubric["dimensions"]) == 4, "Should have 4 dimensions"
        print("[PASS] test_rubric_loads")
    else:
        print("[SKIP] test_rubric_loads - rubric.json not found")


def test_golden_set_labels():
    """Test that golden set labels are valid."""
    labels_path = PROJECT_ROOT / "benchmark" / "golden_set" / "labels.json"
    if labels_path.exists():
        with open(labels_path, "r", encoding="utf-8") as f:
            labels = json.load(f)
        assert len(labels) == 12, f"Should have 12 samples, got {len(labels)}"
        for sample_id, label in labels.items():
            assert "expected_completeness" in label or "expected" in label, \
                f"Sample {sample_id} should have expected results"
        print("[PASS] test_golden_set_labels")
    else:
        print("[SKIP] test_golden_set_labels - labels.json not found")


if __name__ == "__main__":
    print("Running skill-evaluator tests...\n")
    test_scan_finds_files()
    test_rubric_loads()
    test_golden_set_labels()
    print("\nAll tests completed.")
