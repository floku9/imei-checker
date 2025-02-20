from urllib.parse import urljoin
from aiohttp import ClientSession
from services.api.base import BaseAPIService
from services.dto.auth import RegistryUserDTO
from settings import backend_settings
from utils.exceptions import RequestException


class AuthApiService(BaseAPIService):
    async def __aenter__(self):
        self._client_session = ClientSession(base_url=urljoin(backend_settings.BACKEND_URL, "auth"))
        return self

    async def __aexit__(self, *err):
        await super().__aexit__(*err)

    async def registry(self, user: RegistryUserDTO) -> None:
        async with self._client_session.post("add_tg_user", json=user.json()) as response:
            json_response = await response.json()

            if not response.ok:
                raise RequestException(status_code=response.status, error_info=json_response)

            return json_response

    async def auth_by_telegram_id(self, telegram_id: int | str):
        async with self._client_session.get(f"get_token_by_tg_id/{telegram_id}") as response:
            json_response = await response.json()

            if not response.ok:
                raise RequestException(status_code=response.status, error_info=json_response)

            return json_response
