import os
import pytest_asyncio
from backend.application.interactors.imei_checker_client.api import APIImeiCheckerClient


@pytest_asyncio.fixture
def imei_checker_test_client() -> APIImeiCheckerClient:
    client = APIImeiCheckerClient(service_id=14)
    api_test_key: str = os.getenv("IMEI_API_KEY_TEST")
    test_service_id: str = os.getenv("IMEI_TEST_SERVICE_ID")
    client._api_settings.IMEI_API_KEY = api_test_key
    return client
