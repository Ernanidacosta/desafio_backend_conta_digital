from typing import Optional
from pydantic import BaseModel


class BillingCardSchema(BaseModel):
    id: Optional[int]
    card_id: str

    class Config:
        orm_mode = True


class TransferSchema(BaseModel):
    id: Optional[int]
    user_id: Optional[str]
    friend_id: str
    total_to_transfer: int
    billing_card: BillingCardSchema = None

    class Config:
        orm_mode = True
