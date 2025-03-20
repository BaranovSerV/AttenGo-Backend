from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.postgres import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[Integer] = mapped_column(Integer, primary_key=True, index=True)
    group_id: Mapped[Integer] = mapped_column(Integer)
    role: Mapped[String] = mapped_column(String, default="ordinary")
