from typing import Optional
from api.dto.auth import UserDetailDTO, UserCreateDTO
from application.services.repository.base import BaseRepositoryService


class UsersService(BaseRepositoryService):
    async def get_by_telegram_id(self, telegram_id: int) -> Optional[UserDetailDTO]:
        model = await self.repository.get_one_by_filters(telegram_id=telegram_id)
        if model:
            return UserDetailDTO(**model.__dict__)
        return None

    async def add_telegram_user(self, user: UserDetailDTO) -> UserCreateDTO:
        model = await self.repository.create(user.dict())

        return UserCreateDTO(id=model.id)
