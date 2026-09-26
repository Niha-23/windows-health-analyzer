import psutil

from src.utils.logger import get_logger


logger = get_logger(__name__)


def get_disk_usage(path="C:\\") -> float:
    """
    Return the current disk usage percentage.
    """

    disk_percent = psutil.disk_usage(path).percent

    logger.info(
        "Disk usage collected for %s: %.1f%%",
        path,
        disk_percent,
    )

    return disk_percent