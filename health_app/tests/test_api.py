from unittest.mock import MagicMock, patch

import pytest
from fastapi.testclient import TestClient

from health_app.backend_api.main import app


@pytest.fixture(scope="session")
def test_client():
    yield TestClient(app)


def test_upload_endpoint_without_api_key(
    test_client, test_file="../data/test_data.json", api_key=""
):
    with open(test_file, "rb") as f:
        response = test_client.post(
            "/upload",
            files={"file": (test_file, f, "text/plain")},
            headers={"x-api-key": api_key},
        )

    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid or missing API Key"}


def test_upload_endpoint_without_api_key_header(
    test_client, test_file="../data/test_data.json", api_key=""
):
    with open(test_file, "rb") as f:
        response = test_client.post(
            "/upload",
            files={"file": (test_file, f, "text/plain")},
        )

    assert response.status_code == 401
    assert response.json() == {"detail": "Invalid or missing API Key"}


def test_upload_wrong_format(test_client, test_file="../data/test.csv", api_key="test"):
    with open(test_file, "rb") as f:
        response = test_client.post(
            "/upload",
            files={"file": (test_file, f, "text/plain")},
            headers={"x-api-key": api_key},
        )

    assert response.status_code == 500
    assert response.json() == {"detail": "Incorrect file format provided"}
