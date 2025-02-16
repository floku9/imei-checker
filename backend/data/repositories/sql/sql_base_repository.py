from abc import ABC, abstractmethod
from typing import Any


class SQLBaseRepositoryAsync(ABC):
    @abstractmethod
    async def get_one(self, id: int):
        raise NotImplementedError

    @abstractmethod
    async def get_one_by_filters(self, **filters: dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    async def get_many(self, **filters: dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    async def create(self, data: dict[str, Any]):
        raise NotImplementedError

    @abstractmethod
    async def update(self, idx: int, data: dict[str, Any]):
        raise NotImplementedError

    async def delete(self, idx: int):
        raise NotImplementedError
