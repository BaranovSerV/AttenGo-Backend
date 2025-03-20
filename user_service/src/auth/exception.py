from src.logger import logger


class TokenError(Exception):
    ...


class ExpiredTokenError(TokenError):
    def __init__(self):
        logger.error("Срок токена истек")


class InvalidTokenError(TokenError):
    def __init__(self):
        logger.error("Невалидный токен")
