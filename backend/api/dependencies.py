from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from application.interactors.imei_checker_client.api import model_description_imei_checker
from application.services.imei_checker.api_based import APIImeiCheckerService
from application.services.imei_checker.sandbox import SandboxImeiCheckerService
from application.services.repository.users import UsersService
from utils.configuration.db import async_session_factory
from data.repositories.sql.orm.db_models_repositories import WhitelistRepository
from application.services.repository.whitelist import WhitelistService
from data.repositories.sql.orm.db_models_repositories import UserRepository
from application.interactors.imei_checker_client.sandbox import sandbox_imei_checker_client


async def get_db_session():
    async with async_session_factory() as session:
        yield session


def get_whitelist_service(session: AsyncSession = Depends(get_db_session)):
    repo = WhitelistRepository(session)
    return WhitelistService(repo)


def get_users_service(session: AsyncSession = Depends(get_db_session)):
    repo = UserRepository(session)
    return UsersService(repo)


def get_imei_checker_service() -> APIImeiCheckerService:
    checker_client = model_description_imei_checker
    return APIImeiCheckerService(checker_client)


def get_sandbox_imei_checker_service() -> SandboxImeiCheckerService:
    checker_client = sandbox_imei_checker_client
    return SandboxImeiCheckerService(checker_client)
