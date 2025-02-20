from urllib.parse import urljoin
from aiohttp import ClientSession
import aiohttp
from services.api.base import BaseAPIService
from settings import backend_settings
from utils.exceptions import RequestException


class IMEIInfoReceiverServiceV1(BaseAPIService):
    _api_version: str = "v1"

    def __init__(self, auth_token: str):
        self._auth_token = auth_token

    async def __aenter__(self):
        self._client_session = ClientSession(
            base_url=urljoin(backend_settings.BACKEND_URL, self._api_version),
            auth=aiohttp.BasicAuth(token=self._auth_token),
        )
        return self

    async def __aexit__(self, *err):
        await super().__aexit__(*err)

    async def get_imei_info(self, imei: str) -> dict:

        async with self._client_session.get(f"imei_checker/check/{imei}") as response:
            json_response = await response.json()

            if not response.ok:
                raise RequestException(status_code=response.status, error_info=json_response)

            return json_response


class IMEIInfoReceiverServiceSandbox(IMEIInfoReceiverServiceV1):
    _api_version: str = "sandbox"
