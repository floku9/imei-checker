from aiohttp import ClientSession, ClientTimeout

from utils.configuration.logging import get_logger

from .base import BaseAPIImeiCheckerClient
from settings import imei_api_settings, IMEIApiSettings
from utils.exceptions import RequestException

API_REQUEST_TIMEOUT = 20
logger = get_logger()


class APIImeiCheckerClient(BaseAPIImeiCheckerClient):
    service_id: int = 1
    _api_settings: IMEIApiSettings = imei_api_settings

    def __init__(self, service_id: int):
        self.service_id = service_id

    async def __aenter__(self):
        self._session = ClientSession(
            timeout=ClientTimeout(total=API_REQUEST_TIMEOUT),
            base_url="https://api.imeicheck.net/",
            headers={
                "Authorization": f"Bearer {self._api_settings.IMEI_API_KEY}",
                "Accept-Language": "en",
            },
        )
        return self

    async def __aexit__(self, *err):
        return await super().__aexit__(*err)

    @logger.catch(reraise=True)
    async def check_imei(self, imei: str) -> dict:
        logger.info(f"Checking imei {imei}")
        body = {"deviceId": imei, "serviceId": self.service_id}

        async with self._session.post("v1/checks", json=body) as response:

            json_response = await response.json()

            if not response.ok:
                raise RequestException(status_code=response.status, error_info=json_response)

            logger.info(f"Imei {imei} checked successfully")
            return json_response

    async def get_services(self) -> dict:
        async with self._session.get("v1/services") as response:
            json_response = await response.json()

            if not response.ok:
                raise RequestException(status_code=response.status, error_info=json_response)

            return json_response


model_description_imei_checker = APIImeiCheckerClient(service_id=24)
