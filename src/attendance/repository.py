from datetime import datetime
from sqlalchemy.future import select

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.exc import IntegrityError

from src.models import Attendance
from src.logger import logger



class AttendanceRepository:
    def __init__(self, db_session: AsyncSession):
        self.db_session = db_session

    async def save_attendance(
        self, 
        student_id: int, 
        date: str,
        attendance_data: dict
    ) -> Attendance:
        try:
            query = select(Attendance).where(
                Attendance.student_id == student_id,
                Attendance.date == date
            )
            result = await self.db_session.execute(query)
            existing_attendance = result.scalars().first()

            if existing_attendance:
                existing_attendance.attendance = attendance_data
                logger.debug(
                    f"Обновлена запись посещаемости: {existing_attendance.id}"
                )
                self.db_session.add(existing_attendance)
                await self.db_session.commit()
                await self.db_session.refresh(existing_attendance)
                return existing_attendance
            else:
                new_attendance = Attendance(
                    student_id=student_id,
                    date=date,
                    attendance=attendance_data
                )
                self.db_session.add(new_attendance)
                logger.debug(
                    f"Создана новая запись посещаемости для студента {student_id} на {date}"
                )
                await self.db_session.commit()
                await self.db_session.refresh(new_attendance)
        
        except IntegrityError as e:
            await self.db_session.rollback()
            logger.error(f"Ошибка при сохранении посещаемости: {str(e)}")
            raise


