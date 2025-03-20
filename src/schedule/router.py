from fastapi import APIRouter, Depends, Query

from src.schedule.schedule_api import APISchedule


router = APIRouter(prefix="/api/schedule_api", tags=["schedule"])


@router.get("/id/{group_name}")
async def get_group_id(
    group_name: str
):
    schedule_api = APISchedule()

    group_id = await schedule_api.group_id(group_name)

    return {"group_id": group_id}
