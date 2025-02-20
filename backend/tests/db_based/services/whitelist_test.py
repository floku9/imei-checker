import pytest
import pytest_asyncio

from application.services.repository.whitelist import WhitelistService
from data.repositories.sql.orm.db_models_repositories import WhitelistRepository


@pytest_asyncio.fixture(scope="function")
async def whitelist_test_service(test_db_session) -> WhitelistService:
    repository = WhitelistRepository(session=test_db_session)
    return WhitelistService(repository)


@pytest.mark.asyncio
async def test_user_whitelisted(
    whitelist_test_service: WhitelistService,
):
    is_user_whitelist = await whitelist_test_service.is_user_whitelisted(1)
    assert is_user_whitelist


@pytest.mark.asyncio
async def test_user_not_whitelisted(
    whitelist_test_service: WhitelistService,
):
    is_user_whitelist = await whitelist_test_service.is_user_whitelisted(3)
    assert not is_user_whitelist
