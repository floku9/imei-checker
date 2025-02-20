from typing import Any, Optional
import redis
from settings import redis_settings
from data.cache_repository.base import BaseCacheRepository


class RedisCacheRepository(BaseCacheRepository):
    def __init__(self):
        self._redis_client = redis.Redis(
            host=redis_settings.REDIS_HOST,
            port=redis_settings.REDIS_PORT,
            username=redis_settings.REDIS_USER,
            password=redis_settings.REDIS_PASSWORD,
        )

    def add(self, key: str, value: str, expiration_seconds: int) -> None:
        self._redis_client.set(key, value, ex=expiration_seconds)

    def get(self, key: str) -> Optional[Any]:
        value: Optional[bytes] = self._redis_client.get(key)  # type: ignore

        if value:
            return value.decode("utf-8")
        return None


redis_cache = RedisCacheRepository()
