import os
from typing import Optional

from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_STATE = os.getenv("ENV_STATE", ".dev")
CURRENT_ENV_FILE = f".env{ENV_STATE}"


class EnvSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=CURRENT_ENV_FILE, extra="ignore")


class BackendSettings(EnvSettings):
    BACKEND_URL: str


class CacheSettings(EnvSettings):
    CACHE_TOKEN_EXPIRATION_SECONDS: int


class RedisSettings(EnvSettings):
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_USER: Optional[str] = None
    REDIS_PASSWORD: Optional[str] = None


backend_settings = BackendSettings()
redis_settings = RedisSettings()
cache_settings = CacheSettings()