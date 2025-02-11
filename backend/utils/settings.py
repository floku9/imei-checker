import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict


class JWTSettings(BaseSettings):
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str
    JWT_ACCESS_TOKEN_EXPIRE_MINUTES: int

    model_config = SettingsConfigDict(env_file=dotenv.find_dotenv(".env"), extra="ignore")


jwt_settings = JWTSettings()
