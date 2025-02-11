from backend.application.services.repository.base import BaseRepositoryService


class UsersService(BaseRepositoryService):
    async def get_by_telegram_id(self, telegram_id: int):
        return await self.repository.get_one_by_filters(telegram_id=telegram_id)
