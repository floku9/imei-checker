import time

from data.cache.redis import RedisCache


def test_redis_cache_add_and_get(test_redis_cache: RedisCache):
    test_redis_cache.add("test_key", "test_value", 10)
    assert test_redis_cache.get("test_key") == "test_value"


def test_redis_cache_get_expired(test_redis_cache: RedisCache):
    test_redis_cache.add("test_key", "test_value", 1)
    time.sleep(1.1)
    assert test_redis_cache.get("test_key") is None


def test_redis_cache_get_not_expired(test_redis_cache: RedisCache):
    test_redis_cache.add("test_key", "test_value", 2)
    time.sleep(0.1)
    assert test_redis_cache.get("test_key") == "test_value"


def test_redis_cache_delete(test_redis_cache: RedisCache):
    test_redis_cache.add("test_key", "test_value", 10)
    test_redis_cache.delete("test_key")
    assert test_redis_cache.get("test_key") is None
