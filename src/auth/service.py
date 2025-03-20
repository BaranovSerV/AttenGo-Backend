from src.logger import logger
from src.user.repository import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def auth(self):
        user = await self.user_repository.get_or_create()
