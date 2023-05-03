from core.configs import settings

from sqlalchemy import Column, Integer, String


class CardModel(settings.DBBaseModel):
    __tablename__ = 'cards'

    id: int = Column(Integer, primary_key=True, autoincrement=True)
    card_id: str = Column(String(100))
    title: str = Column(String(100))
    pan: str = Column(String(100))
    expiry_mm: str = Column(String(100))
    expiry_yyyy: str = Column(String(100))
    security_code: str = Column(String(100))
    date: str = Column(String(100))
