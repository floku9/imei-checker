from backend.application.services.repository.base import BaseRepositoryService


class WhitelistService(BaseRepositoryService):

    async def is_user_whitelisted(self, user_id: int) -> bool:
        whitelist_record = await self.repository.get_one_by_filters(user_id=user_id)
        return whitelist_record is not None
