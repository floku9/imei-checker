import pytest
import pytest_asyncio
from sqlalchemy.exc import IntegrityError

from api.dto.auth import UserAddDTO
from application.services.repository.users import UsersService
from data.repositories.sql.orm.db_models_repositories import UserRepository


@pytest_asyncio.fixture(scope="function")
async def users_test_service(test_db_session) -> UsersService:
    repository = UserRepository(session=test_db_session)
    return UsersService(repository)


@pytest.mark.asyncio
async def test_get_user_by_telegram_id_successfully(
    users_test_service: UsersService,
):
    user = await users_test_service.get_by_telegram_id(123)
    assert user is not None


@pytest.mark.asyncio
async def test_get_user_by_telegram_id_not_found(users_test_service: UsersService):
    user = await users_test_service.get_by_telegram_id(111111111)
    assert user is None


@pytest.mark.asyncio
async def test_add_user_to_db(users_test_service: UsersService):
    user = UserAddDTO(telegram_id=123456789, first_name="John", last_name="Doe")
    db_user = await users_test_service.add_telegram_user(user)

    assert db_user.id is not None


@pytest.mark.asyncio
async def test_add_user_to_db_already_exists(users_test_service: UsersService):
    user = UserAddDTO(telegram_id=123, username="user1")
    with pytest.raises(IntegrityError) as e:
        await users_test_service.add_telegram_user(user)

    assert e is not None
