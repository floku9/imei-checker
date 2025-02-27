from typing import Optional

from api.dto.auth import UserAddDTO, UserCreateDTO, UserGetDTO
from application.services.repository.base import BaseRepositoryService


class UsersService(BaseRepositoryService):
    async def get_by_telegram_id(self, telegram_id: int) -> Optional[UserGetDTO]:
        model = await self.repository.get_one_by_filters(telegram_id=telegram_id)
        if model:
            return UserGetDTO(**model.__dict__)
        return None

    async def add_telegram_user(self, user: UserAddDTO) -> UserCreateDTO:
        model = await self.repository.create(user.model_dump())

        return UserCreateDTO(id=model.id)
