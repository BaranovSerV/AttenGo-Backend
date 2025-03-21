from fastapi import APIRouter, Depends

from src.attendance.repository import AttendanceRepository
from src.attendance.dependency import get_attendance_repository
from src.attendance.shemas import AttendanceData
from src.auth.dependency import get_current_auth_user
from src.auth.shemas import AuthUserShema

router = APIRouter(prefix="/api/attendance", tags=["attendance"])


@router.post("/")
async def attendance(
    body: AttendanceData,
    user: AuthUserShema = Depends(get_current_auth_user),
    attendance_repository: AttendanceRepository = Depends(get_attendance_repository)
):

    attendance = await attendance_repository.save_attendance(
    student_id=user.id,
    date=body.date,
    attendance_data=body.attendance_data
    )

    return {"data": attendance}
