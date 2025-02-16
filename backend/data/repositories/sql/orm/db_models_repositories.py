from data.db.models.user import User
from data.db.models.whitelist import Whitelist
from data.repositories.sql.orm.generic_repository import GenericORMRepository


class UserRepository(GenericORMRepository[User]):
    model = User


class WhitelistRepository(GenericORMRepository[Whitelist]):
    model = Whitelist
