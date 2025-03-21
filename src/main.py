import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.settings import settings
from src import ROUTERS


app = FastAPI(title="user_service")

for router in ROUTERS:
    app.include_router(router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://ultimately-talented-louse.ngrok-free.app",
        "http://localhost:5173"
    ],  
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
