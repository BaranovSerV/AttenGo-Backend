from datetime import timedelta

from fastapi import APIRouter, Request, Response, HTTPException, Depends

from src.auth.exception import AuthDataError
from src.auth.shemas import TelegramAuthRequest
from src.auth.verify import verify_telegram_auth
from src.auth.token import create_token
from src.auth.dependency import get_current_refresh_token_payload
from src.settings import settings


router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login")
async def login(request: TelegramAuthRequest, response: Response):
    try:
        verify_telegram_auth(request.model_dump())
    except AuthDataError:
        raise HTTPException(status_code=400, detail="Bad Request")

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



@router.get("/refresh")
async def refresh_access_token(
    payload = Depends(get_current_refresh_token_payload)

):
    new_access_token = create_token(
        payload,
        timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": new_access_token}

