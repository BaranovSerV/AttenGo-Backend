from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from src.attendance.repository import AttendanceRepository
from src.dependency import get_db_session


async def get_attendance_repository(
    db_session: AsyncSession = Depends(get_db_session)
):
    return AttendanceRepository(db_session)
