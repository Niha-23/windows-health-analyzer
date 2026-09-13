from src.collectors.system import get_system_metrics
from src.diagnostics.engine import analyze_system


def display_report(metrics: dict, diagnosis: dict) -> None:
    """Display a human-friendly health report."""

    print("\n========================================")
    print("       WINDOWS HEALTH ANALYZER")
    print("========================================\n")

    print(f"CPU Usage:    {metrics['cpu_percent']:.1f}%")
    print(f"Memory Usage: {metrics['memory_percent']:.1f}%")
    print(f"Disk Usage:   {metrics['disk_percent']:.1f}%")

    print("\n----------------------------------------")
    print("DIAGNOSTIC REPORT")
    print("----------------------------------------\n")

    print(f"Overall Status: {diagnosis['overall_status']}")

    for result in diagnosis["results"]:
        print(f"\n[{result['severity']}] {result['component']}")
        print(f"Issue: {result['message']}")
        print(f"What this means: {result['explanation']}")
        print(f"Recommended action: {result['recommendation']}")


def main():
    metrics = get_system_metrics()

    diagnosis = analyze_system(metrics)

    display_report(metrics, diagnosis)


if __name__ == "__main__":
    main()