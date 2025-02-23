from abc import ABC, abstractmethod

from aiohttp import ClientSession


class BaseAPIClient(ABC):
    """
    An abstract base class for API clients that provides a context manager
    interface for managing the client session.

    The `BaseAPIClient` class defines two abstract methods, `__aenter__` and `__aexit__`,
    that must be implemented by concrete subclasses. These methods are used to manage the
    lifecycle of the client session, ensuring that the session is properly opened and closed.

    The `__aexit__` method is responsible for closing the client
    session and setting the `_client_session` attribute to `None`.
    """

    _client_session: ClientSession

    @abstractmethod
    async def __aenter__(self):
        raise NotImplementedError

    @abstractmethod
    async def __aexit__(self, *err):
        await self._client_session.close()
        self._client_session = None
