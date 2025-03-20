from datetime import datetime, timedelta, timezone


import jwt


from src.auth.exception import InvalidTokenError, ExpiredTokenError
from src.settings import settings


def create_token(data: dict, expires_delta: timedelta) -> str:
    to_encode = data.copy()


    expire = datetime.now(tz=timezone.utc) + expires_delta

    to_encode.update({"exp": expire})

    token = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return token


def decode_token(token: str) -> dict:
    try:
        payload = jwt.decode(

            token, 
            settings.SECRET_KEY, 
            algorithms=[settings.ALGORITHM]
        )
        return payload

    except jwt.ExpiredSignatureError:
        raise ExpiredTokenError()    
    except jwt.InvalidTokenError:

        raise InvalidTokenError()
