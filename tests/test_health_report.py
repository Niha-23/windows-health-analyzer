from src.reports.health_report import generate_health_report


def test_generate_health_report_normal():
    metrics = {
        "cpu_percent": 20.0,
        "memory_percent": 50.0,
        "disk_percent": 40.0,
        "internet_connected": True,
    }

    analysis = {
        "overall_status": "NORMAL",
        "results": [
            {
                "component": "CPU",
                "severity": "NORMAL",
                "explanation": "CPU usage is normal.",
                "recommendation": "No action is required.",
            },
            {
                "component": "Memory",
                "severity": "NORMAL",
                "explanation": "Memory usage is normal.",
                "recommendation": "No action is required.",
            },
            {
                "component": "Disk",
                "severity": "NORMAL",
                "explanation": "Disk space is normal.",
                "recommendation": "No action is required.",
            },
        ],
    }

    report = generate_health_report(metrics, analysis)

    assert "WINDOWS HEALTH ANALYZER" in report
    assert "CPU" in report
    assert "MEMORY" in report
    assert "DISK" in report
    assert "NETWORK" in report
    assert "OVERALL SYSTEM HEALTH: NORMAL" in report
    assert "Internet: CONNECTED" in report


def test_generate_health_report_disconnected_network():
    metrics = {
        "cpu_percent": 20.0,
        "memory_percent": 50.0,
        "disk_percent": 40.0,
        "internet_connected": False,
    }

    analysis = {
        "overall_status": "NORMAL",
        "results": [
            {
                "component": "CPU",
                "severity": "NORMAL",
                "explanation": "CPU usage is normal.",
                "recommendation": "No action is required.",
            },
            {
                "component": "Memory",
                "severity": "NORMAL",
                "explanation": "Memory usage is normal.",
                "recommendation": "No action is required.",
            },
            {
                "component": "Disk",
                "severity": "NORMAL",
                "explanation": "Disk space is normal.",
                "recommendation": "No action is required.",
            },
        ],
    }

    report = generate_health_report(metrics, analysis)

    assert "Internet: DISCONNECTED" in report
    assert "Status: CRITICAL" in report
    assert "Check your Wi-Fi or Ethernet connection." in report