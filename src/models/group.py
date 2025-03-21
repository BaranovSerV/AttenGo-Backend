from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.infrastructure.postgres import Base


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    local_group_name: Mapped[str] = mapped_column(String, unique=True)

    university_group_id: Mapped[int] = mapped_column(Integer)

    users: Mapped[list["User"]] = relationship("User", back_populates="group")

