from abc import ABC, abstractmethod

from aiohttp import ClientSession


class BaseImeiCheckerClient(ABC):
    async def check_imei(self, imei: str) -> dict:
        raise NotImplementedError


class BaseAPIImeiCheckerClient(BaseImeiCheckerClient):
    _session: ClientSession

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *err):
        await self._session.close()
        self._session = None

    @abstractmethod
    async def check_imei(self, imei: str) -> dict:
        raise NotImplementedError
