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

    class Config:
        case_sensitive = True


settings = Settings()
