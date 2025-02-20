from abc import ABC, abstractmethod
from aiohttp import ClientSession


class BaseAPIService(ABC):
    _client_session: ClientSession

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *err):
        await self._client_session.close()
        self._client_session = None
