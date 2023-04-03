import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "The online Karnaf shop"
    API_PREFIX: str = "/api"
    HOST: str = "localhost"
    PORT: int = 8000
    RELOAD: bool = True

    REDIS_HOST: str = os.environ.get('REDIS_HOST', "172.17.0.2")
    REDIS_PORT: int = int(os.environ.get('REDIS_PORT', 6379))
    REDIS_DB: int = int(os.environ.get('REDIS_DB', 0))
    REDIS_PASSWORD: str = None

settings = Settings()