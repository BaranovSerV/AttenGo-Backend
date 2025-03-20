from datetime import timedelta

from fastapi import APIRouter, Request, Response

from src.auth.shemas import TelegramAuthRequest
from src.auth.token import create_token
from src.settings import settings


router = APIRouter(prefix="/api/auth", tags=["auth"])



@router.post("/login")
async def login(request: TelegramAuthRequest, response: Response):
    access_token = create_token(
        request.model_dump(), 
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    )

    refresh_token = create_token(
        request.model_dump(), 
        timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )
    
    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,
        samesite="none",
        secure=True
    )

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=False,
        samesite="none",

        secure=True
    )

    return {"access_token": access_token}
