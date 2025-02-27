from abc import ABC
from typing import Tuple
from urllib.parse import urljoin

from aiohttp import ClientResponse, ClientSession

from application.dto.auth import GetTokenDTO, RegistryUserDTO
from application.interactors.api.base import BaseAPIClient
from application.interactors.api.response_handler import handle_api_response
from settings import backend_settings


class BaseAuthAPIClient(BaseAPIClient, ABC):
    async def __aenter__(self):
        raise NotImplementedError

    async def __aexit__(self, *err):
        await super().__aexit__(*err)

    async def registry(self, user: RegistryUserDTO):
        raise NotImplementedError

    async def auth_by_telegram_id(self, telegram_id: int | str):
        raise NotImplementedError


class AuthApiClient(BaseAuthAPIClient):
    _backend_url = backend_settings.BACKEND_URL
    _auth_route = "auth/"

    async def __aenter__(self):
        self._client_session = ClientSession(base_url=urljoin(self._backend_url, self._auth_route))
        return self

    async def __aexit__(self, *err):
        await super().__aexit__(*err)

    @handle_api_response()
    async def registry(self, user: RegistryUserDTO) -> Tuple[ClientResponse, dict]:
        async with self._client_session.post("add_tg_user", json=user.dict()) as response:
            json_response = await response.json()

            return response, json_response

    @handle_api_response(pydantic_model=GetTokenDTO)
    async def auth_by_telegram_id(self, telegram_id: int | str) -> Tuple[ClientResponse, dict]:
        async with self._client_session.get(f"get_token_by_tg_id/{telegram_id}") as response:
            json_response = await response.json()
            return response, json_response


auth_api_client = AuthApiClient()
