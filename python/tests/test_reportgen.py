from src.reportgen import build_report


def test_build_report_structure():
    report = build_report(2, 1)
    assert "generated_at_utc" in report
    assert "git_commit" in report
    assert report["test_summary"]["typescript_tests_passed"] == 2
    assert report["test_summary"]["python_tests_passed"] == 1