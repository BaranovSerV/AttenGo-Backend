from src.logger import logger


class ScheduleError(Exception):
    ...


class BadRequestGroupError(ScheduleError):
    def __init__(self):
        logger.error("Bad Request group data")
