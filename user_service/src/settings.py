from pydantic_settings import BaseSettings, SettingsConfigDict


class API(BaseSettings):
    API_HOST: str
    API_PORT: int


class JWT(BaseSettings):
    SECRET_KEY: str  
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int


class Settings(
    API, JWT
):
    model_config = SettingsConfigDict(env_file=".env")



settings = Settings()
