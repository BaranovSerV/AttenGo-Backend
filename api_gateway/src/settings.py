from pydantic_settings import BaseSettings, SettingsConfigDict


class API(BaseSettings):
    API_HOST: str
    API_PORT: int

class APIServices(BaseSettings):
    API_USER_SERVICE: str
    API_GROUP_SERVICE: str
    API_ATTENDANCE_SERVICE: str


class Settings(APIServices, API):
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
