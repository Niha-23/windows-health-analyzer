from src.diagnostics.engine import analyze_system
from src.reports.health_report import generate_health_report
from src.system.monitor import collect_system_metrics


def main():
    """
    Run the Windows Health Analyzer application.
    """

    metrics = collect_system_metrics()
    analysis = analyze_system(metrics)
    report = generate_health_report(metrics, analysis)

    print(report)


if __name__ == "__main__":
    main()