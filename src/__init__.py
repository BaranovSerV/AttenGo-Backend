from src.auth.router import router as auth_router
from src.schedule.router import router as schedule_router
from src.attendance.router import router as attendace_router


ROUTERS = [ 
    auth_router, 
    schedule_router, 
    attendace_router
]
