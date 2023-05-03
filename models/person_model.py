from sqlalchemy import Column, Integer, String
from core.configs import settings


class PersonModel(settings.DBBaseModel):
    __tablename__ = 'persons'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    first_name: str = Column(String(100))
    last_name: str = Column(String(100))
    birthday: str = Column(String(10))
    password: str = Column(String(50))
    username: str = Column(String(100))
    user_id: str = Column(String(100))
