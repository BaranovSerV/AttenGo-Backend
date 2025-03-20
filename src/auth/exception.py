from src.logger import logger


class AuthError(Exception):
    ...

class TokenError(AuthError):
    ...


class ExpiredTokenError(TokenError):
    def __init__(self):
        logger.error("Срок токена истек")


class InvalidTokenError(TokenError):
    def __init__(self):
        logger.error("Невалидный токен")


class AuthDataError(AuthError):
    def __init__(self):
        logger.error("Ошибка верификации данных")

