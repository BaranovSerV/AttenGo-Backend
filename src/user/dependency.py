from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.user.repository import UserRepository
from src.dependency import get_db_session


async def get_user_repository(
    db_session: AsyncSession = Depends(get_db_session)
):
    return UserRepository(db_session)
