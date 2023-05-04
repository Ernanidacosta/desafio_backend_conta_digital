from typing import Optional

from pydantic import BaseModel as SCBaseModel


class BillingCardSchema(SCBaseModel):
    id: Optional[int]
    card_id: str


class TransferSchema(SCBaseModel):
    id: Optional[int]
    friend_id: str
    total_to_pay: int
    billing_card: BillingCardSchema
