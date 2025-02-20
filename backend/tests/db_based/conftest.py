from pytest import Session
import pytest_asyncio
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from data.db.models import User, Whitelist  # noqa
from data.db.models import Base  # noqa


test_db_url = "sqlite+aiosqlite:///:memory:"


@pytest_asyncio.fixture(scope="module")
async def test_db_engine():
    """Creates an in-memory SQLite engine that persists for the test session."""
    engine = create_async_engine(test_db_url, echo=False, connect_args={"check_same_thread": False})
    async with engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)  # Create tables once
    yield engine
    await engine.dispose()  # Cleanup after tests


@pytest_asyncio.fixture(scope="module")
async def test_db_session(test_db_engine):
    """Creates a new database session per test."""
    async_session_maker = async_sessionmaker(
        bind=test_db_engine, class_=AsyncSession, expire_on_commit=False
    )
    async with async_session_maker() as session:
        yield session  # Provide session to test
        await session.rollback()  # Rollback changes after test


@pytest_asyncio.fixture(autouse=True, scope="module")
async def populate_test_db(test_db_session):
    users = [
        User(telegram_id=123, username="user1"),
        User(telegram_id=456, username="user2"),
        User(telegram_id=789, username="user3"),
    ]
    whitelists = [
        Whitelist(user_id=1),
    ]
    test_db_session.add_all(users)
    test_db_session.add_all(whitelists)
    await test_db_session.commit()
