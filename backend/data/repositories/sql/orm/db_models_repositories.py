from backend.data.db.models.user import User
from backend.data.db.models.whitelist import Whitelist
from backend.data.repositories.sql.orm.generic_repository import GenericORMRepository


class TelegramUserRepository(GenericORMRepository[User]):
    model = User


class WhitelistRepository(GenericORMRepository[Whitelist]):
    model = Whitelist
