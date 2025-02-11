import os
import pytest
import pytest_asyncio

from backend.application.interactors.imei_checker_client.api import APIImeiCheckerClient
from backend.utils.exceptions import RequestException


@pytest.mark.asyncio
async def test_check_imei_successfully(imei_checker_test_client: APIImeiCheckerClient):
    async with imei_checker_test_client as client:
        imei = "861536030196001"
        response = await client.check_imei(imei)

    assert response is not None


async def test_check_imei_failed(imei_checker_test_client: APIImeiCheckerClient):
    async with imei_checker_test_client as client:
        imei = "123456789012345"
        with pytest.raises(RequestException) as e:
            await client.check_imei(imei)

        assert e.value.status_code is not None


async def test_get_services_successfully(imei_checker_test_client: APIImeiCheckerClient):
    async with imei_checker_test_client as client:
        response = await client.get_services()
    assert response is not None
