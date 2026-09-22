import requests


BASE_URL = "http://localhost:8501"


def test_application_is_running():
    response = requests.get(BASE_URL, timeout=10)

    assert response.status_code == 200


def test_application_does_not_expose_server_header():
    response = requests.get(BASE_URL, timeout=10)

    server_header = response.headers.get("Server", "")

    assert "python" not in server_header.lower()


def test_application_returns_html():
    response = requests.get(BASE_URL, timeout=10)

    content_type = response.headers.get("Content-Type", "")

    assert "text/html" in content_type.lower()


def test_application_handles_invalid_path():
    response = requests.get(
        f"{BASE_URL}/this-page-does-not-exist",
        timeout=10
    )

    assert response.status_code in [200, 404]