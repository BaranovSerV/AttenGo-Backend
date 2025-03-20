from datetime import timedelta

from fastapi import APIRouter

from src.auth.shemas import TelegramAuthRequest
from src.auth.token import create_token
from src.settings import settings


router = APIRouter(prefix="/api/users/auth", tags=["auth"])



@router.post("/login")
async def login(request: TelegramAuthRequest):
    access_token = create_token(
        request.model_dump(), 
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    )

    refresh_token = create_token(
        request.model_dump(), 
        timedelta(days=settings.REFRESH_TOKEN_EXPIRE_DAYS)
    )

    return {"access_token": access_token, "refresh_token": refresh_token}
