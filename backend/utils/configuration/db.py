from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

from backend.data.db.settings import db_settings

async_engine = create_async_engine(url=db_settings.DB_URL, echo=False)

async_session_factory = async_sessionmaker(
    async_engine, class_=AsyncSession, expire_on_commit=False
)
