import time

import psutil


def get_cpu_usage() -> float:
    """Return total system CPU usage percentage."""
    return psutil.cpu_percent(interval=1)


def get_memory_usage() -> float:
    """Return total system memory usage percentage."""
    return psutil.virtual_memory().percent


def get_disk_usage() -> float:
    """Return C: drive usage percentage."""
    return psutil.disk_usage("C:\\").percent


def get_top_processes(limit: int = 5) -> list:
    """Return processes using the most CPU."""

    processes = []

    # First measurement
    for process in psutil.process_iter(
        ["pid", "name", "memory_percent"]
    ):
        try:
            process.cpu_percent(None)

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            continue

    # Wait for CPU activity
    time.sleep(1)

    # Second measurement
    for process in psutil.process_iter(
        ["pid", "name", "memory_percent"]
    ):
        try:
            name = process.info["name"] or "Unknown"

            # Ignore Windows Idle Process
            if name.lower() == "system idle process":
                continue

            cpu_usage = process.cpu_percent(None)

            processes.append(
                {
                    "pid": process.info["pid"],
                    "name": name,
                    "cpu_percent": cpu_usage,
                    "memory_percent": process.info["memory_percent"],
                }
            )

        except (
            psutil.NoSuchProcess,
            psutil.AccessDenied,
            psutil.ZombieProcess,
        ):
            continue

    processes.sort(
        key=lambda process: process["cpu_percent"],
        reverse=True,
    )

    return processes[:limit]

def get_system_metrics() -> dict:
    """Collect basic Windows system metrics."""

    return {
        "cpu_percent": get_cpu_usage(),
        "memory_percent": get_memory_usage(),
        "disk_percent": get_disk_usage(),
        "top_processes": get_top_processes(),
    }