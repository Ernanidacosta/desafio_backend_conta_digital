from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base


class Settings(BaseSettings):
    """
    Configurações gerais da aplicação
    """

    API_V1_STR: str = '/api/v1'
    # BD_URL: str = 'postgresql+asyncpg://admin:admin@localhost:5432/digital_account_database'
    # BD_URL: str = 'postgresql+asyncpg://admin:F0LX8MapIloxCQ5c5sV92do88Lnt45pe@dpg-chn84iu4dad1d57c7kjg-a.oregon-postgres.render.com/digital_account_database'
    BD_URL: str = 'sqlite+aiosqlite:///digital_account_database.db'
    DBBaseModel = declarative_base()

    class Config:
        case_sensitive = True


settings = Settings()
