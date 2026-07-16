import json
from pathlib import Path

REPORT = Path("/app/report.json")

# Expected values for the fixed input at /app/access.log:
# 6 request lines, 3 distinct client IPs, and /index.html is the most
# frequently requested path (3 of the 6 requests).
EXPECTED_TOTAL_REQUESTS = 6
EXPECTED_UNIQUE_IPS = 3
EXPECTED_TOP_PATH = "/index.html"


def _report():
    return json.loads(REPORT.read_text())


def test_report_is_valid_json_object():
    """Criterion 1: /app/report.json exists and contains a single valid JSON object."""
    assert REPORT.exists(), "no /app/report.json found"
    data = _report()
    assert isinstance(data, dict), "report.json must contain a single JSON object"


def test_total_requests():
    """Criterion 2: "total_requests" is an integer equal to the number of request lines in the log."""
    value = _report().get("total_requests")
    assert isinstance(value, int) and not isinstance(value, bool), "total_requests must be an integer"
    assert value == EXPECTED_TOTAL_REQUESTS, f"total_requests is {value}, expected {EXPECTED_TOTAL_REQUESTS}"


def test_unique_ips():
    """Criterion 3: "unique_ips" is an integer equal to the number of distinct client IPs."""
    value = _report().get("unique_ips")
    assert isinstance(value, int) and not isinstance(value, bool), "unique_ips must be an integer"
    assert value == EXPECTED_UNIQUE_IPS, f"unique_ips is {value}, expected {EXPECTED_UNIQUE_IPS}"


def test_top_path():
    """Criterion 4: "top_path" is a string equal to the most frequently requested path."""
    value = _report().get("top_path")
    assert isinstance(value, str), "top_path must be a string"
    assert value == EXPECTED_TOP_PATH, f"top_path is {value!r}, expected {EXPECTED_TOP_PATH!r}"
