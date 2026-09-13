from src.diagnostics.engine import (
    analyze_cpu,
    analyze_memory,
    analyze_disk,
    analyze_system,
)


def test_cpu_critical():
    result = analyze_cpu(95)

    assert result["severity"] == "CRITICAL"


def test_memory_warning():
    result = analyze_memory(90)

    assert result["severity"] == "WARNING"


def test_disk_normal():
    result = analyze_disk(50)

    assert result["severity"] == "NORMAL"


def test_system_overall_status():
    metrics = {
        "cpu_percent": 20,
        "memory_percent": 90,
        "disk_percent": 40,
    }

    result = analyze_system(metrics)

    assert result["overall_status"] == "WARNING"