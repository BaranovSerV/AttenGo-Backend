import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.settings import settings
from src.routers.auth import router


app = FastAPI(title="api_gateway")

app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://ultimately-talented-louse.ngrok-free.app"],  
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


if __name__ == "__main__":
    uvicorn.run(
        app="src.main:app", 
        host=settings.API_HOST, 
        port=settings.API_PORT,
        reload=True
    )

