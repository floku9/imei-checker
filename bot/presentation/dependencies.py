from application.interactors.api.auth import auth_api_client
from application.services.registration import RegistrationService
from application.services.token import TokenService
from data.cache.redis import redis_cache

token_service = TokenService(cache=redis_cache, auth_client=auth_api_client)
registration_service = RegistrationService(auth_client=auth_api_client)
