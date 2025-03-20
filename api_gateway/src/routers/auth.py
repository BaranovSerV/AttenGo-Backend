import httpx
from fastapi import APIRouter, Request, HTTPException, Response
from src.settings import settings


router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/login")
async def login(request: Request, response: Response):
    request_data = await request.json()

    async with httpx.AsyncClient() as client:
        auth_response = await client.post(
            f"{settings.API_USER_SERVICE}/auth/login",
            json=request_data
        )

        if auth_response.status_code != 200:
            raise HTTPException(
                status_code=auth_response.status_code, 
                detail=auth_response.text
        )

    response_data = auth_response.json()

    access_token = response_data.get("access_token")
    refresh_token = response_data.get("refresh_token")

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

    return {"message": "Login successful"}



