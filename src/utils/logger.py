import logging


def get_logger(name):
    """
    Create and return a logger for the application.
    """

    logger = logging.getLogger(name)

    if not logger.handlers:
        handler = logging.StreamHandler()

        formatter = logging.Formatter(
            "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )

        handler.setFormatter(formatter)
        logger.addHandler(handler)

    logger.setLevel(logging.INFO)

    return logger