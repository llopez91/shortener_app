from pydantic import BaseSettings
from functools import lru_cache


class Settings(BaseSettings):
    ENV: str
    DEBUG: bool
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000

    class Config:
        env_file = ".env"


@lru_cache()
def get_config():
    return Settings()


config = get_config()
