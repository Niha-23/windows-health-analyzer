from src.collectors.cpu import get_cpu_usage
from src.collectors.memory import get_memory_usage
from src.collectors.disk import get_disk_usage
from src.collectors.network import get_network_status

from src.utils.logger import get_logger


logger = get_logger(__name__)


def collect_system_metrics() -> dict:
    """
    Collect current health metrics from the Windows computer.
    """

    logger.info("Collecting system health metrics.")

    cpu_percent = get_cpu_usage()
    memory_percent = get_memory_usage()
    disk_percent = get_disk_usage()
    network_status = get_network_status()

    metrics = {
        "cpu_percent": cpu_percent,
        "memory_percent": memory_percent,
        "disk_percent": disk_percent,
        "internet_connected": network_status["internet_connected"],
    }

    logger.info("System health metrics collected successfully.")

    return metrics