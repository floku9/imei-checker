from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import relationship
from backend.data.db.models.base import BaseWithCreation


class User(BaseWithCreation):
    __tablename__ = "users"

    telegram_id: Mapped[int] = mapped_column(unique=True)
    username: Mapped[str] = mapped_column(String, nullable=True)
    first_name: Mapped[str] = mapped_column(String, nullable=True)
    last_name: Mapped[str] = mapped_column(String, nullable=True)

    whitelist_record: Mapped["Whitelist"] = relationship(back_populates="user")  # type: ignore
