from sqlalchemy import Column, Integer, String
from core.configs import settings


class PersonModel(settings.DBBaseModel):
    __tablename__ = 'persons'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    first_name: str = Column(String(256), nullable=True)
    last_name: str = Column(String(256), nullable=True)
    birthday: str = Column(String(256), nullable=True)
    password: str = Column(String(256))
    username: str = Column(String(256), index=True, nullable=False, unique=True)
    user_id: str = Column(String(256), nullable=True)
