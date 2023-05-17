from core.configs import settings

from sqlalchemy import Column, Integer, String


class CardModel(settings.DBBaseModel):
    __tablename__ = 'cards'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    card_id: str = Column(String)
    title: str = Column(String)
    pan: str = Column(String)
    expiry_mm: str = Column(String)
    expiry_yyyy: str = Column(String)
    security_code: str = Column(String)
    date: str = Column(String)
