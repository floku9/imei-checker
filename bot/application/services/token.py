from application.interactors.api.auth import AuthApiClient
from data.cache.base import BaseCache
from settings import cache_settings


class TokenService:
    def __init__(self, cache: BaseCache, auth_client: AuthApiClient):
        self.cache = cache
        self.auth_client = auth_client

    async def get_token(self, telegram_user_id: str) -> str:
        token = self.cache.get(telegram_user_id)
        if token is None:
            token = await self.auth_client.auth_by_telegram_id(telegram_user_id)
            self.cache.add(telegram_user_id, token, cache_settings.CACHE_TOKEN_EXPIRATION_SECONDS)
        return token
