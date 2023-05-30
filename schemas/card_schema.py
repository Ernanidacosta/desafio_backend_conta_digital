from typing import Optional

from pydantic import BaseModel


class CardSchema(BaseModel):
    id: Optional[int]
    card_id: str
    title: str
    pan: str
    expiry_mm: str
    expiry_yyyy: str
    security_code: str
    date: str

    class Config:
        orm_mode = True
