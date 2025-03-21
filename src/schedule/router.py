from datetime import datetime

from fastapi import APIRouter, Depends, Query, HTTPException

from src.schedule.schedule_api import APISchedule
from src.schedule.exception import BadRequestGroupError
from src.schedule.validator import validate_schedule
from src.auth.shemas import AuthUserShema
from src.auth.dependency import get_current_auth_user


router = APIRouter(prefix="/api/schedule", tags=["schedule"])


@router.get("/{group_id}")
async def group_schedule(
    group_id: int,
    start_time: datetime = Query(..., description="Начальное время расписания"),
    end_time: datetime = Query(..., description="Конечное время расписания")
):
    schedule_api = APISchedule()

    data = await schedule_api.schedule_by_group(
        group_id,
        start_time,
        end_time
    )

    schedule = validate_schedule(data)

    return {"schedule": schedule}

@router.get("/{group_name}/id")
async def get_group_id(
    group_name: str
):
    try:
        schedule_api = APISchedule()

        group_id = await schedule_api.group_id(group_name)

        return {"group_id": group_id}
    except BadRequestGroupError:
        raise HTTPException(status_code=400, detail="Bad Request group")

@router.post("/create")
async def create_group(
    user: AuthUserShema = Depends(get_current_auth_user)

):
    return {"user": user}
