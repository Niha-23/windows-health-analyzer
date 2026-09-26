import psutil

from src.utils.logger import get_logger


logger = get_logger(__name__)


def get_memory_usage() -> float:
    """
    Return the current memory usage percentage.
    """

    memory_percent = psutil.virtual_memory().percent

    logger.info(
        "Memory usage collected: %.1f%%",
        memory_percent,
    )

    return memory_percent