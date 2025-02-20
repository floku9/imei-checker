import os
from pydantic_settings import BaseSettings, SettingsConfigDict

ENV_STATE = os.getenv("ENV_STATE", ".dev")
CURRENT_ENV_FILE = f".env{ENV_STATE}"


class DBSettings(BaseSettings):
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASS: str
    DB_NAME: str

    @property
    def DB_URL(self) -> str:
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"

    model_config = SettingsConfigDict(env_file=CURRENT_ENV_FILE, extra="ignore")


class JWTSettings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=CURRENT_ENV_FILE, extra="ignore")


class IMEIApiSettings(BaseSettings):
    IMEI_API_KEY: str

    model_config = SettingsConfigDict(env_file=CURRENT_ENV_FILE, extra="ignore")


imei_api_settings = IMEIApiSettings()
db_settings = DBSettings()
jwt_settings = JWTSettings()
