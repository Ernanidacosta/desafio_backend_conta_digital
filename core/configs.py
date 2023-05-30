from decouple import config

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais da aplicação
    """

    API_V1_STR: str = '/api/v1'
    BD_URL: str = config('DATABASE_URL')
    DBBaseModel = declarative_base()

    JWT_SECRET: str = config('JWT_SECRET')
    ALGORITHM: str = config('ALGORITHM')

    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7


    class Config:
        case_sensitive = True


settings: Settings = Settings()
