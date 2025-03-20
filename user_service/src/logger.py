from loguru import logger
import sys



logger.remove()

logger.add("logs/debug.log", level="DEBUG", rotation="10 MB", compression="zip")


logger.add("logs/info.log", level="INFO", rotation="10 MB", compression="zip")

logger.add("logs/errors.log", level="ERROR", rotation="5 MB", compression="zip")

logger.add(

    sys.stdout,
    level="INFO",
    format="<level>{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}</level>",
)
