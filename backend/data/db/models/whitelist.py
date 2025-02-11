from sqlalchemy import ForeignKey, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.data.db.models.base import BaseWithCreation
from backend.data.db.models.user import User


class Whitelist(BaseWithCreation):
    __tablename__ = "whitelist"

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    user: Mapped["User"] = relationship(back_populates="whitelist_record")
