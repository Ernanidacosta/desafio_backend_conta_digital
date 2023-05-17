from typing import Optional, List
from pydantic import BaseModel


class BillingCardSchema(BaseModel):
    card_id: str

    class Config:
        orm_mode = True


class TransferSchema(BaseModel):
    user_id: str
    friend_id: str
    total_to_transfer: int
    billing_card: BillingCardSchema = None

    class Config:
        orm_mode = True
