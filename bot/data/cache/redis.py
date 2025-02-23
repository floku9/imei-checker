from typing import Any, Optional
import redis
from settings import redis_settings
from data.cache.base import BaseCache


class RedisCache(BaseCache):
    def __init__(self, redis_client: redis.Redis):
        self._redis_client = redis_client

    def add(self, key: str, value: str, expiration_seconds: int) -> None:
        self._redis_client.set(key, value, ex=expiration_seconds)

    def get(self, key: str) -> Optional[Any]:
        return self._redis_client.get(key)

    def delete(self, key: str) -> None:
        self._redis_client.delete(key)


redis_cache = RedisCache(
    redis.Redis(
        host=redis_settings.REDIS_HOST,
        port=redis_settings.REDIS_PORT,
        username=redis_settings.REDIS_USER,
        password=redis_settings.REDIS_PASSWORD,
        decode_responses=True,
    )
)
