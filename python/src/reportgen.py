import json
import os
import platform
import subprocess
from datetime import datetime, timezone
from typing import Dict, Any


def get_git_commit() -> str:
    try:
        out = subprocess.check_output(
            ["git", "rev-parse", "HEAD"],
            stderr=subprocess.DEVNULL
        )
        return out.decode().strip()
    except Exception:
        return "unknown"


def build_report(ts_tests_passed: int, py_tests_passed: int) -> Dict[str, Any]:
    return {
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "git_commit": get_git_commit(),
        "environment": {
            "python_version": platform.python_version(),
            "os": platform.platform(),
            "ci": os.environ.get("CI", "false"),
            "jenkins_url": os.environ.get("JENKINS_URL", ""),
            "job_name": os.environ.get("JOB_NAME", ""),
            "build_number": os.environ.get("BUILD_NUMBER", "")
        },
        "test_summary": {
            "typescript_tests_passed": ts_tests_passed,
            "python_tests_passed": py_tests_passed
        }
    }


def main() -> None:
    ts_passed = int(os.environ.get("TS_TESTS_PASSED", "0"))
    py_passed = int(os.environ.get("PY_TESTS_PASSED", "0"))
    out_path = os.environ.get("BUILD_REPORT_PATH", "build_report.json")

    report = build_report(ts_passed, py_passed)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)

    print(f"[reportgen] wrote {out_path}")


if __name__ == "__main__":
    main()