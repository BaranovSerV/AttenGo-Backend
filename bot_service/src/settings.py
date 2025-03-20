from pydantic_settings import BaseSettings, SettingsConfigDict


class Bot(BaseSettings):
    BOT_API_TOKEN: str


class Settings(Bot):
    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
