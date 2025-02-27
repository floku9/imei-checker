from application.dto.auth import RegistryUserDTO
from application.interactors.api.auth import BaseAuthAPIClient


class RegistrationService:
    def __init__(self, auth_client: BaseAuthAPIClient):
        self.auth_client = auth_client

    async def register_user(self, user: RegistryUserDTO) -> None:
        async with self.auth_client as client:
            await client.registry(user)
