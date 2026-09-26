import psutil

from src.utils.logger import get_logger


logger = get_logger(__name__)


def get_cpu_usage() -> float:
    """
    Return the current CPU usage percentage.
    """

    cpu_percent = psutil.cpu_percent(interval=1)

    logger.info(
        "CPU usage collected: %.1f%%",
        cpu_percent,
    )

    return cpu_percent