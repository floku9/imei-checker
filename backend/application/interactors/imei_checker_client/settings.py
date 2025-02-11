import dotenv
from pydantic_settings import BaseSettings, SettingsConfigDict

API_REQUEST_TIMEOUT = 20


class IMEIApiSettings(BaseSettings):
    IMEI_API_KEY: str

    model_config = SettingsConfigDict(env_file=dotenv.find_dotenv(".env"), extra="ignore")


imei_api_settings = IMEIApiSettings()
