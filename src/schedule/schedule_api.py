from datetime import datetime

import aiohttp
from pydantic import TypeAdapter

from src.schedule.exception import BadRequestGroupError
from src.schedule.shemas import LessonShema, ScheduleShema, LessonsDay
from src.logger import logger
from src.settings import settings


class APISchedule:
    def __init__(self):
        self.base_url = settings.API_SCHEDULE
  

    async def _get_data(self, url: str) -> dict | list | None:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(url) as response:
                    if response.status == 200:
                        return await response.json()
                    else:
                        logger.error(f"Ошибка при запросе к {url}: {response.status}")
                        return None
        except Exception as e:
            logger.error(f"Произошла ошибка при запросе к {url}: {e}")
            return None


    async def schedule_by_group(
        self,
        group_id: int,
        start_time: datetime,
        end_time: datetime
    ):
       
        start_date = start_time.strftime("%Y-%m-%d")

        end_date = end_time.strftime("%Y-%m-%d")

        url = f"{self.base_url}/schedule/group/{group_id}?start={start_date}&finish={end_date}"


        data = await self._get_data(url)

        if data is None:
            return None
        
        return data


    async def group_id(self, group: str) -> int:
        url = f"{self.base_url}/search?type=group&term={group}"
        data = await self._get_data(url)
        
        if isinstance(data, list) and len(data) == 1:
            return data[0].get("id")

        else:
            raise BadRequestGroupError()
