from fastapi import Depends, HTTPException, status, Cookie

from src.auth.exception import ExpiredTokenError, InvalidTokenError
from src.auth.token import decode_token
from src.auth.service import AuthService
from src.auth.shemas import AuthUserShema
from src.user.repository import UserRepository
from src.user.dependency import get_user_repository


async def get_auth_service(
    user_repository: UserRepository = Depends(get_user_repository)
):
    return AuthService(user_repository)


async def get_current_refresh_token_payload(
    refresh_token: str = Cookie(None)
):
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Access token is missing",
        )

    try:
        payload = decode_token(refresh_token)
        return payload
    except ExpiredTokenError:
        raise HTTPException(status_code=401, detail="Access token expired")

    except InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid access token")


async def get_current_auth_user(
    payload: dict = Depends(get_current_refresh_token_payload)
):
    return AuthUserShema(**payload)
