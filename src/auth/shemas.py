from pydantic import BaseModel


class TelegramAuthRequest(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    photo_url: str
    auth_date: int
    hash: str


class AuthUserShema(BaseModel):
    id: int
    group_id: int | None
    role: str


