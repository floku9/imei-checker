import pytest

import redis
from data.cache.redis import RedisCache


@pytest.fixture
def test_redis_cache() -> RedisCache:
    redis_client = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True,
    )

    return RedisCache(redis_client)
