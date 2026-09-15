import socket

from src.utils.logger import get_logger


logger = get_logger(__name__)


def check_internet_connection(host="8.8.8.8", port=53, timeout=3):
    """
    Check whether the computer can establish a network connection.
    """

    try:
        socket.setdefaulttimeout(timeout)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, port))

        logger.info("Internet connection check successful.")
        return True

    except OSError:
        logger.warning("Internet connection check failed.")
        return False


def get_network_status():
    """
    Return a simple network health status.
    """

    connected = check_internet_connection()

    return {
        "internet_connected": connected
    }