from sqlalchemy import Column, Integer, String
from core.configs import settings


class FriendsModel(settings.DBBaseModel):
    __tablename__ = 'friends'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    first_name: str = Column(String(100))
    last_name: str = Column(String(100))
    birthday: str = Column(String(10))
    username: str = Column(String(100))
    user_id: str = Column(String(100))
