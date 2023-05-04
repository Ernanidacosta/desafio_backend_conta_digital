from typing import Optional
from sqlmodel import Field, SQLModel


class CardModel(SQLModel, table=True):
    __tablename__ = 'cards'

    id: Optional[int] = Field(default=None, primary_key=True)
    card_id: str
    title: str
    pan: str
    expiry_mm: str
    expiry_yyyy: str
    security_code: str
    date: str
