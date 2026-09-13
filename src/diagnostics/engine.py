from typing import Any


def analyze_cpu(cpu_percent: float) -> dict[str, Any]:
    """Analyze CPU usage."""

    if cpu_percent >= 90:
        return {
            "component": "CPU",
            "severity": "CRITICAL",
            "message": "CPU usage is very high.",
            "explanation": (
                "Your computer is using most of its "
                "processing capacity."
            ),
            "recommendation": (
                "Check which applications are using "
                "the most CPU."
            ),
        }

    if cpu_percent >= 75:
        return {
            "component": "CPU",
            "severity": "WARNING",
            "message": "CPU usage is elevated.",
            "explanation": (
                "Your computer is working harder "
                "than usual."
            ),
            "recommendation": (
                "Check running applications and "
                "background tasks."
            ),
        }

    return {
        "component": "CPU",
        "severity": "NORMAL",
        "message": "CPU usage is normal.",
        "explanation": (
            "Your computer has available processing "
            "capacity."
        ),
        "recommendation": "No action is required.",
    }


def analyze_memory(memory_percent: float) -> dict[str, Any]:
    """Analyze memory usage."""

    if memory_percent >= 95:
        return {
            "component": "Memory",
            "severity": "CRITICAL",
            "message": "Memory usage is critically high.",
            "explanation": (
                "Your computer may have very little "
                "available memory."
            ),
            "recommendation": (
                "Close unnecessary applications and "
                "check available RAM."
            ),
        }

    if memory_percent >= 85:
        return {
            "component": "Memory",
            "severity": "WARNING",
            "message": "Memory usage is high.",
            "explanation": (
                "Your computer is using a large "
                "portion of its memory."
            ),
            "recommendation": (
                "Check applications using the most "
                "memory."
            ),
        }

    if memory_percent >= 75:
        return {
            "component": "Memory",
            "severity": "ELEVATED",
            "message": "Memory usage is elevated.",
            "explanation": (
                "Memory usage is above the normal "
                "range for this initial assessment."
            ),
            "recommendation": (
                "Monitor memory usage and check "
                "large applications if needed."
            ),
        }

    return {
        "component": "Memory",
        "severity": "NORMAL",
        "message": "Memory usage is normal.",
        "explanation": (
            "Your computer has a reasonable amount "
            "of memory available."
        ),
        "recommendation": "No action is required.",
    }


def analyze_disk(disk_percent: float) -> dict[str, Any]:
    """Analyze disk space usage."""

    if disk_percent >= 95:
        return {
            "component": "Disk",
            "severity": "CRITICAL",
            "message": "Disk space is critically low.",
            "explanation": (
                "Your storage drive is almost full."
            ),
            "recommendation": (
                "Free up disk space by removing "
                "unnecessary files."
            ),
        }

    if disk_percent >= 85:
        return {
            "component": "Disk",
            "severity": "WARNING",
            "message": "Disk space is running low.",
            "explanation": (
                "Your storage drive has limited "
                "free space."
            ),
            "recommendation": (
                "Review large files and free up "
                "storage space."
            ),
        }

    return {
        "component": "Disk",
        "severity": "NORMAL",
        "message": "Disk space is normal.",
        "explanation": (
            "Your storage drive has a reasonable "
            "amount of free space."
        ),
        "recommendation": "No action is required.",
    }


def analyze_system(metrics: dict) -> dict[str, Any]:
    """Analyze system metrics and return a report."""

    cpu_result = analyze_cpu(metrics["cpu_percent"])
    memory_result = analyze_memory(metrics["memory_percent"])
    disk_result = analyze_disk(metrics["disk_percent"])

    results = [
        cpu_result,
        memory_result,
        disk_result,
    ]

    severity_order = {
        "NORMAL": 0,
        "ELEVATED": 1,
        "WARNING": 2,
        "CRITICAL": 3,
    }

    overall_result = max(
        results,
        key=lambda result: severity_order[result["severity"]],
    )

    return {
        "overall_status": overall_result["severity"],
        "results": results,
    }