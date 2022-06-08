import os
from pydantic import BaseSettings,AnyHttpUrl
from typing import List
from dotenv import load_dotenv

load_dotenv()

class Settings(BaseSettings):

    # PROJECT INFO
    PROJECT_NAME:str = "Mongo CRUD"
    PROJECT_VERSION:str = "v0.0.1"
    API_V1_STR:str = "/api/v1"
    
    # SECURITY UTILS
    SECRET_KEY: str = "5126402477d3baacae24c2be"
    # SECRET_KEY: str = os.getenv("SECRET_KEY") or os.urandom(12).hex()
    ACCESS_TOKEN_EXPIRE_MINUTES: int = os.getenv("TOKEN_EXPIRE_MINUTES") or 60
    ALGORITHM: str = "HS256"

    # MONGO GENERAL CREDENTIALS
    _MG_NAME: str = os.getenv("MG_NAME") or None
    _MG_USER: str = os.getenv("MG_USER") or None
    _MG_PASSWORD: str = os.getenv("MG_PASSWORD") or None
    _MG_HOST: str = os.getenv("MG_HOST") or None
    _MG_PORT:str = os.getenv("MG_PORT") or None
    MONGO_DATABASE_URL: str = f"mongodb://{_MG_USER}:{_MG_PASSWORD}@{_MG_HOST}:{_MG_PORT}/"
    
    # CORS
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []


settings = Settings()