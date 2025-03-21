from src.logger import logger
from src.user.repository import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def auth(self, user_data: dict):
        user = await self.user_repository.get_or_create(user_data)

        return {
            "id": user.id, 
            "group_id": user.group_id, 
            "role": user.role
        }
