from abc import ABC, abstractmethod
from typing import Any, Optional


class BaseCache(ABC):
    @abstractmethod
    def add(self, key: str, value: Any, expiration_seconds: int) -> None:
        raise NotImplementedError

    @abstractmethod
    def get(self, key: str) -> Optional[Any]:
        raise NotImplementedError

    def delete(self, key: str) -> None:
        raise NotImplementedError
