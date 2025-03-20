from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.postgres import Base


class Group(Base):
    __tablename__ = "groups"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, autoincrement=True)
    local_group_name: Mapped[String] = mapped_column(String, unique=True)
    university_group_id: Mapped[Integer] = mapped_column(Integer)
