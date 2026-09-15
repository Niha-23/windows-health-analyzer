from unittest.mock import patch

from src.collectors.network import (
    check_internet_connection,
    get_network_status,
)

from src.diagnostics.engine import (
    analyze_cpu,
    analyze_memory,
    analyze_disk,
    analyze_system,
)
def test_cpu_critical():
    result = analyze_cpu(95)

    assert result["severity"] == "CRITICAL"


def test_memory_warning():
    result = analyze_memory(90)

    assert result["severity"] == "WARNING"


def test_disk_normal():
    result = analyze_disk(50)

    assert result["severity"] == "NORMAL"


def test_system_overall_status():
    metrics = {
        "cpu_percent": 20,
        "memory_percent": 90,
        "disk_percent": 40,
    }

    result = analyze_system(metrics)

    assert result["overall_status"] == "WARNING"

@patch("src.collectors.network.socket.socket")
def test_internet_connection_success(mock_socket):
    mock_socket.return_value.__enter__.return_value.connect.return_value = None

    result = check_internet_connection()

    assert result is True


@patch("src.collectors.network.socket.socket")
def test_internet_connection_failure(mock_socket):
    mock_socket.return_value.__enter__.return_value.connect.side_effect = OSError

    result = check_internet_connection()

    assert result is False


@patch("src.collectors.network.check_internet_connection")
def test_network_status_connected(mock_connection):
    mock_connection.return_value = True

    result = get_network_status()

    assert result["internet_connected"] is True


@patch("src.collectors.network.check_internet_connection")
def test_network_status_disconnected(mock_connection):
    mock_connection.return_value = False

    result = get_network_status()

    assert result["internet_connected"] is False