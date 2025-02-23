from typing import Tuple
from urllib.parse import urljoin

from aiohttp import ClientResponse, ClientSession

from application.interactors.api.base import BaseAPIClient
from application.interactors.api.response_handler import handle_api_response
from settings import backend_settings


class IMEIClientV1(BaseAPIClient):

    _api_version = "v1/"
    _backend_url = backend_settings.BACKEND_URL

    def __init__(self, auth_token: str):
        self._auth_token = auth_token

    async def __aenter__(self):
        self._client_session = ClientSession(
            base_url=urljoin(base=self._backend_url, url=self._api_version),
            headers={"Authorization": f"Bearer {self._auth_token}"},
        )
        return self

    async def __aexit__(self, *err):
        await super().__aexit__(*err)

    @handle_api_response()
    async def get_imei_info(self, imei: str) -> Tuple[ClientResponse, dict]:
        async with self._client_session.get(f"imei_checker/check/{imei}") as response:
            json_response = await response.json()
            return response, json_response


class IMEIClientSandbox(IMEIClientV1):
    _api_version = "sandbox/"
