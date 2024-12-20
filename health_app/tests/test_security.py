import pytest
from fastapi import HTTPException, status

from health_app.lib.security import get_api_key


def test_get_api_key_valid():
    """Test with a valid API key."""
    api_key = "test"
    assert get_api_key(api_key_header=api_key) == api_key


def test_get_api_key_invalid():
    """Test with an invalid API key."""
    invalid_key = "invalid_key"
    with pytest.raises(HTTPException) as excinfo:
        get_api_key(api_key_header=invalid_key)
    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excinfo.value.detail == "Invalid or missing API Key"


def test_get_api_key_missing():
    """Test with no API key."""
    with pytest.raises(HTTPException) as excinfo:
        get_api_key(api_key_header=None)
    assert excinfo.value.status_code == status.HTTP_401_UNAUTHORIZED
    assert excinfo.value.detail == "Invalid or missing API Key"
