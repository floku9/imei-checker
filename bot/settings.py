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

    @property
    def REDIS_URL(self) -> str:
        if self.REDIS_USER and self.REDIS_PASSWORD:
            return f"redis://{self.REDIS_USER}:{self.REDIS_PASSWORD}@{self.REDIS_HOST}:{self.REDIS_PORT}"
        else:
            return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}"


class BotSettings(EnvSettings):
    BOT_TOKEN: str


backend_settings = BackendSettings()
redis_settings = RedisSettings()
cache_settings = CacheSettings()
bot_settings = BotSettings()
