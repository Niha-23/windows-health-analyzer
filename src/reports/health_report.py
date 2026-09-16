from src.utils.logger import get_logger


logger = get_logger(__name__)


def generate_health_report(metrics: dict, analysis: dict) -> str:
    """
    Generate a human-readable Windows health report.
    """

    lines = []

    lines.append("=" * 45)
    lines.append("       WINDOWS HEALTH ANALYZER")
    lines.append("=" * 45)
    lines.append("")

    cpu_percent = metrics["cpu_percent"]
    memory_percent = metrics["memory_percent"]
    disk_percent = metrics["disk_percent"]
    internet_connected = metrics["internet_connected"]

    lines.append("CPU")
    lines.append(f"Usage: {cpu_percent:.1f}%")

    cpu_result = next(
        result
        for result in analysis["results"]
        if result["component"] == "CPU"
    )

    lines.append(f"Status: {cpu_result['severity']}")
    lines.append(cpu_result["explanation"])
    lines.append(f"Recommendation: {cpu_result['recommendation']}")
    lines.append("")

    lines.append("MEMORY")
    lines.append(f"Usage: {memory_percent:.1f}%")

    memory_result = next(
        result
        for result in analysis["results"]
        if result["component"] == "Memory"
    )

    lines.append(f"Status: {memory_result['severity']}")
    lines.append(memory_result["explanation"])
    lines.append(
        f"Recommendation: {memory_result['recommendation']}"
    )
    lines.append("")

    lines.append("DISK")
    lines.append(f"Usage: {disk_percent:.1f}%")

    disk_result = next(
        result
        for result in analysis["results"]
        if result["component"] == "Disk"
    )

    lines.append(f"Status: {disk_result['severity']}")
    lines.append(disk_result["explanation"])
    lines.append(f"Recommendation: {disk_result['recommendation']}")
    lines.append("")

    lines.append("NETWORK")

    if internet_connected:
        lines.append("Internet: CONNECTED")
        lines.append("Status: NORMAL")
    else:
        lines.append("Internet: DISCONNECTED")
        lines.append("Status: CRITICAL")
        lines.append(
            "Recommendation: Check your Wi-Fi or Ethernet connection."
        )

    lines.append("")

    lines.append("-" * 45)
    lines.append(
        f"OVERALL SYSTEM HEALTH: {analysis['overall_status']}"
    )
    lines.append("-" * 45)

    report = "\n".join(lines)

    logger.info("Health report generated successfully.")

    return report