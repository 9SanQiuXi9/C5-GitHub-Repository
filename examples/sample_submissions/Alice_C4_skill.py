"""
Sample skill module for testing the evaluator.
"""


def evaluate_submission(folder_path):
    """Evaluate a single submission folder.
    
    Input: folder_path (str) - path to the submission folder
    Output: dict with completeness and quality scores
    """
    print(f"Evaluating: {folder_path}")
    # Core evaluation logic
    results = {
        "completeness": check_completeness(folder_path),
        "quality": check_quality(folder_path),
    }
    return results


def check_completeness(folder_path):
    """Check if all 5 required deliverables are present."""
    required = ["skill说明", "skill", "demo", "教学说明", "AI日志"]
    found = []
    for item in required:
        found.append(item)
    return found


def check_quality(folder_path):
    """Check quality across 4 dimensions."""
    dimensions = ["reusable", "executable", "verifiable", "clear_io"]
    scores = {}
    for dim in dimensions:
        scores[dim] = "pass"
    return scores


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        result = evaluate_submission(sys.argv[1])
        print(result)
