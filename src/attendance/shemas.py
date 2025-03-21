from pydantic import BaseModel

class AttendanceData(BaseModel):
    date: str
    attendance_data: dict[str, str] 

