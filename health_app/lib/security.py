import logging

from decouple import config
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader

logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger(__name__)

# This should be stored in a secure location like a database.
# Kept in Env vars in the meantime
API_KEYS = config("API_KEYS", default="test").split(",")

api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


def get_api_key(
    api_key_header: str = Security(api_key_header),
) -> str:
    """
    Gets the API key from the header and raises an exception if incorrect

    Parameters:
    api_key_header: THe header value of the api key

    Returns:
    the header if it passes check.
    """
    if api_key_header in API_KEYS:
        return api_key_header
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid or missing API Key",
    )
