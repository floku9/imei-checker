from typing import TypeVar, List, Any, Type, Optional

from sqlalchemy import select, insert, update
from sqlalchemy.ext.asyncio import AsyncSession

from data.db.models.base import Base
from data.repositories.sql.sql_base_repository import SQLBaseRepositoryAsync

T = TypeVar("T", bound=Base)


class GenericORMRepository[T](SQLBaseRepositoryAsync):
    model: Type[T] = None  # type: ignore

    def __init__(self, session: AsyncSession):
        self._session = session

    async def get_one(self, id: int) -> Optional[T]:
        stmt = select(self.model).where(self.model.id == id)
        result = await self._session.execute(stmt)
        return result.scalar()

    async def get_one_by_filters(self, **filters: dict[str, Any]) -> Optional[T]:
        stmt = select(self.model).filter_by(**filters)
        result = await self._session.execute(stmt)
        return result.scalar()

    async def get_many(self, **filters: dict[str, Any]) -> List[T]:
        stmt = select(self.model).filter_by(**filters)
        result = await self._session.execute(stmt)
        result = [res[0] for res in result.all()]
        return result

    async def create(self, data: dict[str, Any]) -> T:
        stmt = insert(self.model).values(**data).returning(self.model)
        result = await self._session.execute(stmt)
        await self._session.flush()
        await self._session.commit()
        record = result.scalar_one()
        await self._session.refresh(record)
        return record

    async def update(self, idx: int, data: dict[str, Any]) -> T:
        stmt = update(self.model).where(self.model.id == idx).values(**data).returning(self.model)
        result = await self._session.execute(stmt)
        await self._session.flush()
        await self._session.commit()
        record = result.scalar_one()
        return record

    async def delete(self, idx: int) -> None:
        record = self.get_one(idx)
        if record:
            await self._session.delete(record)
            await self._session.flush()
            await self._session.commit()
