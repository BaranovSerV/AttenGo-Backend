from pydantic_settings import BaseSettings, SettingsConfigDict


class API(BaseSettings):
    API_HOST: str
    API_PORT: int


class Schedule(BaseSettings):
    API_SCHEDULE: str

class Bot(BaseSettings):
    BOT_API_TOKEN: str

class JWT(BaseSettings):
    SECRET_KEY: str  
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    REFRESH_TOKEN_EXPIRE_DAYS: int


class Postgres(BaseSettings):
    POSTGRES_HOST: str
    POSTGRES_PORT: int
    POSTGRES_USER: str
    POSTGRES_DB: str
    POSTGRES_PASSWORD: str
    POSTGRES_DRIVER: str

    @property
    def postgres_url(self):
        return (
            f"{self.POSTGRES_DRIVER}://{self.POSTGRES_USER}:"\
            f"{self.POSTGRES_PASSWORD}@{self.POSTGRES_HOST}:"\
            f"{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

class Settings(
    API, JWT, Postgres, Bot, Schedule
):
    model_config = SettingsConfigDict(env_file=".env")



settings = Settings()
